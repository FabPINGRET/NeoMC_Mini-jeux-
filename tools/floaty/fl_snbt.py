r"""Lecteur SNBT / JSON qui GARDE LES POSITIONS dans la ligne (fonctions pures ; sert fl_tr, qui réécrit une chaîne sans toucher au reste).

    r = fl_snbt.parse(texte, i=0, warns=None)      # (valeur, fin) ou None ; warns : liste où l'on ajoute le motif de l'échec
    leaf = fl_snbt.string(texte, i, warns=None)    # Leaf de la chaîne qui s'ouvre en texte[i], ou None
    fl_snbt.encode(valeur, '"')                    # la chaîne ré-écrite avec son guillemet : fl_snbt.encode(leaf.v, leaf.q)
    fl_snbt.leaves(noeud)                          # tous les Leaf d'un arbre

Valeurs rendues : dict (clés décodées), Arr (liste ; Arr.kind = 'B' / 'I' / 'L' pour `[I;1,2]`, '' sinon), Leaf(v, a, b, q) pour une chaîne
(v = valeur décodée, texte[a:b] = la chaîne guillemets compris, q = son guillemet `"` ou `'`) et Raw(v, a, b) pour un mot nu (nombre, `1b`,
`true`, identifiant sans guillemets). Échappements SNBT 26.2 : \\ \" \' \n \t \r \b \f \s \xXX \uXXXX \UXXXXXXXX \N{nom}.
encode() écrit \\, le guillemet, \n, \r et \t en échappements ; tout le reste (UTF-8, emoji) en clair.
Aucune exception ne sort : une erreur (chaîne non fermée, crochet manquant, échappement inconnu, imbrication folle) rend None.
"""
import re
import unicodedata
from collections import namedtuple

Leaf = namedtuple('Leaf', 'v a b q')
Raw = namedtuple('Raw', 'v a b')
_BARE = re.compile(r'[A-Za-z0-9_.+\-]+')
_TYPED = re.compile(r'([BIL])\s*;')
_RUN = {'"': re.compile(r'[^"\\]*'), "'": re.compile(r"[^'\\]*")}      # suite de caractères sans guillemet ni antislash
_ESC = {'\\': '\\', '"': '"', "'": "'", 'n': '\n', 't': '\t', 'r': '\r', 'b': '\b', 'f': '\f', 's': ' '}
_HEX = {'x': 2, 'u': 4, 'U': 8}


class Arr(list):
    """Liste SNBT ; kind = 'B' / 'I' / 'L' pour une liste typée `[I;...]`, '' sinon."""
    kind = ''


class _Err(Exception):
    pass


def _ws(t, i):
    while i < len(t) and t[i] in ' \t\r\n':
        i += 1
    return i


def _escape(t, j):
    """t[j] = le caractère après l'antislash -> (position suivante, caractère décodé)."""
    c = t[j] if j < len(t) else ''
    if c in _ESC:
        return j + 1, _ESC[c]
    if c in _HEX:
        h = t[j + 1:j + 1 + _HEX[c]]
        if len(h) == _HEX[c] and re.fullmatch(r'[0-9A-Fa-f]+', h):
            try:
                return j + 1 + len(h), chr(int(h, 16))
            except (ValueError, OverflowError):
                pass
    elif c == 'N' and t[j + 1:j + 2] == '{' and '}' in t[j:]:
        k = t.index('}', j)
        try:
            return k + 1, unicodedata.lookup(t[j + 2:k])
        except KeyError:
            pass
    raise _Err(f'échappement inconnu en {j - 1}')


def _string(t, i):
    q = t[i]
    out, j = [], i + 1
    while j < len(t):
        m = _RUN[q].match(t, j)
        out.append(m.group())
        j = m.end()
        if j >= len(t):
            break
        if t[j] == q:
            return Leaf(''.join(out), i, j + 1, q)
        j, ch = _escape(t, j + 1)
        out.append(ch)
    raise _Err(f'chaîne non fermée (ouverte en {i})')


def _value(t, i):
    i = _ws(t, i)
    if i >= len(t):
        raise _Err('valeur attendue en fin de texte')
    c = t[i]
    if c in '"\'':
        leaf = _string(t, i)
        return leaf, leaf.b
    if c == '{':
        return _compound(t, i)
    if c == '[':
        return _array(t, i)
    m = _BARE.match(t, i)
    if not m:
        raise _Err(f'caractère inattendu {c!r} en {i}')
    return Raw(m.group(), m.start(), m.end()), m.end()


def _compound(t, i):
    out, i = {}, _ws(t, i + 1)
    while i < len(t) and t[i] != '}':
        if t[i] in '"\'':
            key = _string(t, i)
            k, i = key.v, key.b
        else:
            m = _BARE.match(t, i)
            if not m:
                raise _Err(f'clé attendue en {i}')
            k, i = m.group(), m.end()
        i = _ws(t, i)
        if t[i:i + 1] != ':':
            raise _Err(f'« : » attendu en {i}')
        out[k], i = _value(t, i + 1)
        i = _ws(t, i)
        if t[i:i + 1] == ',':
            i = _ws(t, i + 1)
        elif t[i:i + 1] != '}':
            raise _Err(f'« , » ou « }} » attendu en {i}')
    if i >= len(t):
        raise _Err('« } » manquant')
    return out, i + 1


def _array(t, i):
    out, i = Arr(), _ws(t, i + 1)
    m = _TYPED.match(t, i)
    if m:
        out.kind, i = m.group(1), _ws(t, m.end())
    while i < len(t) and t[i] != ']':
        v, i = _value(t, i)
        out.append(v)
        i = _ws(t, i)
        if t[i:i + 1] == ',':
            i = _ws(t, i + 1)
        elif t[i:i + 1] != ']':
            raise _Err(f'« , » ou « ] » attendu en {i}')
    if i >= len(t):
        raise _Err('« ] » manquant')
    return out, i + 1


def _guard(fn, warns, *a):
    try:
        return fn(*a)
    except (_Err, RecursionError) as e:
        if warns is not None:
            warns.append(str(e) or 'imbrication trop profonde')
        return None


def parse(t, i=0, warns=None):
    """Valeur SNBT / JSON qui commence en t[i] (espaces ignorés) -> (valeur, position de fin) ; None si illisible (motif dans warns)."""
    return _guard(_value, warns, t, i)


def string(t, i, warns=None):
    """Chaîne qui s'ouvre en t[i] (guillemet `"` ou `'`) -> Leaf, ou None."""
    return _guard(_string, warns, t, i)


def encode(s, q='"'):
    """Valeur décodée -> chaîne SNBT avec le guillemet q : \\, le guillemet, \\n, \\r et \\t échappés ; le reste (UTF-8, emoji) en clair."""
    body = s.replace('\\', '\\\\').replace(q, '\\' + q).replace('\n', '\\n').replace('\r', '\\r').replace('\t', '\\t')
    return q + body + q


def leaves(node):
    """Tous les Leaf d'un arbre rendu par parse (valeurs de dict et éléments de liste ; les clés ne sont pas des Leaf)."""
    if isinstance(node, Leaf):
        yield node
    elif isinstance(node, dict):
        for v in node.values():
            yield from leaves(v)
    elif isinstance(node, list):
        for v in node:
            yield from leaves(v)
