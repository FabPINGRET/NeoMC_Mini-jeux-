"""Lecture des fichiers region (.mca) de la carte « Scourge of the Floaty Isles » et repérage des commandes du terrain.

    stats = Counter()
    finds, pending = fl_terrain.scan_file(chemin_mca, stats)   # Found(kind, pos, command, auto, file) ; pending : chunks « à vérifier »
    fl_terrain.classify(commande)                              # noms des risques (RISKS), du plus grave au moins grave
    fl_terrain.string_selectors(commande)                      # @x laissés dans des chaînes (non examinés), blocs imbriqués compris

Lecture seule (rien n'est écrit ; la réécriture est fl_terrain_rw). Format .mca : voir fl_mca (lz4, externe, inconnu : comptés dans stats ;
un chunk tronqué ou illisible est compté « corrompu » / « illisible », jamais fatal : ce sont les clés UNREAD, chunks NON analysés).
stats['chunks'] = entrées de l'en-tête dont l'enregistrement est complet (lisibles ou non ; une entrée corrompue n'y est pas). En 26.x
les block entities sont sous la racine du chunk (`block_entities`) et les entités dans entities/*.mca (`Entities` : seul le
command_block_minecart nous intéresse, y compris en passager `Passengers`). Les panneaux (`sign`, `hanging_sign`) sont lus aussi : voir
fl_signs. Found.ref = (conteneur, clé) de la chaîne `Command` d'un bloc ou d'un minecart (None pour un panneau) : pour fl_terrain_rw.

Pré-filtre : un chunk n'est analysé que si son NBT brut contient « command_block » ou « run_command » (le NBT complet d'un chunk est
coûteux à lire en Python pur : 800 Mo de région en quelques minutes au lieu d'une heure). Trois cas sont comptés dans stats ET listés
(fichier, cx, cz) dans `pending`, clés A_VERIFIER (chunks analysés mais à regarder à la main) ; HOLDER = block entity ou entité de
bloc de commande, de minecart de commande ou de panneau (déjà analysés), hors palettes de blocs et ticks planifiés (fl_signs.count_outside) :
- « sans_bloc » : aucun bloc de commande ni minecart trouvé alors que « command_block » est présent (format non reconnu, ou bloc sans block
  entity), OU « command_block » hors de tout holder, même dans un chunk qui a aussi un vrai bloc : objet de coffre, SpawnData d'un
  spawner, TileEntityData d'un falling_block... Un panneau ne compte pas comme bloc pour cette 1re condition ; il reste un holder pour les
  deux tokens (command_block et run_command).
- « rc_hors_panneau » : « run_command » hors de tout holder, par exemple un livre ou un coffre : jamais compté dans sans_bloc.
- « panneau_illisible » : un panneau contient plus de « run_command » que de commandes extraites (JSON invalide, type inattendu).
`sel_chaine` (stats) : total des @x laissés dans d'autres chaînes que « selector » / `Command:` des commandes trouvées (non examinés).
"""
import math
import re
import struct
import zlib
from collections import namedtuple
from pathlib import Path

import fl_mca
import fl_nbt
import fl_rewrite
import fl_sel
import fl_signs

BLOCK_IDS = ('command_block', 'chain_command_block', 'repeating_command_block', 'command_block_minecart')
HOLDERS = frozenset(BLOCK_IDS) | fl_signs.SIGN_IDS
UNREAD = ('lz4', 'externe', 'inconnu', 'corrompu', 'illisible')       # clés de stats = chunks NON analysés par fl_terrain
A_VERIFIER = ('sans_bloc', 'rc_hors_panneau', 'panneau_illisible')    # chunks analysés mais à regarder à la main
Found = namedtuple('Found', 'kind pos command auto file ref', defaults=(None,))     # pos : (x, y, z) entiers ; auto : « Toujours actif » (byte `auto`)
READ_ERRORS = (ValueError, struct.error, AttributeError, TypeError, RecursionError, zlib.error, OSError, EOFError)     # NBT illisible

