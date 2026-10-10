"""⛏ Mini UHC Run (id 94) et 🏹 Mini Hunger Games (id 95), parties de ~5 min.

    python tools/arcade/gen_survival.py .

Les deux cartes sont des mini-mondes générés ici (relief, eau, arbres ; minerais pour l'UHC), reconstruits
à chaque partie. Pas de vraie bordure (elle est globale à la dimension, le lobby en souffrirait) : une « zone »
carrée qui rétrécit, matérialisée par des particules, inflige des dégâts à l'extérieur.

UHC Run (z 22400, 81×81) : survie, minage rapide (Célérité II), minerais cuits automatiquement, pas de
régénération naturelle (pommes d'or). 2 min 30 de farm sans PvP, puis PvP + zone de 40 → 5 en 2 min 30.
Hunger Games (z 22800, 101×101) : aventure, coffres (corne d'abondance au centre), départ sur des socles après
10 s de compte à rebours, PvP après 20 s, coffres remplis à 2 min 30, zone de 50 → 6 de 3 min à 5 min.
Dernier en vie gagne ; inventaire lâché à la mort (keep_inventory coupé pendant la partie).
"""
import json
import math
import os
import random
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js


def noise2(seed, size, scale, octaves=3):
    rnd = random.Random(seed)
    grids = []
    for o in range(octaves):
        step = max(2, int(scale / (2 ** o)))
        n = size // step + 3
        grids.append((step, [[rnd.random() for _ in range(n)] for _ in range(n)], 0.5 ** o))

    def smooth(t):
        return t * t * (3 - 2 * t)

    def val(x, z):
        tot = norm = 0
        for step, g, amp in grids:
            gx, gz = x / step, z / step
            i, j = int(gx), int(gz)
            fx, fz = smooth(gx - i), smooth(gz - j)
            a = g[i][j] * (1 - fx) + g[i + 1][j] * fx
            b = g[i][j + 1] * (1 - fx) + g[i + 1][j + 1] * fx
            tot += amp * (a * (1 - fz) + b * fz)
            norm += amp
        return tot / norm
    return val


THEMES = {   # sol, sous-sol, rivage, roche, eau, arbres (« cactus » = cactus sur le sable)
    'plaines': dict(top='grass_block', sub='dirt', shore='sand', stone='stone', water='water', woods=['oak', 'oak', 'birch', 'spruce']),
    'desert': dict(top='sand', sub='sandstone', shore='sand', stone='stone', water='water', woods=['acacia', 'cactus', 'cactus', 'oak']),
    'taiga': dict(top='snow_block', sub='dirt', shore='gravel', stone='stone', water='ice', woods=['spruce', 'spruce', 'spruce', 'birch']),
    'jungle': dict(top='grass_block', sub='dirt', shore='sand', stone='mossy_cobblestone', water='water', woods=['jungle', 'jungle', 'oak', 'jungle']),
    'mesa': dict(top='red_sand', sub='orange_terracotta', shore='red_sand', stone='terracotta', water='water', woods=['dark_oak', 'cactus', 'cactus', 'acacia']),
}


