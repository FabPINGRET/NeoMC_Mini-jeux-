"""Fonctions de jeu propres a un parcours (mg:elyrace/c<N>/*) : tick d'un joueur, barre d'action, installation du depart
(portillon, chargement force, perchoir), texte du depart. Les tables d'anneaux, de reprises et de places sont dans
rings.py, la construction dans build_chain.py ; la logique commune a tous les parcours est dans game.py.
Python stdlib uniquement (compatible 3.8).
"""
import course_common as CC
import game as G

SB = G.SB


def player_lines(c):
    spec = c.spec
    respawn = 'function ' + CC.fn(spec, 'respawn')
    return ['# @s = joueur en course (pas encore arrivé) : position, délais, règles',
            'execute store result score @s mg.xx run data get entity @s Pos[0]',
            'scoreboard players operation @s mg.xp > @s mg.xx',
            'scoreboard players remove @s[scores={mg.xg=1..}] mg.xg 1',
            'scoreboard players remove @s[scores={mg.xk=1..}] mg.xk 1',
            'execute if predicate mg:gliding run scoreboard players set @s mg.xl 1',
            'execute if predicate mg:gliding run scoreboard players set @s mg.xn 0',
            'execute unless predicate mg:gliding if score @s mg.xl matches 1 run scoreboard players add @s mg.xn 1',
            'function mg:elyrace/speed',
            '# Mort (filet) ou sorti de la zone construite (monde vide) : retour au dernier point de reprise',
            'execute if score @s mg.deaths matches 1.. run return run ' + respawn,
            'execute unless entity @s[x=%d,y=0,z=%d,dx=%d,dy=330,dz=%d] run return run %s'
            % (spec.X0, spec.Z0, spec.X1 - spec.X0, spec.Z1 - spec.Z0, respawn),
            '# Encore sur la plateforme de départ : aucune règle',
            'execute if score @s mg.xx matches ..%d run return 0' % (G.LEFT_X - 1),
            'execute if score @s mg.xg matches 0 if score @s mg.xn matches %d.. run return run %s' % (G.STALL + 1, respawn),
            'execute if score @s mg.xg matches 0 at @s if block ~ ~ ~ minecraft:water run return run ' + respawn,
            'execute if score @s mg.xg matches 0 at @s if data entity @s {OnGround:1b} run return run ' + respawn,
            'function ' + CC.fn(spec, 'rings')]


def hud_lines(c):
    tail = ('{"text":"   ◎ ","color":"aqua"},{%s,"color":"white"},{"text":" / %d","color":"gray"},'
            '{"text":"   ★ ","color":"gold"},{%s,"color":"white"},{"text":" / %d","color":"gray"}]'
            % (SB % 'mg.xa', len(c.rings), SB % 'mg.xo', len(c.golds)))
    hearts = [('3..', '{"text":"♥♥♥","color":"red"}'),
              ('2', '{"text":"♥♥","color":"red"},{"text":"♡","color":"dark_gray"}'),
              ('1', '{"text":"♥","color":"red"},{"text":"♡♡","color":"dark_gray"}'),
              ('..0', '{"text":"♡♡♡","color":"dark_gray"}')]
    return ['# @s = joueur : barre d\'action (cœurs, anneaux, anneaux d\'or)'] + [
        'execute if score @s mg.xh matches %s run title @s actionbar [%s,%s' % (m, h, tail) for m, h in hearts]


def gate_lines(spec, blk):
    """Portillon de depart : une grille de 5 blocs de haut sur 25 de large, devant les joueurs."""
    return 'fill %d %d %d %d %d %d minecraft:%s' % (spec.GATE_X, spec.START_Y, spec.CZ - 12, spec.GATE_X, spec.START_Y + 4, spec.CZ + 12, blk)


def fl_box(spec):
    """Zone de depart chargee de force pendant la partie : (x1, z1, x2, z2)."""
    return spec.X0, spec.CZ - 32, spec.X0 + 96, spec.CZ + 32


def setup_lines(spec):
    """Installation du depart de ce parcours (appelee par prepare) : chargement force, portillon, perchoir, point d'apparition."""
    return ['# Installation du départ du parcours %d (%s) : zone chargée, portillon fermé, perchoir des spectateurs, point d\'apparition' % (spec.NUM, spec.NAME),
            'function ' + CC.fn(spec, 'fl_add'), 'function ' + CC.fn(spec, 'gate_on'),
            '# perchoir des spectateurs (éliminés / reconnectés)',
            'scoreboard players set $px mg.st 24', 'scoreboard players set $py mg.st %d' % (spec.START_Y + 19),
            'scoreboard players set $pz mg.st %d' % spec.CZ,
            'execute as @a[tag=mg.play] run spawnpoint @s 24 %d %d' % (spec.START_Y, spec.CZ)]


def go_text_lines(c):
    spec = c.spec
    intro = ('tellraw @a[tag=mg.play] [{"text":"🪽 COURSE D\'ÉLYTRES — %s : ","color":"aqua","bold":true},{"text":"saute de la falaise, ouvre tes élytres (espace en l\'air) '
             'et franchis les %d anneaux dans l\'ordre, par le trou. %%s (3 minutes au plus).","color":"gray"}]' % (spec.NAME.upper(), len(c.rings)))
    return ['# Texte du départ du parcours %d (@a[tag=mg.play]) ; fin de la 1re phrase selon $xs (contre-la-montre solo : pas de gagnant)' % spec.NUM,
            'execute unless score $xs mg.st matches 1 run ' + intro % 'Le premier arrivé gagne',
            'execute if score $xs mg.st matches 1 run ' + intro % 'Ton temps est enregistré',
            'tellraw @a[tag=mg.play] [{"text":"♥ 3 cœurs : chaque choc contre un mur en retire un. Plus de cœur, anneau raté, sol, eau ou trop longtemps sans planer : retour en l\'air au dernier point de reprise (colonnes lumineuses).","color":"gray"}]',
            'tellraw @a[tag=mg.play] [{"text":"★ %d anneaux d\'or en détour : chacun donne une fusée (clic droit en vol pour accélérer).","color":"gold"}]' % len(c.golds)]


def functions(c):
    """Fonctions de jeu d'un parcours : {nom relatif a c<N>/: lignes}."""
    spec = c.spec
    return {'player': player_lines(c), 'hud': hud_lines(c), 'setup': setup_lines(spec), 'go_text': go_text_lines(c),
            'gate_on': ['# Portillon de départ (verre rouge)', gate_lines(spec, 'red_stained_glass')],
            'gate_off': ['# GO : ouvre le portillon', gate_lines(spec, 'air')],
            'fl_add': ['# Zone de départ chargée pendant la partie', 'forceload add %d %d %d %d' % fl_box(spec)],
            'fl_remove': ['forceload remove %d %d %d %d' % fl_box(spec), 'function mg:core/forceloads']}
