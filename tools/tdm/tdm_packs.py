"""TDM sniper : packs de soin sporadiques (item_display pomme dorée, tag mg.tmhk), écrits par gen_tdm.py.

Un premier pack 20 s après le GO ($tmhc = 400, posé par tdm/go), puis un toutes les 45-60 s ; 2 présents au plus (limite atteinte :
nouvel essai dans 5 s ; emplacement occupé : dans 1 s). Seul un joueur à 1 PV (ou moins) le ramasse : PV remis à 2.
Emplacements fixes par carte (x, y du bloc d'air où se pose le pack, zl), vérifiés au build par check_spots() : air en y et y+1,
bloc plein en y-1, sur la géométrie réelle de l'arène (Arena rejouée dans l'ordre).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'duel'))
from duel_geom import Arena

SPOTS = {
    'canyon': [(0, 89, 0), (5, 73, -8), (-5, 73, 8), (10, 73, -20), (-10, 73, 20), (15, 89, -40), (-15, 89, 40)],
    'ville': [(0, 81, -43), (0, 81, 43), (-10, 81, -29), (10, 81, 29), (0, 81, -6), (0, 81, 6)],
    'glacier': [(0, 81, -20), (0, 81, 20), (-10, 81, -40), (10, 81, 40), (0, 81, -8), (0, 81, 8)],
}
PACK = 'minecraft:item_display'
HEAL = 'tag=mg.play,gamemode=adventure,distance=..1.3,scores={mg.tmhp=..1}'
CHANCE = '{condition:"minecraft:random_chance",chance:0.15}'


def _state(lines, x, y, z):
    """Bloc posé en (x, y, z) après rejeu des fill / setblock (None = jamais posé = air)."""
    cur = None
    for l in lines:
        t = l.split(' ')
        if t[0] == 'setblock':
            if (int(t[1]), int(t[2]), int(t[3])) == (x, y, z):
                cur = t[4].split('[')[0]
        elif t[0] == 'fill':
            if len(t) != 8:
                raise SystemExit(f'check_spots : fill inattendu (mode ?) : {l}')
            x1, y1, z1, x2, y2, z2 = map(int, t[1:7])
            if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2) and min(z1, z2) <= z <= max(z1, z2):
                cur = t[7].split('[')[0]
    return cur


def check_spots(maps, starts=()):
    """Chaque emplacement de pack et chaque départ doit avoir de l'air en y et y+1 et un bloc non-air en y-1 (sinon SystemExit).

    Le bloc testé est celui où l'on se pose : (x, z) pour un pack (positioned x+0.5, z+0.5 : même bloc) ; pour un départ,
    y = m['y'] et (x, zl) = [(x, zl)] de starts (le tp vise le centre du même bloc)."""
    for m in maps:
        a = Arena(m['z'])
        a.prologue()
        m['build'](a)
        a.cage()
        spots = [('pack', x, y, zl) for x, y, zl in SPOTS[m['key']]] + [('départ', x, m['y'], zl) for x, zl in starts]
        for kind, x, y, zl in spots:
            z = m['z'] + zl
            air = lambda yy: _state(a.L, x, yy, z) in (None, 'minecraft:air', 'air')
            if not (air(y) and air(y + 1) and not air(y - 1)):
                raise SystemExit(f'check_spots : {m["key"]} ({x}, {y}, {zl}) : {kind} mal posé (y-1 = {_state(a.L, x, y - 1, z)}, '
                                 f'y = {_state(a.L, x, y, z)}, y+1 = {_state(a.L, x, y + 1, z)})')


def build(w, js, maps):
    """w(rel, lignes) écrit une fonction ; js = sérialiseur de texte JSON ; maps = MAPS du duel (z du centre, y du sol)."""
    w('tdm/pack_tick', [
        '# Packs de soin (tdm/tick, état 2) : échéance du prochain pack, puis ramassage par un joueur à 1 PV',
        'scoreboard players remove $tmhc mg.st 1',
        'execute if score $tmhc mg.st matches ..0 run function mg:tdm/pack_try',
        f'execute as @e[type={PACK},tag=mg.tmhk] at @s run function mg:tdm/pack_chk',
    ])
    pt = ['# Échéance : prochain essai dans 45-60 s par défaut ; 2 packs présents = nouvel essai dans 5 s ; emplacement tiré au hasard',
          'execute store result score $tmhc mg.st run random value 900..1200',
          f'execute store result score #tmhn mg.st if entity @e[type={PACK},tag=mg.tmhk]',
          'execute if score #tmhn mg.st matches 2.. run return run scoreboard players set $tmhc mg.st 100']
    for i, m in enumerate(maps, 1):
        pt.append(f'execute if score $tma mg.st matches {i} store result score #tmhs mg.st run random value 0..{len(SPOTS[m["key"]]) - 1}')
    for i, m in enumerate(maps, 1):
        for k, (x, y, zl) in enumerate(SPOTS[m['key']]):
            pt.append(f'execute if score $tma mg.st matches {i} if score #tmhs mg.st matches {k} positioned {x + 0.5} {y} {m["z"] + zl + 0.5} run function mg:tdm/pack_new')
    w('tdm/pack_try', pt)
    w('tdm/pack_new', [
        '# Pose un pack ici (position = emplacement) ; un pack à moins de 2 blocs = nouvel essai dans 1 s',
        f'execute if entity @e[type={PACK},tag=mg.tmhk,distance=..2] run return run scoreboard players set $tmhc mg.st 20',
        f'summon {PACK} ~ ~0.6 ~ {{Tags:["mg.tmhk"],billboard:"vertical",Glowing:1b,item:{{id:"minecraft:golden_apple",count:1}},'
        'transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}',
    ])
    w('tdm/pack_chk', [
        '# @s = pack, position exécutée = le pack : particules, ramassage par le joueur le plus proche à 1 PV',
        f'execute if predicate {CHANCE} run particle minecraft:heart ~ ~0.5 ~ 0.25 0.25 0.25 0 1',
        f'execute store success score #tmhs mg.st if entity @a[{HEAL}]',
        f'execute if score #tmhs mg.st matches 1 as @p[{HEAL}] run function mg:tdm/pack_take',
        'execute if score #tmhs mg.st matches 1 run kill @s',
    ])
    w('tdm/pack_take', [
        '# Pack ramassé (@s = joueur à 1 PV) : PV remis à 2',
        'scoreboard players set @s mg.tmhp 2',
        'execute at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 0.8 1.6',
        'execute at @s run particle minecraft:heart ~ ~1.2 ~ 0.4 0.4 0.4 0 8',
        'title @s actionbar ' + js({'text': '❤ Soigné', 'color': 'green', 'bold': True}),
    ])