def terrain(seed, R, Z, base, lo, hi, water, ores, flat_center=0, tree_div=90, theme='plaines'):
    """Mini-monde carré de demi-côté R centré (0, Z). Renvoie (lignes de construction, hauteurs)."""
    rnd = random.Random(seed)
    T = THEMES[theme]
    nz = noise2(seed, 2 * R + 1, 18)
    H = {}
    for x in range(-R, R + 1):
        for z in range(-R, R + 1):
            v = nz(x + R, z + R)
            edge = max(abs(x), abs(z)) / R          # bords un peu plus bas : île
            h = lo + (hi - lo) * v - max(0, edge - 0.85) * 25
            d = math.hypot(x, z)
            if flat_center and d < flat_center:
                h = (lo + hi) / 2
            H[(x, z)] = int(round(h))
    L = [f'# Mini-monde (graine {seed}) — généré par tools/arcade/gen_survival.py']
    # nettoyage (≤ 32768 blocs par fill)
    side = 2 * R + 5
    per = max(1, 32000 // (side * side))
    y = base - 1
    while y <= 112:
        L.append(f'fill {-R - 2} {y} {Z - R - 2} {R + 2} {min(112, y + per - 1)} {Z + R + 2} minecraft:air')
        y += per
    # colonnes regroupées par lignes de même hauteur
    for z in range(-R, R + 1):
        x = -R
        while x <= R:
            h = H[(x, z)]
            k = x
            while k + 1 <= R and H[(k + 1, z)] == h:
                k += 1
            if h >= base:
                shore = h <= water + 1
                top = T['shore'] if shore else T['top']
                if h - 4 >= base:
                    L.append(f'fill {x} {base} {Z + z} {k} {h - 4} {Z + z} minecraft:{T["stone"]}')
                L.append(f'fill {x} {max(base, h - 3)} {Z + z} {k} {h - 1} {Z + z} minecraft:{T["shore"] if shore else T["sub"]}')
                L.append(f'fill {x} {h} {Z + z} {k} {h} {Z + z} minecraft:{top}')
                if h < water:
                    L.append(f'fill {x} {h + 1} {Z + z} {k} {water} {Z + z} minecraft:water')
                    if T['water'] != 'water':
                        L.append(f'fill {x} {water} {Z + z} {k} {water} {Z + z} minecraft:{T["water"]}')
            x = k + 1
    # minerais (amas)
    for ore, count, ymax_off, size in ores:
        for _ in range(count):
            x, z = rnd.randint(-R + 1, R - 1), rnd.randint(-R + 1, R - 1)
            h = H[(x, z)]
            if h - 5 <= base:
                continue
            y = rnd.randint(base, min(h - 5, base + ymax_off))
            for _ in range(size):
                L.append(f'setblock {x} {y} {Z + z} minecraft:{ore} replace')
                x += rnd.choice((-1, 0, 1))
                z = max(-R, min(R, z + rnd.choice((-1, 0, 1))))
                y = max(base, min(H.get((x, z), base) - 4, y + rnd.choice((-1, 0, 1))))
    # arbres
    trees = []
    for _ in range(int((2 * R) ** 2 / tree_div)):
        x, z = rnd.randint(-R + 3, R - 3), rnd.randint(-R + 3, R - 3)
        h = H[(x, z)]
        if h <= water + 1 or (flat_center and math.hypot(x, z) < flat_center + 3):
            continue
        if any(abs(x - a) < 4 and abs(z - b) < 4 for a, b in trees):
            continue
        trees.append((x, z))
        t = rnd.randint(4, 6)
        wood = rnd.choice(T['woods'])
        if wood == 'cactus':
            L.append(f'fill {x} {h + 1} {Z + z} {x} {h + rnd.randint(2, 3)} {Z + z} minecraft:cactus')
            continue
        L += [f'fill {x - 2} {h + t - 2} {Z + z - 2} {x + 2} {h + t - 1} {Z + z + 2} minecraft:{wood}_leaves[persistent=true]',
              f'fill {x - 1} {h + t} {Z + z - 1} {x + 1} {h + t + 1} {Z + z + 1} minecraft:{wood}_leaves[persistent=true]',
              f'fill {x} {h + 1} {Z + z} {x} {h + t} {Z + z} minecraft:{wood}_log']
    # barrières autour + plafond
    L += [f'fill {-R - 1} {base} {Z - R - 1} {R + 1} 110 {Z - R - 1} minecraft:barrier',
          f'fill {-R - 1} {base} {Z + R + 1} {R + 1} 110 {Z + R + 1} minecraft:barrier',
          f'fill {-R - 1} {base} {Z - R} {-R - 1} 110 {Z + R} minecraft:barrier',
          f'fill {R + 1} {base} {Z - R} {R + 1} 110 {Z + R} minecraft:barrier']
    return L, H


# ---------- zone qui rétrécit (commune) : $<p>r = demi-côté courant, dégâts à l'extérieur chaque seconde
def zone(key, Z):
    w(f'{key}/zone', [f'# Zone carrée de demi-côté $zr centrée en (0, {Z}) : 2 dégâts/s dehors, particules sur les bords',
                      'execute as @a[tag=mg.play] store result score @s mg.tx run data get entity @s Pos[0]',
                      'execute as @a[tag=mg.play] store result score @s mg.tz run data get entity @s Pos[2]',
                      f'scoreboard players remove @a[tag=mg.play] mg.tz {Z}',
                      'execute as @a[tag=mg.play,scores={mg.tx=..-1}] run scoreboard players operation @s mg.tx *= #-1 mg.st',
                      'execute as @a[tag=mg.play,scores={mg.tz=..-1}] run scoreboard players operation @s mg.tz *= #-1 mg.st',
                      'execute as @a[tag=mg.play] if score @s mg.tx > $zr mg.st run tag @s add mg.zout',
                      'execute as @a[tag=mg.play] if score @s mg.tz > $zr mg.st run tag @s add mg.zout',
                      'execute as @a[tag=mg.zout] run damage @s 2 minecraft:outside_border',
                      'title @a[tag=mg.zout] actionbar {"text":"⚠ Hors de la zone ! Reviens vers le centre","color":"red","bold":true}',
                      'tag @a remove mg.zout',
                      'execute store result storage mg:zone r int 1 run scoreboard players get $zr mg.st',
                      'scoreboard players operation $zn mg.st = $zr mg.st', 'scoreboard players operation $zn mg.st *= #-1 mg.st',
                      'execute store result storage mg:zone n int 1 run scoreboard players get $zn mg.st',
                      f'data modify storage mg:zone z set value {Z}',
                      f'scoreboard players set $zp mg.st {Z}', 'scoreboard players operation $zp mg.st += $zr mg.st',
                      f'scoreboard players set $zm mg.st {Z}', 'scoreboard players operation $zm mg.st -= $zr mg.st',
                      'execute store result storage mg:zone zp int 1 run scoreboard players get $zp mg.st',
                      'execute store result storage mg:zone zm int 1 run scoreboard players get $zm mg.st',
                      f'function mg:{key}/zone_fx with storage mg:zone'])
    w(f'{key}/zone_fx', ['# Bords de la zone (macro)',
                         '$particle minecraft:dust{color:[1.0,0.2,0.2],scale:2} $(r) 90 $(z) 0 10 $(r) 0 120 force',
                         '$particle minecraft:dust{color:[1.0,0.2,0.2],scale:2} $(n) 90 $(z) 0 10 $(r) 0 120 force',
                         '$particle minecraft:dust{color:[1.0,0.2,0.2],scale:2} 0 90 $(zp) $(r) 10 0 0 120 force',
                         '$particle minecraft:dust{color:[1.0,0.2,0.2],scale:2} 0 90 $(zm) $(r) 10 0 0 120 force'])


def lastman(prefix):
    return ['execute store result score $alive mg.st if entity @a[tag=mg.play]',
            'execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $alive mg.st matches 1 as @a[tag=mg.play,limit=1] run return run function mg:core/win_player',
            'execute if score $state mg.st matches 2 if score $n0 mg.st matches ..1 if score $alive mg.st matches 1 as @a[tag=mg.play,limit=1] if score $' + prefix + 't mg.st matches 6000.. run return run function mg:core/win_player',
            'execute if score $state mg.st matches 2 if score $alive mg.st matches 0 run function mg:core/draw']


# =====================================================================  UHC RUN
ZU, RU = C.param('ZU', 22400), 40
L, HU = terrain(C.param('seed_uhc', 9401), RU, ZU, 60, 70, 84, 69,
                [('iron_ore', 760, 18, 5), ('gold_ore', 260, 12, 4), ('diamond_ore', 150, 6, 3),
                 ('redstone_ore', 50, 8, 3), ('lapis_ore', 40, 8, 3)], tree_div=40, theme=C.param('uhc_theme', 'plaines'))
# ressources en surface (UHC) : affleurements de minerais, graviers (silex), canne à sucre, coffres
_r = random.Random(9402)
_used = set()


def _spot(margin=3, dry=True):
    for _ in range(200):
        x, z = _r.randint(-RU + margin, RU - margin), _r.randint(-RU + margin, RU - margin)
        if (x, z) in _used or (dry and HU[(x, z)] <= 70):
            continue
        _used.add((x, z))
        return x, z, HU[(x, z)]
    return None


for _ in range(30):                       # rochers avec minerais visibles
    s = _spot()
    if not s:
        continue
    x, z, h = s
    ore = _r.choice(['iron_ore', 'iron_ore', 'iron_ore', 'iron_ore', 'gold_ore', 'gold_ore', 'diamond_ore', 'diamond_ore'])
    L.append(f'fill {x - 1} {h + 1} {ZU + z - 1} {x + 1} {h + 1} {ZU + z + 1} minecraft:cobblestone')
    L.append(f'setblock {x} {h + 2} {ZU + z} minecraft:{ore}')
    L += [f'setblock {x + dx} {h + 1} {ZU + z + dz} minecraft:{ore}' for dx, dz in _r.sample([(-1, 0), (1, 0), (0, -1), (0, 1)], 2)]
for _ in range(14):                       # tas de gravier (silex pour les flèches)
    s = _spot()
    if s:
        x, z, h = s
        L.append(f'fill {x - 1} {h} {ZU + z - 1} {x + 1} {h} {ZU + z + 1} minecraft:gravel replace minecraft:grass_block')
for x in range(-RU + 1, RU):              # canne à sucre au bord de l'eau (livres)
    for z in range(-RU + 1, RU):
        h = HU[(x, z)]
        if h == 69 and any(HU.get((x + a, z + b), 99) < 69 for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1))) and _r.random() < 0.35:
            L.append(f'fill {x} {h + 1} {ZU + z} {x} {h + _r.randint(2, 3)} {ZU + z} minecraft:sugar_cane replace minecraft:air')
