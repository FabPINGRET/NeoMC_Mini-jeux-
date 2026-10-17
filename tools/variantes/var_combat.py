"""Variantes de combat : arènes (construction, perchoir, élimination, placement) et préparation/réglages de chaque mode.

Jamais lancé seul : gen_variants.py appelle run() après var_common.init().
"""
from var_common import w
from var_data import ARENAS


def run():
    # ============================================================ arènes de combat : setup (construction + placement)
    for a in ARENAS:
        k = a['k']
        d, r, u = a['sp']
        L = [f'# Arène {k} « {a["name"]} » (carte {a["src"]}, centre 0 ~ {a["z"]}) : construction, perchoir, élimination, placement. Généré.']
        if a.get('setup'):
            L += [f'function mg:{a["setup"]}',
                  'scoreboard players operation $ky mg.st = $tty mg.st']
        else:
            L += [f'function mg:{a["build"]}',
                  f'kill @e[type=minecraft:item,x={a["items"].split()[0]},y={a["items"].split()[1]},z={a["items"].split()[2]},'
                  f'dx={a["items"].split()[3]},dy={a["items"].split()[4]},dz={a["items"].split()[5]}]',
                  'scoreboard players set $px mg.st 0', f'scoreboard players set $py mg.st {a["py"]}', f'scoreboard players set $pz mg.st {a["z"]}',
                  f'scoreboard players set $ky mg.st {a["ky"]}',
                  'gamemode adventure @a[tag=mg.play]',
                  f'execute as @a[tag=mg.play] run spawnpoint @s {a["spawn"]}',
                  f'spreadplayers 0 {a["z"]} {d} {r} under {u} false @a[tag=mg.play]']
        L.append(f'data modify storage mg:var a set value {{x:0,z:{a["z"]},r:{r},u:{u}}}')
        w(f'var/arena/a{k}', L)
        if a['ceil']:
            x1, y, z1, x2, z2 = a['ceil']
            w(f'var/arena/ceil{k}', [f'# Plafond de barrière (garde les flèches dans l’arène {a["name"]}) ; retiré à la prochaine construction de la carte',
                                     f'fill {x1} {y} {z1} {x2} {y} {z2} minecraft:barrier replace #minecraft:air'])

    w('var/arena/setup', ['# Construit l’arène $ar et place les joueurs (@a[tag=mg.play]). Généré.'] +
      [f'execute if score $ar mg.st matches {a["k"]} run function mg:var/arena/a{a["k"]}' for a in ARENAS])
    w('var/arena/ceil', ['# Plafond de barrière pour One in the Chamber sur les arènes ouvertes. Généré.'] +
      [f'execute if score $ar mg.st matches {a["k"]} run function mg:var/arena/ceil{a["k"]}' for a in ARENAS if a['ceil']])
    w('var/spread_one', ['# Réapparition (@s) dans l’arène de la variante (storage mg:var a = x z r under)',
                         'function mg:var/spread_m with storage mg:var a'])
    w('var/spread_m', ['# Macro : placement aléatoire de @s dans l’arène',
                       '$spreadplayers $(x) $(z) 2 $(r) under $(u) false @s'])

    # ============================================================ modes de combat : préparation + réglages
    w('var/mode/pvp_prepare', [
        '# Arène PvP sur une autre carte ($ar) — appelé par pvp/prepare. Généré.',
        'function mg:var/arena/setup',
        'scoreboard players reset @a mg.pk'])
    w('var/mode/pvp_go', [
        '# Arène PvP, variante : kit selon la difficulté (appelé à la fin de pvp/go). Généré.',
        'execute if score $dif mg.st matches 1 run give @a[tag=mg.play] minecraft:golden_apple 2',
        'execute if score $dif mg.st matches 1 run give @a[tag=mg.play] minecraft:arrow 16',
        'execute if score $dif mg.st matches 3.. run item replace entity @a[tag=mg.play] weapon.offhand with minecraft:air',
        'execute if score $dif mg.st matches 3 run clear @a[tag=mg.play] minecraft:golden_apple 1',
        'execute if score $dif mg.st matches 4 run clear @a[tag=mg.play] minecraft:golden_apple',
        'execute if score $dif mg.st matches 4 run item replace entity @a[tag=mg.play] armor.chest with minecraft:leather_chestplate',
        'execute if score $dif mg.st matches 4 run tellraw @a[tag=mg.play] {"text":"★★★★ Pas de bouclier, pas de pomme d’or, plastron en cuir : chaque coup compte.","color":"red"}'])
    w('var/mode/oitc_prepare', [
        '# One in the Chamber sur une autre carte ($ar) — appelé par oitc/prepare. Généré.',
        'kill @e[distance=0..,type=minecraft:arrow]',
        'function mg:var/arena/setup',
        'function mg:var/arena/ceil',
        'scoreboard players reset @a mg.pk',
        'scoreboard players set @a[tag=mg.play] mg.lv 3',
        'scoreboard players set @a[tag=mg.play] mg.ok 0',
        'scoreboard players set @a[tag=mg.play] mg.cd 0'])
    w('var/mode/oitc_go', [
        '# One in the Chamber, variante : kills pour gagner ($og) et flèches enchantées ($osi). Généré.',
        'execute if score $dif mg.st matches 1 run scoreboard players set $og mg.st 7',
        'execute if score $dif mg.st matches 4 run scoreboard players set $og mg.st 12',
        'execute if score $dif mg.st matches 1 run scoreboard players set $osi mg.st 300',
        'execute if score $dif mg.st matches 3 run scoreboard players set $osi mg.st 900',
        'execute if score $dif mg.st matches 4 run scoreboard players set $osi mg.st 2000000000',
        'tellraw @a[tag=mg.play] [{"text":"➶ Objectif de la variante : ","color":"gold"},{"score":{"name":"$og","objective":"mg.st"},"color":"yellow","bold":true},{"text":" kills.","color":"gold"}]'])
    qsz = {'XS': (20, 7200), 'S': (20, 7200), 'M': (25, 9600), 'L': (30, 12000), 'XL': (30, 12000)}
    L = ['# Quakecraft sur une autre carte ($ar) — appelé par quake/prepare. Généré.',
         'kill @e[distance=0..,type=minecraft:item]',
         'scoreboard players reset @a mg.qs', 'tag @a remove mg.prot', 'tag @a remove mg.qdd', 'tag @a remove mg.qsh']
    for a in ARENAS:
        g, t = qsz[a['size']]
        L += [f'execute if score $ar mg.st matches {a["k"]} run scoreboard players set $qg mg.st {g}',
              f'execute if score $ar mg.st matches {a["k"]} run scoreboard players set $qt mg.st {t}']
    L += ['scoreboard players set $qcd mg.st 22',
          'execute if score $dif mg.st matches 1 run scoreboard players set $qcd mg.st 16',
          'execute if score $dif mg.st matches 3 run scoreboard players set $qcd mg.st 28',
          'execute if score $dif mg.st matches 4 run scoreboard players set $qcd mg.st 34',
          'function mg:var/arena/setup',
          'scoreboard players set @a[tag=mg.play] mg.qk 0', 'scoreboard players set @a[tag=mg.play] mg.cd 0']
    w('var/mode/quake_prepare', L)
    w('var/mode/tnttag_prepare', [
        '# TNT Tag sur une autre carte ($ar) — appelé par tnttag/prepare. Généré.',
        'function mg:var/arena/setup',
        'scoreboard players operation $tty mg.st = $ky mg.st'])
    w('var/mode/tnttag_go', [
        '# TNT Tag, variante : durée de la bombe = base + 5 s par survivant en plus, plafonnée. Généré.',
        'execute if score $dif mg.st matches 1 run scoreboard players set $ttb mg.st 300',
        'execute if score $dif mg.st matches 1 run scoreboard players set $mx mg.st 800',
        'execute if score $dif mg.st matches 3 run scoreboard players set $ttb mg.st 160',
        'execute if score $dif mg.st matches 3 run scoreboard players set $mx mg.st 450',
        'execute if score $dif mg.st matches 4 run scoreboard players set $ttb mg.st 120',
        'execute if score $dif mg.st matches 4 run scoreboard players set $mx mg.st 300'])
