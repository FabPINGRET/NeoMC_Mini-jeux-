"""🧟 Zombies façon Call of Duty (id 97) et 🧪 Infection (id 98). Même carte : bunker de 4 salles en z 23200.

    python tools/arcade/gen_zombies.py .

Zombies (97) : coop contre des manches de zombies de plus en plus nombreux et résistants. Armes réelles (tools/arcade/guns.py),
points (+10 par balle qui touche, +60 par kill), portes à acheter, armes au mur, boîte mystère, Juggernog, Speed Cola.
Mort → spectateur jusqu'à la fin de la manche (réanimé avec pistolet). 20 manches = victoire, tout le monde mort = défaite.
Façon Call of Duty : boissons (Juggernog, Speed Cola, Quick Revive, Double Tap, Stamin-Up, Mule Kick), Pack-a-Punch (arme ×3),
fenêtres barricadées que les zombies cassent et que l'on répare accroupi devant, bonus lâchés par les zombies (mort instantanée,
Kaboom, points doubles, charpentier, vente de feu), grenade singe, lance-roquettes, batte, mobs variés (rapides, rampants, brutes)
et manches des chiens à la 5, 10 et 15. Munitions illimitées (seul le chargeur se recharge). Q = jeter une arme à un coéquipier.
Partie commune à toutes les cartes (bonus, singe, roquettes, fenêtres) : fonctions zx/.
Infection (98) : un ou plusieurs joueurs commencent zombies ; un survivant tué devient zombie. Survivants armés,
zombies au corps à corps (plus rapides et plus forts), réapparition infinie. 3 min : les survivants restants gagnent.
Seul : mode entraînement (pas de victoire, fin au chrono ou menu → Arrêter).
"""
import json
import os
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
import guns as G

w, js = C.w, C.js
Z = C.param('Z', 23200)
THEME = C.param('blocks', {})     # carte supplémentaire : remplacement des blocs du décor (tools/arcade/gen_maps.py)
NAME = C.param('name', 'Bunker')
ROUNDS = 20
LAYOUT = C.param('layout', None)   # carte au plan différent (tools/arcade/zombie_layouts.py), sinon le bunker
G.build()

ROOMS = {'a': (-10, 10, Z - 10, Z + 10), 'b': (-10, 10, Z - 32, Z - 12), 'c': (12, 32, Z - 10, Z + 10), 'd': (12, 32, Z - 32, Z - 12)}
# portes : id → (nom, coût, (x1,z1,x2,z2) du barrage, position interaction, salle ouverte)
DOORS = {1: ('A → B', 750, (-1, Z - 11, 1, Z - 11), (0.5, Z - 10.5), 'b'),
         2: ('A → C', 750, (11, Z - 1, 11, Z + 1), (11.5, Z + 0.5), 'c'),
         3: ('B → D', 1000, (11, Z - 23, 11, Z - 21), (11.5, Z - 21.5), 'd'),
         4: ('C → D', 1000, (21, Z - 11, 23, Z - 11), (22.5, Z - 10.5), 'd')}
# fenêtres (salle, x, z, normale vers l'extérieur)
WIN = [('a', -11, Z + 4, -1, 0), ('a', 0, Z + 11, 0, 1), ('b', -11, Z - 22, -1, 0), ('b', 0, Z - 33, 0, -1),
       ('c', 33, Z + 4, 1, 0), ('c', 22, Z + 11, 0, 1), ('d', 33, Z - 22, 1, 0), ('d', 22, Z - 33, 0, -1)]
# achats au mur : tag, nom, coût, position interaction (x, z), arme (0 = autre), position (arme collée à la face du mur, côté salle ; suppose un modèle plat handheld/generated) et orientation de l'affichage
WALL = [('zb11', 'Fusil M14', 500, (-9.5, Z + 6.5), 4, (-9.95, Z + 6.5), 90),
        ('zb12', 'Fusil à pompe', 500, (10.5, Z + 6.5), 3, (10.95, Z + 6.5), -90),
        ('zb13', 'Mitraillette', 1000, (-9.5, Z - 15.5), 2, (-9.95, Z - 15.5), 90),
        ('zb14', 'Sniper', 1500, (10.5, Z - 28.5), 5, (10.95, Z - 28.5), -90),
        ('zb15', 'Grenades singe ×3', 1000, (-9.5, Z - 26.5), 11, (-9.95, Z - 26.5), 90)]
# armes hors guns.py : 10 = lance-roquettes, 11 = grenades singe, 12 = batte
EXTRA = {10: ('Lance-roquettes', 'red'), 11: ('Grenades singe', 'gold'), 12: ('Batte cloutée', 'gold')}
# boissons et Pack-a-Punch : tag interaction, nom, texte, coût, bloc de la machine (x, z), interaction (x, z), étiquette (x, z), blocs (bas, milieu)
PERKS = [('zb23', '💙 Quick Revive', 'relevé 5 s après ta mort (une fois)', 1500, (-10, Z - 4), (-8.5, Z - 3.5), (-8.0, Z - 3.5), ('light_blue_glazed_terracotta', 'light_blue_stained_glass')),
         ('zb24', '🍺 Double Tap', 'tir plus rapide, dégâts ×2', 2000, (10, Z - 14), (9.5, Z - 13.5), (9.0, Z - 13.5), ('orange_glazed_terracotta', 'orange_stained_glass')),
         ('zb25', '🏃 Stamin-Up', 'tu cours plus vite', 2000, (32, Z - 4), (31.5, Z - 3.5), (31.0, Z - 3.5), ('yellow_glazed_terracotta', 'yellow_stained_glass')),
         ('zb26', '🐴 Mule Kick', 'une 3e arme', 4000, (32, Z - 28), (31.5, Z - 27.5), (31.0, Z - 27.5), ('green_glazed_terracotta', 'green_stained_glass')),
         ('zb27', '⚡ Pack-a-Punch', 'arme en main améliorée (×3)', 3000, (28, Z - 32), (28.5, Z - 30.5), (28.5, Z - 31.0), ('obsidian', 'crying_obsidian'))]
BARRELS = [(-6, Z - 6), (5, Z + 4), (-5, Z - 26), (6, Z - 19), (17, Z - 5), (27, Z + 2), (16, Z - 29), (27, Z - 20)]
# machines fixes : (bloc, interaction, étiquette) ; boîte mystère ; départ ; zone de la carte (x1, z1, x2, z2)
JUG = ((32, Z + 6), (31.5, Z + 6.5), (31.0, Z + 6.5))
SPEED = ((32, Z - 15), (31.5, Z - 14.5), (31.0, Z - 14.5))
BOXP = (22, Z - 27)
SX, SZ = 0, Z
AREA = (-17, Z - 39, 39, Z + 17)
LY = None
if LAYOUT:
    import zombie_layouts
    LY = zombie_layouts.get(LAYOUT, Z)
    ROOMS, DOORS, WIN, WALL, BARRELS = LY['rooms'], LY['doors'], LY['wins'], LY['walls'], LY['barrels']
    PERKS = [(t, nm, tx, c, LY['perks'][t][0], LY['perks'][t][1], LY['perks'][t][2], blk) for (t, nm, tx, c, _, _, _, blk) in PERKS]
    JUG, SPEED, BOXP = LY['jug'], LY['speed'], LY['box']
    SX, SZ = LY['start']
    AREA = LY['area']
AX1, AZ1, AX2, AZ2 = AREA


def inf_spread(sel):
    """Infection : joueurs répartis dans la carte (bunker : autour du centre ; plan : centre d'une salle au hasard)"""
    if LY:
        return f'execute as {sel} run tp @s @e[type=minecraft:marker,tag=mg.zrc,sort=random,limit=1]'
    return f'spreadplayers 11 {Z - 11} 4 18 under 84 false {sel}'

# ------------------------------------------------------------------ carte
L = ['# 🧟 Bunker (Zombies / Infection) — 4 salles 21×21, x −11..33, z 23167..23211, sol y 80, toit y 86']
L += [f'fill {AX1} {y} {AZ1} {AX2} {y} {AZ2} minecraft:air' for y in range(78, 92)]
if LY:
    # plan : tout plein, puis les salles creusées (murs d'un bloc entre salles voisines)
    L[0] = f'# 🧟 {NAME} (Zombies / Infection) — ' + ', '.join(LY['names'].values()) + ' — sol y 80, toit y 86'
    L += [f'fill {AX1 + 1} 79 {AZ1 + 1} {AX2 - 1} 79 {AZ2 - 1} minecraft:stone',
          # une couche par fill (limite de 32 768 blocs par commande)
          *[f'fill {AX1 + 1} {y} {AZ1 + 1} {AX2 - 1} {y} {AZ2 - 1} minecraft:{LY["wall"]}' for y in range(80, 86)],
          f'fill {AX1 + 1} 81 {AZ1 + 1} {AX2 - 1} 81 {AZ2 - 1} minecraft:{LY["band"]}',
          f'fill {AX1 + 1} 86 {AZ1 + 1} {AX2 - 1} 86 {AZ2 - 1} minecraft:{LY["roof"]}']
    for r, (x1, x2, z1, z2) in ROOMS.items():
        L += [f'fill {x1} 80 {z1} {x2} 80 {z2} minecraft:{LY["floors"][r]}', f'fill {x1} 81 {z1} {x2} 85 {z2} minecraft:air']
        L += [f'setblock {x} 86 {z} minecraft:{LY["light"]}' for x in range(x1 + 2, x2 - 1, 5) for z in range(z1 + 2, z2 - 1, 5)]
else:
    L += [f'fill -11 79 {Z - 33} 33 79 {Z + 11} minecraft:stone']
for r, (x1, x2, z1, z2) in (ROOMS.items() if not LY else []):
    L.append(f'fill {x1} 80 {z1} {x2} 80 {z2} minecraft:{ {"a": "polished_andesite", "b": "stone_bricks", "c": "polished_deepslate", "d": "mossy_stone_bricks"}[r] }')
L += [] if LY else [f'fill -11 80 {Z - 33} 33 85 {Z - 33} minecraft:stone_bricks', f'fill -11 80 {Z + 11} 33 85 {Z + 11} minecraft:stone_bricks',
      f'fill -11 80 {Z - 32} -11 85 {Z + 10} minecraft:stone_bricks', f'fill 33 80 {Z - 32} 33 85 {Z + 10} minecraft:stone_bricks',
      f'fill 11 80 {Z - 32} 11 85 {Z + 10} minecraft:stone_bricks', f'fill -10 80 {Z - 11} 32 85 {Z - 11} minecraft:stone_bricks',
      f'fill -11 86 {Z - 33} 33 86 {Z + 11} minecraft:smooth_stone',
      f'fill -11 81 {Z - 33} 33 81 {Z + 11} minecraft:cracked_stone_bricks replace minecraft:stone_bricks']
L += [] if LY else [f'setblock {x} 86 {z} minecraft:sea_lantern' for x in range(-6, 33, 6) for z in range(Z - 30, Z + 11, 6)]
# portes : ouverture 3×3 + barricade en planches
for d, (nm, cost, (x1, z1, x2, z2), _, _) in DOORS.items():
    L.append(f'fill {x1} 81 {z1} {x2} 83 {z2} minecraft:dark_oak_planks')
# fenêtres + enclos d'apparition
for (r, x, z, nx, nz) in WIN:
    px, pz = (0, 1) if nx else (1, 0)          # axe perpendiculaire
    def P(d, p):
        return x + nx * d + px * p, z + nz * d + pz * p
    ax, az = P(1, -2); bx, bz = P(4, 2)
    L.append(f'fill {min(ax, bx)} 80 {min(az, bz)} {max(ax, bx)} 84 {max(az, bz)} minecraft:stone_bricks')
    ax, az = P(1, -1); bx, bz = P(3, 1)
    L.append(f'fill {min(ax, bx)} 81 {min(az, bz)} {max(ax, bx)} 83 {max(az, bz)} minecraft:air')
    L.append(f'fill {x} 81 {z} {x} 82 {z} minecraft:air')
    L.append(f'fill {x - px} 83 {z - pz} {x + px} 83 {z + pz} minecraft:iron_bars')