CHESTS = []
for _ in range(16):                       # coffres (remplis à chaque partie)
    s = _spot(5)
    if s:
        CHESTS.append(s)
        x, z, h = s
        L.append(f'setblock {x} {h + 1} {ZU + z} minecraft:chest[facing={_r.choice(["north", "south", "east", "west"])}]{{LootTable:"mg:uhc/chest"}}')
w('uhc/build', L)
os.makedirs(os.path.join(C.D, 'loot_table/uhc'), exist_ok=True)
_e = lambda n, wgt, a=1, b=1: dict({'type': 'minecraft:item', 'name': 'minecraft:' + n, 'weight': wgt},
                                   **({'functions': [{'function': 'minecraft:set_count', 'count': {'type': 'minecraft:uniform', 'min': a, 'max': b}}]} if b > 1 else {}))
with open(os.path.join(C.D, 'loot_table/uhc/chest.json'), 'w', encoding='utf-8', newline='\n') as f:
    json.dump({'type': 'minecraft:chest', 'pools': [{'rolls': {'type': 'minecraft:uniform', 'min': 4, 'max': 7}, 'entries': [
        _e('iron_ingot', 10, 2, 6), _e('gold_ingot', 8, 2, 5), _e('diamond', 3, 1, 2), _e('golden_apple', 3), _e('apple', 6, 1, 3),
        _e('cooked_beef', 8, 2, 5), _e('bread', 6, 2, 4), _e('bow', 4), _e('arrow', 7, 6, 16), _e('string', 4, 2, 4),
        _e('feather', 4, 2, 6), _e('flint', 3, 1, 3), _e('book', 3, 1, 2), _e('leather', 4, 2, 4), _e('oak_log', 6, 4, 10),
        _e('iron_helmet', 2), _e('iron_boots', 2), _e('shield', 2), _e('water_bucket', 2), _e('lava_bucket', 1),
        _e('experience_bottle', 3, 2, 5), _e('enchanting_table', 1), _e('lapis_lazuli', 3, 3, 8), _e('anvil', 1)]}]},
              f, ensure_ascii=False, indent=2)