DIM = 'mg:floaty'
_CMD = r'(?:^\s*/?|\brun\s+)'                 # position d'une commande : début de ligne ou derrière « run » (pas dans le texte d'un tellraw)
_CMD_FN = r'(?:^\s*/?|\b(?:run|if|unless)\s+)'    # idem + les conditions `execute if|unless function X`
_SET_VALUE = re.compile(r'\bCommand\s+set\s+value\s+(?=["\'])')      # data modify block ~ ~ ~ Command set value "..."
_IN = re.compile(r'(?<!\S)in\s+([a-z0-9_.-]+(?::[a-z0-9_./-]+)?)(?![\w.:/-])')      # `in <id de dimension>` (mot seul : pas `#in`), espace de noms facultatif
_TP = re.compile(_CMD + r'(?:tp|teleport)\s+\S')
_AT = re.compile(r'(?<![\w@])@[aeprn](?!\w)')      # repli quand fl_sel ne sait pas lire la ligne
_REGION = re.compile(r'r\.(-?\d+)\.(-?\d+)\.mca$')
# (nom, motif) : du plus grave au moins grave (l'ordre fixe aussi le tri des exemples du rapport). Les motifs s'appliquent au texte HORS
# chaînes (fl_sel.outside_strings) : « run stop » dans un tellraw n'est pas un stop ; les Command:"..." imbriquées sont classées à part.
RISKS = (
    ('stop', re.compile(_CMD + r'stop\b')),
    ('setworldspawn', re.compile(_CMD + r'setworldspawn\b')),
    ('gamerule', re.compile(_CMD + r'gamerule\b')),
    ('time', re.compile(_CMD + r'time\s+(?:set|add)\b')),
    ('weather', re.compile(_CMD + r'weather\b')),
    ('difficulty', re.compile(_CMD + r'difficulty\b')),
    ('defaultgamemode', re.compile(_CMD + r'defaultgamemode\b')),
    ('worldborder', re.compile(_CMD + r'worldborder\b')),
    ('tick', re.compile(_CMD + r'tick\b')),
    ('datapack', re.compile(_CMD + r'datapack\b')),
    ('reload', re.compile(_CMD + r'reload\b')),
    ('sauvegarde', re.compile(_CMD + r'save-(?:off|on|all)\b')),
    ('admin_serveur', re.compile(_CMD + r'(?:setidletimeout|debug|jfr|perf)\b')),
    ('admin_joueurs', re.compile(_CMD + r'(?:op|deop|ban|ban-ip|pardon|pardon-ip|kick|whitelist)\b')),
    ('tp_autre_dim', None),                   # tp / teleport + « in <autre dimension que mg:floaty> » (calculé par classify)
    ('in_autre_dim', None),                   # « in <autre dimension> » sans tp (setblock, fill, summon... dans l'overworld)
    ('fonction_vanilla', re.compile(_CMD_FN + r'function\s+#?(?:minecraft:|[^\s:]+(?:\s|$))')),     # sans espace de noms = minecraft:
    ('fonction_neomc', re.compile(_CMD_FN + r'function\s+#?mg:')),
    ('scoreboard_purge', re.compile(_CMD + r'scoreboard\s+(?:objectives\s+remove\b|players\s+reset\s+\*)')),
    ('advancement', re.compile(_CMD + r'advancement\s+revoke\b')),
    ('setdisplay', re.compile(_CMD + r'scoreboard\s+objectives\s+setdisplay\b')),
    ('schedule', re.compile(_CMD + r'schedule\s+(?:function|clear)\b(?!\s+floaty:sched/)')),     # floaty:sched/ : trampoline de gen_floaty
    ('say', re.compile(_CMD + r'say\s+\S')),
    ('selecteur_global', None),               # sélecteur sans borne de dimension (règle de fl_sel, voir _selecteur_global)
)
RISK_NAMES = tuple(n for n, _ in RISKS)


class _Probe:
    """Faux « stats » pour fl_sel.scan : retient qu'il a dû abandonner (chaîne ou crochet non fermé) et les @x laissés dans des chaînes."""
    def __init__(self):
        self.failed, self.str_skipped, self.str_examples = False, 0, []

    def warn(self, reason, line):
        self.failed = True


def _unescape(body, q):
    """Corps d'une chaîne NBT entre guillemets q -> texte (fl_rewrite.unescape) ; échappement inconnu (\\n, \\u...) : repli indulgent,
    \\n \\t \\r deviennent un espace, tout autre antislash est retiré (une seule passe : `\\\\n` reste un antislash puis « n »)."""
    text = fl_rewrite.unescape(body, q)
    return re.sub(r'\\(.)', lambda m: ' ' if m[1] in 'ntr' else m[1], body, flags=re.S) if text is None else text