# décor : caisses, tables, éclairage
for (x, z) in BARRELS:
    L +=[f'fill {x} 81 {z} {x + 1} 81 {z + 1} minecraft:barrel[facing=up]', f'setblock {x} 82 {z} minecraft:barrel[facing=up]']
for (x, z) in ([] if LY else [(3, Z - 3), (-3, Z - 20), (20, Z + 3), (24, Z - 24)]):
    L += [f'fill {x} 81 {z} {x + 2} 81 {z} minecraft:spruce_slab[type=top]', f'setblock {x + 1} 82 {z} minecraft:lantern']
# machines : Juggernog (rouge), Speed Cola (vert), boîte mystère
(jx, jz), (sx_, sz_), (bx_, bz_) = JUG[0], SPEED[0], BOXP
L += [f'setblock {jx} 81 {jz} minecraft:red_glazed_terracotta', f'setblock {jx} 82 {jz} minecraft:red_stained_glass',
      f'setblock {jx} 83 {jz} minecraft:redstone_lamp[lit=true]',
      f'setblock {sx_} 81 {sz_} minecraft:lime_glazed_terracotta', f'setblock {sx_} 82 {sz_} minecraft:lime_stained_glass',
      f'setblock {sx_} 83 {sz_} minecraft:redstone_lamp[lit=true]',
      f'setblock {bx_} 81 {bz_} minecraft:chest[facing=south]', f'setblock {bx_ - 1} 81 {bz_} minecraft:spruce_planks',
      f'setblock {bx_ + 1} 81 {bz_} minecraft:spruce_planks', f'setblock {bx_} 85 {bz_} minecraft:soul_lantern[hanging=true]']
for _, _, _, _, (bx, bz), _, _, (b1, b2) in PERKS:
    L += [f'setblock {bx} 81 {bz} minecraft:{b1}', f'setblock {bx} 82 {bz} minecraft:{b2}', f'setblock {bx} 83 {bz} minecraft:redstone_lamp[lit=true]']
import re
L = [re.sub(r'minecraft:([a-z_]+)', lambda m: 'minecraft:' + THEME.get(m.group(1), m.group(1)), l) for l in L]
L[0] = L[0].replace('Bunker', NAME)
w('zm/build', L)

# entités : portes, achats, apparitions
E = ['# Entités du bunker (portes, achats, apparitions) — tag mg.zent', 'kill @e[tag=mg.zent]']
for (r, x, z, nx, nz) in WIN:
    E.append(f'summon minecraft:marker {x + nx * 2 + .5} 81 {z + nz * 2 + .5} {{Tags:["mg.zent","mg.zsp","mg.zr_{r}"]}}')
for d, (nm, cost, (x1, z1, x2, z2), (ix, iz), room) in DOORS.items():
    ox, oz = (0, 1.5) if z1 == z2 else (1.5, 0)    # une étiquette sur chaque face du mur (décalage perpendiculaire au mur)
    txt = f'[{{"text":"🚪 Porte {nm}","color":"gold","bold":true}},{{"text":"\\nclic droit — {cost} pts","color":"yellow"}}]'
    E += [f'summon minecraft:interaction {ix} 81 {iz} {{Tags:["mg.zent","mg.zbuy","mg.zb{d}","mg.zd{d}"],width:3.4f,height:3f,response:1b}}',
          *[f'summon minecraft:text_display {ix + s * ox} 84.3 {iz + s * oz} {{Tags:["mg.zent","mg.zd{d}"],billboard:"center",text:{txt}}}' for s in (-1, 1)]]
for tag, nm, cost, (ix, iz), gn, (dx, dz), rot in WALL:
    TF = 'transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]}'
    icon = '🐵' if gn == 11 else '🔫'
    E += [f'summon minecraft:interaction {ix} 81 {iz} {{Tags:["mg.zent","mg.zbuy","mg.{tag}"],width:1.3f,height:2.4f,response:1b}}',
          f'summon minecraft:text_display {round(dx + (0.95 if rot == 90 else -0.95), 2)} 83.3 {dz} {{Tags:["mg.zent"],billboard:"center",text:[{{"text":"{icon} {nm}","color":"aqua","bold":true}},{{"text":"\\n{cost} pts","color":"yellow"}}]}}']
    if gn in G.GUNS:
        E += [f'execute if score $rp mg.st matches 1 run summon minecraft:item_display {dx} 82.4 {dz} {{Tags:["mg.zent"],Rotation:[{rot}f,0f],item:{{id:"minecraft:warped_fungus_on_a_stick",count:1,components:{{"minecraft:item_model":"mg:gun_{G.GUNS[gn][1]}"}}}},{TF}}}',
              f'execute unless score $rp mg.st matches 1 run summon minecraft:item_display {dx} 82.4 {dz} {{Tags:["mg.zent"],Rotation:[{rot}f,0f],item:{{id:"minecraft:crossbow",count:1}},{TF}}}']
    else:
        E.append(f'summon minecraft:item_display {dx} 82.4 {dz} {{Tags:["mg.zent"],Rotation:[{rot}f,0f],item:{{id:"minecraft:snowball",count:1}},{TF}}}')
for tag, nm, txt, cost, _, (ix, iz), (tx, tz), _ in PERKS:
    E += [f'summon minecraft:interaction {ix} 81 {iz} {{Tags:["mg.zent","mg.zbuy","mg.{tag}"],width:1.3f,height:2.4f,response:1b}}',
          f'summon minecraft:text_display {tx} 84.4 {tz} {{Tags:["mg.zent"],billboard:"center",text:' +
          js([{'text': nm, 'color': 'light_purple' if tag == 'zb27' else 'aqua', 'bold': True}, {'text': f'\n{txt}, {cost} pts', 'color': 'yellow'}]) + '}']
# caisses : une interaction par-dessus pour qu'on ne puisse pas les ouvrir
E += [f'summon minecraft:interaction {x + 1} 81 {z + 1} {{Tags:["mg.zent","mg.zlock"],width:2.05f,height:2.05f}}' for (x, z) in BARRELS]
# fenêtres : un marqueur dans chaque ouverture (barricade, zx/win_*)
E += [f'summon minecraft:marker {x + .5} 81 {z + .5} {{Tags:["mg.zent","mg.zwin"]}}' for (r, x, z, nx, nz) in WIN]
(jix, jiz), (jtx, jtz), (six, siz), (stx, stz) = JUG[1], JUG[2], SPEED[1], SPEED[2]
bix, biz = BOXP[0] + 0.5, BOXP[1] + 0.5
if LY:   # infection : centres des salles (répartition des joueurs)
    E += [f'summon minecraft:marker {(x1 + x2) / 2 + .5} 81 {(z1 + z2) / 2 + .5} {{Tags:["mg.zent","mg.zrc"]}}' for (x1, x2, z1, z2) in ROOMS.values()]
E += [f'summon minecraft:interaction {jix} 81 {jiz} {{Tags:["mg.zent","mg.zbuy","mg.zb21"],width:1.3f,height:2.4f,response:1b}}',
      f'summon minecraft:text_display {jtx} 84.4 {jtz} {{Tags:["mg.zent"],billboard:"center",text:[{{"text":"❤ Juggernog","color":"red","bold":true}},{{"text":"\\n2× plus de vie — 2500 pts","color":"yellow"}}]}}',
      f'summon minecraft:interaction {six} 81 {siz} {{Tags:["mg.zent","mg.zbuy","mg.zb22"],width:1.3f,height:2.4f,response:1b}}',
      f'summon minecraft:text_display {stx} 84.4 {stz} {{Tags:["mg.zent"],billboard:"center",text:[{{"text":"⚡ Speed Cola","color":"green","bold":true}},{{"text":"\\nrecharge 2× plus vite — 3000 pts","color":"yellow"}}]}}',
      f'summon minecraft:interaction {bix} 81 {biz} {{Tags:["mg.zent","mg.zbuy","mg.zb20"],width:1.6f,height:1.6f,response:1b}}',
      f'summon minecraft:text_display {bix} 83.4 {biz} {{Tags:["mg.zent"],billboard:"center",text:[{{"text":"❓ Boîte mystère","color":"light_purple","bold":true}},{{"text":"\\narme au hasard — 950 pts","color":"yellow"}}]}}',
      'tag @e[tag=mg.zr_a] add mg.zon']
w('zm/entities', E)
w('zm/open_all', ['# Infection : toutes les portes ouvertes, pas d\'achats'] +
  [f'fill {x1} 81 {z1} {x2} 83 {z2} minecraft:air' for d, (_, _, (x1, z1, x2, z2), _, _) in DOORS.items()] +
  ['kill @e[tag=mg.zbuy]', 'kill @e[type=minecraft:text_display,tag=mg.zent]', 'kill @e[type=minecraft:item_display,tag=mg.zent]',
   'kill @e[tag=mg.zwin]', f'summon minecraft:interaction {bix} 81 {biz} {{Tags:["mg.zent","mg.zlock"],width:1.1f,height:1.1f}}',
   'tag @e[tag=mg.zsp] add mg.zon'])
w('zm/kill_all', ['kill @e[tag=mg.zz]', 'kill @e[tag=mg.zent]',
                  f'kill @e[type=minecraft:item,x={AX1},y=70,z={AZ1},dx={AX2 - AX1},dy=25,dz={AZ2 - AZ1}]',
                  f'kill @e[type=minecraft:experience_orb,x={AX1},y=70,z={AZ1},dx={AX2 - AX1},dy=25,dz={AZ2 - AZ1}]'])

# ------------------------------------------------------------------ commun (dispatch 97 / 98)
w('zmode/prepare', ['execute if score $game mg.st matches 97 run function mg:zm/prepare', 'execute if score $game mg.st matches 98 run function mg:inf/prepare'])
w('zmode/go', ['execute if score $game mg.st matches 97 run function mg:zm/go', 'execute if score $game mg.st matches 98 run function mg:inf/go'])
w('zmode/tick', ['execute if score $game mg.st matches 97 as @a[tag=mg.play,scores={mg.qs=1..}] if items entity @s weapon.mainhand *[custom_data~{zrpg:1b}] at @s run function mg:zx/rpg_fire',
                 'function mg:gun/tick', 'execute if score $game mg.st matches 97 run function mg:zm/tick', 'execute if score $game mg.st matches 98 run function mg:inf/tick'])
w('zmode/cleanup', ['scoreboard players set $zpts mg.st 0', 'function mg:zx/reset', 'function mg:zm/kill_all', 'execute as @a[tag=mg.zjug] run attribute @s minecraft:max_health base set 20',
                    'tag @a remove mg.zjug', 'tag @a remove mg.zsc', 'tag @a remove mg.zdead', 'tag @a remove mg.inf', 'tag @a remove mg.gtg',
                    'tag @a remove mg.zqr', 'tag @a remove mg.zqrw', 'tag @a remove mg.zdbl', 'tag @a remove mg.zst', 'tag @a remove mg.zmu',
                    'execute as @a run function mg:gun/reset', 'team leave @a[team=mg_green]',
                    'effect clear @a[tag=mg.play] minecraft:speed', 'effect clear @a[tag=mg.play] minecraft:strength',
                    'scoreboard players reset * mg.zpt'])

# ------------------------------------------------------------------ ZOMBIES
w('zm/prepare', ['# 🧟 Zombies — préparation', 'function mg:zm/build', 'function mg:zm/kill_all', 'function mg:zm/entities',
                 'scoreboard players set @e[type=minecraft:marker,tag=mg.zwin] mg.zws 6', 'execute as @e[type=minecraft:marker,tag=mg.zwin] at @s run function mg:zx/win_set',
                 f'scoreboard players set $px mg.st {SX}', 'scoreboard players set $py mg.st 84', f'scoreboard players set $pz mg.st {SZ}',
                 'clear @a[tag=mg.play]', 'gamemode adventure @a[tag=mg.play]', 'team join mg_blue @a[tag=mg.play]',
                 f'spreadplayers {SX} {SZ} 2 6 under 84 false @a[tag=mg.play]', 'execute as @a[tag=mg.play] at @s run spawnpoint @s ~ ~ ~'])
w('zm/kit', ['# @s : couteau + pistolet', 'clear @s', 'function mg:gun/reset',
             'item replace entity @s hotbar.0 with minecraft:iron_sword[unbreakable={},custom_name=[{"text":"🔪 Couteau","color":"gray","italic":false}]]',
             G.give(1, 'hotbar.1'), 'item replace entity @s hotbar.8 with minecraft:cooked_beef 16'])
