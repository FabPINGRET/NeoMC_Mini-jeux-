"""Rattrapage d'un joueur qui entre (ou revient) dans la partie COMMUNE de la carte « Scourge of the Floaty Isles » (fonctions pures).

    reg = fl_catchup.Registry()
    lines = fl_catchup.instrument('dungeon:1/start', lines_reecrites, reg)     # + marqueurs ; après tous les fichiers :
    fns = fl_catchup.functions(reg, spawn)                                      # {chemin sous mg/function : lignes} : floaty/cu/*

Une seule partie pour tout le serveur : celui qui arrive doit retrouver l'état du groupe. L'état est repéré par INSTRUMENTATION des
fonctions de la carte (les lignes de la carte ne sont jamais changées, on ajoute une ligne-témoin juste après) :
- point de contrôle : chaque `spawnpoint @a[tag=mg.flw] x y z [yaw pitch]` (43 sites) reçoit, avec le MÊME préfixe `execute ... run`
  (donc les mêmes conditions), `scoreboard players set $flsp mg.st K` ; K = n° du point (coordonnées distinctes, ordre de lecture) ;
  $flsp = 0 : aucun point. `spawnpoint @s` (game:join, individuel) n'est pas suivi ;
- avancements du groupe : chaque `advancement grant @a[tag=mg.flw] only <id>` pose `scoreboard players set $fla<N> mg.fla 1`
  (N = n° de l'avancement). Les `@s` / `@p` (individuels) et les `through` (debug) ne sont pas suivis ;
- un préfixe contenant `store` ne peut pas être dupliqué sans changer le résultat : la ligne est comptée (Registry.skipped), pas suivie ;
- game:initialize (nouvelle partie) remet $flsp et les drapeaux à zéro.
Objets clés (arc, amulette...) : AUCUNE source fiable dans le datapack — les drapeaux `Inventory <Objet>` ne sont jamais mis à 1 par une
fonction, ce sont des blocs de commande du TERRAIN (L5) qui les posent et remplissent le « coffre de récupération » de la carte. Rien
n'est redonné ici : le coffre de la carte et le coffre Floaty du joueur (mg:floaty/vault_*) couvrent les objets.
Fonctions générées (appelées par mg:floaty/enter et core/reconnect) :
- floaty/cu/run : @s, vie max = 2 x compteur de cœurs (`Inventory HeartContainers`), point de réapparition, avancements du groupe ;
  sans effet sur la partie elle-même tant qu'elle n'a pas commencé (`mainstory Story` < 0) sauf le point de réapparition ;
- floaty/cu/tp : @s au dernier point de contrôle du groupe, ou au spawn de la carte s'il n'y en a pas ;
- floaty/cu/hp : macro (h) pour la vie max.
"""
import re

FLAGS = 'mg.fla'                  # objectif : un faux joueur $fla<N> par avancement
POINT = '$flsp'                   # faux joueur de mg.st : dernier point de contrôle (0 = aucun)
_NUM = r'-?\d+(?:\.\d+)?'
_PRE = r'(?P<pre>\$?(?:execute .* run )?)'
_SPAWNPOINT = re.compile(_PRE + r'spawnpoint @a\[tag=mg\.flw\] (?P<args>-?\d+ -?\d+ -?\d+(?: ' + _NUM + ' ' + _NUM + r')?)$')
_GRANT = re.compile(_PRE + r'advancement grant @a\[tag=mg\.flw\] only (?P<id>[a-z0-9_.-]+:[a-z0-9_./-]+)$')
RESET = ['scoreboard players set $flsp mg.st 0', f'scoreboard players reset * {FLAGS}']     # game:initialize (nouvelle partie)
INITIALIZE = 'game:initialize'


class Registry:
    """Points de contrôle et avancements rencontrés (un objet partagé par tous les fichiers d'un passage)."""

    def __init__(self):
        self.points = {}              # 'x y z [yaw pitch]' -> K (1..)
        self.advancements = {}        # id -> N (1..)
        self.spawn_sites = self.grant_sites = 0
        self.skipped = []             # lignes non suivies (préfixe avec `store`)
        self.other = []               # spawnpoint / grant @a[tag=mg.flw] d'une autre forme (ex. cible plus précise) : non suivis

    def counts(self):
        return {'spawn_sites': self.spawn_sites, 'checkpoints': len(self.points), 'grant_sites': self.grant_sites,
                'advancements': len(self.advancements), 'skipped': len(self.skipped), 'other': len(self.other)}


