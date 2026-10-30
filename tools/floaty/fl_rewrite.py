"""Cantonne une ligne de .mcfunction de la carte « Scourge of the Floaty Isles » à la dimension mg:floaty (fonctions pures).

    lines = fl_rewrite.rewrite_line(ligne, roots, stats)     # 0, 1 ou N lignes (la ligne est retirée ou éclatée)

Tout tourne `in mg:floaty` (L3 pose la position et la dimension). Les sélecteurs sont confinés par fl_sel (joueurs : tag=mg.flw ;
entités : distance=0.. ; @s intact ; voir fl_sel). Ici, les commandes :
- propriétés NBT `LastOutput:'...'` (dernier message d'un bloc de commande : bruit, UUID de l'auteur) : retirées d'abord de la ligne.
- ligne contenant LordDrewpicus (pseudo de l'auteur, commandes de debug) HORS chaîne entre guillemets : retirée. Dans une chaîne
  (texte d'un tellraw, valeur NBT) la commande est fonctionnelle : conservée.
- `scoreboard objectives setdisplay ...` : retirée (global au serveur : écraserait le tableau des mini-jeux), comptée et signalée.
- `say X` (serveur entier) : `tellraw @a[tag=mg.flw] "X"` (JSON échappé).
- `advancement revoke <cible> everything` : un `revoke ... from <racine>` par advancement racine de la carte (roots), sans toucher aux vanilla.
- `gamerule fall_damage <bool>` : ATTRIBUT fall_damage_multiplier (0 / 1) des joueurs de la dimension. Choix prudent : on ne sait pas
  vérifier en jeu que ce gamerule est par dimension. `attribute` n'accepte qu'UNE cible : `execute as @a[tag=mg.flw] run attribute @s ...`
  (un `attribute @a[...]` échoue dès que deux joueurs sont dans la dimension). NOTE POUR L3 : ce choix pose l'attribut sur les joueurs, donc L3 doit le remettre
  (comme core/attr_reset ou <jeu>/leave : `attribute @s minecraft:fall_damage_multiplier base set 0`) quand le joueur quitte mg:floaty.
  `gamerule advance_time|random_tick_speed` et `time set|add` : RETIRÉS (st.neutral). Prouvé sur un serveur 26.2 : un gamerule est GLOBAL
  (`execute in <dim> run gamerule advance_time false` change aussi l'overworld) et `time set` agit sur l'horloge du type de dimension
  (mg:floaty est de type minecraft:overworld : même horloge que le lobby / la survie). Les poser tels quels figerait / décalerait le temps
  de tout le serveur. `time query` (lecture seule) et les autres gamerule : préfixés `execute in mg:floaty` (aucun autre dans la carte).
  Dans un bloc de commande `Command:"..."`, la commande retirée est remplacée par NOOP (jamais laissée telle quelle).
- `dimension:"minecraft:overworld"` (cible des boussoles lodestone_tracker) : `dimension:"mg:floaty"`.
- terrain seulement (Stats.own_dim, fl_terrain_cmd.Ctx) : `in <dimension source>` et `if|unless dimension <dimension source>` hors chaînes et hors
  texte libre d'un `tell` / `msg` / `w` / `me` / `teammsg` / `tm` (fl_sel.text_start) : `mg:floaty` ; la boussole suit la même dimension source.
- `schedule function|clear X` : devient floaty:sched/<ns>/<chemin>, un trampoline généré qui relance X `in mg:floaty positioned <spawn>`
  (une fonction planifiée tourne sinon dans l'overworld, à la position du spawn du monde).
- chaînes `Command:"/..."` / `Command:'...'` (blocs de commande posés par setblock) : déséchappées, réécrites comme une ligne, ré-échappées.
- lignes de macro (`$...`) : mêmes règles, le `$` est conservé.
Les motifs non traités sûrement (chaîne non fermée, crochet déséquilibré, schedule inattendu...) vont dans Stats.unsafe via warn().
"""
import json
import re
from collections import Counter, namedtuple

import fl_sel

TAG = fl_sel.TAG
DIM = 'mg:floaty'
AUTHOR = 'LordDrewpicus'
_OVERWORLD = re.compile(r'\bdimension:"minecraft:overworld"')
_SCHED = re.compile(r'schedule (function|clear) ([a-z0-9_.-]+:[a-z0-9_./-]+)(.*)$')       # l'id est ensuite validé par segment : valid_function_id
_SEGMENT = re.compile(r'[a-z0-9_.-]+')
_GLOBAL = re.compile(r'(gamerule (advance_time|random_tick_speed)|time (set|add))\b')     # état global du serveur : jamais rejoué tel quel
NOOP = 'scoreboard players add #fl_noop mg.st 0'     # commande sans effet qui remplace une commande retirée dans un bloc de commande
fix_selector = fl_sel.fix_selector