def _set_values(cmd, probe):
    """Chaînes de `Command set value "..."` (data modify) -> [(début, fin, guillemet)] comme fl_sel.scan ; elles sont examinées comme niveau
    à part, donc leurs @x ne sont plus « non examinés »."""
    out = []
    for m in _SET_VALUE.finditer(cmd):
        end = fl_sel.skip_str(cmd, m.end())
        if end > 0:
            out.append((m.end() + 1, end - 1, cmd[m.end()]))
            if _AT.search(cmd[m.end() + 1:end - 1]):
                probe.str_skipped = max(0, probe.str_skipped - 1)
    return out


def levels(command):
    """La commande puis, déséchappées, chacune de ses `Command:"..."` / `Command set value "..."` imbriquées (récursif) -> [(texte, _Probe,
    spans de fl_sel)]."""
    out, todo = [], [command]
    while todo:
        cmd = todo.pop()
        probe = _Probe()
        spans, _, cmds = fl_sel.scan(cmd, probe)
        out.append((cmd, probe, spans))
        todo += [_unescape(cmd[a:b], q) for a, b, q in cmds + _set_values(cmd, probe)]
    return out


def _selecteur_global(cmd, probe, spans):
    """Vrai si un sélecteur du niveau n'est pas borné à la dimension de la source : même règle que L1 (fl_sel.fix_selector), joueurs
    (@a, @p/@r sans autre type) sans `tag=mg.flw`, entités sans argument de position ; @s jamais. Une ligne que fl_sel ne sait pas lire
    (chaîne / crochet non fermé) est signalée par prudence dès qu'elle contient un @a @e @n @p @r."""
    if probe.failed and _AT.search(cmd):
        return True
    return any(fl_sel.split_args(inner or '') is None or fl_sel.fix_selector(letter, inner)[0] is not None
               for _, _, letter, inner, _ in spans)


def _dim_id(m):
    """Correspondance de _IN -> id complet de la dimension (sans espace de noms : minecraft:)."""
    return m.group(1) if ':' in m.group(1) else 'minecraft:' + m.group(1)


def classify(command):
    """Texte d'une commande -> noms des risques qu'elle porte (dans l'ordre de gravité), [] si aucun. Les commandes `Command:"..."`
    imbriquées (setblock command_block{...}, summon command_block_minecart, data merge block) sont classées aussi : union dédupliquée.
    Un niveau que fl_sel ne sait pas lire (apostrophe hors guillemets : `if score l'ile ...`) vide le reste de la ligne : par prudence les
    motifs s'appliquent alors AUSSI au texte brut. Limite connue : deux apostrophes hors guillemets (`l'ile ... l'autre`) forment une
    « chaîne » fermée pour fl_sel, donc rien ne signale l'échec et le texte entre elles est vidé : un risque placé là n'est pas vu."""
    out = set()
    for cmd, probe, spans in levels(command):
        for text in ((fl_sel.outside_strings(cmd), cmd) if probe.failed else (fl_sel.outside_strings(cmd),)):
            out.update(n for n, rx in RISKS if rx is not None and rx.search(text))
        head = cmd[:fl_sel.text_start(cmd)]       # le texte libre d'un `msg` / `tell`... n'est pas une commande : `go back in overworld` n'est pas une dimension
        for text in ((fl_sel.outside_strings(head), head) if probe.failed else (fl_sel.outside_strings(head),)):
            if any(_dim_id(m) != DIM for m in _IN.finditer(text)):
                out.add('tp_autre_dim' if _TP.search(text) else 'in_autre_dim')
        if _selecteur_global(cmd, probe, spans):
            out.add('selecteur_global')
    return sorted(out, key=RISK_NAMES.index)


def string_selectors(command):
    """Nombre de @x laissés dans des chaînes autres que `"selector"` et `Command:` (non examinés), blocs imbriqués compris."""
    return sum(probe.str_skipped for _, probe, _ in levels(command))


def _content(root):
    """Ancien format (avant 1.18) : tout est sous `Level`."""
    level = root.get('Level')
    return level if isinstance(level, dict) else root


def _tile_entities(content):
    return list(content.get('block_entities') or []) + list(content.get('TileEntities') or [])      # TileEntities : avant 1.18


def _pos(be):
    return be.get('x', 0), be.get('y', 0), be.get('z', 0)