w('zm/go', ['# Départ', 'scoreboard players set $zpts mg.st 1', 'scoreboard players set $zr mg.st 0', 'scoreboard players set $zph mg.st 0', 'scoreboard players set $zb mg.st 100',
            'scoreboard players set #2 mg.st 2', 'scoreboard players set @a[tag=mg.play] mg.zpt 500', 'scoreboard players reset @a mg.zkl',
            'scoreboard objectives setdisplay sidebar mg.zpt', 'scoreboard players set @a mg.deaths 0', 'function mg:zx/reset',
            'scoreboard players set $zid mg.st 0', 'execute as @a[tag=mg.play] store result score @s mg.zid run scoreboard players add $zid mg.st 1',
            'execute as @a[tag=mg.play] run function mg:zm/kit',
            'tellraw @a[tag=mg.play] ' + js([{'text': '🧟 ZOMBIES : ', 'color': 'dark_green', 'bold': True},
                                             {'text': f'survivez à {ROUNDS} manches ! Clic droit = tirer, accroupi = recharger, munitions illimitées. Chaque balle qui touche = 10 pts, chaque kill = 60 pts. Clic droit sur les portes, armes au mur, boîte mystère, boissons et Pack-a-Punch pour les acheter. Un joueur mort revient à la manche suivante.', 'color': 'gray'}]),
            'tellraw @a[tag=mg.play] ' + js([{'text': ' 🪵 Fenêtres : ', 'color': 'gold'}, {'text': 'les zombies cassent les planches, accroupis-toi devant pour les reclouer (+10 pts). ', 'color': 'gray'},
                                             {'text': '🎁 Bonus : ', 'color': 'gold'}, {'text': 'les zombies lâchent parfois mort instantanée, Kaboom, points doubles, charpentier ou vente de feu, marche dessus. ', 'color': 'gray'},
                                             {'text': '🔫 Q : ', 'color': 'gold'}, {'text': 'jeter ton arme à un coéquipier.', 'color': 'gray'}])])
w('zm/tick', ['# 🧟 Zombies — tick',
              'execute as @a[tag=mg.play,tag=!mg.zdead,scores={mg.deaths=1..}] run function mg:zm/die',
              'execute as @a[tag=mg.play,scores={mg.zkl=1..}] run function mg:zm/kill_points',
              'execute as @a[tag=mg.zqrw] run function mg:zm/qr_tick', 'function mg:zx/tick',
              'execute as @e[type=minecraft:interaction,tag=mg.zbuy] if data entity @s interaction run function mg:zm/buy',
              'execute if score $zph mg.st matches 0 run function mg:zm/break_tick',
              'execute if score $zph mg.st matches 1 run function mg:zm/round_tick',
              'scoreboard players add $zt mg.st 1', 'scoreboard players operation $zq mg.st = $zt mg.st', 'scoreboard players set #20 mg.st 20',
              'scoreboard players operation $zq mg.st %= #20 mg.st', 'execute if score $zq mg.st matches 0 run function mg:zm/second',
              'execute if score $state mg.st matches 2 unless entity @a[tag=mg.play,tag=!mg.zdead] unless entity @a[tag=mg.zqrw] run function mg:zm/defeat'])
w('zm/kill_points', ['scoreboard players operation $zk mg.st = @s mg.zkl', 'scoreboard players set #60 mg.st 60',
                     'execute if score $zdp mg.st matches 1.. run scoreboard players set #60 mg.st 120',
                     'scoreboard players operation $zk mg.st *= #60 mg.st', 'scoreboard players operation @s mg.zpt += $zk mg.st',
                     'scoreboard players set #60 mg.st 60', 'scoreboard players reset @s mg.zkl'])
w('zm/qr_tick', ['# @s (Quick Revive) : relevé au bout de 5 s', 'scoreboard players remove @s mg.zrt 1',
                 'execute if score @s mg.zrt matches 1.. run return 0', 'tag @s remove mg.zqrw',
                 'tellraw @a[tag=mg.play] [{"text":"💙 ","color":"aqua"},{"selector":"@s","color":"aqua"},{"text":" est relevé par sa Quick Revive !","color":"gray"}]',
                 'function mg:zm/revive'])
w('zm/break_tick', ['scoreboard players remove $zb mg.st 1', 'execute if score $zb mg.st matches ..0 run function mg:zm/round_start'])
w('zm/round_start', ['# Nouvelle manche : nombre, vie et vitesse des zombies', 'scoreboard players add $zr mg.st 1',
                     'scoreboard players set $zph mg.st 1', 'scoreboard players set $zsc mg.st 0', 'scoreboard players reset * mg.zrp',
                     # nombre = (5 + 4r) × (2n − 1) / 2 (seul : ×1), max 160 — +1 « part » complète par joueur au-delà de 2
                     'scoreboard players operation $zleft mg.st = $zr mg.st', 'scoreboard players set #4 mg.st 4',
                     'scoreboard players operation $zleft mg.st *= #4 mg.st', 'scoreboard players add $zleft mg.st 5',
                     'execute store result score $zpn mg.st if entity @a[tag=mg.play]',
                     'scoreboard players operation $zn mg.st = $zpn mg.st', 'scoreboard players operation $zn mg.st *= #2 mg.st', 'scoreboard players remove $zn mg.st 1',
                     'execute if score $zn mg.st matches ..1 run scoreboard players set $zn mg.st 2',
                     'scoreboard players operation $zleft mg.st *= $zn mg.st', 'scoreboard players operation $zleft mg.st /= #2 mg.st',
                     'execute if score $zleft mg.st matches 161.. run scoreboard players set $zleft mg.st 160',
                     # zombies en vie en même temps : 16 + 4n, max 40
                     'scoreboard players operation $zmx mg.st = $zpn mg.st', 'scoreboard players operation $zmx mg.st *= #4 mg.st',
                     'scoreboard players add $zmx mg.st 16', 'execute if score $zmx mg.st matches 41.. run scoreboard players set $zmx mg.st 40',
                     # vie = 16 + 8 (r − 1), max 150 ; vitesse 0,23 / 0,27 / 0,32 ; cadence d'apparition 22 − 2r (min 8)
                     'scoreboard players operation $zhp mg.st = $zr mg.st', 'scoreboard players set #8 mg.st 8',
                     'scoreboard players operation $zhp mg.st *= #8 mg.st', 'scoreboard players add $zhp mg.st 8',
                     'execute if score $zhp mg.st matches 151.. run scoreboard players set $zhp mg.st 150',
                     'scoreboard players set $zsp mg.st 23', 'execute if score $zr mg.st matches 4.. run scoreboard players set $zsp mg.st 27',
                     'execute if score $zr mg.st matches 7.. run scoreboard players set $zsp mg.st 32', 'execute if score $zr mg.st matches 13.. run scoreboard players set $zsp mg.st 35',
                     'scoreboard players operation $zsi mg.st = $zr mg.st', 'scoreboard players operation $zsi mg.st *= #2 mg.st',
                     'scoreboard players set $zsj mg.st 22', 'scoreboard players operation $zsj mg.st -= $zsi mg.st',
                     'execute if score $zsj mg.st matches ..7 run scoreboard players set $zsj mg.st 8',
                     'execute if score $zpn mg.st matches 3.. run scoreboard players operation $zsj mg.st -= $zpn mg.st',
                     'execute if score $zpn mg.st matches 3.. run scoreboard players add $zsj mg.st 2',
                     'execute if score $zsj mg.st matches ..3 run scoreboard players set $zsj mg.st 4',
                     'execute store result storage mg:zm hp int 1 run scoreboard players get $zhp mg.st',
                     'execute store result storage mg:zm sp double 0.01 run scoreboard players get $zsp mg.st',
                     # variantes : rapides et rampants (vie ×0,6, +0,07 vitesse), brutes (vie ×3, −0,03), chiens (vie ×0,5, +0,12)
                     'scoreboard players set #10 mg.st 10', 'scoreboard players set #6 mg.st 6',
                     'scoreboard players operation $zx mg.st = $zhp mg.st', 'scoreboard players operation $zx mg.st *= #6 mg.st', 'scoreboard players operation $zx mg.st /= #10 mg.st',
                     'execute store result storage mg:zm hpf int 1 run scoreboard players get $zx mg.st',
                     'scoreboard players operation $zx mg.st = $zhp mg.st', 'scoreboard players operation $zx mg.st *= #3 mg.st',
                     'execute store result storage mg:zm hpb int 1 run scoreboard players get $zx mg.st',
                     'scoreboard players operation $zx mg.st = $zhp mg.st', 'scoreboard players operation $zx mg.st /= #2 mg.st',
                     'execute store result storage mg:zm hpd int 1 run scoreboard players get $zx mg.st',
                     'scoreboard players operation $zx mg.st = $zsp mg.st', 'scoreboard players add $zx mg.st 7',
                     'execute store result storage mg:zm spf double 0.01 run scoreboard players get $zx mg.st',
                     'scoreboard players remove $zx mg.st 10', 'execute store result storage mg:zm spb double 0.01 run scoreboard players get $zx mg.st',
                     'scoreboard players add $zx mg.st 15', 'execute store result storage mg:zm spd double 0.01 run scoreboard players get $zx mg.st',
                     # manches 5, 10 et 15 : chiens de l'enfer (6 + 3 par joueur)
                     'scoreboard players set $zdog mg.st 0', 'execute if score $zr mg.st matches 5 run scoreboard players set $zdog mg.st 1',
                     'execute if score $zr mg.st matches 10 run scoreboard players set $zdog mg.st 1', 'execute if score $zr mg.st matches 15 run scoreboard players set $zdog mg.st 1',
                     'execute if score $zdog mg.st matches 1 run scoreboard players operation $zleft mg.st = $zpn mg.st',
                     'execute if score $zdog mg.st matches 1 run scoreboard players operation $zleft mg.st *= #3 mg.st',
                     'execute if score $zdog mg.st matches 1 run scoreboard players add $zleft mg.st 6',
                     'execute if score $zdog mg.st matches 1 run title @a[tag=mg.play] title {"text":"🔥 Chiens de l\'enfer","color":"gold","bold":true}',
                     'execute if score $zdog mg.st matches 1 run title @a[tag=mg.play] subtitle [{"score":{"name":"$zleft","objective":"mg.st"},"color":"yellow"},{"text":" chiens","color":"gray"}]',
                     'execute if score $zdog mg.st matches 1 as @a[tag=mg.play] at @s run playsound minecraft:entity.wolf.howl master @s ~ ~ ~ 1 0.6',
                     'execute if score $zdog mg.st matches 1 run return 0',
                     'title @a[tag=mg.play] title [{"text":"Manche ","color":"dark_red","bold":true},{"score":{"name":"$zr","objective":"mg.st"},"color":"red","bold":true}]',
                     'title @a[tag=mg.play] subtitle [{"score":{"name":"$zleft","objective":"mg.st"},"color":"yellow"},{"text":" zombies","color":"gray"}]',
                     'execute as @a[tag=mg.play] at @s run playsound minecraft:entity.wither.spawn master @s ~ ~ ~ 0.3 0.6'])
w('zm/round_tick', ['# Manche en cours : apparitions, fin de manche',
                    'scoreboard players add $zsc mg.st 1',
                    'execute store result score $zal mg.st if entity @e[tag=mg.zz]',
                    'execute if score $zsc mg.st >= $zsj mg.st if score $zleft mg.st matches 1.. if score $zal mg.st < $zmx mg.st run function mg:zm/spawn',
                    'execute if score $zleft mg.st matches ..0 if score $zal mg.st matches 0 run function mg:zm/round_end'])
w('zm/spawn', ['scoreboard players set $zsc mg.st 0', 'scoreboard players remove $zleft mg.st 1',
               'execute as @e[type=minecraft:marker,tag=mg.zsp,tag=mg.zon,sort=random,limit=1] at @s run function mg:zx/spawn_pick'])
