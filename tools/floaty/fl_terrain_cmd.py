"""Réécriture, au build, d'UNE commande du terrain (bloc de commande, minecart, clic de panneau) de « Scourge of the Floaty Isles » : les
mêmes règles que pour les fonctions (fl_rewrite, L1), plus deux règles propres aux commandes figées dans le terrain (fonctions pures).

    ctx = fl_terrain_cmd.Ctx('minecraft:overworld')                # cache par commande distincte + effets ; dimension source de la carte
    new, action, reason = fl_terrain_cmd.rewrite_command(cmd, ctx)

action : 'inchange' (new None), 'reecrit' (new = la commande réécrite), 'noop' (new = NOOP : la commande est retirée), 'laisse' (new
None : la commande reste telle quelle, reason dit pourquoi). reason :
- laisse / 'non_analysable' : L1 ne sait pas la lire (chaîne non fermée, crochet déséquilibré, schedule inattendu, `say` avec @... : tout
  avertissement de fl_rewrite sauf celui de setdisplay, qui est retiré) : laissée telle quelle ET listée par le rapport, SAUF si elle
  contient un `in <dim>` (voir 'risque_dur' ci-dessous : alors NOOP) ;
- noop / 'eclate' : `advancement revoke|grant <cible> everything` HORS chaîne, quelle que soit la cible (@s compris : `everything` touche
  aussi les advancements mg:* et vanilla du joueur ; L1 le développe en une ligne par advancement racine de la carte, impossible dans une
  seule commande), à n'importe quel niveau : dans la commande, ou dans une `Command:"..."` / `Command set value "..."` imbriquée
  (fl_terrain.levels, récursif ; le texte d'une autre chaîne, un tellraw par exemple, n'est pas une commande) ; ou L1 rend plusieurs
  lignes : retirée, listée par le rapport (« Non reecrits ») ;
- noop / 'retiree' (time set|add, gamerule advance_time|random_tick_speed : état global), 'auteur' (LordDrewpicus hors chaîne : testé AVANT
  `everything`), 'setdisplay', ou 'risque_dur' : après réécriture, il reste un risque DUR (HARD : tout ce qui change l'état du serveur
  entier, gamerule compris : un gamerule est global, `in mg:floaty` n'y change rien ; `in <autre dimension>`, avec ou sans tp). Les
  références à la dimension SOURCE de la carte (ctx.dim) dans `in <dim>`, `if|unless dimension <dim>` et la cible des boussoles sont réécrites
  `mg:floaty` par L1 (fl_rewrite.Stats.own_dim) ; le texte libre d'un `msg` / `tell` / `w` / `me` / `teammsg` / `tm` n'est ni réécrit ni classé
  (fl_sel.text_start). Pour une commande ANALYSABLE, seules les AUTRES dimensions de `in <dim>` restent un risque dur (un `if|unless dimension
  <autre>` est un test sans effet : laissé tel quel). Une commande NON analysable n'est pas réécrite : tout `in <dim>` qu'elle contient,
  dimension source comprise, reste un risque dur (fl_terrain.classify ne voit que `mg:floaty` comme sûre) et la commande devient un NOOP
  `risque_dur` ; voulu, car laissée telle quelle elle viserait le lobby (`in minecraft:overworld`) ;
- reecrit / 'selecteur_residuel' : réécrite, mais il reste un sélecteur non borné que L1 ne sait pas confiner (listé par le rapport).
Les commandes imbriquées (`Command:"..."` de setblock, summon, data merge) sont réécrites par L1 (récursif) puis reclassées par
fl_terrain.classify (récursif aussi). LIMITE : les chaînes `data modify block ~ ~ ~ Command set value "..."` sont classées et leur
`everything` détecté, mais PAS réécrites (seul `Command:"..."` l'est) : une valeur avec `execute in minecraft:overworld` devient un NOOP
`risque_dur` (la commande entière), une valeur avec `say` reste globale (signalée par le rapport, inchangée). La commande `schedule function X` devient `schedule function floaty:sched/<ns>/<chemin>` : le
trampoline correspondant est généré par gen_floaty (liste terrain_sched.txt écrite par build_terrain, voir ctx.sched). Les espaces de
tête puis le `/` d'une commande sont retirés avant L1 ; le `/` est remis après (les espaces de tête d'une commande réécrite sont perdus).
ctx.fx[cmd] : Counter des effets (tag, distance, say, retire, fall, dim, revoke, imbrique, last_output, auteur, setdisplay) ;
ctx.sched[cmd] : cibles `schedule function` de la commande (utiles si elle est réécrite).
"""
import re
from collections import Counter

