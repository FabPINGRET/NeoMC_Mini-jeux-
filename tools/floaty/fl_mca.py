"""Fichiers region (.mca) : lecture des chunks (fl_terrain) et reconstruction avec des chunks remplacés (fl_terrain_rw).

    for i, raw in fl_mca.payloads(data, stats): ...      # (index 0..1023, NBT brut décompressé) de chaque chunk lisible
    new = fl_mca.rebuild(data, {i: nouveau_brut})         # .mca avec ces chunks remplacés (zlib, niveau 6)
    fl_mca.check(data, new, {i: nouveau_brut})            # relit new : tout ce qui n'a pas changé est identique, octet pour octet

Format : en-tête de 8 Ko (1024 entrées « offset sur 3 octets en secteurs de 4 Ko + nombre de secteurs », puis 1024 horodatages), chaque
chunk = longueur (4 octets) + type de compression + données ; types 1 gzip, 2 zlib, 3 brut. Non gérés mais comptés dans stats : 4 (LZ4 :
« lz4 »), 128+ (chunk externe .mcc : « externe »), autres (« inconnu »). Un chunk tronqué ou illisible est compté (« corrompu »), jamais
fatal. rebuild : les chunks gardent l'ordre des offsets d'origine à partir du secteur 2, alignés sur 4 Ko, offsets et nombres de secteurs
recalculés, horodatages recopiés ; un enregistrement non remplacé (LZ4, externe, inchangé) est recopié tel quel. Il refuse (McaError) un
fichier dont une entrée d'en-tête est corrompue : rien n'est alors réécrit. Le NBT lui-même est un autre sujet (fl_nbt).
"""
import gzip
import struct
import zlib

SECTOR = 4096
MAX_SECTORS = 255                # le nombre de secteurs d'une entrée tient sur 1 octet
LEVEL = 6


class Skip(Exception):
    """Chunk non lisible par ce script (le message est la clé de stats)."""


class McaError(Exception):
    """Fichier .mca dont l'en-tête est inutilisable : il n'est pas réécrit."""


class VerifyError(Exception):
    """Le .mca reconstruit ne relit pas comme prévu : bug, le build doit échouer."""


def decode(ctype, body):
    if ctype == 2:
        return zlib.decompress(body)
    if ctype == 1:
        return gzip.decompress(body)
    if ctype == 3:
        return body
    if ctype == 4:
        raise Skip('lz4')
    if ctype & 128:
        raise Skip('externe')
    raise Skip('inconnu')


def locate(data, i):
    """Entrée i de l'en-tête -> None (vide), (offset en octets, longueur, type de compression), ou False (corrompue : dans l'en-tête,
    hors du fichier, nombre de secteurs nul, longueur nulle ou qui dépasse les secteurs annoncés ou le fichier)."""
    entry = int.from_bytes(data[4 * i:4 * i + 3], 'big')
    if not entry:
        return None
    off, count = entry * SECTOR, data[4 * i + 3]
    if entry < 2 or count == 0 or off + 5 > len(data):         # < 2 : le « chunk » commencerait dans l'en-tête
        return False
    length, ctype = struct.unpack_from('>IB', data, off)
    if length < 1 or 4 + length > count * SECTOR or off + 4 + length > len(data):
        return False
    return off, length, ctype


def payloads(data, stats):
    """Octets d'un .mca -> (index 0..1023, NBT brut décompressé) de chaque chunk lisible ; les autres sont comptés dans stats."""
    if len(data) < 2 * SECTOR:
        if data:
            stats['corrompu'] += 1
        return
    for i in range(1024):
        loc = locate(data, i)
        if loc is None:
            continue
        if loc is False:
            stats['corrompu'] += 1
            continue
        off, length, ctype = loc
        stats['chunks'] += 1
        try:
            yield i, decode(ctype, data[off + 5:off + 4 + length])
        except Skip as e:
            stats[str(e)] += 1
        except (zlib.error, OSError, EOFError):
            stats['corrompu'] += 1


def record(raw):
    """NBT brut -> enregistrement d'un chunk : longueur, type 2 (zlib), données compressées au niveau 6."""
    body = zlib.compress(raw, LEVEL)
    return struct.pack('>IB', len(body) + 1, 2) + body


def sectors(rec):
    return -(-len(rec) // SECTOR)


def rebuild(data, changes):
    """.mca d'origine + {index: nouveau NBT brut} -> octets du nouveau .mca. McaError si l'en-tête est corrompu, ou si un chunk dépasse
    255 secteurs (l'appelant l'écarte avant : sectors(record(raw)))."""
    if len(data) < 2 * SECTOR:
        raise McaError('fichier plus court que son en-tête')
    entries = []
    for i in range(1024):
        loc = locate(data, i)
        if loc is False:
            raise McaError(f'entrée {i} de l\'en-tête corrompue')
        if loc:
            entries.append((int.from_bytes(data[4 * i:4 * i + 3], 'big'), i, loc))
    if set(changes) - {i for _, i, _ in entries}:
        raise McaError('chunk remplacé absent de l\'en-tête')
    header, body, sector = bytearray(data[:2 * SECTOR]), [], 2          # horodatages (2e moitié) recopiés
    for _, i, (off, length, _) in sorted(entries):
        rec = record(changes[i]) if i in changes else data[off:off + 4 + length]
        n = sectors(rec)
        if n > MAX_SECTORS or sector + n > 0xFFFFFF:
            raise McaError(f'chunk {i} : {n} secteurs')
        header[4 * i:4 * i + 4] = (sector << 8 | n).to_bytes(4, 'big')
        body.append(rec + b'\0' * (n * SECTOR - len(rec)))
        sector += n
    return bytes(header) + b''.join(body)


def check(old, new, changes):
    """Relit le nouveau .mca : mêmes chunks que l'ancien, enregistrements non remplacés identiques octet pour octet, chunks remplacés
    relus égaux à changes[i], horodatages recopiés, plages de secteurs disjointes. VerifyError sinon."""
    if new[SECTOR:2 * SECTOR] != old[SECTOR:2 * SECTOR]:
        raise VerifyError('horodatages modifiés')
    spans = []
    for i in range(1024):
        a, b = locate(old, i), locate(new, i)
        if not a:
            if b is not None:
                raise VerifyError(f'chunk {i} apparu')
            continue
        if not b:
            raise VerifyError(f'chunk {i} perdu ou corrompu')
        if i in changes:
            if b[2] != 2 or zlib.decompress(new[b[0] + 5:b[0] + 4 + b[1]]) != changes[i]:
                raise VerifyError(f'chunk {i} relu différent de ce qui a été écrit')
        elif old[a[0]:a[0] + 4 + a[1]] != new[b[0]:b[0] + 4 + b[1]]:
            raise VerifyError(f'chunk {i} modifié alors qu\'il devait être recopié')
        n = new[4 * i + 3]
        if n != sectors(new[b[0]:b[0] + 4 + b[1]]):
            raise VerifyError(f'chunk {i} : nombre de secteurs incohérent')
        spans.append((b[0], b[0] + n * SECTOR))
    spans.sort()
    if any(spans[k][1] > spans[k + 1][0] for k in range(len(spans) - 1)) or (spans and spans[-1][1] > len(new)):
        raise VerifyError('plages de secteurs qui se chevauchent ou débordent du fichier')