w('zm/spawn_one', ['# Un zombie (macro : $(hp) vie, $(sp) vitesse)',
                   '$summon minecraft:zombie ~ ~ ~ {Tags:["mg.zz","mg.gtg","mg.mob"],PersistenceRequired:1b,CanPickUpLoot:0b,IsBaby:0b,CanBreakDoors:0b,DeathLootTable:"minecraft:empty",Health:$(hp)f,attributes:[{id:"minecraft:max_health",base:$(hp)d},{id:"minecraft:follow_range",base:64d},{id:"minecraft:movement_speed",base:$(sp)d},{id:"minecraft:spawn_reinforcements",base:0d}]}',
                   'particle minecraft:large_smoke ~ ~1 ~ 0.3 0.5 0.3 0.02 10'])
w('zm/round_end', [f'# Manche terminée', f'execute if score $zr mg.st matches {ROUNDS}.. run return run function mg:zm/victory',
                   'scoreboard players set $zph mg.st 0', 'scoreboard players set $zb mg.st 200',
                   'tellraw @a[tag=mg.play] [{"text":"🧟 Manche ","color":"dark_green"},{"score":{"name":"$zr","objective":"mg.st"},"color":"green","bold":true},{"text":" terminée ! Prochaine dans 10 s.","color":"gray"}]',
                   'execute as @a[tag=mg.play,tag=mg.zdead] run function mg:zm/revive',
                   'execute as @a[tag=mg.play] at @s run playsound minecraft:block.bell.use master @s ~ ~ ~ 1 0.8'])
w('zm/die', ['# @s est tombé : spectateur jusqu\'à la fin de la manche, perd ses boissons', 'scoreboard players set @s mg.deaths 0',
             'tag @s add mg.zdead', 'gamemode spectator @s', f'tp @s {SX} 84 {SZ}',
             'execute if entity @s[tag=mg.zjug] run attribute @s minecraft:max_health base set 20', 'tag @s remove mg.zjug', 'tag @s remove mg.zsc',
             'tag @s remove mg.zdbl', 'tag @s remove mg.zst', 'tag @s remove mg.zmu',
             'execute if entity @s[tag=mg.zqr] run scoreboard players set @s mg.zrt 100', 'execute if entity @s[tag=mg.zqr] run tag @s add mg.zqrw',
             'execute if entity @s[tag=mg.zqr] run return run tag @s remove mg.zqr',
             'tellraw @a[tag=mg.play] [{"text":"☠ ","color":"red"},{"selector":"@s","color":"red"},{"text":" est tombé ! Il reviendra à la fin de la manche.","color":"gray"}]'])
w('zm/revive', ['# @s revient (pistolet + couteau)', 'tag @s remove mg.zdead', 'tag @s remove mg.zqrw', 'gamemode adventure @s',
                f'spreadplayers {SX} {SZ} 1 4 under 84 false @s', 'function mg:zm/kit', 'effect give @s minecraft:instant_health 1 4 true'])
w('zm/second', ['# Chaque seconde : zombies tombés hors de la carte ou perdus',
                'execute as @e[tag=mg.zz] at @s if entity @s[y=-64,dy=139] run function mg:zm/lost',
                'execute as @e[tag=mg.zz] at @s unless entity @a[tag=mg.play,tag=!mg.zdead,distance=..48] run function mg:zm/lost',
                'function mg:zx/second',
                'execute if score $zph mg.st matches 1 run title @a[tag=mg.play] actionbar [{"text":"🧟 Manche ","color":"dark_green"},{"score":{"name":"$zr","objective":"mg.st"},"color":"green","bold":true},{"text":" — restants : ","color":"gray"},{"score":{"name":"$zal","objective":"mg.st"},"color":"yellow"},{"text":" + ","color":"gray"},{"score":{"name":"$zleft","objective":"mg.st"},"color":"yellow"}]'])
w('zm/lost', ['# @s (zombie) perdu : réapparaît dans un enclos ouvert',
              'execute at @e[type=minecraft:marker,tag=mg.zsp,tag=mg.zon,sort=random,limit=1] run tp @s ~ ~ ~'])
w('zm/victory', [f'# {ROUNDS} manches !', 'kill @e[tag=mg.zz]', 'tag @a[tag=mg.play] add mg.win', 'scoreboard players add @a[tag=mg.play] mg.wins 1',
                 'scoreboard players set $state mg.st 3', 'scoreboard players set $timer mg.st 140',
                 'title @a[tag=!mg.surv] title {"text":"VICTOIRE !","color":"gold","bold":true}',
                 f'title @a[tag=!mg.surv] subtitle {{"text":"{ROUNDS} manches de zombies repoussées","color":"yellow"}}',
                 'tellraw @a {"text":"★ Le bunker a tenu — bravo aux survivants !","color":"gold"}',
                 'execute as @a[tag=!mg.surv] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1'])
w('zm/defeat', ['# Tout le monde est tombé', 'kill @e[tag=mg.zz]', 'scoreboard players set $state mg.st 3', 'scoreboard players set $timer mg.st 80',
                'title @a[tag=!mg.surv] title {"text":"GAME OVER","color":"dark_red","bold":true}',
                'title @a[tag=!mg.surv] subtitle [{"text":"Tombés à la manche ","color":"gray"},{"score":{"name":"$zr","objective":"mg.st"},"color":"red","bold":true}]',
                'tellraw @a [{"text":"☠ Les zombies ont envahi le bunker à la manche ","color":"gray"},{"score":{"name":"$zr","objective":"mg.st"},"color":"red","bold":true}]',
                'execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.wither.death master @s ~ ~ ~ 0.5 0.8'])

# achats
B = ['# @s = interaction cliquée', 'execute on target run tag @s add mg.zbuyer', 'data remove entity @s interaction',
     'execute unless entity @a[tag=mg.zbuyer,tag=mg.play,tag=!mg.zdead] run return run tag @a remove mg.zbuyer']
for d, (nm, cost, *_ ) in DOORS.items():
    B.append(f'execute if entity @s[tag=mg.zb{d}] run scoreboard players set $zc mg.st {cost}')
    B.append(f'execute if entity @s[tag=mg.zb{d}] if function mg:zm/pay run function mg:zm/door_{d}')
for tag, nm, cost, _, gn, _, _ in WALL:
    B.append(f'execute if entity @s[tag=mg.{tag}] run scoreboard players set $zc mg.st {cost}')
    B.append(f'execute if entity @s[tag=mg.{tag}] if function mg:zm/pay run function mg:zm/buy_gun {{n:{gn}}}')
PERK_FN = {'zb23': ('mg.zqr', 'qr'), 'zb24': ('mg.zdbl', 'dt'), 'zb25': ('mg.zst', 'st'), 'zb26': ('mg.zmu', 'mu')}
for tag, nm, txt, cost, *_ in PERKS:
    if tag in PERK_FN:
        ptag, fn = PERK_FN[tag]
        B += [f'execute if entity @s[tag=mg.{tag}] if entity @a[tag=mg.zbuyer,tag={ptag}] run return run function mg:zm/already',
              f'execute if entity @s[tag=mg.{tag}] run scoreboard players set $zc mg.st {cost}',
              f'execute if entity @s[tag=mg.{tag}] if function mg:zm/pay as @a[tag=mg.zbuyer] run function mg:zm/perk_{fn}']
    else:
        B += [f'execute if entity @s[tag=mg.{tag}] as @a[tag=mg.zbuyer] unless items entity @s weapon.mainhand *[custom_data~{{mg_gun:1b}}] run return run function mg:zm/pap_no',
              f'execute if entity @s[tag=mg.{tag}] as @a[tag=mg.zbuyer] if items entity @s weapon.mainhand *[custom_data~{{pap:1b}}] run return run function mg:zm/pap_no',
              f'execute if entity @s[tag=mg.{tag}] run scoreboard players set $zc mg.st {cost}',
              f'execute if entity @s[tag=mg.{tag}] if function mg:zm/pay as @a[tag=mg.zbuyer] run function mg:zm/pap']
B += ['execute if entity @s[tag=mg.zb20] run scoreboard players set $zc mg.st 950',
      'execute if entity @s[tag=mg.zb20] if score $zfs mg.st matches 1.. run scoreboard players set $zc mg.st 10',
      'execute if entity @s[tag=mg.zb20] if function mg:zm/pay run function mg:zm/box',
      'execute if entity @s[tag=mg.zb21] if entity @a[tag=mg.zbuyer,tag=mg.zjug] run return run function mg:zm/already',
      'execute if entity @s[tag=mg.zb21] run scoreboard players set $zc mg.st 2500',
      'execute if entity @s[tag=mg.zb21] if function mg:zm/pay as @a[tag=mg.zbuyer] run function mg:zm/jug',
      'execute if entity @s[tag=mg.zb22] if entity @a[tag=mg.zbuyer,tag=mg.zsc] run return run function mg:zm/already',
      'execute if entity @s[tag=mg.zb22] run scoreboard players set $zc mg.st 3000',
      'execute if entity @s[tag=mg.zb22] if function mg:zm/pay as @a[tag=mg.zbuyer] run function mg:zm/cola',
      'tag @a remove mg.zbuyer']
w('zm/buy', B)
w('zm/already', ['tellraw @a[tag=mg.zbuyer] {"text":"Tu as déjà cette boisson.","color":"gray"}', 'tag @a remove mg.zbuyer'])
w('zm/pay', ['# Paie $zc points (acheteur : mg.zbuyer) ; échoue si pas assez',
             'scoreboard players operation $zh mg.st = @a[tag=mg.zbuyer,limit=1] mg.zpt',
             'execute if score $zh mg.st < $zc mg.st run tellraw @a[tag=mg.zbuyer] [{"text":"Pas assez de points (","color":"red"},{"score":{"name":"$zc","objective":"mg.st"},"color":"yellow"},{"text":" requis).","color":"red"}]',
             'execute if score $zh mg.st < $zc mg.st as @a[tag=mg.zbuyer] at @s run playsound minecraft:block.note_block.bass player @s ~ ~ ~ 1 0.6',
             'execute if score $zh mg.st < $zc mg.st run return fail',
             'scoreboard players operation @a[tag=mg.zbuyer] mg.zpt -= $zc mg.st',
             'execute as @a[tag=mg.zbuyer] at @s run playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 1 0.8',
             'return 1'])
for d, (nm, cost, (x1, z1, x2, z2), _, room) in DOORS.items():
    w(f'zm/door_{d}', [f'# Porte {nm} ouverte', f'fill {x1} 81 {z1} {x2} 83 {z2} minecraft:air', f'kill @e[tag=mg.zd{d}]',
                       f'tag @e[tag=mg.zr_{room}] add mg.zon',
                       f'particle minecraft:poof {(x1 + x2) / 2 + .5} 82 {(z1 + z2) / 2 + .5} 1 1 1 0.05 40',
                       f'playsound minecraft:block.wooden_door.open master @a {(x1 + x2) / 2} 82 {(z1 + z2) / 2} 1 0.6',
                       'tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte ' + nm + '.","color":"gray"}]'])
w('zm/buy_gun', ['# Macro $(n) : arme achetée (déjà possédée → chargeur rempli)', '$scoreboard players set $zgn mg.st $(n)',
                 'execute as @a[tag=mg.zbuyer] run function mg:zm/give_gun'])
GG = ['# @s reçoit l\'arme $zgn : recharge si déjà possédée, sinon 2e emplacement (3e avec Mule Kick), sinon remplace l\'arme en main',
      'execute if score $zgn mg.st matches 11 run return run function mg:zx/monkey_give',
      'execute if score $zgn mg.st matches 12 run return run function mg:zx/bat_give',
      'execute if score $zgn mg.st matches 10 if items entity @s container.* *[custom_data~{zrpg:1b}] run return 0']
for n, g in G.GUNS.items():
    GG.append(f'execute if score $zgn mg.st matches {n} if items entity @s container.* *[custom_data~{{gun:{n}}}] run return run scoreboard players set @s mg.g{n} {g[4]}')
GG += ['execute unless items entity @s hotbar.2 * run return run function mg:zm/put {slot:"hotbar.2"}',
       'execute if entity @s[tag=mg.zmu] unless items entity @s hotbar.3 * run return run function mg:zm/put {slot:"hotbar.3"}',
       'execute if items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] run return run function mg:zm/put {slot:"weapon.mainhand"}',
       'execute if items entity @s weapon.mainhand *[custom_data~{zrpg:1b}] run return run function mg:zm/put {slot:"weapon.mainhand"}',
       'function mg:zm/put {slot:"hotbar.2"}']
