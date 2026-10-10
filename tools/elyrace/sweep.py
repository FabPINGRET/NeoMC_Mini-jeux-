"""Detection BALAYEE des anneaux : le joueur est suivi d'un tick a l'autre (origine = sa position au tick precedent), et un anneau est
franchi quand le segment origine -> position coupe le plan de l'anneau DANS son trou. Un anneau d'un bloc d'epaisseur ne peut pas etre
saute meme a grande vitesse (l'ancien volume dx=BOX_X a x-1..x+4 devait couvrir le deplacement maximal par tick).
Tous les plans sont normaux a x et franchis vers +x : le plan d'un anneau de bloc x est P = 100 * x + 50 (milieu du cadre d'un bloc, en
centiemes de bloc comme speed). Unites : centiemes de bloc, scores de mg.st et du joueur (mg.xq1..3 = origine x, y, z).
Fonctions generees : elyrace/sweep (@s = joueur en course, en tete de c<N>/rings : lit l'origine et la position, memorise la position) et
elyrace/cross (macro : #xhit = 1 si le segment coupe le plan p dans le trou yl..yh x zl..zh). hits() est le jumeau Python de ce calcul
(meme arithmetique : floor(v * 100), et // = floorDiv, comme la division de scores de Minecraft) : verify.py s'en sert pour
decider si un vol franchit un anneau. Python stdlib uniquement (compatible 3.8).
"""
import math

STEP_MAX = 1900          # deplacement maximal accepte entre deux ticks (centiemes, 19 blocs) : au-dela c'est une teleportation, sans anneau franchi ;
                         # couvre les rafales du serveur (3 a 4 ticks a vitesse max (4 b/tick) d'un coup), et reste sous l'ecart min de 20 blocs entre deux plans
FAR = 2147483647         # « pas d'origine » : plus grand que tout plan, la condition #xox ..P-1 echoue
ORIGIN_RESET = -1000000  # valeur de mg.xq1 apres une teleportation (reapparition, place) : le tick suivant n'a pas d'origine valide
RESET_LINE = 'scoreboard players set @s mg.xq1 %d' % ORIGIN_RESET      # rings.respawn et place_tp ; verifie par checks.gravity_problems
HOLE_R = 4               # rayon du trou des anneaux obligatoires (9 x 9 blocs) ; les anneaux d'or et de vent : GOLD_R (7 x 7)
GOLD_R = 3


def plane(x):
    """Plan de l'anneau de bloc x, en centiemes."""
    return 100 * x + 50


def bounds(cy, cz, r):
    """Bornes (centiemes, incluses) du trou de rayon r centre sur le bloc (cy, cz) : pieds en y (le centre du joueur, 0,3 plus haut, doit
    etre dans le trou), z du joueur. Trou de 9 blocs (r = 4) : y de cy - 4 a cy + 4,999 pour le centre."""
    return {'yl': 100 * (cy - r) - 30, 'yh': 100 * (cy + r + 1) - 31, 'zl': 100 * (cz - r), 'zh': 100 * (cz + r + 1) - 1}


def _cent(p):
    return [int(math.floor(v * 100)) for v in p[:3]]


def hits(a, b, x, cy, cz, r):
    """True si le tick a -> b (positions des pieds, x y z en tete du tuple) franchit le plan de l'anneau x dans son trou de rayon r."""
    (ox, oy, oz), (qx, qy, qz) = _cent(a), _cent(b)
    p, qd = plane(x), qx - ox
    if not 1 <= qd <= STEP_MAX or not ox < p <= qx:
        return False
    ta = p - ox
    iy = (qy - oy) * ta // qd + oy              # // = floorDiv, comme la division de scores
    iz = (qz - oz) * ta // qd + oz
    bd = bounds(cy, cz, r)
    # Minecraft deplace d'abord en Y, puis sur l'axe horizontal le plus long, puis sur l'autre : le trajet reel passe par (iy, iz) (segment droit)
    # mais aussi par (qy, oz) et (qy, qz) ; un seul de ces trois points dans le trou suffit
    return any(bd['yl'] <= y <= bd['yh'] and bd['zl'] <= z <= bd['zh'] for y, z in ((iy, iz), (qy, oz), (qy, qz)))


