"""Lecteur NBT minimal (stdlib) : level.dat, data/*.dat, chunks des fichiers region (partagé par les outils floaty).

    root = fl_nbt.load('level.dat')       # gzip, zlib ou NBT brut (détecté) -> dict du compound racine (le nom est ignoré)
    fl_nbt.spawn(root)                    # (x, y, z) du point d'apparition du monde

Types Python : compound -> dict, list -> list, byte/short/int/long -> int, float/double -> float, string -> str,
byte array -> bytes, int array / long array -> list[int]. Les chaînes sont du MUTF-8 de Java, décodées de façon STRICTE (mutf8_decode :
paires de substitution recombinées, ValueError sur un octet invalide, jamais de remplacement silencieux). Lecture seule : aucune
sérialisation d'arbre. Seule exception, le remplacement d'une chaîne dans des octets déjà lus : loads_spans(brut) donne les positions
des chaînes, encode_str(s) les octets d'une chaîne en MUTF-8 (le reste du NBT est recopié tel quel : voir fl_terrain_rw).

    root = fl_nbt.load('x.dat', snbt=True)    # mêmes dict / list, mais chaque feuille est un fragment SNBT typé (Snbt : 1b, 2s, 3, 4L,
    fl_nbt.snbt(root['data'])                 # 1.5f, 2.5d, "texte", [B;..], [I;..], [L;..]) : snbt() rend le texte SNBT d'un sous-arbre
"""
import gzip
import json
import math
import re
import struct
import zlib

_NUM = {1: '>b', 2: '>h', 3: '>i', 4: '>q', 5: '>f', 6: '>d'}
_SUFFIX = {1: 'b', 2: 's', 3: '', 4: 'L', 5: 'f', 6: 'd'}
_BARE_KEY = re.compile(r'[A-Za-z0-9_.+-]+')


_ASTRAL = re.compile('[\U00010000-\U0010ffff]')


def mutf8_decode(b):
    """Octets d'une chaîne NBT (MUTF-8 de Java : DataInput.readUTF) -> texte, de façon STRICTE : ValueError sur un octet de tête invalide
    (dont 0xF0..0xF7 : l'UTF-8 sur 4 octets n'existe pas en MUTF-8), une séquence tronquée ou une forme trop longue (hors C0 80 = NUL).
    Les paires de substitution (2 x 3 octets) sont recombinées en un caractère ; un surrogate isolé est gardé tel quel (Java l'accepte)."""
    if b.isascii():
        return b.decode('ascii')
    try:
        s = b.decode('utf-8')
    except UnicodeDecodeError:
        s = None
    if s is not None and not _ASTRAL.search(s):          # UTF-8 valide sans caractère hors BMP : même texte qu'en MUTF-8
        return s
    units, i, n = [], 0, len(b)
    while i < n:
        c = b[i]
        if c < 0x80:
            units.append(c)
            i += 1
        elif c >> 5 == 0b110 and i + 1 < n and b[i + 1] >> 6 == 0b10:
            u = (c & 0x1F) << 6 | b[i + 1] & 0x3F
            if 0 < u < 0x80:
                raise ValueError('MUTF-8 : forme trop longue')
            units.append(u)
            i += 2
        elif c >> 4 == 0b1110 and i + 2 < n and b[i + 1] >> 6 == 0b10 and b[i + 2] >> 6 == 0b10:
            u = (c & 0x0F) << 12 | (b[i + 1] & 0x3F) << 6 | b[i + 2] & 0x3F
            if u < 0x800:
                raise ValueError('MUTF-8 : forme trop longue')
            units.append(u)
            i += 3
        else:
            raise ValueError(f'MUTF-8 invalide : octet 0x{c:02x} à la position {i}')
    return struct.pack(f'<{len(units)}H', *units).decode('utf-16-le', 'surrogatepass')


def mutf8_encode(s):
    """Texte -> octets MUTF-8 : NUL en C0 80, un caractère hors BMP en paire de substitution (2 x 3 octets), un surrogate isolé en 3 octets."""
    if s.isascii() and '\0' not in s:
        return s.encode('ascii')
    out = bytearray()
    for (u,) in struct.iter_unpack('<H', s.encode('utf-16-le', 'surrogatepass')):
        if 0 < u < 0x80:
            out.append(u)
        elif u < 0x800:
            out += bytes((0xC0 | u >> 6, 0x80 | u & 0x3F))
        else:
            out += bytes((0xE0 | u >> 12, 0x80 | u >> 6 & 0x3F, 0x80 | u & 0x3F))
    return bytes(out)


class _Reader:
    def __init__(self, data):
        self.b, self.i = data, 0

    def take(self, n):
        if self.i + n > len(self.b):
            raise ValueError('NBT tronqué')
        s = self.b[self.i:self.i + n]
        self.i += n
        return s

    def num(self, fmt):
        return struct.unpack(fmt, self.take(struct.calcsize(fmt)))[0]

    def string(self):
        return mutf8_decode(self.take(self.num('>H')))

    def payload(self, t):
        if t in _NUM:
            return self.num(_NUM[t])
        if t == 7:
            return bytes(self.take(self.num('>i')))
        if t == 8:
            return self.string()
        if t == 9:
            sub, n = self.num('>b'), self.num('>i')
            return [self.payload(sub) for _ in range(max(n, 0))]
        if t == 10:
            out = {}
            while True:
                k = self.num('>b')
                if k == 0:
                    return out
                name = self.string()
                out[name] = self.payload(k)
        if t in (11, 12):
            n = self.num('>i')
            return [self.num('>i' if t == 11 else '>q') for _ in range(max(n, 0))]
        raise ValueError(f'type NBT inconnu : {t}')