# animaux (nourriture, cuir, plumes) : posés au départ, tués au nettoyage
ANIMALS = []
for kind, n in (('cow', 12), ('chicken', 12), ('sheep', 8), ('pig', 6)):
    for _ in range(n):
        s = _spot(4)
        if s:
            ANIMALS.append(f'summon minecraft:{kind} {s[0]} {s[2] + 1} {ZU + s[1]} {{Tags:["mg.mob","mg.uhcmob"],PersistenceRequired:1b}}')
zone('uhc', ZU)
w('uhc/prepare', ['# ⛏ Mini UHC Run — préparation', 'function mg:uhc/build', 'function mg:uhc/kill_all',
                  'scoreboard players set $px mg.st 0', 'scoreboard players set $py mg.st 105', f'scoreboard players set $pz mg.st {ZU}',
                  'clear @a[tag=mg.play]', 'gamemode adventure @a[tag=mg.play]', 'team leave @a[tag=mg.play]',
                  f'spreadplayers 0 {ZU} 8 {RU - 6} under 100 false @a[tag=mg.play]',
                  'execute as @a[tag=mg.play] at @s run spawnpoint @s ~ ~ ~'])
w('uhc/kill_all', ['kill @e[tag=mg.uhcmob]', f'kill @e[type=minecraft:item,x={-RU - 3},y=50,z={ZU - RU - 3},dx={2 * RU + 6},dy=70,dz={2 * RU + 6}]',
                   f'kill @e[type=minecraft:experience_orb,x={-RU - 3},y=50,z={ZU - RU - 3},dx={2 * RU + 6},dy=70,dz={2 * RU + 6}]',
                   f'kill @e[type=minecraft:arrow,x={-RU - 3},y=50,z={ZU - RU - 3},dx={2 * RU + 6},dy=70,dz={2 * RU + 6}]'])
w('uhc/go', ['# Départ : survie, pas de régénération naturelle, inventaire lâché à la mort',
             'scoreboard players set $uht mg.st 0', 'scoreboard players set #-1 mg.st -1', f'scoreboard players set $zr mg.st {RU + 2}',
             'gamerule natural_health_regeneration false', 'gamerule keep_inventory false',
             'gamemode survival @a[tag=mg.play]', 'team join mg_green @a[tag=mg.play]',
             # outils en fer (le diamant demande au moins du fer), Efficacité V + Célérité III : la roche casse d'un coup
             'give @a[tag=mg.play] minecraft:iron_pickaxe[enchantments={efficiency:5},unbreakable={}]',
             'give @a[tag=mg.play] minecraft:iron_axe[enchantments={efficiency:5},unbreakable={}]',
             'give @a[tag=mg.play] minecraft:iron_shovel[enchantments={efficiency:5},unbreakable={}]',
             'give @a[tag=mg.play] minecraft:crafting_table', 'give @a[tag=mg.play] minecraft:bread 10',
             'effect give @a[tag=mg.play] minecraft:haste infinite 2 true',
             'scoreboard players reset @a mg.uoi', 'scoreboard players reset @a mg.uog', 'scoreboard players reset @a mg.uod',
             'scoreboard players reset @a mg.uor', 'scoreboard players reset @a mg.uol',
             'effect give @a[tag=mg.play] minecraft:instant_health 1 4 true', 'scoreboard players set @a mg.deaths 0'] + ANIMALS + [
             'tellraw @a[tag=mg.play] ' + js([{'text': '⛏ MINI UHC RUN : ', 'color': 'gold', 'bold': True},
                                              {'text': '2 min 30 pour miner et t\'équiper (minerais déjà cuits, minage rapide, coffres, rochers à minerais, animaux), PVP DÉSACTIVÉ. Ensuite PvP et la zone rétrécit. Pas de régénération : pommes d\'or (8 lingots d\'or + 1 pomme) ! Dernier en vie gagne.', 'color': 'gray'}])])
# minerai cassé (statistique « miné », donc avec le bon outil) → un bloc entier (9 lingots) ; la petite récompense normale
# (tombée à la fin du tick précédent : délai de ramassage encore à 10) est retirée
ORES = [('mg.uoi', 'iron_ore', 'raw_iron', 'iron_block'), ('mg.uog', 'gold_ore', 'raw_gold', 'gold_block'),
        ('mg.uod', 'diamond_ore', 'diamond', 'diamond_block'), ('mg.uor', 'redstone_ore', 'redstone', 'redstone_block'),
        ('mg.uol', 'lapis_ore', 'lapis_lazuli', 'lapis_block')]
w('uhc/give_n', ['$give @s minecraft:$(b) $(n)'])
for obj, ore, drop, blk in ORES:
    w(f'uhc/ore_{ore}', [f'# @s a cassé {ore} : un bloc de {blk} par minerai',
                         f'data modify storage mg:uhc o.b set value "{blk}"',
                         f'execute store result storage mg:uhc o.n int 1 run scoreboard players get @s {obj}',
                         'function mg:uhc/give_n with storage mg:uhc o',
                         f'scoreboard players reset @s {obj}',
                         f'execute at @s run kill @e[type=minecraft:item,distance=..8,nbt={{PickupDelay:10s,Item:{{id:"minecraft:{drop}"}}}}]',
                         'execute at @s run playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.6 1.2'])