def _index(table, key):
    return table.setdefault(key, len(table) + 1)


def _marker(line, reg):
    """Ligne-témoin de `line`, ou None (ligne sans intérêt, ou non suivie et enregistrée dans reg)."""
    if 'spawnpoint ' in line or 'advancement grant @a[' in line:
        m = _SPAWNPOINT.match(line)
        g = _GRANT.match(line)
        hit = m or g
        if not hit:
            if 'spawnpoint @a[' in line or 'advancement grant @a[' in line:
                reg.other.append(line)
            return None
        if hit.group('pre').count(' store '):
            reg.skipped.append(line)
            return None
        if m:
            reg.spawn_sites += 1
            return f'{m.group("pre")}scoreboard players set {POINT} mg.st {_index(reg.points, m.group("args"))}'
        reg.grant_sites += 1
        return f'{g.group("pre")}scoreboard players set $fla{_index(reg.advancements, g.group("id"))} {FLAGS} 1'
    return None


def instrument(fn_id, lines, reg):
    """Lignes (déjà réécrites pour mg:floaty) de la fonction fn_id -> mêmes lignes + témoins ; reg est mis à jour."""
    out = []
    for l in lines:
        out.append(l)
        mk = _marker(l, reg)
        if mk:
            out.append(mk)
    if fn_id == INITIALIZE:
        out += RESET
    return out


def _tp(args):
    """'x y z [yaw pitch]' (coordonnées de bloc) -> arguments de tp : centre du bloc, même orientation."""
    p = args.split()
    return ' '.join([f'{int(p[0]) + 0.5}', p[1], f'{int(p[2]) + 0.5}'] + p[3:])


def functions(reg, spawn):
    """{chemin sous data/mg/function : lignes} des fonctions de rattrapage (spawn = (x, y, z) entiers de la carte)."""
    sx, sy, sz = spawn
    head = '# généré par tools/floaty/fl_catchup.py : ne pas éditer'
    pts = sorted((k, a) for a, k in reg.points.items())
    run = [f'# Rattrape la partie commune pour @s (contexte quelconque) ; {head}',
           f'execute unless score {POINT} mg.st matches 1.. in mg:floaty run spawnpoint @s {sx} {sy} {sz}'] + \
          [f'execute if score {POINT} mg.st matches {k} in mg:floaty run spawnpoint @s {a}' for k, a in pts] + \
          ['# partie pas commencée : rien d\'autre à rattraper (mainstory Story = -1 à l\'installation)',
           'execute unless score mainstory Story matches 0.. run return 0',
           '# vie max = 2 x cœurs du groupe',
           'execute if score Inventory HeartContainers matches 1.. store result storage mg:floaty cu.h int 2 run scoreboard players get Inventory HeartContainers',
           'execute if score Inventory HeartContainers matches 1.. run function mg:floaty/cu/hp with storage mg:floaty cu',
           '# avancements déjà accordés au groupe'] + \
          [f'execute if score $fla{n} {FLAGS} matches 1 run advancement grant @s only {adv}' for adv, n in sorted(reg.advancements.items(), key=lambda e: e[1])]
    tp = [f'# @s au dernier point de contrôle du groupe, sinon au spawn de la carte ; {head}'] + \
         [f'execute if score {POINT} mg.st matches {k} in mg:floaty run tp @s {_tp(a)}' for k, a in pts] + \
         [f'execute unless score {POINT} mg.st matches 1.. in mg:floaty run tp @s {sx + 0.5} {sy} {sz + 0.5}']
    return {'floaty/cu/run': run, 'floaty/cu/tp': tp,
            'floaty/cu/hp': ['# macro (h) : vie max de @s', '$attribute @s minecraft:max_health base set $(h)']}