def _quote(s):
    """Chaîne -> littéral SNBT entre guillemets. Un surrogate isolé (Java l'accepte) s'écrit en échappement \\uXXXX (ensure_ascii) : en clair,
    le texte ne s'encoderait plus en UTF-8 (UnicodeEncodeError à l'écriture des fonctions générées)."""
    try:
        s.encode('utf-8')
    except UnicodeEncodeError:
        return json.dumps(s, ensure_ascii=True)
    return json.dumps(s, ensure_ascii=False)


class Snbt(str):
    """Fragment SNBT déjà écrit (scalaire typé, chaîne entre guillemets, tableau typé) : feuille d'un arbre lu avec snbt=True."""


class _SnbtReader(_Reader):
    """Même lecture, mais chaque feuille est un Snbt : les types (byte, short, long, float...) survivent, ce que int / float perdent."""

    def payload(self, t):
        if t in (9, 10):
            return super().payload(t)          # conteneurs : dict / list, les enfants repassent par cette méthode
        if t in _NUM:
            v = self.num(_NUM[t])
            if t in (5, 6) and not math.isfinite(v):
                raise ValueError('flottant NBT non fini : pas d\'écriture SNBT')
            return Snbt((format(v, '.9g') if t == 5 else repr(v) if t == 6 else str(v)) + _SUFFIX[t])
        if t == 8:
            return Snbt(_quote(self.string()))
        if t == 7:
            return Snbt('[B;' + ','.join(f'{b - 256 if b > 127 else b}b' for b in self.take(self.num('>i'))) + ']')
        n = self.num('>i')
        sym, fmt, suf = ('I', '>i', '') if t == 11 else ('L', '>q', 'L')
        return Snbt(f'[{sym};' + ','.join(f'{self.num(fmt)}{suf}' for _ in range(max(n, 0))) + ']')


class _SpanReader(_Reader):
    """Même lecture que _Reader, et retient la position (début du préfixe u16, fin des octets) de chaque TAG_String d'un compound ou d'une liste."""

    def __init__(self, data):
        super().__init__(data)
        self.spans = {}

    def child(self, box, key, t):
        start = self.i
        v = self.payload(t)
        if t == 8:
            self.spans[(id(box), key)] = (start, self.i)
        return v

    def payload(self, t):
        if t == 9:
            sub, n = self.num('>b'), self.num('>i')
            out = []
            for i in range(max(n, 0)):
                out.append(self.child(out, i, sub))
            return out
        if t == 10:
            out = {}
            while True:
                k = self.num('>b')
                if k == 0:
                    return out
                name = self.string()
                out[name] = self.child(out, name, k)
        return super().payload(t)


def loads_spans(data):
    """Octets de NBT brut (ni gzip ni zlib : un chunk déjà décompressé) -> (racine, spans) : la racine comme loads(), et
    spans {(id(conteneur), clé ou indice): (début, fin)}, les octets [début, fin) d'une TAG_String étant son préfixe u16 puis sa valeur.
    Le NBT ne porte aucune longueur d'octets imbriquée : remplacer ces octets par encode_str(...) laisse tout le reste valable. Les
    conteneurs (dict / list) de la racine doivent rester vivants tant que spans est utilisé (id)."""
    r = _SpanReader(data)
    if r.num('>b') != 10:
        raise ValueError('la racine NBT doit être un compound')
    r.string()
    root = r.payload(10)
    return root, r.spans


def encode_str(s):
    """Texte -> octets d'une TAG_String : préfixe u16 + MUTF-8 (mutf8_encode : le format que lit Java, jamais de l'UTF-8 sur 4 octets) ;
    ValueError si plus de 65535 octets une fois encodé."""
    b = mutf8_encode(s)
    if len(b) > 0xFFFF:
        raise ValueError(f'chaîne NBT trop longue : {len(b)} octets (max 65535)')
    return struct.pack('>H', len(b)) + b


def snbt(v):
    """Texte SNBT d'un (sous-)arbre lu avec snbt=True."""
    if isinstance(v, dict):
        return '{' + ','.join(f'{k if _BARE_KEY.fullmatch(k) else _quote(k)}:{snbt(x)}' for k, x in v.items()) + '}'
    if isinstance(v, list):
        return '[' + ','.join(snbt(x) for x in v) + ']'
    return str(v)


def loads(data, snbt=False):
    """Octets (gzip / zlib / brut) -> dict du compound racine (snbt=True : feuilles en Snbt, voir l'en-tête)."""
    if data[:2] == b'\x1f\x8b':
        data = gzip.decompress(data)
    elif data[:1] == b'\x78':
        data = zlib.decompress(data)
    r = (_SnbtReader if snbt else _Reader)(data)
    if r.num('>b') != 10:
        raise ValueError('la racine NBT doit être un compound')
    r.string()
    return r.payload(10)


def load(path, snbt=False):
    with open(path, 'rb') as f:
        return loads(f.read(), snbt)


def spawn(root):
    """(x, y, z) du spawn du monde : 26.x `Data.spawn.pos`, sinon anciens `Data.SpawnX/Y/Z`."""
    d = root.get('Data', root)
    pos = d.get('spawn', {}).get('pos')
    if pos and len(pos) == 3:
        return tuple(pos)
    if all(k in d for k in ('SpawnX', 'SpawnY', 'SpawnZ')):
        return d['SpawnX'], d['SpawnY'], d['SpawnZ']
    raise ValueError('spawn introuvable dans le NBT (ni Data.spawn.pos ni Data.SpawnX/Y/Z)')