class Stats:
    """Compteurs d'une exécution (un objet partagé par tous les appels d'un même passage du générateur)."""

    def __init__(self):
        self.lines = self.dropped = self.sel_player = self.sel_entity = self.sel_json = 0
        self.falls = self.times = self.revokes = self.str_skipped = self.dims = 0
        self.setdisplay = self.says = self.blocks = self.announce = self.last_output = self.neutral = 0
        self.criteria = self.criteria_total = 0     # advancements : critères auxquels la condition de dimension est ajoutée / critères vus
        self.gamerules = Counter()      # commande gamerule complète -> occurrences (rapport : liste distincte)
        self.sched = set()              # fonctions planifiées (un trampoline chacune)
        self.unsafe = []                # (raison, ligne) : avertissements
        self.invalid = []               # fichiers écartés (chemin d'id de ressource invalide), rempli par gen_floaty
        self.str_examples = []
        self.tr = None                  # fl_tr.Stats de la traduction française (posé par gen_floaty, qui traduit APRÈS la réécriture) ; None : aucune
        self.own_dim = None             # SourceDim (source_dim) : références à la dimension source à ramener à mg:floaty ; None : fonctions de la carte

    def warn(self, why, line):
        self.unsafe.append((why, line))


SourceDim = namedtuple('SourceDim', 'rx_in rx_compass')


def source_dim(dim_id):
    """Id de la dimension source de la carte (`minecraft:overworld`) -> SourceDim : rx_in = `in <dim>`, `if|unless dimension <dim>` (groupe 1 :
    le début, conservé ; forme courte `overworld` comprise), rx_compass = `dimension:"<dim>"` (cible d'une boussole). Terrain seulement."""
    names = [dim_id] + ([dim_id[len('minecraft:'):]] if dim_id.startswith('minecraft:') else [])
    alt = '|'.join(re.escape(n) for n in names)
    return SourceDim(re.compile(r'(?<!\S)(in|(?:if|unless)\s+dimension)\s+(?:' + alt + r')(?![\w.:/-])'),
                     re.compile(r'\bdimension:"(?:' + alt + r')"'))


def valid_function_id(fn):
    """`ns:chemin` dont l'espace de noms et chaque segment du chemin (séparés par /) sont [a-z0-9_.-]+ et ni vides, ni `.`, ni `..`, ni
    terminés par un point (Windows retire le point final : deux ids donneraient le même fichier) : le trampoline floaty:sched/<ns>/<chemin>
    ne peut pas sortir de data/floaty/function/sched/ (le nom sert de chemin de fichier)."""
    ns, sep, path = fn.partition(':')
    return bool(sep) and all(_SEGMENT.fullmatch(s) and s not in ('.', '..') and not s.endswith('.') for s in [ns] + path.split('/'))


def sched_name(fn):
    """Id d'une fonction -> id du trampoline : boss:1/cutscene/2 -> floaty:sched/boss/1/cutscene/2."""
    ns, _, path = fn.partition(':')
    return f'floaty:sched/{ns}/{path}'


def trampoline(fn, spawn):
    x, y, z = spawn
    return [f'# relance {fn} dans {DIM} (un schedule tourne dans l\'overworld, à la position du spawn du monde)',
            f'execute in {DIM} positioned {x} {y} {z} run function {fn}']


def _cmd_start(s):
    """Index de la commande finale (après le dernier ' run ', après un éventuel $ de macro)."""
    runs = fl_sel.scan(s)[1]
    return runs[-1] if runs else (1 if s.startswith('$') else 0)


def in_dim(s):
    """Préfixe `execute in mg:floaty` (fusionné dans un execute existant, conserve le $ des macros)."""
    pre, body = ('$', s[1:]) if s.startswith('$') else ('', s)
    body = body.lstrip()
    if body.startswith('execute '):
        return f'{pre}execute in {DIM} {body[8:]}'
    return f'{pre}execute in {DIM} run {body}'


def _revoke(s, roots, st):
    m = re.search(r'advancement (revoke|grant) (.+?) everything\s*$', s)
    if not m:
        return [s]
    pre = s[:m.start()]
    if m.group(1) != 'revoke' or not (pre in ('', '$') or pre.endswith(' run ')):
        st.warn('advancement ... everything non géré', s)
        return [s]
    st.revokes += 1
    return [f'{pre}advancement revoke {m.group(2)} from {r}' for r in roots]