C.objectives([(obj, f'minecraft.mined:minecraft.{ore}') for obj, ore, _, _ in ORES])
C.patch('desinstaller', 'scoreboard objectives remove mg.bw', ['data remove storage mg:uhc o'])
w('uhc/tick', ['# ⛏ Mini UHC Run — tick', 'scoreboard players add $uht mg.st 1'] +
  [f'execute as @a[tag=mg.play,scores={{{obj}=1..}}] run function mg:uhc/ore_{ore}' for obj, ore, _, _ in ORES] + [
               'execute as @a[tag=mg.play,scores={mg.deaths=1..}] run function mg:core/eliminate',
               'execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]',
               'execute as @a[tag=mg.play,scores={mg.t=..50}] run function mg:core/eliminate',
               # cuisson automatique
               f'execute as @e[type=minecraft:item,x={-RU - 3},y=50,z={ZU - RU - 3},dx={2 * RU + 6},dy=70,dz={2 * RU + 6}] run function mg:uhc/smelt',
               # chronologie
               'execute if score $uht mg.st matches 1800 run tellraw @a[tag=mg.play] {"text":"⛏ PvP dans 1 minute !","color":"gold"}',
               'execute if score $uht mg.st matches 2800 run tellraw @a[tag=mg.play] {"text":"⛏ PvP dans 10 secondes !","color":"red"}',
               'execute if score $uht mg.st matches 3000 run function mg:uhc/pvp',
               'scoreboard players operation $uhq mg.st = $uht mg.st', 'scoreboard players set #20 mg.st 20', 'scoreboard players operation $uhq mg.st %= #20 mg.st',
               'execute if score $uhq mg.st matches 0 run function mg:uhc/second'] + lastman('uh'))
w('uhc/smelt', ['# @s (objet au sol) : minerais → lingots',
                'execute if items entity @s contents minecraft:raw_iron run data modify entity @s Item.id set value "minecraft:iron_ingot"',
                'execute if items entity @s contents minecraft:raw_gold run data modify entity @s Item.id set value "minecraft:gold_ingot"',
                'execute if items entity @s contents minecraft:raw_copper run data modify entity @s Item.id set value "minecraft:copper_ingot"',
                'execute if items entity @s contents minecraft:beef run data modify entity @s Item.id set value "minecraft:cooked_beef"',
                'execute if items entity @s contents minecraft:porkchop run data modify entity @s Item.id set value "minecraft:cooked_porkchop"',
                'execute if items entity @s contents minecraft:chicken run data modify entity @s Item.id set value "minecraft:cooked_chicken"',
                'execute if items entity @s contents minecraft:mutton run data modify entity @s Item.id set value "minecraft:cooked_mutton"'])
w('uhc/pvp', ['# PvP activé, la zone commence à rétrécir', 'team leave @a[tag=mg.play]',
              'title @a[tag=mg.play] title {"text":"⚔ PvP !","color":"red","bold":true}',
              'title @a[tag=mg.play] subtitle {"text":"la zone rétrécit vers le centre","color":"gray"}',
              'execute as @a[tag=mg.play] at @s run playsound minecraft:entity.ender_dragon.growl master @s ~ ~ ~ 0.6 1.2'])
w('uhc/second', ['# Chaque seconde : zone (40 → 5 entre 2:30 et 5:00) et affichage',
                 'scoreboard players operation $uhs mg.st = $uht mg.st', 'scoreboard players operation $uhs mg.st /= #20 mg.st',
                 # rayon = 42 jusqu'à 150 s, puis 40 - (s-150)*35/150, min 5
                 f'execute if score $uhs mg.st matches 150.. run scoreboard players set $zr mg.st 40',
                 'execute if score $uhs mg.st matches 150.. run scoreboard players operation $uhz mg.st = $uhs mg.st',
                 'execute if score $uhs mg.st matches 150.. run scoreboard players remove $uhz mg.st 150',
                 'execute if score $uhs mg.st matches 150.. run scoreboard players operation $uhz mg.st *= #7 mg.st',
                 'execute if score $uhs mg.st matches 150.. run scoreboard players operation $uhz mg.st /= #30 mg.st',
                 'execute if score $uhs mg.st matches 150.. run scoreboard players operation $zr mg.st -= $uhz mg.st',
                 'execute if score $zr mg.st matches ..4 run scoreboard players set $zr mg.st 5',
                 'execute if score $uhs mg.st matches 150.. run function mg:uhc/zone',
                 'scoreboard players set $uhl mg.st 150', 'scoreboard players operation $uhl mg.st -= $uhs mg.st',
                 'execute if score $uhs mg.st matches ..149 run title @a[tag=mg.play] actionbar [{"text":"⛏ Farm — PvP dans ","color":"green"},{"score":{"name":"$uhl","objective":"mg.st"},"color":"yellow","bold":true},{"text":" s","color":"green"}]',
                 'execute if score $uhs mg.st matches 150.. run title @a[tag=mg.play,tag=!mg.zout] actionbar [{"text":"⚔ PvP — zone ","color":"red"},{"score":{"name":"$zr","objective":"mg.st"},"color":"yellow","bold":true},{"text":" blocs du centre — en vie : ","color":"red"},{"score":{"name":"$alive","objective":"mg.st"},"color":"yellow"}]'])