def ring_lines(x, cy, cz, r, cond, runs):
    """Lignes d'un anneau de plan x : un appel de cross, puis chaque commande de `runs` si le trou est traverse. `cond` = condition
    `if score @s ...` propre a l'anneau (numero attendu, anneau d'or pas encore pris). La garde sur l'origine et la position evite
    l'appel de la macro presque tout le temps."""
    p, bd = plane(x), bounds(cy, cz, r)
    guard = 'execute %s if score #xox mg.st matches ..%d if score #xqx mg.st matches %d..' % (cond, p - 1, p)
    out = [guard + ' run function mg:elyrace/cross {p:%d,yl:%d,yh:%d,zl:%d,zh:%d}' % (p, bd['yl'], bd['yh'], bd['zl'], bd['zh'])]
    return out + [guard + ' if score #xhit mg.st matches 1 run ' + run for run in runs]


def sweep_lines():
    out = ['# @s = joueur en course (en tete de c<N>/rings) : origine du balayage (position du tick precedent, mg.xq1..3) dans #xox..#xoz,',
           '# position courante (centiemes) dans #xqx..#xqz, puis memorisee comme origine du tick suivant']
    out += ['scoreboard players operation #xo%s mg.st = @s mg.xq%d' % (a, i) for i, a in enumerate('xyz', 1)]
    out += ['execute store result score #xq%s mg.st run data get entity @s Pos[%d] 100' % (a, i) for i, a in enumerate('xyz')]
    out += ['scoreboard players operation @s mg.xq%d = #xq%s mg.st' % (i, a) for i, a in enumerate('xyz', 1)]
    return out + ['scoreboard players set #xhit mg.st 0',
                  'scoreboard players operation #xqd mg.st = #xqx mg.st',
                  'scoreboard players operation #xqd mg.st -= #xox mg.st',
                  '# deplacement hors de 1..%d centiemes (teleportation, premier tick, retour en arriere) : aucun anneau franchi ce tick' % STEP_MAX,
                  'execute unless score #xqd mg.st matches 1..%d run scoreboard players set #xox mg.st %d' % (STEP_MAX, FAR)]


def cross_lines():
    out = ['# macro : $(p) = plan de l\'anneau (x, centiemes), $(yl)..$(yh) et $(zl)..$(zh) = trou (voir sweep.bounds) ; appelee seulement quand',
           '# l\'origine #xox est avant le plan et la position #xqx apres (donc #xqd >= 1). #xhit = 1 si le segment origine -> position coupe le trou',
           'scoreboard players set #xhit mg.st 0',
           '$scoreboard players set #xta mg.st $(p)',
           'scoreboard players operation #xta mg.st -= #xox mg.st']
    for a in 'yz':
        out += ['scoreboard players operation #xi%s mg.st = #xq%s mg.st' % (a, a), 'scoreboard players operation #xi%s mg.st -= #xo%s mg.st' % (a, a),
                'scoreboard players operation #xi%s mg.st *= #xta mg.st' % a, 'scoreboard players operation #xi%s mg.st /= #xqd mg.st' % a,
                'scoreboard players operation #xi%s mg.st += #xo%s mg.st' % (a, a)]
    out += ['# ordre de deplacement de Minecraft (Y, puis axe horizontal le plus long, puis autre axe) : trois points du trajet testes, comme sweep.hits',
            '# (#xiy,#xiz) = point du segment droit ; (#xqy,#xoz) et (#xqy,#xqz) = trajets en equerre']
    return out + ['$execute if score %s mg.st matches $(yl)..$(yh) if score %s mg.st matches $(zl)..$(zh) run scoreboard players set #xhit mg.st 1' % (y, z)
                  for y, z in (('#xiy', '#xiz'), ('#xqy', '#xoz'), ('#xqy', '#xqz'))]


def functions():
    return {'sweep': sweep_lines(), 'cross': cross_lines()}