def _minecarts(entities, file, parent, out):
    """Entités -> out : command_block_minecart, passagers (`Passengers`, récursif) compris ; sans `Pos`, la position du porteur."""
    for e in entities:
        if not isinstance(e, dict):
            continue
        pos = [math.floor(v) for v in (e.get('Pos') or [])[:3]]
        pos = tuple(pos + [0] * (3 - len(pos))) if pos else parent
        if fl_signs.kind_of(e) == 'command_block_minecart':
            out.append(Found('command_block_minecart', pos, str(e.get('Command', '')), False, file, (e, 'Command')))
        _minecarts(e.get('Passengers') or [], file, pos, out)


def blocks_of(root, file=''):
    """Racine d'un chunk (NBT lu) -> [Found] : block entities (command_block, chain, repeating) et command_block_minecart."""
    root = _content(root)
    out = []
    for be in _tile_entities(root):
        if fl_signs.kind_of(be) in BLOCK_IDS:
            out.append(Found(fl_signs.kind_of(be), _pos(be), str(be.get('Command', '')), bool(be.get('auto', 0)), file, (be, 'Command')))
    _minecarts(root.get('Entities') or [], file, (0, 0, 0), out)
    return out


def signs_of(root, file=''):
    """Racine d'un chunk (NBT lu) -> ([Found], mal lu) : une trouvaille par commande `run_command` des panneaux (kind « sign[front,2] »...) ;
    mal lu = un panneau contient plus de `run_command` que de commandes extraites (voir fl_signs)."""
    out, bad = [], False
    for be in _tile_entities(_content(root)):
        kind = fl_signs.kind_of(be)
        if kind in fl_signs.SIGN_IDS:
            cmds, seen = fl_signs.sign_commands(be, kind)
            out += [Found(label, _pos(be), cmd, False, file) for label, cmd in cmds]
            bad = bad or fl_signs.count_outside(be, (fl_signs.RUN,), ())[0] > seen
    return out, bad


def _region_xz(name):
    """`r.X.Z.mca` -> (X, Z) ; (0, 0) si le nom n'a pas cette forme (les coordonnées sont alors relatives au fichier)."""
    m = _REGION.match(name)
    return (int(m[1]), int(m[2])) if m else (0, 0)


def chunk_where(label, index):
    """(fichier, cx, cz) du chunk `index` du fichier `label` (`dossier/r.X.Z.mca`) : chunk i du fichier : x = i % 32, z = i // 32."""
    rx, rz = _region_xz(label.rpartition('/')[2])
    return label, rx * 32 + index % 32, rz * 32 + index // 32


def prefilter(raw):
    """Vrai si le NBT brut d'un chunk contient « command_block » ou « run_command » : les autres ne sont jamais lus en entier."""
    return b'command_block' in raw or b'run_command' in raw


def scan_chunk(raw, label, index, stats, pending, root=None):
    """NBT brut du chunk `index` du fichier `label` (`dossier/r.X.Z.mca`) -> [Found] ; stats et pending (voir A_VERIFIER) mis à jour.
    [] si le pré-filtre ne trouve rien, ou si le chunk est illisible (stats['illisible']). root : l'arbre déjà lu (fl_nbt.loads_spans),
    sinon il est lu ici."""
    has_cb, has_rc = b'command_block' in raw, b'run_command' in raw
    if not (has_cb or has_rc):
        return []
    try:
        root = fl_nbt.loads(raw) if root is None else root
        blocks, (signs, bad_sign) = blocks_of(root, label), signs_of(root, label)
        cb_out, rc_out = fl_signs.count_outside(root, ('command_block', fl_signs.RUN), HOLDERS)
    except READ_ERRORS:
        stats['illisible'] += 1
        return []
    where = chunk_where(label, index)
    for key, hit in (('sans_bloc', (has_cb and not blocks) or cb_out > 0), ('rc_hors_panneau', rc_out > 0),
                     ('panneau_illisible', bad_sign)):
        if hit:
            stats[key] += 1
            pending[key].append(where)
    found = blocks + signs
    stats['sel_chaine'] += sum(string_selectors(f.command) for f in found)
    return found


def scan_file(path, stats):
    """Un .mca -> ([Found], pending) ; pending = {clé de A_VERIFIER: [(fichier, cx, cz)]}. Chunks illisibles et totaux dans stats ;
    le fichier n'est jamais modifié."""
    path = Path(path)
    label = f'{path.parent.name}/{path.name}'
    out, pending = [], {k: [] for k in A_VERIFIER}
    for i, raw in fl_mca.payloads(path.read_bytes(), stats):
        out += scan_chunk(raw, label, i, stats, pending)
    return out, pending