w('uhc/cleanup', ['function mg:uhc/kill_all', 'function mg:core/rules', 'gamerule natural_health_regeneration true',
                  'effect clear @a[tag=mg.play] minecraft:haste', 'team leave @a[team=mg_green]'])

# =====================================================================  HUNGER GAMES
ZH, RH = C.param('ZH', 22800), 50
L, HH = terrain(C.param('seed_hg', 9502), RH, ZH, 70, 76, 88, 75, [], flat_center=9, theme=C.param('hg_theme', 'plaines'))
CH = (76 + 88) // 2   # hauteur de la corne d'abondance
L += [f'fill -8 {CH} {ZH - 8} 8 {CH} {ZH + 8} minecraft:smooth_stone', f'fill -8 {CH - 3} {ZH - 8} 8 {CH - 1} {ZH + 8} minecraft:stone',
      f'fill -8 {CH + 1} {ZH - 8} 8 {CH + 6} {ZH + 8} minecraft:air',
      f'fill -2 {CH + 1} {ZH - 2} 2 {CH + 1} {ZH + 2} minecraft:gold_block', f'fill -2 {CH + 4} {ZH - 2} 2 {CH + 4} {ZH + 2} minecraft:smooth_quartz_slab',
      f'fill -2 {CH + 2} {ZH - 2} -2 {CH + 3} {ZH - 2} minecraft:quartz_pillar', f'fill 2 {CH + 2} {ZH - 2} 2 {CH + 3} {ZH - 2} minecraft:quartz_pillar',
      f'fill -2 {CH + 2} {ZH + 2} -2 {CH + 3} {ZH + 2} minecraft:quartz_pillar', f'fill 2 {CH + 2} {ZH + 2} 2 {CH + 3} {ZH + 2} minecraft:quartz_pillar']
# coffres
rnd = random.Random(95)
center = [(-1, -1), (1, -1), (-1, 1), (1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)]
CHESTS = [(x, CH + 2, z, 'center') for x, z in center]
while len(CHESTS) < 8 + 26:
    x, z = rnd.randint(-RH + 4, RH - 4), rnd.randint(-RH + 4, RH - 4)
    if math.hypot(x, z) < 14 or HH[(x, z)] <= 76:
        continue
    if any(abs(x - a) + abs(z - b) < 12 for a, _, b, _ in CHESTS):
        continue
    CHESTS.append((x, HH[(x, z)] + 1, z, 'chest'))
w('hg/build', L)
w('hg/chests', ['# Coffres (remplis par loot table : mg:hg/center au centre, mg:hg/chest ailleurs)'] +
  [f'setblock {x} {y} {ZH + z} minecraft:air' for x, y, z, _ in CHESTS] +
  [f'setblock {x} {y} {ZH + z} minecraft:chest[facing={rnd.choice(["north", "south", "east", "west"])}]{{LootTable:"mg:hg/{k}"}}' for x, y, z, k in CHESTS])
PED = []
for i in range(24):
    a = 2 * math.pi * i / 24
    PED.append((round(7 * math.cos(a)), round(7 * math.sin(a))))
w('hg/pedestals', ['# Socles de départ (24, en cercle autour de la corne)'] +
  [f'setblock {x} {CH} {ZH + z} minecraft:emerald_block' for x, z in PED])
w('hg/place', ['# Place chaque joueur sur un socle (rotation $hgi)', 'scoreboard players set $hgi mg.st 0',
               'execute as @a[tag=mg.play,sort=random] run function mg:hg/place_one'])
w('hg/place_one', ['# @s → socle n°$hgi'] +
  [f'execute if score $hgi mg.st matches {i} run tp @s {x + .5} {CH + 1} {ZH + z + .5} facing 0 {CH + 1} {ZH}' for i, (x, z) in enumerate(PED)] +
  ['execute at @s run spawnpoint @s ~ ~ ~', 'scoreboard players add $hgi mg.st 1',
   'execute if score $hgi mg.st matches 24.. run scoreboard players set $hgi mg.st 0'])
zone('hg', ZH)
w('hg/prepare', ['# 🏹 Mini Hunger Games — préparation', 'function mg:hg/build', 'function mg:hg/pedestals', 'function mg:hg/chests',
                 'function mg:hg/kill_all',
                 'scoreboard players set $px mg.st 0', 'scoreboard players set $py mg.st 110', f'scoreboard players set $pz mg.st {ZH}',
                 'clear @a[tag=mg.play]', 'gamemode adventure @a[tag=mg.play]', 'team leave @a[tag=mg.play]', 'function mg:hg/place'])
w('hg/kill_all', [f'kill @e[type=minecraft:item,x={-RH - 3},y=60,z={ZH - RH - 3},dx={2 * RH + 6},dy=60,dz={2 * RH + 6}]',
                  f'kill @e[type=minecraft:arrow,x={-RH - 3},y=60,z={ZH - RH - 3},dx={2 * RH + 6},dy=60,dz={2 * RH + 6}]',
                  f'kill @e[type=minecraft:experience_orb,x={-RH - 3},y=60,z={ZH - RH - 3},dx={2 * RH + 6},dy=60,dz={2 * RH + 6}]'])