w('zm/give_gun', GG)
w('zm/put', ['# Macro $(slot)'] + [f'$execute if score $zgn mg.st matches {n} run function mg:gun/put_{n} {{slot:"$(slot)"}}' for n in G.GUNS] +
  ['$execute if score $zgn mg.st matches 10 run function mg:zx/rpg_put {slot:"$(slot)"}'])
# boîte mystère (sur 20) : armes de guns.py, lance-roquettes, grenades singe, batte
BOX = [(1, 1, 6), (2, 3, 5), (4, 5, 2), (6, 7, 3), (8, 9, 4), (10, 11, 7), (12, 13, 8), (14, 15, 10), (16, 18, 11), (19, 20, 12)]
w('zm/box', ['# Boîte mystère : ' + ', '.join(f'{(G.GUNS[n][0] if n in G.GUNS else EXTRA[n][0])} {b - a + 1}' for a, b, n in BOX) + ' (sur 20)',
             'execute store result score $zx mg.st run random value 1..20'] +
  [f'execute if score $zx mg.st matches {a}..{b} run scoreboard players set $zgn mg.st {n}' for a, b, n in BOX] +
  ['execute as @a[tag=mg.zbuyer] run function mg:zm/give_gun',
             f'particle minecraft:witch {BOXP[0] + 0.5} 82.5 {BOXP[1] + 0.5} 0.4 0.4 0.4 0.1 30',
             f'playsound minecraft:block.chest.open master @a {BOXP[0] + 0.5} 82 {BOXP[1] + 0.5} 1 0.8',
             f'playsound minecraft:entity.player.levelup master @a {BOXP[0] + 0.5} 82 {BOXP[1] + 0.5} 0.6 1.6'] +
  [f'execute if score $zgn mg.st matches {n} run title @a[tag=mg.zbuyer] actionbar ' + js([{'text': '❓ Boîte mystère : ', 'color': 'light_purple'}, {'text': g[0], 'color': g[8], 'bold': True}])
   for n, g in G.GUNS.items()] +
  [f'execute if score $zgn mg.st matches {n} run title @a[tag=mg.zbuyer] actionbar ' + js([{'text': '❓ Boîte mystère : ', 'color': 'light_purple'}, {'text': nm, 'color': col, 'bold': True}])
   for n, (nm, col) in EXTRA.items()] +
  ['execute if score $zgn mg.st matches 6 run tellraw @a[tag=mg.play] [{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a tiré le RAY GUN !","color":"green","bold":true}]'])
w('zm/jug', ['# @s boit la Juggernog', 'tag @s add mg.zjug', 'attribute @s minecraft:max_health base set 40',
             'effect give @s minecraft:instant_health 1 9 true', 'title @s actionbar {"text":"❤ Juggernog : 20 cœurs !","color":"red","bold":true}',
             'playsound minecraft:entity.generic.drink player @s ~ ~ ~ 1 0.8'])
w('zm/cola', ['# @s boit la Speed Cola', 'tag @s add mg.zsc', 'title @s actionbar {"text":"⚡ Speed Cola : rechargement 2× plus rapide","color":"green","bold":true}',
              'playsound minecraft:entity.generic.drink player @s ~ ~ ~ 1 1.3'])
w('zm/perk_qr', ['# @s boit la Quick Revive', 'tag @s add mg.zqr', 'title @s actionbar {"text":"💙 Quick Revive : tu seras relevé 5 s après ta mort","color":"aqua","bold":true}',
                 'playsound minecraft:entity.generic.drink player @s ~ ~ ~ 1 1.1'])
w('zm/perk_dt', ['# @s boit la Double Tap (tag mg.zdbl : dégâts ×2, voir gun/hit ; cadence ×1,5)', 'tag @s add mg.zdbl',
                 'title @s actionbar {"text":"🍺 Double Tap : tir plus rapide, dégâts ×2","color":"gold","bold":true}',
                 'playsound minecraft:entity.generic.drink player @s ~ ~ ~ 1 0.9'])
w('zm/perk_st', ['# @s boit la Stamin-Up', 'tag @s add mg.zst', 'effect give @s minecraft:speed infinite 0 true',
                 'title @s actionbar {"text":"🏃 Stamin-Up : tu cours plus vite","color":"yellow","bold":true}',
                 'playsound minecraft:entity.generic.drink player @s ~ ~ ~ 1 1.2'])
w('zm/perk_mu', ['# @s boit la Mule Kick', 'tag @s add mg.zmu', 'title @s actionbar {"text":"🐴 Mule Kick : tu peux porter une 3e arme","color":"green","bold":true}',
                 'playsound minecraft:entity.generic.drink player @s ~ ~ ~ 1 0.7'])
w('zm/pap_no', ['tellraw @s {"text":"⚡ Prends en main une arme à feu pas encore améliorée.","color":"gray"}',
                'playsound minecraft:block.note_block.bass player @s ~ ~ ~ 1 0.6', 'tag @a remove mg.zbuyer'])
PAP = ['# @s : l\'arme en main passe au Pack-a-Punch (dégâts ×3, chargeur ×2, voir guns.py)',
       'item modify entity @s weapon.mainhand {function:"minecraft:set_custom_data",tag:{pap:1b}}',
       'item modify entity @s weapon.mainhand {function:"minecraft:set_components",components:{"minecraft:enchantment_glint_override":true}}']
for n, g in G.GUNS.items():
    PAP += [f'execute if items entity @s weapon.mainhand *[custom_data~{{gun:{n}}}] run item modify entity @s weapon.mainhand ' +
            js({'function': 'minecraft:set_name', 'entity': 'this', 'target': 'custom_name', 'name': {'text': f'⚡ {g[0]} (Pack-a-Punch)', 'color': 'light_purple', 'bold': True, 'italic': False}}),
            f'execute if items entity @s weapon.mainhand *[custom_data~{{gun:{n}}}] run scoreboard players set @s mg.g{n} {2 * g[4]}']
PAP += [f'particle minecraft:witch ~ ~1.2 ~ 0.4 0.6 0.4 0.1 40', 'playsound minecraft:block.anvil.use player @a ~ ~ ~ 1 0.6',
        'playsound minecraft:entity.player.levelup player @s ~ ~ ~ 1 0.8',
        'title @s actionbar {"text":"⚡ Pack-a-Punch : arme améliorée (dégâts ×3, chargeur ×2)","color":"light_purple","bold":true}']
w('zm/pap', PAP)

# ------------------------------------------------------------------ INFECTION
LIMIT = 3600
w('inf/prepare', ['# 🧪 Infection — préparation', 'function mg:zm/build', 'function mg:zm/kill_all', 'function mg:zm/entities', 'function mg:zm/open_all',
                  f'scoreboard players set $px mg.st {SX if LY else 11}', 'scoreboard players set $py mg.st 84', f'scoreboard players set $pz mg.st {SZ if LY else Z - 11}',
                  'clear @a[tag=mg.play]', 'gamemode adventure @a[tag=mg.play]', 'team join mg_blue @a[tag=mg.play]',
                  inf_spread('@a[tag=mg.play]'), 'execute as @a[tag=mg.play] at @s run spawnpoint @s ~ ~ ~',
                  'tag @a remove mg.zhit', 'advancement revoke @a only mg:infhit'])
w('inf/kit', ['# @s : survivant (couteau, pistolet, une arme au hasard)', 'clear @s', 'function mg:gun/reset',
              'item replace entity @s hotbar.0 with minecraft:iron_sword[unbreakable={},custom_name=[{"text":"🔪 Couteau","color":"gray","italic":false}]]',
              G.give(1, 'hotbar.1'), 'execute store result score $zx mg.st run random value 2..4',
              'execute if score $zx mg.st matches 2 run ' + G.give(2, 'hotbar.2'), 'execute if score $zx mg.st matches 3 run ' + G.give(3, 'hotbar.2'),
              'execute if score $zx mg.st matches 4 run ' + G.give(4, 'hotbar.2'),
              'item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=3361970,unbreakable={}]',
              'item replace entity @s hotbar.8 with minecraft:cooked_beef 8'])
w('inf/go', ['# Départ : 1 zombie pour 5 joueurs (au moins 1)', f'scoreboard players set $ift mg.st 0', 'scoreboard players set @a mg.deaths 0',
             'execute as @a[tag=mg.play] run function mg:inf/kit',
             'execute store result score $inn mg.st if entity @a[tag=mg.play]', 'scoreboard players set #5 mg.st 5',
             'scoreboard players operation $inn mg.st /= #5 mg.st', 'execute if score $inn mg.st matches ..0 run scoreboard players set $inn mg.st 1',
             'execute if score $n0 mg.st matches 2.. unless score $infm mg.st matches 1 run function mg:inf/pick',
             # mode joueurs contre mobs : tout le monde survivant, les zombies sont des mobs
             'execute if score $infm mg.st matches 1 run function mg:inf/mstart',
             'tellraw @a[tag=mg.play] ' + js([{'text': '🧪 INFECTION : ', 'color': 'dark_green', 'bold': True},
                                              {'text': 'les zombies infectent les survivants qu\'ils tuent. Survivants : tenez 3 minutes (clic droit = tirer, accroupi = recharger) ! Zombies : contaminez tout le monde.', 'color': 'gray'}]),
             # seul : entraînement, pas de zombie ni de victoire
             'execute unless score $n0 mg.st matches 2.. unless score $infm mg.st matches 1 run tellraw @a[tag=mg.play] ' + js([{'text': "🧪 Mode entraînement (seul) : pas de zombie, essaie les armes (clic droit = tirer, accroupi = recharger). Pas de victoire ; il faut au moins 2 joueurs pour une vraie partie.", 'color': 'yellow'}])])
w('inf/pick', ['execute as @a[tag=mg.play,tag=!mg.inf,sort=random,limit=1] run function mg:inf/make_zombie',
               'scoreboard players remove $inn mg.st 1', 'execute if score $inn mg.st matches 1.. run function mg:inf/pick'])
w('inf/make_zombie', ['# @s devient zombie', 'tag @s remove mg.zhit', 'tag @s add mg.inf', 'tag @s add mg.gtg', 'team join mg_green @s', 'clear @s', 'function mg:gun/reset',
                      'scoreboard players set @s mg.deaths 0',
                      'item replace entity @s armor.head with minecraft:zombie_head',
                      'item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=4227072,unbreakable={}]',
                      'item replace entity @s armor.legs with minecraft:leather_leggings[dyed_color=2116640,unbreakable={}]',
                      'item replace entity @s armor.feet with minecraft:leather_boots[dyed_color=2116640,unbreakable={}]',
                      'effect give @s minecraft:speed infinite 0 true', 'effect give @s minecraft:strength infinite 1 true',
                      'effect give @s minecraft:saturation infinite 0 true', 'function mg:inf/zspawn',
                      'title @s title {"text":"🧟 Tu es INFECTÉ","color":"dark_green","bold":true}',
                      'title @s subtitle {"text":"tue les survivants pour les contaminer","color":"gray"}',
                      'tellraw @a[tag=mg.play] [{"text":"🧪 ","color":"dark_green"},{"selector":"@s","color":"green"},{"text":" a été infecté !","color":"gray"}]',
                      'execute as @a[tag=mg.play] at @s run playsound minecraft:entity.zombie_villager.converted master @s ~ ~ ~ 0.8 1'])
w('inf/zspawn', ['# @s (zombie) : dans un enclos au hasard, 2 s de protection',
                 'execute at @e[type=minecraft:marker,tag=mg.zsp,sort=random,limit=1] run tp @s ~ ~ ~',
                 'execute at @s run spawnpoint @s ~ ~ ~', 'effect give @s minecraft:resistance 2 4 true', 'effect give @s minecraft:instant_health 1 4 true'])