import fl_rewrite as R
import fl_sel
import fl_terrain

HARD = frozenset(('stop', 'setworldspawn', 'gamerule', 'time', 'weather', 'difficulty', 'defaultgamemode', 'worldborder', 'tick',
                  'datapack', 'reload', 'admin_joueurs', 'admin_serveur', 'sauvegarde',
                  'in_autre_dim', 'tp_autre_dim'))        # risques qui touchent le serveur entier ou une autre dimension que mg:floaty
_INFO = ('scoreboard objectives setdisplay',)      # avertissements de fl_rewrite qui ne disent pas « non analysable » : la commande est retirée
_EVERYTHING = re.compile(r'(?:^\s*[/$]?\s*|\brun\s+)advancement\s+(?:revoke|grant)\s+.+?\s+everything\b')     # en position de commande : pas le texte d'un `say`
_EFFECTS = (('tag', 'sel_player'), ('distance', 'sel_entity'), ('say', 'says'), ('retire', 'neutral'), ('fall', 'falls'),
            ('dim', 'dims'), ('revoke', 'revokes'), ('imbrique', 'blocks'), ('last_output', 'last_output'), ('auteur', 'dropped'),
            ('setdisplay', 'setdisplay'))            # (clé de ctx.fx, compteur de fl_rewrite.Stats)


class Ctx:
    """Cache par commande distincte (le terrain en répète beaucoup) et effets : voir l'en-tête. dim : id de la dimension SOURCE de la carte
    (build_terrain : `minecraft:overworld`) ; ses références `in <dim>` deviennent `in mg:floaty` (sans dim : aucune, donc NOOP si une reste)."""

    def __init__(self, dim=None):
        self.cache, self.fx, self.sched = {}, {}, {}
        self.dim, self.own_dim = dim, R.source_dim(dim) if dim else None


def _hard(text):
    return [n for n in fl_terrain.classify(text) if n in HARD]


def _noop(slash, reason):
    return ('/' if slash else '') + R.NOOP, 'noop', reason


def _record(ctx, cmd, st):
    ctx.fx[cmd] = Counter({k: getattr(st, a) for k, a in _EFFECTS if getattr(st, a)})
    ctx.sched[cmd] = frozenset(st.sched)


def _decide(cmd, ctx):
    text = cmd.lstrip()
    slash = text.startswith('/')
    body = text[1:] if slash else text
    outside = fl_sel.outside_strings(body)                       # les règles ci-dessous ignorent le texte des chaînes (un tellraw n'est pas un ordre)
    if R.AUTHOR in outside:                                      # avant `everything` : une ligne de l'auteur est retirée, quelle que soit la commande
        return _noop(slash, 'auteur')
    if any(_EVERYTHING.search(fl_sel.outside_strings(t)) for t, _, _ in fl_terrain.levels(body)):      # la commande, puis chaque Command:"..." /
        return _noop(slash, 'eclate')                            # Command set value "..." imbriquée : `everything` touche aussi les advancements mg:* et vanilla
    st = R.Stats()
    st.own_dim = ctx.own_dim
    lines = R.rewrite_line(body, [], st)
    _record(ctx, cmd, st)
    if any(not why.startswith(_INFO) for why, _ in st.unsafe):      # non analysable : non réécrite ; un `in <dim>` (même la source) = NOOP
        return _noop(slash, 'risque_dur') if _hard(body) else (None, 'laisse', 'non_analysable')
    if not lines:
        return _noop(slash, 'auteur' if st.dropped else 'setdisplay' if st.setdisplay else 'retiree')
    if len(lines) > 1:
        return _noop(slash, 'eclate')
    risks = fl_terrain.classify(lines[0])
    if any(r in HARD for r in risks):
        return _noop(slash, 'risque_dur')
    residual = 'selecteur_residuel' if 'selecteur_global' in risks else None
    if lines[0] == body.rstrip('\r\n'):
        return None, 'inchange', residual
    return ('/' if slash else '') + lines[0], 'reecrit', residual


def rewrite_command(cmd, ctx):
    """Commande -> (nouvelle commande ou None, action, raison) : voir l'en-tête du module."""
    if cmd not in ctx.cache:
        ctx.cache[cmd] = _decide(cmd, ctx)
    return ctx.cache[cmd]