w('hg/go', ['# Départ : 10 s figés sur les socles', 'scoreboard players set $hgt mg.st 0', 'scoreboard players set #-1 mg.st -1',
            f'scoreboard players set $zr mg.st {RH + 2}', 'gamerule keep_inventory false', 'scoreboard players set @a mg.deaths 0',
            'team join mg_green @a[tag=mg.play]',
            'tellraw @a[tag=mg.play] ' + js([{'text': '🏹 MINI HUNGER GAMES : ', 'color': 'gold', 'bold': True},
                                             {'text': 'fouille les coffres (les meilleurs sont à la corne d\'abondance au centre). PvP après 20 s, coffres remplis à 2 min 30, la zone rétrécit à partir de 3 min. Dernier en vie gagne !', 'color': 'gray'}])])
w('hg/tick', ['# 🏹 Mini Hunger Games — tick', 'scoreboard players add $hgt mg.st 1',
              # compte à rebours figé sur les socles
              'execute if score $hgt mg.st matches ..199 as @a[tag=mg.play] at @s run tp @s ~ ~ ~',
              'execute if score $hgt mg.st matches ..199 run effect give @a[tag=mg.play] minecraft:slowness 1 9 true',
              'execute if score $hgt mg.st matches 1..199 run function mg:hg/countdown',
              'execute if score $hgt mg.st matches 200 run title @a[tag=mg.play] title {"text":"GO !","color":"green","bold":true}',
              'execute if score $hgt mg.st matches 200 as @a[tag=mg.play] at @s run playsound minecraft:entity.firework_rocket.blast master @s ~ ~ ~ 1 1',
              'execute if score $hgt mg.st matches 200 run effect clear @a[tag=mg.play] minecraft:slowness',
              'execute if score $hgt mg.st matches 600 run function mg:hg/pvp',
              'execute if score $hgt mg.st matches 3000 run function mg:hg/chests',
              'execute if score $hgt mg.st matches 3000 run tellraw @a[tag=mg.play] {"text":"🏹 Les coffres ont été remplis !","color":"gold"}',
              'execute if score $hgt mg.st matches 3000 as @a[tag=mg.play] at @s run playsound minecraft:block.chest.open master @s ~ ~ ~ 1 0.8',
              'execute as @a[tag=mg.play,scores={mg.deaths=1..}] run function mg:core/eliminate',
              'execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]',
              'execute as @a[tag=mg.play,scores={mg.t=..60}] run function mg:core/eliminate',
              'scoreboard players operation $hgq mg.st = $hgt mg.st', 'scoreboard players set #20 mg.st 20', 'scoreboard players operation $hgq mg.st %= #20 mg.st',
              'execute if score $hgq mg.st matches 0 run function mg:hg/second'] + lastman('hg'))
w('hg/countdown', ['scoreboard players operation $hgq mg.st = $hgt mg.st', 'scoreboard players set #20 mg.st 20',
                   'scoreboard players operation $hgq mg.st %= #20 mg.st', 'execute unless score $hgq mg.st matches 0 run return 0',
                   'scoreboard players set $hgc mg.st 10', 'scoreboard players operation $hgs mg.st = $hgt mg.st',
                   'scoreboard players operation $hgs mg.st /= #20 mg.st', 'scoreboard players operation $hgc mg.st -= $hgs mg.st',
                   'title @a[tag=mg.play] title {"score":{"name":"$hgc","objective":"mg.st"},"color":"gold","bold":true}',
                   'execute as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.4'])
w('hg/pvp', ['team leave @a[tag=mg.play]', 'title @a[tag=mg.play] actionbar {"text":"⚔ PvP activé !","color":"red","bold":true}',
             'execute as @a[tag=mg.play] at @s run playsound minecraft:entity.wither.spawn master @s ~ ~ ~ 0.4 1.5'])
w('hg/second', ['# Chaque seconde : zone 50 → 6 entre 3:00 et 5:00 (+10 s de compte à rebours)',
                'scoreboard players operation $hgs mg.st = $hgt mg.st', 'scoreboard players operation $hgs mg.st /= #20 mg.st',
                'execute if score $hgs mg.st matches 190.. run scoreboard players set $zr mg.st 50',
                'execute if score $hgs mg.st matches 190.. run scoreboard players operation $hgz mg.st = $hgs mg.st',
                'execute if score $hgs mg.st matches 190.. run scoreboard players remove $hgz mg.st 190',
                'execute if score $hgs mg.st matches 190.. run scoreboard players operation $hgz mg.st *= #11 mg.st',
                'execute if score $hgs mg.st matches 190.. run scoreboard players operation $hgz mg.st /= #30 mg.st',
                'execute if score $hgs mg.st matches 190.. run scoreboard players operation $zr mg.st -= $hgz mg.st',
                'execute if score $zr mg.st matches ..5 run scoreboard players set $zr mg.st 6',
                'execute if score $hgs mg.st matches 190.. run function mg:hg/zone',
                'execute if score $hgs mg.st matches 10..189 run title @a[tag=mg.play] actionbar [{"text":"🏹 En vie : ","color":"gold"},{"score":{"name":"$alive","objective":"mg.st"},"color":"yellow","bold":true}]',
                'execute if score $hgs mg.st matches 190.. run title @a[tag=mg.play,tag=!mg.zout] actionbar [{"text":"🏹 Zone ","color":"red"},{"score":{"name":"$zr","objective":"mg.st"},"color":"yellow","bold":true},{"text":" blocs du centre — en vie : ","color":"red"},{"score":{"name":"$alive","objective":"mg.st"},"color":"yellow"}]'])