w('inf/tick', ['# 🧪 Infection — tick', 'scoreboard players add $ift mg.st 1',
               'execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]',
               'execute as @a[tag=mg.play,tag=!mg.inf,scores={mg.t=..74}] run scoreboard players set @s mg.deaths 1',
               'execute if score $n0 mg.st matches 2.. as @a[tag=mg.play,tag=!mg.inf,scores={mg.deaths=1..}] run function mg:inf/make_zombie',
               # seul : pas de zombie, un survivant tombé ou tué revient au bunker
               # joueurs contre mobs : touché par un zombie (mob ou joueur) ou mort → infecté, même seul ; vagues de mobs
               'execute if score $infm mg.st matches 1 as @a[tag=mg.play,tag=!mg.inf,tag=mg.zhit] run function mg:inf/make_zombie',
               'execute if score $infm mg.st matches 1 unless score $n0 mg.st matches 2.. as @a[tag=mg.play,tag=!mg.inf,scores={mg.deaths=1..}] run function mg:inf/make_zombie',
               'execute if score $infm mg.st matches 1 run function mg:inf/mtick',
               'execute unless score $n0 mg.st matches 2.. unless score $infm mg.st matches 1 as @e[type=minecraft:player,tag=mg.play,tag=!mg.inf,scores={mg.deaths=1..}] run function mg:inf/srespawn',
               'execute as @a[tag=mg.play,tag=mg.inf,scores={mg.t=..74}] run scoreboard players set @s mg.deaths 1',
               'execute as @a[tag=mg.play,tag=mg.inf,scores={mg.deaths=1..}] run function mg:inf/zdie',
               'execute store result score $ins mg.st if entity @a[tag=mg.play,tag=!mg.inf]',
               'scoreboard players operation $inq mg.st = $ift mg.st', 'scoreboard players set #20 mg.st 20', 'scoreboard players operation $inq mg.st %= #20 mg.st',
               'execute if score $inq mg.st matches 0 run function mg:inf/second',
               'execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $ins mg.st matches 0 run return run function mg:inf/zombies_win',
               'execute if score $state mg.st matches 2 if score $infm mg.st matches 1 if score $ins mg.st matches 0 run return run function mg:inf/zombies_win',
               f'execute if score $state mg.st matches 2 if score $ift mg.st matches {LIMIT}.. run function mg:inf/survivors_win'])
w('inf/srespawn', ['# @s (entraînement, seul) : mort ou chute → retour au bunker, kit rendu', 'scoreboard players set @s mg.deaths 0',
                   inf_spread('@s'), 'execute at @s run spawnpoint @s ~ ~ ~', 'function mg:inf/kit',
                   'effect give @s minecraft:resistance 2 4 true', 'effect give @s minecraft:instant_health 1 4 true',
                   'tellraw @s {"text":"🧪 Entraînement : retour au bunker.","color":"yellow"}'])
w('inf/zdie', ['# @s (zombie) tué : réapparaît', 'scoreboard players set @s mg.deaths 0', 'function mg:inf/zspawn',
               'effect give @s minecraft:speed infinite 0 true', 'effect give @s minecraft:strength infinite 1 true',
               'effect give @s minecraft:saturation infinite 0 true'])