def _command(s, st):
    """gamerule / time / schedule / say / setdisplay (commande finale de la ligne). None = ligne à retirer."""
    k = _cmd_start(s)
    cmd = s[k:]
    if cmd.startswith('scoreboard objectives setdisplay '):
        st.setdisplay += 1
        st.warn('scoreboard objectives setdisplay retiré (global au serveur)', s)
        return None
    if cmd.startswith('say '):
        st.says += 1
        if '@' in cmd:
            st.warn('say avec @ dans le message (tellraw ne résout pas les sélecteurs)', s)
        return f'{s[:k]}tellraw @a[tag={TAG}] {json.dumps(cmd[4:], ensure_ascii=False)}'
    m = re.fullmatch(r'gamerule fall_damage (true|false)\s*', cmd)
    if m:
        st.falls += 1
        return s[:k] + f'execute as @a[tag={TAG}] run attribute @s minecraft:fall_damage_multiplier base set {int(m.group(1) == "true")}'
    if cmd.startswith('gamerule '):
        st.gamerules[cmd.strip()] += 1
    if _GLOBAL.match(cmd):
        st.neutral += 1
        return None
    if cmd.startswith('gamerule '):
        return in_dim(s)
    if re.match(r'time query\b', cmd):
        st.times += 1
        return in_dim(s)
    if cmd.startswith('schedule '):
        m = _SCHED.match(cmd)
        if not m or not valid_function_id(m.group(2)):               # `..` ou segment vide : refusé (ligne laissée, avertissement)
            st.warn('schedule inattendu', s)
            return s
        if m.group(1) == 'function':
            st.sched.add(m.group(2))
        return f'{s[:k]}schedule {m.group(1)} {sched_name(m.group(2))}{m.group(3)}'
    return s


def unescape(body, q):
    """Corps d'une chaîne NBT entre guillemets q -> texte ; None si un échappement autre que \\\\ et \\q (public : fl_terrain l'utilise)."""
    out, i = [], 0
    while i < len(body):
        if body[i] == '\\':
            if i + 1 >= len(body) or body[i + 1] not in ('\\', q):
                return None
            out.append(body[i + 1])
            i += 2
        else:
            out.append(body[i])
            i += 1
    return ''.join(out)


def _blocks(s, roots, st):
    """Réécrit les commandes `Command:"..."` des blocs de commande (récursif : chaque commande est une ligne)."""
    out, last = [], 0
    for a, b, q in fl_sel.scan(s)[2]:
        cmd = unescape(s[a:b], q)
        if cmd is None:
            st.warn('Command : échappement inconnu', s)
            continue
        slash = cmd.startswith('/')
        new = _rewrite(cmd[1:] if slash else cmd, roots, st)
        if not new:                                  # commande retirée (global au serveur) : jamais laissée dans le bloc
            new = [NOOP]
        if len(new) != 1:
            st.warn('Command : commande retirée ou éclatée', s)
            continue
        text = ('/' if slash else '') + new[0]
        if text != cmd:
            out += [s[last:a], text.replace('\\', '\\\\').replace(q, '\\' + q)]
            last = b
            st.blocks += 1
    return ''.join(out) + s[last:]


def _rewrite(s, roots, st):
    if not s.strip() or s.lstrip().startswith('#'):
        return [s]
    s = fl_sel.apply(s, st)
    s = _command(s, st)
    if s is None:
        return []
    own = st.own_dim                                      # terrain : la dimension source de la carte ; fonctions : None (overworld)
    s, n = (own.rx_compass if own else _OVERWORLD).subn(f'dimension:"{DIM}"', s)     # boussoles (lodestone_tracker) : cible dans la dimension de la carte
    st.dims += n
    if own is not None:                                   # `in <dimension source>` hors chaînes désigne la carte elle-même
        k = fl_sel.text_start(s)                          # sauf le texte libre d'un `msg` / `tell`... : `go back in overworld` reste du texte
        head, n = fl_sel.sub_outside(own.rx_in, rf'\1 {DIM}', s[:k])
        s = head + s[k:]
        st.dims += n
    return _revoke(_blocks(s, roots, st), roots, st)


def rewrite_line(line, roots, st=None):
    """Une ligne de la carte -> liste de lignes pour mg:floaty (vide = ligne retirée). Commentaires et lignes vides inchangés."""
    st = st or Stats()
    s = line.rstrip('\r\n')
    st.lines += 1
    bare = fl_sel.strip_last_output(s)
    st.last_output += bare != s
    s = bare
    if AUTHOR in fl_sel.outside_strings(s):
        st.dropped += 1
        return []
    return _rewrite(s, roots, st)