w('hg/cleanup', ['function mg:hg/kill_all', 'function mg:core/rules', 'team leave @a[team=mg_green]'])

# ---------- loot tables
LT = os.path.join(C.D, 'loot_table/hg')
os.makedirs(LT, exist_ok=True)


def entry(item, weight, cmin=1, cmax=1, ench=None):
    e = {'type': 'minecraft:item', 'name': f'minecraft:{item}', 'weight': weight}
    f = []
    if cmax > 1:
        f.append({'function': 'minecraft:set_count', 'count': {'type': 'minecraft:uniform', 'min': cmin, 'max': cmax}})
    if f:
        e['functions'] = f
    return e


common = [entry('wooden_sword', 6), entry('stone_sword', 5), entry('stone_axe', 4), entry('bow', 3), entry('arrow', 6, 3, 8),
          entry('leather_helmet', 4), entry('leather_chestplate', 4), entry('leather_leggings', 4), entry('leather_boots', 4),
          entry('chainmail_helmet', 2), entry('chainmail_boots', 2), entry('bread', 7, 1, 3), entry('apple', 6, 1, 3),
          entry('cooked_porkchop', 4, 1, 2), entry('fishing_rod', 2), entry('iron_ingot', 3, 1, 2), entry('stick', 3, 1, 2),
          entry('golden_carrot', 2, 1, 2), entry('snowball', 3, 4, 12)]
best = [entry('iron_sword', 5), entry('stone_sword', 4), entry('iron_axe', 3), entry('bow', 4), entry('arrow', 6, 4, 10),
        entry('iron_helmet', 3), entry('iron_chestplate', 2), entry('iron_leggings', 2), entry('iron_boots', 3),
        entry('chainmail_chestplate', 3), entry('chainmail_leggings', 3), entry('golden_apple', 2), entry('cooked_beef', 5, 1, 3),
        entry('shield', 2), entry('ender_pearl', 1), entry('diamond', 1)]
for name, pool, rolls in [('chest', common, (3, 5)), ('center', best, (3, 5))]:
    json.dump({'type': 'minecraft:chest', 'pools': [{'rolls': {'type': 'minecraft:uniform', 'min': rolls[0], 'max': rolls[1]}, 'entries': pool}]},
              open(os.path.join(LT, f'{name}.json'), 'w', encoding='utf-8'), indent=2)

C.register([94, 95], 'survival', [
    C.announce(94, '', '⛏ MINI UHC RUN', 'gold', 'farm, PvP, zone qui rétrécit — 5 min !'),
    C.announce(95, '', '🏹 MINI HUNGER GAMES', 'gold', 'coffres, corne d\'abondance, dernier en vie — 5 min !')])
w('survival/prepare', ['execute if score $game mg.st matches 94 run function mg:uhc/prepare', 'execute if score $game mg.st matches 95 run function mg:hg/prepare'])
w('survival/go', ['execute if score $game mg.st matches 94 run function mg:uhc/go', 'execute if score $game mg.st matches 95 run function mg:hg/go'])
w('survival/tick', ['execute if score $game mg.st matches 94 run function mg:uhc/tick', 'execute if score $game mg.st matches 95 run function mg:hg/tick'])
w('survival/cleanup', ['execute if score $game mg.st matches 94 run function mg:uhc/cleanup', 'execute if score $game mg.st matches 95 run function mg:hg/cleanup'])
C.patch('survie/tick', 'execute if score $game mg.st matches 4 in minecraft:overworld run tag @e[type=minecraft:item,x=-60,y=-64,z=1140,dx=120,dy=384,dz=120] add mg.keep', [
    f'execute if score $game mg.st matches 94 in minecraft:overworld run tag @e[type=minecraft:item,x={-RU - 3},y=40,z={ZU - RU - 3},dx={2 * RU + 6},dy=90,dz={2 * RU + 6}] add mg.keep',
    f'execute if score $game mg.st matches 95 in minecraft:overworld run tag @e[type=minecraft:item,x={-RH - 3},y=40,z={ZH - RH - 3},dx={2 * RH + 6},dy=90,dz={2 * RH + 6}] add mg.keep'])
C.patch('core/load', 'scoreboard objectives add mg.bw trigger', ['scoreboard players set #7 mg.st 7', 'scoreboard players set #11 mg.st 11', 'scoreboard players set #30 mg.st 30'])
C.patch('desinstaller', 'scoreboard objectives remove mg.bw', ['data remove storage mg:zone r'])
C.forceload([f'# Mini UHC Run (z {ZU}) et Mini Hunger Games (z {ZH})', f'forceload add {-RU - 2} {ZU - RU - 2} {RU + 2} {ZU + RU + 2}',
             f'forceload add {-RH - 2} {ZH - RH - 2} {RH + 2} {ZH + RH + 2}'])
print('UHC/HG OK', len(open(os.path.join(C.F, 'uhc/build.mcfunction')).read().split('\n')), 'lignes UHC,',
      len(open(os.path.join(C.F, 'hg/build.mcfunction')).read().split('\n')), 'lignes HG')