w('inf/second', ['scoreboard players set $inl mg.st ' + str(LIMIT // 20), 'scoreboard players operation $ins2 mg.st = $ift mg.st',
                 'scoreboard players operation $ins2 mg.st /= #20 mg.st', 'scoreboard players operation $inl mg.st -= $ins2 mg.st',
                 'title @a[tag=mg.play,tag=mg.inf] actionbar [{"text":"🧟 Survivants : ","color":"dark_green"},{"score":{"name":"$ins","objective":"mg.st"},"color":"yellow","bold":true},{"text":" — ","color":"gray"},{"score":{"name":"$inl","objective":"mg.st"},"color":"yellow"},{"text":" s","color":"gray"}]',
                 # seul : chrono restant
                 'execute if score $infm mg.st matches 1 run title @a[tag=mg.play,tag=!mg.inf] actionbar [{"text":"🧟 Zombies : ","color":"dark_green"},{"score":{"name":"$imz","objective":"mg.st"},"color":"red","bold":true},{"text":" — survivants : ","color":"gray"},{"score":{"name":"$ins","objective":"mg.st"},"color":"yellow"},{"text":" — ","color":"gray"},{"score":{"name":"$inl","objective":"mg.st"},"color":"yellow"},{"text":" s","color":"gray"}]',
                 'execute unless score $n0 mg.st matches 2.. unless score $infm mg.st matches 1 run title @a[tag=mg.play] actionbar [{"text":"🧪 Entraînement : ","color":"yellow"},{"score":{"name":"$inl","objective":"mg.st"},"color":"yellow","bold":true},{"text":" s","color":"gray"}]',
                 'execute if score $inl mg.st matches 60 run tellraw @a[tag=mg.play] {"text":"🧪 Plus qu\'une minute !","color":"gold"}',
                 'execute if score $inl mg.st matches 60 as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 0.8'])
# --- mode joueurs contre mobs ($infm = 1, ids 217..219)
w('inf/mstart', ['# Joueurs contre mobs : réglages des zombies et première vague',
                 'data modify storage mg:zm hp set value 24', 'data modify storage mg:zm sp set value 0.25d',
                 'scoreboard players set $imc mg.st 0', 'scoreboard players set $imz mg.st 0',
                 'execute store result score $imw mg.st if entity @a[tag=mg.play]', 'scoreboard players add $imw mg.st 2',
                 'function mg:inf/mwave',
                 'tellraw @a[tag=mg.play] ' + js([{'text': '🧟 JOUEURS CONTRE MOBS : ', 'color': 'red', 'bold': True},
                                                  {'text': "des zombies envahissent le bunker. Un seul coup d'un zombie et tu es infecté : tu chasses alors les survivants (ton coup les infecte aussi). Tenez 3 minutes !", 'color': 'gray'}])])
w('inf/mwave', ['execute as @e[type=minecraft:marker,tag=mg.zsp,sort=random,limit=1] at @s run function mg:zm/spawn_one with storage mg:zm',
                'scoreboard players remove $imw mg.st 1', 'execute if score $imw mg.st matches 1.. run function mg:inf/mwave'])
w('inf/mtick', ['# Toutes les 2 s : un zombie de plus tant qu\'on est sous le plafond (6 + 3 par survivant, 30 max) ; plus rapide après 90 s',
                'scoreboard players add $imc mg.st 1', 'execute store result score $imz mg.st if entity @e[type=minecraft:zombie,tag=mg.zz]',
                'scoreboard players operation $imx mg.st = $ins mg.st', 'scoreboard players operation $imx mg.st *= #3 mg.st',
                'scoreboard players add $imx mg.st 6', 'execute if score $imx mg.st matches 31.. run scoreboard players set $imx mg.st 30',
                'execute if score $ift mg.st matches 1800.. if score $imc mg.st matches 20.. if score $imz mg.st < $imx mg.st run function mg:inf/mspawn',
                'execute if score $imc mg.st matches 40.. if score $imz mg.st < $imx mg.st run function mg:inf/mspawn',
                'execute if score $imc mg.st matches 40.. run scoreboard players set $imc mg.st 0'])
w('inf/mspawn', ['scoreboard players set $imc mg.st 0',
                 'execute as @e[type=minecraft:marker,tag=mg.zsp,sort=random,limit=1] at @s unless entity @a[tag=mg.play,tag=!mg.inf,distance=..5] run function mg:zm/spawn_one with storage mg:zm'])
w('inf/survivors_win', ['# Temps écoulé : les survivants gagnent',
                        'execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] ' + js([{'text': "🧪 Fin de l'entraînement.", 'color': 'yellow'}]),
                        'execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw',
                        'tellraw @a {"text":"🧪 Les survivants ont tenu 3 minutes !","color":"aqua","bold":true}',
                        'function mg:core/win_blue'])
w('inf/zombies_win', ['# Plus de survivants', 'tellraw @a {"text":"🧟 Tout le monde est infecté !","color":"dark_green","bold":true}',
                      'execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw',
                      'function mg:core/win_green'])

# ------------------------------------------------------------------ ZOMBIES : partie commune à toutes les cartes (zx/)
w('zx/reset', ['# Bonus, grenades singe, roquettes : remis à zéro', 'scoreboard players set $zik mg.st 0', 'scoreboard players set $zdp mg.st 0',
               'scoreboard players set $zfs mg.st 0', 'scoreboard players set $zdog mg.st 0', 'scoreboard players reset * mg.zrp',
               'kill @e[tag=mg.zpu]', 'kill @e[tag=mg.zmk]', 'kill @e[tag=mg.zmt]', 'kill @e[tag=mg.zrk]'])
TIMERS = [('zik', '💀 Fin de la mort instantanée'), ('zdp', '✖2 Fin des points doubles'), ('zfs', '🔥 Fin de la vente de feu')]
w('zx/tick', ['# Zombies, chaque tick : bonus en cours, bonus au sol, grenades singe, roquettes, réparation des fenêtres'] +
  [l for t, msg in TIMERS for l in (f'execute if score ${t} mg.st matches 1 run tellraw @a[tag=mg.play] ' + js({'text': msg, 'color': 'gray'}),
                                    f'execute if score ${t} mg.st matches 1.. run scoreboard players remove ${t} mg.st 1')] +
  ['execute as @e[type=minecraft:item_display,tag=mg.zpu] at @s run function mg:zx/pu_one',
   'execute as @e[type=minecraft:snowball,tag=!mg.zms] if data entity @s Item.components."minecraft:custom_data".monkey at @s run function mg:zx/mk_new',
   'execute as @e[type=minecraft:marker,tag=mg.zmt] run function mg:zx/mk_follow',
   'execute as @e[type=minecraft:item_display,tag=mg.zmk] at @s run function mg:zx/mk_tick',
   'execute as @e[type=minecraft:item_display,tag=mg.zrk] at @s run function mg:zx/rk_tick',
   'scoreboard players add $zxt mg.st 1', 'execute if score $zxt mg.st matches 10.. run function mg:zx/win_fix_all'])
w('zx/second', ['# Chaque seconde : les zombies dans l\'enclos d\'une fenêtre arrachent une planche ; zombie coincé = renvoyé à une apparition',
                'execute if score $zph mg.st matches 1 as @e[type=minecraft:marker,tag=mg.zwin,scores={mg.zws=1..}] at @s if entity @e[tag=mg.zz,distance=..3.6] run function mg:zx/win_hit',
                'execute if score $zph mg.st matches 1 as @e[tag=mg.zz] at @s run function mg:zx/stuck'])
w('zx/stuck', ['# @s (mob) : immobile 12 s loin des joueurs et des fenêtres → retiré, il réapparaîtra (compté dans les restants)',
               'execute store result score $sx mg.st run data get entity @s Pos[0]', 'execute store result score $sz mg.st run data get entity @s Pos[2]',
               'scoreboard players operation $sx mg.st -= @s mg.zqx', 'scoreboard players operation $sz mg.st -= @s mg.zqz',
               'execute store result score @s mg.zqx run data get entity @s Pos[0]', 'execute store result score @s mg.zqz run data get entity @s Pos[2]',
               'scoreboard players add @s mg.zsk 1',
               'execute unless score $sx mg.st matches 0 run scoreboard players set @s mg.zsk 0',
               'execute unless score $sz mg.st matches 0 run scoreboard players set @s mg.zsk 0',
               'execute if entity @a[tag=mg.play,tag=!mg.zdead,distance=..3] run scoreboard players set @s mg.zsk 0',
               'execute if entity @e[type=minecraft:marker,tag=mg.zwin,scores={mg.zws=1..},distance=..3.6] run scoreboard players set @s mg.zsk 0',
               'execute if score @s mg.zsk matches 12.. run function mg:zx/unstick'])
w('zx/unstick', ['scoreboard players add $zleft mg.st 1', 'particle minecraft:large_smoke ~ ~1 ~ 0.3 0.5 0.3 0.02 10', 'tp @s ~ -200 ~', 'kill @s'])

# --- mobs : variantes tirées au sort (stats de la manche dans storage mg:zm, voir zm/round_start)
MOB = '{{Tags:["mg.zz","mg.gtg","mg.mob"],PersistenceRequired:1b,CanPickUpLoot:0b,DeathLootTable:"minecraft:empty",Health:$({h})f,{x}attributes:[{{id:"minecraft:max_health",base:$({h})d}},{{id:"minecraft:follow_range",base:64d}},{{id:"minecraft:movement_speed",base:$({s})d}}{a}]}}'
RF = ',{id:"minecraft:spawn_reinforcements",base:0d}'
w('zx/spawn_pick', ['# Un mob de la manche à cet enclos : zombie, zombie villageois, rapide (manche 3+), rampant (4+), brute (6+), chien (manche 5)',
                    'execute if score $zdog mg.st matches 1 run return run function mg:zx/spawn_dog with storage mg:zm',
                    'execute store result score $zx2 mg.st run random value 1..100',
                    'execute if score $zx2 mg.st matches 1..20 run return run function mg:zx/spawn_villager with storage mg:zm',
                    'execute if score $zr mg.st matches 3.. if score $zx2 mg.st matches 21..40 run return run function mg:zx/spawn_runner with storage mg:zm',
                    'execute if score $zr mg.st matches 4.. if score $zx2 mg.st matches 41..55 run return run function mg:zx/spawn_crawler with storage mg:zm',
                    'execute if score $zr mg.st matches 6.. if score $zx2 mg.st matches 56..65 run return run function mg:zx/spawn_brute with storage mg:zm',
                    'execute if score $zr mg.st matches 8.. if score $zx2 mg.st matches 66..72 run return run function mg:zx/spawn_brute with storage mg:zm',
                    'function mg:zm/spawn_one with storage mg:zm'])
w('zx/spawn_villager', ['$summon minecraft:zombie_villager ~ ~ ~ ' + MOB.format(h='hp', s='sp', x='IsBaby:0b,', a=RF), 'particle minecraft:large_smoke ~ ~1 ~ 0.3 0.5 0.3 0.02 10'])
w('zx/spawn_runner', ['# Rapide (husk) : moins de vie, plus vite', '$summon minecraft:husk ~ ~ ~ ' + MOB.format(h='hpf', s='spf', x='IsBaby:0b,', a=RF),
                      'particle minecraft:large_smoke ~ ~1 ~ 0.3 0.5 0.3 0.02 10'])
w('zx/spawn_crawler', ['# Rampant (araignée venimeuse) : petit, rapide', '$summon minecraft:cave_spider ~ ~ ~ ' + MOB.format(h='hpf', s='spf', x='', a=''),
                       'particle minecraft:large_smoke ~ ~0.5 ~ 0.3 0.3 0.3 0.02 10'])
w('zx/spawn_brute', ['# Brute (noyé en armure) : 3× plus de vie, frappe fort, plus lent',
                     '$summon minecraft:drowned ~ ~ ~ ' + MOB.format(h='hpb', s='spb', x='IsBaby:0b,equipment:{head:{id:"minecraft:iron_helmet",count:1},chest:{id:"minecraft:iron_chestplate",count:1}},drop_chances:{head:0f,chest:0f},',
                                                                     a=RF + ',{id:"minecraft:attack_damage",base:7d}'),
                     'particle minecraft:large_smoke ~ ~1 ~ 0.4 0.6 0.4 0.02 16'])
w('zx/spawn_dog', ['# Chien de l\'enfer (petit zoglin) : peu de vie, très rapide', '$summon minecraft:zoglin ~ ~ ~ ' + MOB.format(h='hpd', s='spd', x='IsBaby:1b,', a=',{id:"minecraft:attack_damage",base:4d}'),
                   'particle minecraft:flame ~ ~0.5 ~ 0.3 0.3 0.3 0.05 20', 'playsound minecraft:entity.wolf.growl hostile @a ~ ~ ~ 1 0.6'])

# --- fenêtres barricadées (marqueur mg.zwin dans l'ouverture, mg.zws = planches 0..6)
w('zx/win_set', ['# Blocs de la fenêtre (@s, à sa position) selon ses planches',
                 'execute if score @s mg.zws matches 5.. run fill ~ ~ ~ ~ ~1 ~ minecraft:spruce_planks',
                 'execute if score @s mg.zws matches 3..4 run setblock ~ ~ ~ minecraft:spruce_planks',
                 'execute if score @s mg.zws matches 3..4 run setblock ~ ~1 ~ minecraft:spruce_fence',
                 'execute if score @s mg.zws matches 1..2 run setblock ~ ~ ~ minecraft:spruce_fence',
                 'execute if score @s mg.zws matches 1..2 run setblock ~ ~1 ~ minecraft:air',
                 'execute if score @s mg.zws matches ..0 run fill ~ ~ ~ ~ ~1 ~ minecraft:air'])
w('zx/win_hit', ['# Un zombie arrache une planche', 'scoreboard players remove @s mg.zws 1', 'function mg:zx/win_set',
                 'particle minecraft:block{block_state:"minecraft:spruce_planks"} ~ ~1 ~ 0.3 0.5 0.3 0 12',
                 'playsound minecraft:entity.zombie.attack_wooden_door hostile @a ~ ~ ~ 0.8 1'])
w('zx/win_fix_all', ['# Toutes les 0,5 s : un joueur accroupi devant une fenêtre abîmée recloue une planche', 'scoreboard players set $zxt mg.st 0',
                     'execute as @e[type=minecraft:marker,tag=mg.zwin,scores={mg.zws=..5}] at @s as @a[tag=mg.play,tag=!mg.zdead,distance=..2.6,sort=nearest,limit=1] if predicate mg:sneak run function mg:zx/win_fix'])
w('zx/win_fix', ['# @s recloue une planche (à la position de la fenêtre) : +10 pts, 20 fois par manche au plus',
                 'execute as @e[type=minecraft:marker,tag=mg.zwin,sort=nearest,limit=1] run function mg:zx/win_up',
                 'execute if score @s mg.zrp matches ..19 run scoreboard players add @s mg.zpt 10',
                 'execute if score @s mg.zrp matches ..19 if score $zdp mg.st matches 1.. run scoreboard players add @s mg.zpt 10',
                 'scoreboard players add @s mg.zrp 1',
                 'playsound minecraft:block.wood.place player @a ~ ~ ~ 1 0.8', 'playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 0.4 1.6'])
w('zx/win_up', ['scoreboard players add @s mg.zws 1', 'function mg:zx/win_set'])

# --- bonus lâchés par les zombies (4 %, 2 au sol au plus) : 1 mort instantanée, 2 Kaboom, 3 points doubles, 4 charpentier, 5 vente de feu
PU = {1: ('💀 MORT INSTANTANÉE', 'un coup suffit pendant 30 s', 'minecraft:skeleton_skull', 'white'),
      2: ('💥 KABOOM', 'tous les zombies explosent, +400 pts', 'minecraft:tnt', 'red'),
      3: ('✖2 POINTS DOUBLES', 'pendant 30 s', 'minecraft:experience_bottle', 'yellow'),
      4: ('🪚 CHARPENTIER', 'toutes les fenêtres réparées, +200 pts', 'minecraft:iron_axe', 'gold'),
      5: ('🔥 VENTE DE FEU', 'boîte mystère à 10 pts pendant 30 s', 'minecraft:blaze_powder', 'light_purple')}
w('zx/drop_roll', ['# @s : zombie tué par une arme (à sa position)',
                   'execute store result score $zx2 mg.st if entity @e[type=minecraft:item_display,tag=mg.zpu]',
                   'execute if score $zx2 mg.st matches 2.. run return 0',
                   'execute store result score $zx2 mg.st run random value 1..100',
                   'execute if score $zx2 mg.st matches ..4 run function mg:zx/drop'])
w('zx/drop', ['execute store result score $zx2 mg.st run random value 1..5'] +
  [f'execute if score $zx2 mg.st matches {n} run summon minecraft:item_display ~ ~1 ~ {{Tags:["mg.zent","mg.zpu","mg.zpun"],Glowing:1b,glow_color_override:5635925,brightness:{{sky:15,block:15}},item:{{id:"{it}",count:1}},transformation:{{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}}}'
   for n, (_, _, it, _) in PU.items()] +
  ['scoreboard players operation @e[tag=mg.zpun] mg.zpy = $zx2 mg.st', 'scoreboard players set @e[tag=mg.zpun] mg.zpl 0', 'tag @e[tag=mg.zpun] remove mg.zpun',
   'playsound minecraft:block.amethyst_block.chime master @a ~ ~ ~ 1.5 1.2'])
w('zx/pu_one', ['# @s : bonus au sol (30 s), tourne, pris par le premier joueur qui marche dessus', 'scoreboard players add @s mg.zpl 1',
                'tp @s ~ ~ ~ ~8 ~', 'particle minecraft:end_rod ~ ~ ~ 0.2 0.2 0.2 0.01 1',
                'execute if score @s mg.zpl matches 600.. run return run kill @s',
                'execute if entity @a[tag=mg.play,tag=!mg.zdead,distance=..1.8] run function mg:zx/pu_take'])
PT = ['# @s (bonus) pris par le joueur le plus proche (mg.zpk)', 'tag @a[tag=mg.play,tag=!mg.zdead,distance=..1.8,sort=nearest,limit=1] add mg.zpk']
for n, (nm, sub, _, col) in PU.items():
    PT += [f'execute if score @s mg.zpy matches {n} run title @a[tag=mg.play] title ' + js({'text': nm, 'color': col, 'bold': True}),
           f'execute if score @s mg.zpy matches {n} run title @a[tag=mg.play] subtitle ' + js({'text': sub, 'color': 'gray'}),
           f'execute if score @s mg.zpy matches {n} run tellraw @a[tag=mg.play] ' + js([{'text': '🎁 ', 'color': col}, {'selector': '@a[tag=mg.zpk]', 'color': 'yellow'}, {'text': ' a pris : ', 'color': 'gray'}, {'text': nm, 'color': col, 'bold': True}])]
PT += ['execute if score @s mg.zpy matches 1 run function mg:zx/pu_ik', 'execute if score @s mg.zpy matches 2 run function mg:zx/pu_kaboom',
       'execute if score @s mg.zpy matches 3 run scoreboard players set $zdp mg.st 600', 'execute if score @s mg.zpy matches 4 run function mg:zx/pu_carp',
       'execute if score @s mg.zpy matches 5 run scoreboard players set $zfs mg.st 600',
       'execute as @a[tag=mg.play] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 0.6 1.4',
       'tag @a remove mg.zpk', 'kill @s']
w('zx/pu_take', PT)
w('zx/pu_ik', ['scoreboard players set $zik mg.st 600', 'effect give @a[tag=mg.play,tag=!mg.zdead] minecraft:strength 30 100 true'])
w('zx/pu_kaboom', ['execute as @e[tag=mg.zz] at @s run particle minecraft:explosion ~ ~1 ~ 0.3 0.3 0.3 0 2 force', 'kill @e[tag=mg.zz]',
                   'scoreboard players add @a[tag=mg.play] mg.zpt 400', 'effect give @a[tag=mg.play] minecraft:blindness 1 0 true',
                   'execute as @a[tag=mg.play] at @s run playsound minecraft:entity.generic.explode master @s ~ ~ ~ 1 0.6'])
w('zx/pu_carp', ['scoreboard players set @e[type=minecraft:marker,tag=mg.zwin] mg.zws 6',
                 'execute as @e[type=minecraft:marker,tag=mg.zwin] at @s run function mg:zx/win_set',
                 'scoreboard players add @a[tag=mg.play] mg.zpt 200',
                 'execute as @a[tag=mg.play] at @s run playsound minecraft:block.anvil.use master @s ~ ~ ~ 0.6 1.2'])

# --- grenade singe : boule de neige marquée, suivie par un marqueur ; à l'arrêt, attire les zombies 6 s puis explose (rayon 6)
MONKEY = ('minecraft:snowball[custom_data={monkey:1b},custom_name=' + js({'text': '🐵 Grenade singe', 'color': 'gold', 'bold': True, 'italic': False}) +
          ',lore=[' + js({'text': 'Lance-la : elle attire les zombies puis explose', 'color': 'gray', 'italic': False}) + ']]')
w('zx/monkey_give', ['# @s : 3 grenades singe', f'give @s {MONKEY} 3'])
w('zx/mk_new', ['# @s : grenade singe qui vient d\'être lancée (le lanceur est le joueur le plus proche)', 'tag @s add mg.zms',
                'scoreboard players add $zmid mg.st 1', 'scoreboard players operation @s mg.zmi = $zmid mg.st',
                'summon minecraft:marker ~ ~ ~ {Tags:["mg.zent","mg.zmt","mg.zmn"]}',
                'scoreboard players operation @e[type=minecraft:marker,tag=mg.zmn] mg.zmi = $zmid mg.st',
                'scoreboard players operation @e[type=minecraft:marker,tag=mg.zmn] mg.zmo = @p[tag=mg.play] mg.zid',
                'tag @e[tag=mg.zmn] remove mg.zmn'])
w('zx/mk_follow', ['# @s (marqueur) suit sa grenade ; grenade disparue = elle s\'est posée ici', 'scoreboard players operation $zq mg.st = @s mg.zmi',
                   'scoreboard players set $zf mg.st 0', 'tag @s add mg.zme',
                   'execute as @e[type=minecraft:snowball,tag=mg.zms] if score @s mg.zmi = $zq mg.st at @s run function mg:zx/mk_pos',
                   'tag @s remove mg.zme', 'execute if score $zf mg.st matches 0 at @s run function mg:zx/mk_land'])
w('zx/mk_pos', ['tp @e[type=minecraft:marker,tag=mg.zme,limit=1] ~ ~ ~', 'scoreboard players set $zf mg.st 1'])
w('zx/mk_land', ['summon minecraft:item_display ~ ~0.25 ~ {Tags:["mg.zent","mg.zmk","mg.zmkn"],Glowing:1b,glow_color_override:16755200,item:{id:"minecraft:note_block",count:1},'
                 'transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.45f,0.45f,0.45f]}}',
                 'scoreboard players operation @e[tag=mg.zmkn] mg.zmo = @s mg.zmo', 'scoreboard players set @e[tag=mg.zmkn] mg.zmc 0',
                 'tag @e[tag=mg.zmkn] remove mg.zmkn', 'kill @s'])
w('zx/mk_tick', ['# @s : grenade singe posée (6 s) : les zombies à 24 blocs marchent vers elle (sans traverser les murs)', 'scoreboard players add @s mg.zmc 1',
                 'tp @s ~ ~ ~ ~18 ~',
                 'execute as @e[tag=mg.zz,distance=..24] at @s facing entity @e[type=minecraft:item_display,tag=mg.zmk,sort=nearest,limit=1] feet rotated ~ 0 positioned ^ ^ ^0.2 '
                 'if block ~ ~0.1 ~ #mg:ray_pass if block ~ ~1.1 ~ #mg:ray_pass unless entity @e[type=minecraft:item_display,tag=mg.zmk,distance=..1.2] run tp @s ~ ~ ~ ~ ~',
                 'scoreboard players operation $zq mg.st = @s mg.zmc', 'scoreboard players set #5 mg.st 5', 'scoreboard players operation $zq mg.st %= #5 mg.st',
                 'execute if score $zq mg.st matches 0 run particle minecraft:note ~ ~0.6 ~ 0.3 0.3 0.3 1 2',
                 'execute if score $zq mg.st matches 0 run playsound minecraft:block.note_block.bell master @a ~ ~ ~ 1.5 1.8',
                 'execute if score @s mg.zmc matches 120.. run function mg:zx/mk_boom'])
BOOM = ['scoreboard players operation $zo mg.st = @s mg.zmo', 'execute as @a[tag=mg.play] if score @s mg.zid = $zo mg.st run tag @s add mg.gsh']
w('zx/mk_boom', ['# La grenade singe explose : zombies à 6 blocs tués (crédités au lanceur)'] + BOOM +
  ['scoreboard players set $gdm mg.st 1000000', 'execute as @e[tag=mg.zz,distance=..6] run function mg:gun/hit_mob', 'tag @a remove mg.gsh',
   'particle minecraft:explosion_emitter ~ ~ ~ 0 0 0 0 1 force', 'particle minecraft:flame ~ ~ ~ 2 1 2 0.1 40 force',
   'playsound minecraft:entity.generic.explode master @a ~ ~ ~ 3 0.9', 'kill @s'])

# --- lance-roquettes (munitions illimitées, une roquette toutes les 1,5 s, sans casser le décor)
RPGB = ('minecraft:warped_fungus_on_a_stick[custom_data={zrpg:1b},unbreakable={},custom_name=' + js({'text': '🚀 Lance-roquettes', 'color': 'red', 'bold': True, 'italic': False}) +
        ',lore=[' + js({'text': 'Clic droit : tirer une roquette', 'color': 'gray', 'italic': False}) + ']')
w('zx/rpg_put', ['# Macro $(slot) : lance-roquettes', f'$execute if score $rp mg.st matches 1 run item replace entity @s $(slot) with {RPGB},item_model="mg:gun_rpg"]',
                 f'$execute unless score $rp mg.st matches 1 run item replace entity @s $(slot) with {RPGB},item_model="minecraft:crossbow"]'])
w('zx/rpg_fire', ['# @s tire une roquette', 'scoreboard players reset @s mg.qs', 'execute if score @s mg.gcd matches 1.. run return 0',
                  'scoreboard players set @s mg.gcd 30',
                  'execute anchored eyes positioned ^-0.2 ^-0.1 ^1 run summon minecraft:item_display ~ ~ ~ {Tags:["mg.zent","mg.zrk","mg.zrkn"],'
                  'item:{id:"minecraft:firework_rocket",count:1},teleport_duration:1,'
                  'transformation:{left_rotation:[0.5f,0.5f,-0.5f,0.5f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.4f,1.4f,1.4f]}}',
                  'execute anchored eyes positioned ^-0.2 ^-0.1 ^1 rotated as @s run tp @e[type=minecraft:item_display,tag=mg.zrkn] ~ ~ ~ ~ ~',
                  'scoreboard players operation @e[type=minecraft:item_display,tag=mg.zrkn] mg.zmo = @s mg.zid',
                  'scoreboard players set @e[type=minecraft:item_display,tag=mg.zrkn] mg.zmc 0', 'tag @e[tag=mg.zrkn] remove mg.zrkn',
                  'playsound minecraft:entity.firework_rocket.launch player @a ~ ~ ~ 1.5 0.6', 'playsound minecraft:entity.blaze.shoot player @a ~ ~ ~ 1 0.5'])
w('zx/rk_tick', ['# @s : roquette en vol, 3 pas de 0,7 bloc par tick', 'scoreboard players add @s mg.zmc 1',
                 'execute if score @s mg.zmc matches 40.. run return run function mg:zx/rk_boom',
                 'function mg:zx/rk_step', 'execute if entity @s at @s run function mg:zx/rk_step', 'execute if entity @s at @s run function mg:zx/rk_step',
                 'execute if entity @s run particle minecraft:flame ~ ~ ~ 0.05 0.05 0.05 0.02 3'])
w('zx/rk_step', ['execute unless block ^ ^ ^0.7 #mg:ray_pass positioned ^ ^ ^0.4 run return run function mg:zx/rk_boom',
                 'execute positioned ^ ^ ^0.7 positioned ~ ~-1 ~ if entity @e[tag=mg.zz,distance=..1.3] positioned ~ ~1 ~ run return run function mg:zx/rk_boom',
                 'tp @s ^ ^ ^0.7'])
w('zx/rk_boom', ['# La roquette explose : 100 de dégâts dans un rayon de 4 (crédités au tireur)'] + BOOM +
  ['scoreboard players set $gdm mg.st 1000', 'execute as @e[tag=mg.zz,distance=..4] run function mg:gun/hit_mob', 'tag @a remove mg.gsh',
   'particle minecraft:explosion_emitter ~ ~ ~ 0 0 0 0 1 force', 'particle minecraft:flame ~ ~ ~ 1.5 1.2 1.5 0.12 40 force',
   'playsound minecraft:entity.generic.explode master @a ~ ~ ~ 4 0.8', 'kill @s'])

# --- batte (comme dans Neo GTA, en plus forte) : remplace le couteau
BATZ = ('item replace entity @s hotbar.0 with minecraft:wooden_sword[item_model="$(m)",unbreakable={},'
        f'custom_name={js({"text": "🏏 Batte cloutée", "color": "gold", "italic": False})},'
        'attribute_modifiers=[{type:"minecraft:attack_damage",id:"mg:zbat",amount:13.0,operation:"add_value",slot:"mainhand"},'
        '{type:"minecraft:attack_knockback",id:"mg:zbatk",amount:1.0,operation:"add_value",slot:"mainhand"}]]')
w('zx/bat', ['# Macro $(m) : modèle', '$' + BATZ])
w('zx/bat_give', ['execute if score $rp mg.st matches 1 run function mg:zx/bat {m:"mg:bat"}',
                  'execute unless score $rp mg.st matches 1 run function mg:zx/bat {m:"minecraft:stick"}'])

C.w('infhit/hit', ['# Avancement mg:infhit : @s touché par un zombie (mob) ou un joueur infecté (équipe verte)',
                   'advancement revoke @s only mg:infhit',
                   'execute if score $state mg.st matches 2 if score $infm mg.st matches 1 if entity @s[tag=mg.play,tag=!mg.inf] run tag @s add mg.zhit'])
_adv = os.path.join(C.D, 'advancement', 'infhit.json')
os.makedirs(os.path.dirname(_adv), exist_ok=True)
with open(_adv, 'w', encoding='utf-8', newline='\n') as _f:
    json.dump({'criteria': {
        'mob': {'trigger': 'minecraft:entity_hurt_player', 'conditions': {'damage': {'type': {'source_entity': {'minecraft:entity_type': 'minecraft:zombie'}}}}},
        'joueur': {'trigger': 'minecraft:entity_hurt_player', 'conditions': {'damage': {'type': {'source_entity': {'minecraft:entity_type': 'minecraft:player', 'team': 'mg_green'}}}}}},
        'requirements': [['mob', 'joueur']], 'rewards': {'function': 'mg:infhit/hit'}}, _f, ensure_ascii=False, indent=2)
    _f.write('\n')
if not C.MAP:
    # 217/218/219 : Infection « joueurs contre mobs » sur Bunker / Laboratoire / Manoir → jeu 98/211/213 + $infm = 1
    C.patch('core/request', 'execute if score $game mg.st matches 91..92 run scoreboard players set $game mg.st 28', [
        '# Infection : 217 Bunker, 218 Laboratoire, 219 Manoir = joueurs contre mobs → jeu 98 / 211 / 213 + $infm 1',
        'scoreboard players set $infm mg.st 0',
        'execute if score $game mg.st matches 217..219 run scoreboard players set $infm mg.st 1',
        'execute if score $game mg.st matches 217 run scoreboard players set $game mg.st 98',
        'execute if score $game mg.st matches 218 run scoreboard players set $game mg.st 211',
        'execute if score $game mg.st matches 219 run scoreboard players set $game mg.st 213'])
    C.go_range(219)
C.register([97, 98], 'zmode', [
    C.announce(97, '', '🧟 ZOMBIES', 'dark_green', f'survivez à {ROUNDS} manches dans le bunker !'),
    C.announce(98, '', '🧪 INFECTION', 'dark_green', 'survivants armés contre zombies contagieux, 3 min !')])
C.objectives([('mg.zpt', 'dummy {"text":"🧟 Points","color":"dark_green"}'), ('mg.zk', 'minecraft.killed:minecraft.zombie')])
C.objectives([('mg.zkl', 'minecraft.custom:minecraft.mob_kills'), ('mg.zid', 'dummy'), ('mg.zmi', 'dummy'), ('mg.zmo', 'dummy'), ('mg.zmc', 'dummy'),
              ('mg.zws', 'dummy'), ('mg.zpy', 'dummy'), ('mg.zpl', 'dummy'), ('mg.zrt', 'dummy'), ('mg.zrp', 'dummy')])
C.objectives([('mg.zqx', 'dummy'), ('mg.zqz', 'dummy'), ('mg.zsk', 'dummy')])
C.patch('core/load', 'scoreboard objectives add mg.bw trigger', ['scoreboard players set #2 mg.st 2', 'scoreboard players set #3 mg.st 3',
                                                                 'scoreboard players set #5 mg.st 5', 'scoreboard players set #8 mg.st 8',
                                                                 'scoreboard players set #60 mg.st 60'])
C.patch('desinstaller', 'scoreboard objectives remove mg.bw', ['data remove storage mg:zm hp'])
C.forceload([f'# {NAME} Zombies / Infection (z {Z})', f'forceload add {AX1} {AZ1} {AX2} {AZ2}'])
print('Zombies/Infection OK')
