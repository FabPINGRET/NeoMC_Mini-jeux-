"""🚓 Neo GTA : la ville de Neo City, monde libre (dimension mg:gta) relié au lobby par un portail, hors mini-jeux.

    python tools/arcade/gen_gta.py .          (après gen_bomber.py : réutilise sa ville et ses explosions)

Monde
- Dimension mg:gta (data/mg/dimension/gta.json) : vide, biome the_void (aucun monstre naturel). La ville du Bombardier y est
  construite une fois (mg:gta/world_build, ~2 min au premier chargement), puis réparée en tâche de fond quand le dernier
  joueur s'en va (mg:gta/session_end). Ajouter la dimension demande un redémarrage du serveur (pas un simple /reload).
- Portail au lobby (nord-est de la place, x 9 z -33), reconstruit s'il disparaît. Sortie : panneau 🚪 au carrefour de départ,
  ou le menu (les joueurs du GTA portent mg.surv, comme la survie : exclus des mini-jeux, menu « retour au lobby »).
- Session : démarre au premier joueur (forceload + entités), s'arrête au dernier. Les dollars (mg.gta) sont gardés.

Jeu
- Batte et pistolet au départ, 16 points d'armes (mitraillette, fusil à pompe, fusil, sniper avec lunette accroupi,
  Ray Gun, lance-roquettes qui détruit les immeubles, soins, gilet), réapparition 30 s. Armes : mg:gun (guns.py).
- Voitures (chevaux invisibles rapetissés, carrosserie block_display) : on est assis dans l'habitacle, elles renversent
  ce qu'elles percutent, explosent sous les tirs et réapparaissent ailleurs. Hélicos : happy ghasts invisibles et
  rapetissés, modèle d'hélicoptère complet (fuselage, cockpit, queue, rotors, patins), destructibles eux aussi.
- Passants : 40 villageois. Police : ★ 0 à 5 (passant ou policier tué), -1 ★ toutes les 20 s sans délit. Plus d'étoiles,
  plus de policiers (4 / 8 / 12 / 16 / 22), SWAT dès 3 ★. Les policiers portent un pistolet (SWAT : fusil) et tirent de
  vraies balles sur les joueurs recherchés uniquement (les autres sont dans l'équipe mg_gciv, alliée de la police).
- Dollars : joueur +100 $, policier +25 $, passant +5 $, valises +75 $, dégâts matériels à la roquette.
  WASTED (BUSTED si recherché) : -25 % lâchés en liasse là où on meurt.
- Interface (resource pack, $rp = 1) : étoiles en haut de l'écran, viseur (rouge sur une cible), lunette du sniper,
  dollars en chiffres verts, radio dans les véhicules.
"""
import json
import os
import random
import sys
import common as C
import guns as G

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
DIM = 'mg:gta'
Z = 32400
HX, YT = 88, 170
AV = [-76, -44, -12, 20, 52]                     # mêmes avenues et rues que tools/arcade/gen_bomber.py
ST = [-78, -54, -30, -6, 18, 42, 66]
PARK = (-40, 21, 16, 63)
import os as _os
_BB = _os.listdir(_os.path.join(C.F, 'bomber', 'b'))     # étapes de construction du Bombardier (sol g*, ville p*)
NG, NP = sum(f.startswith('g') for f in _BB), sum(f.startswith('p') for f in _BB)
FL = f'-{HX} {Z - HX} {HX} {Z + HX}'
PX, PZ = 9, -19                                  # portail du lobby, le long de l'avenue nord (ouverture x 9, z -20..-18)
OLD_P = (9, -33)                                 # ancien emplacement du portail (remis en herbe)
EXIT = (-17, -10)                                # sortie dans la ville (trottoir du carrefour de départ)
SPAWN = (-12, -6)
random.seed(197)


def in_park(x, z):
    return PARK[0] <= x <= PARK[2] and PARK[1] <= z <= PARK[3]


INTER = [(c, s) for c in AV for s in ST if not in_park(c, s)]
SIDE = [(c + dx, s + dz) for (c, s) in INTER for dx in (-5, 5) for dz in (-4, 4) if not in_park(c + dx, s + dz)
        and -HX + 1 <= c + dx <= 63 and -HX + 1 <= s + dz <= HX - 1 and (c + dx, s + dz) != EXIT]
PADS_AT = random.sample([i for i in INTER if i != SPAWN], 12)
PAD_TYPES = ['heal_free'] * 6 + ['s_smg', 's_shotgun', 's_rifle', 's_smg', 's_shotgun', 's_sniper']   # rue : soins et quelques armes gratuites
ARMORY = (-22, 24, -6, 34)                       # armurerie (bâtie par gen_bomber.py) : tout, recharge 10 s
ARM_PADS = list(zip(range(ARMORY[0] + 1, ARMORY[2], 2), ['smg', 'shotgun', 'rifle', 'sniper', 'raygun', 'rpg', 'heal', 'armor']))
PAD = {  # type : (n° interne, libellé, couleur, objet affiché sans pack)
    'smg': (2, '🔫 Mitraillette', 'aqua', 'minecraft:crossbow'), 'shotgun': (3, '🔫 Fusil à pompe', 'gold', 'minecraft:crossbow'),
    'rifle': (4, '🔫 Fusil M14', 'yellow', 'minecraft:crossbow'), 'sniper': (5, '🎯 Sniper', 'light_purple', 'minecraft:spyglass'),
    'raygun': (6, '✦ Ray Gun', 'green', 'minecraft:heart_of_the_sea'), 'rpg': (7, '🚀 Lance-roquettes', 'red', 'minecraft:firework_rocket'),
    'heal': (8, '✚ Trousse de soins', 'red', 'minecraft:golden_apple'), 'armor': (9, '🛡 Gilet pare-balles', 'gray', 'minecraft:iron_chestplate'),
}
PAD.update({'s_smg': (52, '🔫 Mitraillette (gratuite)', 'aqua', 'minecraft:crossbow'), 's_shotgun': (53, '🔫 Fusil à pompe (gratuit)', 'gold', 'minecraft:crossbow'),
            's_rifle': (54, '🔫 Fusil M14 (gratuit)', 'yellow', 'minecraft:crossbow'), 's_sniper': (55, '🎯 Sniper (gratuit)', 'light_purple', 'minecraft:spyglass'),
            'heal_free': (11, '✚ Soins gratuits', 'red', 'minecraft:golden_apple'),
            'moto': (21, '🏍 Moto', 'gold', 'minecraft:saddle'), 'muscle': (22, '🚗 Muscle car', 'red', 'minecraft:minecart'),
            'supercar': (23, '🏎 Supercar', 'light_purple', 'minecraft:golden_horse_armor'), 'heli': (24, '🚁 Hélico privé', 'yellow', 'minecraft:feather'),
            'plane': (25, '✈ Avion', 'aqua', 'minecraft:elytra')})
PRICE = {2: 250, 3: 350, 4: 500, 5: 800, 6: 1500, 7: 1200, 8: 75, 9: 200, 11: 0, 21: 800, 22: 1800, 23: 3500, 24: 6000, 25: 9000}
CITY = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'neo_city.json'), encoding='utf-8'))
SHOW = CITY['showroom']
SHOW_PADS = list(zip(range(SHOW[0] + 2, SHOW[2] - 1, 3), ['moto', 'muscle', 'supercar', 'heli', 'plane']))
BANK = CITY['bank']
VAULT = ((BANK[0] + BANK[2]) // 2, BANK[3] - 2)
AIRF = ((CITY['airfield'][0] + CITY['airfield'][2]) // 2, (CITY['airfield'][1] + CITY['airfield'][3]) // 2)
CAR_DROP = ((SHOW[0] + SHOW[2]) // 2, 18)
NH = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'neo_villa.json'), encoding='utf-8'))   # Neo Hills (gen_villa.py)
VY = NH['ground'] + 1                                           # on marche à y 71 sur le domaine
VPADS = list(zip([p[0] for p in NH['garage_pads']], [p[1] for p in NH['garage_pads']], ['g_moto', 'g_muscle', 'g_super', 'g_heli', 'g_plane']))
VWEAP = list(zip([p[0] for p in NH['weapon_pads']], [p[1] for p in NH['weapon_pads']], ['g_smg', 'g_shotgun', 'g_rifle', 'g_sniper', 'g_raygun', 'g_rpg']))
VFRONT = tuple(NH['front'])                                     # arrivée à Neo GTA : derrière le portail du domaine
LIFT = tuple(NH['lift_up'])                                     # ascenseur hall ↔ toit-terrasse (y : NH['lift_y'])
NA = NH['area']
FL2 = f'{NA[0]} {Z + NA[1]} {NA[2]} {Z + NA[3] + 4}'            # chargement forcé du domaine
PAD.update({'slot': (70, '🎰 Machine à sous', 'gold', 'minecraft:gold_ingot'), 'roulette': (71, '🎡 Roulette', 'red', 'minecraft:clock'),
            'dice': (72, '🎲 Dés', 'aqua', 'minecraft:white_concrete'),
            'paint': (60, '🎨 Peinture', 'light_purple', 'minecraft:magenta_dye'), 'g_moto': (31, '🏍 Moto', 'gold', 'minecraft:saddle'), 'g_muscle': (32, '🚗 Muscle car', 'red', 'minecraft:minecart'),
            'g_super': (33, '🏎 Supercar', 'light_purple', 'minecraft:golden_horse_armor'), 'g_heli': (34, '🚁 Hélico', 'yellow', 'minecraft:feather'),
            'g_plane': (35, '✈ Avion', 'aqua', 'minecraft:elytra'), 'g_smg': (42, '🔫 Mitraillette', 'aqua', 'minecraft:crossbow'),
            'g_shotgun': (43, '🔫 Fusil à pompe', 'gold', 'minecraft:crossbow'), 'g_rifle': (44, '🔫 Fusil M14', 'yellow', 'minecraft:crossbow'),
            'g_sniper': (45, '🎯 Sniper', 'light_purple', 'minecraft:spyglass'), 'g_raygun': (46, '✦ Ray Gun', 'green', 'minecraft:heart_of_the_sea'),
            'g_rpg': (47, '🚀 Lance-roquettes', 'red', 'minecraft:firework_rocket'), 'g_armor': (49, '🛡 Gilet pare-balles', 'gray', 'minecraft:iron_chestplate')})
BASE = {31: 21, 32: 22, 33: 23, 34: 24, 35: 25, 42: 2, 43: 3, 44: 4, 45: 5, 46: 6, 47: 7, 49: 9}   # objet de la villa → achat qui le débloque
SHOP_CLERK = ['farmer', 'librarian', 'mason', 'butcher', 'cleric', 'cartographer']                       # voitures achetées : livrées dans la rue devant la concession
GUNM = {1: 'pistol', 2: 'smg', 3: 'shotgun', 4: 'rifle', 5: 'sniper', 6: 'raygun', 7: 'rpg'}
GUNM.update({n + o: m for n, m in list(GUNM.items()) if n >= 2 for o in (40, 50)})   # présentoirs de la villa (42..47) et de la rue (52..55)          # présentoirs d'armes de la villa (42..47)
CARS = [  # (n°, carrosserie, toit, nom, vitesse)
    (1, 'yellow_concrete', 'black_concrete', '🚕 Taxi', 0.34), (2, 'yellow_concrete', 'black_concrete', '🚕 Taxi', 0.34),
    (3, 'red_concrete', 'black_stained_glass', '🚗 Berline', 0.34), (4, 'blue_concrete', 'black_stained_glass', '🚗 Berline', 0.34),
    (5, 'white_concrete', 'blue_concrete', '🚓 Voiture de police', 0.38), (6, 'black_concrete', 'gray_stained_glass', '🏎 Coupé sport', 0.42),
    (7, 'lime_concrete', 'black_stained_glass', '🏎 Coupé sport', 0.42), (8, 'white_concrete', 'light_gray_concrete', '🚐 Van', 0.30),
    (9, 'orange_concrete', 'black_stained_glass', '🚗 Berline', 0.34), (10, 'yellow_concrete', 'black_concrete', '🚕 Taxi', 0.34),
]
CAR_AT = random.sample([i for i in INTER if i not in PADS_AT and i != SPAWN], 16)   # 16 vraies voitures en ville
HELI_AT = [(-30, 30, 'red_concrete'), (0, 32, 'blue_concrete'), (52, -78, 'black_concrete'), (-76, 66, 'white_concrete')]
NAMES = ['Tony', 'Carla', 'Vinnie', 'Rosa', 'Eddie', 'Lola', 'Frankie', 'Mia', 'Sal', 'Nina', 'Joey', 'Gina', 'Marco', 'Lucy', 'Rico', 'Ava']
VTYPES = ['plains', 'desert', 'savanna', 'snow', 'taiga', 'jungle', 'swamp']
STATIONS = [('Neo FM', 'pigstep'), ('Radio Pixel', 'chirp'), ('Bass City', 'otherside'), ('Lo-fi Avenue', 'mall'),
            ('Retro 88', 'blocks'), ('Night Drive', 'far'), ('Creator FM', 'creator'), ('Ocean Radio', 'precipice')]
STAR_F, STAR_E, THIN, RET_W, RET_R, SCOPE = '', '', '', '', '', ''
COPS_FOR = {1: 4, 2: 8, 3: 12, 4: 16, 5: 22}     # policiers voulus autour d'un joueur, selon ses étoiles
TR = 'transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[%sf,%sf,%sf],scale:[%sf,%sf,%sf]}'
AREA = f'x={-HX - 2},y=40,z={Z - HX - 2},dx={2 * HX + 4},dy=140,dz={2 * HX + 4}'

# ---------------------------------------------------------------- ancienne version « mini-jeu 197 » : câblage retiré
for rel in ('core/request', 'core/begin', 'core/game_tick', 'core/return_lobby'):
    L = C.lines_of(rel)
    L2 = [l for l in L if 'mg.st matches 197 run' not in l]
    if L2 != L:
        C.w(rel, L2[:-1] if L2 and L2[-1] == '' else L2)
_go = C.lines_of('core/go')
if any('mg.go matches 1..197 unless' in l for l in _go):
    C.w('core/go', [l.replace('mg.go matches 1..197 unless', 'mg.go matches 1..99 unless') for l in _go][:-1])

# ---------------------------------------------------------------- dimension
import json, os
os.makedirs(os.path.join(C.D, 'dimension'), exist_ok=True)
with open(os.path.join(C.D, 'dimension', 'gta.json'), 'w', encoding='utf-8', newline='\n') as f:
    json.dump({'type': 'minecraft:overworld', 'generator': {'type': 'minecraft:flat', 'settings': {
        'biome': 'minecraft:the_void', 'layers': [], 'lakes': False, 'features': False, 'structure_overrides': []}}}, f, indent=2)
    f.write('\n')

# ---------------------------------------------------------------- construction et réparation de la ville (dans mg:gta)
WB = ['# Une étape de construction de Neo City par tick ($gwb), dans la dimension mg:gta. Planifiée.',
      'scoreboard players add $gwb mg.st 1']
WB += [f'execute if score $gwb mg.st matches {i} in {DIM} run function mg:bomber/b/g{i}' for i in range(1, NG + 1)]
WB += [f'execute if score $gwb mg.st matches {NG + i} in {DIM} run function mg:bomber/b/p{i}' for i in range(1, NP + 1)]
WB += [f'execute if score $gwfull mg.st matches 1 if score $gwb mg.st matches {NG + NP + i} in {DIM} run function mg:gta/villa/p{i}' for i in range(1, NH['parts'] + 1)]   # Neo Hills : construction complète seulement
WB += [f'execute if score $gwb mg.st matches {NG + NP + NH["parts"] + 1} run function mg:gta/wb_done',
       f'execute if score $gwb mg.st matches ..{NG + NP + NH["parts"]} run schedule function mg:gta/wb_step 1t']
w('gta/wb_step', WB)
w('gta/wb_done', ['# Ville prête : murs invisibles, drapeau, plus de chargement forcé si personne ne joue',
                  f'execute in {DIM} run kill @e[type=minecraft:item,x={NA[0] - 2},y=50,z={Z + NA[1] - 2},dx={NA[2] - NA[0] + 4},dy=60,dz={NA[3] - NA[1] + 12}]',
                  f'execute in {DIM} run function mg:gta/walls',
                  f'execute in {DIM} if block 0 58 {Z} minecraft:stone run data modify storage mg:gta built set value 1b',
                  f'execute unless score $gtw mg.st matches 1 in {DIM} run forceload remove {FL}',
                  f'execute unless score $gtw mg.st matches 1 in {DIM} run forceload remove {FL2}'])
w('gta/world_build', ['# Première construction de Neo City (ou reconstruction complète)',
                      f'execute in {DIM} run forceload add {FL}', f'execute in {DIM} run forceload add {FL2}', 'scoreboard players set $gwb mg.st 0',
                      'scoreboard players set $gwfull mg.st 1',
                      'schedule function mg:gta/wb_step 40t'])
w('gta/walls', ['# Bord de la carte et plafond des hélicos (barrières)',
                f'fill -{HX} {YT} {Z - HX} {HX} {YT} {Z + HX} minecraft:barrier',
                f'fill {-HX - 1} 57 {Z - HX - 1} {-HX - 1} {YT - 1} {Z + HX + 1} minecraft:barrier',
                f'fill {HX + 1} 65 {Z - HX - 1} {HX + 1} {YT - 1} {Z + HX + 1} minecraft:barrier',
                f'fill {-HX} 57 {Z - HX - 1} {HX} {YT - 1} {Z - HX - 1} minecraft:barrier',
                f'fill {-HX} 57 {Z + HX + 1} {HX} {YT - 1} {Z + HX + 1} minecraft:barrier',
                # Neo Hills : trouée dans le mur nord (avenue 20), enceinte et plafond du domaine
                f'fill 17 66 {Z - HX - 1} 23 80 {Z - HX - 1} minecraft:air',
                f'fill 17 65 {Z - HX - 1} 23 65 {Z - HX - 1} minecraft:polished_andesite_slab',
                f'fill {NA[0] - 1} 57 {Z + NA[1] - 1} {NA[0] - 1} {YT - 1} {Z - HX - 2} minecraft:barrier',
                f'fill {NA[2] + 1} 57 {Z + NA[1] - 1} {NA[2] + 1} {YT - 1} {Z - HX - 2} minecraft:barrier',
                f'fill {NA[0] - 1} 57 {Z + NA[1] - 1} {NA[2] + 1} {YT - 1} {Z + NA[1] - 1} minecraft:barrier',
                f'fill {NA[0] - 1} {YT} {Z + NA[1] - 1} {NA[2] + 1} {YT} {Z - HX - 2} minecraft:barrier'])

# ---------------------------------------------------------------- portail du lobby (monde des mini-jeux)
PB = ['# Portail de Neo GTA au lobby (avenue nord, côté est), reconstruit par mg:gta/lobby_tick s\'il disparaît',
      'kill @e[tag=mg.gtap]',
      f'fill {OLD_P[0] - 4} 64 {OLD_P[1] - 4} {OLD_P[0] + 4} 73 {OLD_P[1] + 4} minecraft:air',
      f'fill {OLD_P[0] - 4} 63 {OLD_P[1] - 4} {OLD_P[0] + 4} 63 {OLD_P[1] + 4} minecraft:grass_block',
      f'fill {PX - 4} 64 {PZ - 4} {PX + 4} 73 {PZ + 4} minecraft:air',
      f'fill {PX - 4} 63 {PZ - 4} {PX + 4} 63 {PZ + 4} minecraft:polished_blackstone_bricks',
      f'fill {PX - 3} 63 {PZ - 3} {PX + 3} 63 {PZ + 3} minecraft:black_concrete',
      f'fill {PX - 4} 63 {PZ} {PX - 1} 63 {PZ} minecraft:yellow_concrete']
for k in range(-4, 5, 2):                                     # bandes jaunes et noires (chantier) sur le pourtour
    PB += [f'setblock {PX + k} 63 {PZ - 4} minecraft:yellow_concrete', f'setblock {PX + k} 63 {PZ + 4} minecraft:yellow_concrete',
           f'setblock {PX - 4} 63 {PZ + k} minecraft:yellow_concrete', f'setblock {PX + 4} 63 {PZ + k} minecraft:yellow_concrete']
PB += [f'fill {PX} 64 {PZ - 2} {PX} 69 {PZ - 2} minecraft:black_concrete', f'fill {PX} 64 {PZ + 2} {PX} 69 {PZ + 2} minecraft:black_concrete',
       f'fill {PX} 70 {PZ - 2} {PX} 70 {PZ + 2} minecraft:black_concrete',
       f'fill {PX} 64 {PZ - 3} {PX} 70 {PZ - 3} minecraft:yellow_concrete', f'fill {PX} 64 {PZ + 3} {PX} 70 {PZ + 3} minecraft:yellow_concrete',
       f'fill {PX} 71 {PZ - 3} {PX} 71 {PZ + 3} minecraft:yellow_concrete',
       f'setblock {PX} 72 {PZ - 3} minecraft:redstone_lamp[lit=true]', f'setblock {PX} 72 {PZ + 3} minecraft:redstone_lamp[lit=true]',
       f'setblock {PX - 1} 71 {PZ - 3} minecraft:end_rod[facing=west]', f'setblock {PX - 1} 71 {PZ + 3} minecraft:end_rod[facing=west]',
       f'setblock {PX} 63 {PZ} minecraft:chiseled_polished_blackstone',
       # haie de l'avenue ouverte devant le portail, passage pavé jusqu'à l'avenue (x 4 à 8)
       f'fill 4 64 {PZ - 1} {PX - 1} 66 {PZ + 1} minecraft:air', f'fill 4 63 {PZ - 1} {PX - 5} 63 {PZ + 1} minecraft:stone_bricks',
       f'setblock {PX - 3} 64 {PZ - 4} minecraft:iron_bars', f'setblock {PX - 3} 65 {PZ - 4} minecraft:iron_bars', f'setblock {PX - 3} 66 {PZ - 4} minecraft:lantern',
       f'setblock {PX - 3} 64 {PZ + 4} minecraft:iron_bars', f'setblock {PX - 3} 65 {PZ + 4} minecraft:iron_bars', f'setblock {PX - 3} 66 {PZ + 4} minecraft:lantern',
       f'summon minecraft:text_display {PX - 0.6} 72.6 {PZ + 0.5} {{Tags:["mg.gtap"],Rotation:[90f,0f],text:{js({"text": "🚓 NEO GTA", "color": "gold", "bold": True})},'
       f'background:-1442840576,{TR % (0, 0, 0, 2.6, 2.6, 2.6)}}}',
       f'summon minecraft:text_display {PX - 0.6} 72.15 {PZ + 0.5} {{Tags:["mg.gtap"],Rotation:[90f,0f],text:{js({"text": "Monde GTA libre : armes, voitures, hélicos, police", "color": "gray"})},'
       f'background:0,{TR % (0, 0, 0, 0.9, 0.9, 0.9)}}}',
       f'summon minecraft:text_display {PX - 0.6} 64.4 {PZ + 0.5} {{Tags:["mg.gtap"],Rotation:[90f,0f],text:{js({"text": "▶ entre dans le portail", "color": "yellow"})},'
       f'background:0,{TR % (0, 0, 0, 0.8, 0.8, 0.8)}}}']
# petit taxi garé à côté du portail
for (blk, tx, ty, tz, sx, sy, sz) in [('yellow_concrete', -0.95, 0.05, -1.7, 1.9, 0.75, 3.4), ('black_concrete', -0.8, 0.8, -0.9, 1.6, 0.65, 1.7),
                                       ('yellow_concrete', -0.3, 1.45, -0.3, 0.6, 0.2, 0.6), ('black_concrete', -1.0, 0.0, -1.25, 0.25, 0.45, 0.6),
                                       ('black_concrete', 0.75, 0.0, -1.25, 0.25, 0.45, 0.6), ('black_concrete', -1.0, 0.0, 0.85, 0.25, 0.45, 0.6),
                                       ('black_concrete', 0.75, 0.0, 0.85, 0.25, 0.45, 0.6)]:
    PB.append(f'summon minecraft:block_display {PX + 2.5} 64 {PZ + 0.5} {{Tags:["mg.gtap"],block_state:{{Name:"minecraft:{blk}"}},{TR % (tx, ty, tz, sx, sy, sz)}}}')
w('gta/portal_build', PB)
w('gta/lobby_tick', ['# Chaque tick (core/tick, monde des mini-jeux) : portail de Neo City, session du monde GTA',
                     f'execute if score $setup mg.st matches 1 as @a[tag=!mg.play,tag=!mg.out,tag=!mg.surv,tag=!mg.inplot,tag=!mg.visit,tag=!mg.lk,tag=!mg.pkr,tag=!mg.ely,tag=!mg.elyf,gamemode=adventure,x={PX},y=64,z={PZ - 1},dx=0,dy=2,dz=2] run function mg:gta/enter',
                     f'particle minecraft:dust{{color:[1.0,0.82,0.1],scale:1.1}} {PX + 0.5} 66.5 {PZ + 0.5} 0.05 1.3 1.1 0 3',
                     f'particle minecraft:portal {PX + 0.5} 66.5 {PZ + 0.5} 0.05 1.3 1.1 0.3 4',
                     f'execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 unless block {PX} 63 {PZ} minecraft:chiseled_polished_blackstone run function mg:gta/portal_build',
                     'execute unless score $gtw mg.st matches 1 if entity @a[tag=mg.gtw] run function mg:gta/session_start',
                     'execute if score $gtw mg.st matches 1 unless entity @a[tag=mg.gtw] run function mg:gta/session_end',
                     'execute if score $gtw mg.st matches 1 run function mg:gta/tick'])
w('gta/pre_tick', ['# Avant la survie (core/tick) : un joueur du GTA sorti de la dimension sans passer par la sortie perd ses tags',
                   f'execute as @a[tag=mg.gtw] at @s unless dimension {DIM} run function mg:gta/strayed'])
w('gta/strayed', ['# @s a quitté Neo City autrement (téléportation…) : il n\'est plus considéré comme joueur du GTA',
                  'tag @s remove mg.gtw', 'tag @s remove mg.surv', 'function mg:gta/untag'])

# ---------------------------------------------------------------- entrée, sortie, session
P_LINES = ['# @s : à un carrefour au hasard de Neo City (dans la dimension du contexte)',
           f'execute store result score $gr mg.st run random value 0..{len(INTER) - 1}']
P_LINES += [f'execute if score $gr mg.st matches {i} run tp @s {x + 0.5} 65 {Z + z + 0.5}' for i, (x, z) in enumerate(INTER)]
w('gta/place', P_LINES)
w('gta/enter', ['# @s entre dans le portail de Neo City',
                'execute unless data storage mg:gta built run return run function mg:gta/not_ready',
                'execute if entity @s[tag=mg.mpp] run return run tellraw @s {"text":"⚠ Tu participes à la Mini Party : Neo GTA sera accessible après.","color":"red"}',
                'function mg:lobkart/leave', 'function mg:parkour/quit',
                'tag @s remove mg.inplot', 'tag @s remove mg.plabel', 'tag @s remove mg.visit',
                'tag @s add mg.surv', 'tag @s add mg.gtw',
                'execute if score $state mg.st matches 0 run scoreboard players reset @s mg.vc',
                'execute if score $state mg.st matches 0 run function mg:vote/refresh',
                'team leave @s', 'effect clear @s', 'clear @s', 'gamemode adventure @s', 'function mg:core/attr_reset',
                'attribute @s minecraft:fall_damage_multiplier base set 1',
                'function mg:gta/join',
                f'execute in {DIM} run spawnpoint @s {VFRONT[0]} {VY} {Z + VFRONT[1]}',
                f'execute in {DIM} run tp @s {VFRONT[0] + 0.5} {VY} {Z + VFRONT[1] + 0.5} 180 0',
                'function mg:gta/kit',
                'title @s times 10 50 20', 'title @s title {"text":"NEO GTA","color":"gold","bold":true}',
                'title @s subtitle {"text":"Bienvenue en ville. Fais-toi un nom.","color":"gray"}',
                'tellraw @s ' + js([{'text': '🚓 NEO GTA ', 'color': 'gold', 'bold': True},
                                    {'text': 'Armes sur les trottoirs, voitures et hélicos (clic droit pour monter), lunette du sniper en s\'accroupissant. '
                                             'Passants et flics tués = ★ : la police débarque, de plus en plus nombreuse. Tes dollars sont gardés. ', 'color': 'gray'},
                                    {'text': 'Retour au lobby : panneau 🚪 près du carrefour de départ, ou menu (Échap → ≡ Menu).', 'color': 'yellow'}]),
                'execute at @s run playsound minecraft:block.portal.travel master @s ~ ~ ~ 0.3 1.6'])
w('gta/not_ready', ['# Neo City pas encore construite : on recule le joueur', f'tp @s {PX - 3}.5 64 {PZ + 0.5} -90 0',
                    'tellraw @s {"text":"🚧 Neo GTA est en construction (environ 2 minutes après le démarrage du serveur). Réessaie bientôt !","color":"yellow"}'])
w('gta/join', ['# @s : réglages d\'arrivée (les dollars sont gardés d\'une visite à l\'autre)',
               'tag @s add mg.gtg', 'execute unless score @s mg.gta matches -2147483648.. run scoreboard players set @s mg.gta 0',
               'scoreboard players set @s mg.gwl 0', 'scoreboard players set @s mg.gwt 0', 'scoreboard players set @s mg.grk 0',
               'scoreboard players add $bidn mg.st 1', 'scoreboard players operation @s mg.bid = $bidn mg.st',
               'scoreboard players reset @s mg.gkp', 'scoreboard players reset @s mg.gkv', 'scoreboard players reset @s mg.gks',
               'scoreboard players reset @s mg.gkw', 'scoreboard players reset @s mg.gqs', 'scoreboard players set @s mg.deaths 0',
               'function mg:gun/reset', 'scoreboard players set @s mg.gtl 0', 'scoreboard players set @s mg.gal 0', 'tag @s remove mg.gdrv',
               'team join mg_gciv @s'])
w('gta/untag', ['# @s : plus joueur du GTA (tags, sons, titres, étoiles, mission)', 'function mg:gta/mis_clean', 'tag @s remove mg.gtg', 'tag @s remove mg.gclub', 'tag @s remove mg.gdrv',
                'tag @s remove mg.gscope', 'tag @s remove mg.grd', 'tag @s remove mg.gro', 'stopsound @s record',
                'title @s clear', 'title @s reset', 'scoreboard players reset @s mg.gwl', 'scoreboard players reset @s mg.gwt',
                'function mg:gun/reset', 'team leave @s'])
w('gta/leave', ['# @s retourne au lobby (appelé dans le monde des mini-jeux : execute in minecraft:overworld)',
                'execute unless entity @s[tag=mg.gtw] run return 0',
                'tag @s remove mg.gtw', 'tag @s remove mg.surv', 'function mg:gta/untag',
                'function mg:core/reset_player', 'attribute @s minecraft:fall_damage_multiplier base set 0',
                'tellraw @s [{"text":"⌂ Retour au lobby. Tes dollars restent à Neo City : ","color":"gold"},'
                '{"score":{"name":"@s","objective":"mg.gta"},"color":"green","bold":true},{"text":" $","color":"green"}]'])
w('gta/session_start', ['# Premier joueur à Neo City : chargement de la ville, entités dans 1,5 s',
                        'scoreboard players set $gtw mg.st 1', 'scoreboard players set $gtt mg.st 0',
                        f'execute in {DIM} run forceload add {FL}', f'execute in {DIM} run forceload add {FL2}', 'schedule function mg:gta/session_setup 30t'])
w('gta/session_setup', ['# Session : entités de Neo City (dans la dimension)',
                        'execute unless score $gtw mg.st matches 1 run return 0', f'execute in {DIM} run function mg:gta/setup_in'])
w('gta/session_end', ['# Plus personne à Neo City : entités retirées, ville réparée en tâche de fond, puis plus de chargement forcé',
                      'scoreboard players set $gtw mg.st 0', 'scoreboard players set $gsu mg.st 0', 'schedule clear mg:gta/session_setup', 'function mg:gta/clear',
                      'function mg:gta/bars_remove', 'team remove mg_gciv',
                      f'scoreboard players set $gwb mg.st {NG}', 'scoreboard players set $gwfull mg.st 0', 'schedule function mg:gta/wb_step 20t'])
w('gta/clear', ['# Retire tout ce que le GTA a posé (entités, objets au sol, flèches)', 'kill @e[tag=mg.gta]',
                f'execute in {DIM} run kill @e[type=minecraft:item,x={NA[0] - 2},y=50,z={Z + NA[1] - 2},dx={NA[2] - NA[0] + 4},dy=60,dz={NA[3] - NA[1] + 12}]',
                f'execute in {DIM} run kill @e[type=minecraft:item,{AREA}]',
                f'execute in {DIM} run kill @e[type=#minecraft:arrows,{AREA}]',
                f'execute in {DIM} run kill @e[type=minecraft:experience_orb,{AREA}]'])

def shop_label(nm):
    return [{"text": nm, "color": "white", "bold": True}, {"text": "\nbraquable : accroupi + arme devant la caisse", "color": "gray", "bold": False}]


S = ['# Entités de la session (contexte : dimension mg:gta)', 'function mg:gta/clear', 'function mg:gta/walls',
     'scoreboard players set $gvid mg.st 0', 'team add mg_gciv', 'team modify mg_gciv friendlyFire true', 'team modify mg_gciv seeFriendlyInvisibles false',
     'team modify mg_gciv nametagVisibility always', 'team join mg_gciv @a[tag=mg.gtw,scores={mg.gwl=0}]', 'function mg:gta/bars']
S += [f'summon minecraft:marker {x} 65 {Z + z} {{Tags:["mg.gta","mg.gix"]}}' for (x, z) in INTER]
S += [f'summon minecraft:marker {x} 65 {Z + z} {{Tags:["mg.gta","mg.gsw"]}}' for (x, z) in SIDE]
for (x, z), t in zip(PADS_AT, PAD_TYPES):
    n = PAD[t][0]
    px, pz = x - 5, z - 4
    S += [f'summon minecraft:marker {px} 65 {Z + pz} {{Tags:["mg.gta","mg.gpad","mg.gpn"]}}',
          f'scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt {n}', 'scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0',
          'execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show',
          f'summon minecraft:block_display {px - 0.5} 65 {Z + pz - 0.5} {{Tags:["mg.gta","mg.gpdb"],block_state:{{Name:"minecraft:light_weighted_pressure_plate"}}}}',
          'tag @e[tag=mg.gpn] remove mg.gpn']
for x, t in ARM_PADS:                                         # présentoirs de l'armurerie (plancher y 65)
    z = ARMORY[3] - 2
    S += [f'summon minecraft:marker {x} 66 {Z + z} {{Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}}',
          f'scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt {PAD[t][0]}', 'scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0',
          'execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show',
          f'summon minecraft:block_display {x - 0.5} 66 {Z + z - 0.5} {{Tags:["mg.gta","mg.gpdb"],block_state:{{Name:"minecraft:light_weighted_pressure_plate"}}}}',
          'tag @e[tag=mg.gpn] remove mg.gpn']
for x, t in SHOW_PADS:                                        # concession (plancher y 65)
    z = SHOW[3] - 3
    S += [f'summon minecraft:marker {x} 66 {Z + z} {{Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}}',
          f'scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt {PAD[t][0]}', 'scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0',
          'execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show',
          f'summon minecraft:block_display {x - 0.5} 66 {Z + z - 0.5} {{Tags:["mg.gta","mg.gpdb"],block_state:{{Name:"minecraft:light_weighted_pressure_plate"}}}}',
          'tag @e[tag=mg.gpn] remove mg.gpn']
S += [f'summon minecraft:text_display {(SHOW[0] + SHOW[2]) / 2 + 0.5} 71.5 {Z + SHOW[1] - 0.05} {{Tags:["mg.gta"],Rotation:[0f,0f],text:{js({"text": "🏎 NEO MOTORS", "color": "light_purple", "bold": True})},'
      f'background:0,{TR % (0, 0, 0, 2.0, 2.0, 2.0)}}}',
      f'summon minecraft:text_display {(BANK[0] + BANK[2]) / 2 + 0.5} 72.6 {Z + BANK[1] - 1.1} {{Tags:["mg.gta"],Rotation:[0f,0f],text:{js({"text": "🏦 BANQUE DE NEO CITY", "color": "gold", "bold": True})},'
      f'background:0,{TR % (0, 0, 0, 1.6, 1.6, 1.6)}}}',
      f'summon minecraft:marker {VAULT[0]} 66 {Z + VAULT[1]} {{Tags:["mg.gta","mg.gbank"]}}', 'scoreboard players set @e[type=minecraft:marker,tag=mg.gbank] mg.gpc 0',
      f'summon minecraft:text_display {VAULT[0] + 0.5} 68.2 {Z + VAULT[1] + 0.5} {{Tags:["mg.gta","mg.gbkl"],billboard:"center",text:{js({"text": "💰 Coffres : accroupi + arme pendant 15 s", "color": "gold"})},'
      f'background:1073741824,{TR % (0, 0, 0, 0.6, 0.6, 0.6)}}}',
      f'summon minecraft:marker {AIRF[0]} 66 {Z + AIRF[1]} {{Tags:["mg.gta","mg.gair"]}}']
for (x, z, y, ts) in [(x, z, VY, t) for x, z, t in VPADS] + [(x, z, VY, t) for x, z, t in VWEAP] + \
                     [(NH['heal_pad'][0], NH['heal_pad'][1], VY, 'heal_free'), (NH['armor_pad'][0], NH['armor_pad'][1], VY, 'g_armor'),
                      (NH['garage_pads'][-1][0] + 3, NH['garage_pads'][-1][1], VY, 'paint')]:
    S += [f'summon minecraft:marker {x} {y} {Z + z} {{Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}}',
          f'scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt {PAD[ts][0]}', 'scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0',
          'execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show',
          f'summon minecraft:block_display {x - 0.5} {y} {Z + z - 0.5} {{Tags:["mg.gta","mg.gpdb"],block_state:{{Name:"minecraft:light_weighted_pressure_plate"}}}}',
          'tag @e[tag=mg.gpn] remove mg.gpn']
S += [f'summon minecraft:marker {LIFT[0]} {NH["lift_y"][0]} {Z + LIFT[1]} {{Tags:["mg.gta","mg.glup"]}}',
      f'summon minecraft:marker {LIFT[0]} {NH["lift_y"][1]} {Z + LIFT[1]} {{Tags:["mg.gta","mg.gldn"]}}',
      f'summon minecraft:text_display {LIFT[0] + 0.5} {NH["lift_y"][0] + 1.8} {Z + LIFT[1] + 0.5} {{Tags:["mg.gta"],billboard:"center",text:{js({"text": "⬆ Toit-terrasse : jacuzzi et bar", "color": "aqua"})},background:1073741824,{TR % (0, 0, 0, 0.6, 0.6, 0.6)}}}',
      f'summon minecraft:text_display {LIFT[0] + 0.5} {NH["lift_y"][1] + 1.8} {Z + LIFT[1] + 0.5} {{Tags:["mg.gta"],billboard:"center",text:{js({"text": "⬇ Descendre", "color": "aqua"})},background:1073741824,{TR % (0, 0, 0, 0.6, 0.6, 0.6)}}}',
      f'summon minecraft:block_display {LIFT[0] - 0.5} {NH["lift_y"][0]} {Z + LIFT[1] - 0.5} {{Tags:["mg.gta"],block_state:{{Name:"minecraft:heavy_weighted_pressure_plate"}}}}',
      f'summon minecraft:block_display {LIFT[0] - 0.5} {NH["lift_y"][1]} {Z + LIFT[1] - 0.5} {{Tags:["mg.gta"],block_state:{{Name:"minecraft:heavy_weighted_pressure_plate"}}}}',
      f'summon minecraft:text_display {NH["sign"][0] + 0.5} {VY + 9.6} {Z + NH["sign"][1] + 0.6} {{Tags:["mg.gta"],Rotation:[0f,0f],'
      f'text:[{js({"text": "NEO HILLS", "color": "gold", "bold": True})},{js({"text": "\nla villa des joueurs : tout ce qui a été acheté une fois est ici, gratuit", "color": "gray"})}],'
      f'background:-1442840576,{TR % (0, 0, 0, 1.4, 1.4, 1.4)}}}']
for (x, z, ts) in [(p_[0], p_[1], 'slot') for p_ in CITY['places']['casino']['slots']] + [(CITY['places']['casino']['roulette'][0], CITY['places']['casino']['roulette'][1], 'roulette'),
                                                                                        (CITY['places']['casino']['roulette'][0], CITY['places']['casino']['roulette'][1] + 4, 'dice')]:
    S += [f'summon minecraft:marker {x} 66 {Z + z} {{Tags:["mg.gta","mg.gpad","mg.garm","mg.gpn"]}}',
          f'scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpt {PAD[ts][0]}', 'scoreboard players set @e[type=minecraft:marker,tag=mg.gpn] mg.gpc 0',
          'execute as @e[type=minecraft:marker,tag=mg.gpn] at @s run function mg:gta/pad_show', 'tag @e[tag=mg.gpn] remove mg.gpn']
S.append('function mg:gta/places_setup')
for k, (mx, sz, nm, col) in enumerate(CITY['shops']):                    # caissier derrière le comptoir, mode d'emploi du braquage
    S += [f'summon minecraft:villager {mx}.5 66 {Z + sz + 5}.5 {{Tags:["mg.gta","mg.npc","mg.gclerk"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,'
          f'Rotation:[180f,0f],VillagerData:{{profession:"minecraft:{SHOP_CLERK[k % len(SHOP_CLERK)]}",type:"minecraft:plains",level:2}},'
          f'CustomName:{js({"text": "Caissier", "color": "gray"})},CustomNameVisible:0b}}',
          f'summon minecraft:text_display {mx + 0.5} 67.55 {Z + sz + 3.65} {{Tags:["mg.gta"],Rotation:[180f,0f],'
          f'text:[{js({"text": "🔫 BRAQUAGE", "color": "red", "bold": True})},{js({"text": "\nAccroupis-toi devant la caisse, arme en main (5 s)", "color": "white"})},'
          f'{js({"text": "\n💰 200 à 450 $  ·  ★★ police", "color": "gold"})}],background:-1442840576,{TR % (0, 0, 0, 0.45, 0.45, 0.45)}}}']
for k, (mx, sz, nm, col) in enumerate(CITY['shops']):
    S += [f'summon minecraft:marker {mx} 66 {Z + sz + 3} {{Tags:["mg.gta","mg.gshop"]}}',
          f'scoreboard players set @e[type=minecraft:marker,tag=mg.gshop,limit=1,sort=nearest,x={mx},y=66,z={Z + sz + 3}] mg.gsid {k}',
          f'scoreboard players set @e[type=minecraft:marker,tag=mg.gshop,limit=1,sort=nearest,x={mx},y=66,z={Z + sz + 3}] mg.gpc 0',
          f'summon minecraft:text_display {mx + 0.5} 70.4 {Z + sz - 1.2} {{Tags:["mg.gta","mg.gshl"],Rotation:[180f,0f],text:{js(shop_label(nm))},'
          f'background:-1442840576,{TR % (0, 0, 0, 1.1, 1.1, 1.1)}}}',
          f'scoreboard players set @e[type=minecraft:text_display,tag=mg.gshl,limit=1,sort=nearest,x={mx + 0.5},y=70.4,z={Z + sz - 1.2}] mg.gsid {k}']
S += [f'summon minecraft:text_display -13.5 70.5 {Z + ARMORY[1] - 0.05} {{Tags:["mg.gta"],Rotation:[0f,0f],text:{js({"text": "🔫 ARMURERIE", "color": "white", "bold": True})},'
      f'background:0,{TR % (0, 0, 0, 2.2, 2.2, 2.2)}}}',
      f'summon minecraft:text_display -13.5 70.05 {Z + ARMORY[1] - 0.05} {{Tags:["mg.gta"],Rotation:[0f,0f],text:{js({"text": "Toutes les armes, en libre-service", "color": "yellow"})},'
      f'background:0,{TR % (0, 0, 0, 0.7, 0.7, 0.7)}}}']
for (car, (x, z)) in zip(CARS * 2, CAR_AT):
    S.append(f'execute positioned {x + 2} 65 {Z + z} run function mg:gta/car/spawn_{car[0]}')
for (x, z, col) in HELI_AT:
    S.append(f'execute positioned {x} 66 {Z + z} run function mg:gta/heli_spawn {{c:"{col}"}}')
ex, ez = EXIT
S += [f'summon minecraft:marker {ex} 65 {Z + ez} {{Tags:["mg.gta","mg.gexit"]}}',
      f'summon minecraft:block_display {ex - 0.5} 65 {Z + ez - 0.5} {{Tags:["mg.gta"],block_state:{{Name:"minecraft:heavy_weighted_pressure_plate"}}}}',
      f'summon minecraft:text_display {ex + 0.5} 67.2 {Z + ez + 0.5} {{Tags:["mg.gta"],billboard:"center",text:{js({"text": "🚪 Retour au lobby", "color": "gold", "bold": True})},'
      f'background:1073741824,{TR % (0, 0, 0, 0.9, 0.9, 0.9)}}}',
      'execute as @e[type=minecraft:marker,tag=mg.gsw,sort=random,limit=40] at @s run function mg:gta/ped_spawn',
      'scoreboard players set $gsu mg.st 2', 'function mg:gta/dots_init']
w('gta/setup_in', S)

# ---------------------------------------------------------------- kit
BAT = ('item replace entity @s hotbar.0 with minecraft:wooden_sword[item_model="$(m)",unbreakable={},'
       f'custom_name={js({"text": "🏏 Batte de baseball", "color": "gold", "italic": False})},'
       'attribute_modifiers=[{type:"minecraft:attack_damage",id:"mg:bat",amount:4.0,operation:"add_value",slot:"mainhand"},'
       '{type:"minecraft:attack_knockback",id:"mg:batk",amount:1.0,operation:"add_value",slot:"mainhand"}]]')
w('gta/bat', ['# @s : batte (macro : $(m) = modèle)', '$' + BAT])
w('gta/kit', ['# @s : batte, pistolet', 'clear @s', 'function mg:gun/reset',
              'execute if score $rp mg.st matches 1 run function mg:gta/bat {m:"mg:bat"}',
              'execute unless score $rp mg.st matches 1 run function mg:gta/bat {m:"minecraft:stick"}', G.give(1, 'hotbar.1'),
              'scoreboard players set @s mg.grk 0',
              'function mg:gta/kit_plus',
              'item replace entity @s hotbar.7 with minecraft:warped_fungus_on_a_stick[custom_data={gtahome:1b},item_model="minecraft:oak_door",unbreakable={},'
              f'custom_name={js({"text": "🏠 Retour à la villa", "color": "aqua", "bold": True, "italic": False})},'
              f'lore=[{js({"text": "Clic droit : Neo Hills (pas avec la police aux trousses)", "color": "gray", "italic": False})}]]',
              'item replace entity @s hotbar.8 with minecraft:paper[custom_data={gtamap:1b},item_model="minecraft:filled_map",'
              f'custom_name={js({"text": "🗺 Carte de Neo City", "color": "aqua", "bold": True, "italic": False})},'
              f'lore=[{js({"text": "En main : plan de la ville et ta position", "color": "gray", "italic": False})}]]',
              'effect give @s minecraft:saturation infinite 0 true', 'effect give @s minecraft:resistance 3 4 true'])

# ---------------------------------------------------------------- tick de la session
w('gta/tick', ['# 🚓 Neo City : chaque tick tant qu\'un joueur y est', 'scoreboard players add $gtt mg.st 1',
               # armes : clic (objectif mg.gqs, la survie remet mg.qs à zéro pour les joueurs taggés mg.surv)
               'execute as @a[tag=mg.gtw,scores={mg.gqs=1..}] if items entity @s weapon.mainhand *[custom_data~{gtaphone:1b}] run function mg:gta/phone',
               'execute as @a[tag=mg.gtw,scores={mg.gqs=1..}] if items entity @s weapon.mainhand *[custom_data~{gtanitro:1b}] run function mg:gta/nitro',
               'execute as @a[tag=mg.gtw,scores={mg.gmis=1..}] run function mg:gta/mis_cmd',
               'scoreboard players remove @a[tag=mg.gtw,scores={mg.gnit=1..}] mg.gnit 1',
               'execute as @a[tag=mg.gtw,scores={mg.gcas=1..}] at @s run function mg:gta/cas_cmd',
               'scoreboard players remove @a[tag=mg.gtw,scores={mg.gcre=1..}] mg.gcre 1',
               'execute as @a[tag=mg.gtw,scores={mg.gcre=1}] run function mg:gta/cas_reopen_tick',
               'execute as @a[tag=mg.gtw,scores={mg.gqs=1..}] if items entity @s weapon.mainhand *[custom_data~{rpg:1b}] at @s run function mg:gta/panic',
               'execute as @a[tag=mg.gtw,scores={mg.gqs=1..}] at @s if items entity @s weapon.mainhand *[custom_data~{rpg:1b}] run function mg:gta/rpg_fire',
               'execute as @a[tag=mg.gtw,scores={mg.gqs=1..}] if items entity @s weapon.mainhand *[custom_data~{gtahome:1b}] run function mg:gta/home',
               'execute as @a[tag=mg.gtw,scores={mg.gqs=1..}] at @s run function mg:gun/use',
               'execute as @a[tag=mg.gtw,scores={mg.gqs=1..}] if items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] at @s run function mg:gta/panic',
               'execute as @a[tag=mg.gtw,scores={mg.gqs=1..}] if items entity @s weapon.mainhand *[custom_data~{rpg:1b}] at @s run function mg:gta/panic',
               'scoreboard players reset @a[scores={mg.gqs=1..}] mg.gqs',
               'execute as @e[type=minecraft:marker,tag=mg.gtraf] at @s run function mg:gta/traffic/tick',
               'execute as @e[type=minecraft:interaction,tag=mg.gcint] if data entity @s interaction run function mg:gta/car_int',
               'execute as @e[type=minecraft:interaction,tag=mg.gtint] if data entity @s interaction run function mg:gta/traffic/int',
               'execute as @e[type=minecraft:marker,tag=mg.gphel] at @s run function mg:gta/pheli_tick',
               'function mg:gta/panic_tick',
               'scoreboard players remove @a[tag=mg.gtw,scores={mg.gcd=1..}] mg.gcd 1',
               'execute as @a[tag=mg.gtw,scores={mg.grl=1..}] at @s run function mg:gun/reload_tick',
               'execute as @a[tag=mg.gtw,scores={mg.gsn=1..}] if items entity @s weapon.mainhand *[custom_data~{gun:5}] run scoreboard players reset @s mg.gsn',
               'execute as @a[tag=mg.gtw,scores={mg.gsn=1..}] at @s run function mg:gun/sneak',
               'scoreboard players reset @a[tag=mg.gtw,scores={mg.gsn=1..}] mg.gsn',
               'execute as @a[tag=mg.gscope] unless items entity @s weapon.mainhand *[custom_data~{gun:5}] run function mg:gta/unscope',
               'execute as @a[tag=mg.gscope] unless predicate mg:sneak run function mg:gta/unscope',
               'execute as @e[type=minecraft:item_display,tag=mg.grkt] at @s run function mg:gta/rocket_tick',
               # interface
               'scoreboard players remove @a[tag=mg.gtw,scores={mg.gtl=1..}] mg.gtl 1',
               'scoreboard players remove @a[tag=mg.gtw,scores={mg.gal=1..}] mg.gal 1',
               'scoreboard players operation $gq2 mg.st = $gtt mg.st', 'scoreboard players set #2 mg.st 2', 'scoreboard players operation $gq2 mg.st %= #2 mg.st',
               'execute if score $gq2 mg.st matches 0 if score $rp mg.st matches 1 as @a[tag=mg.gtw,scores={mg.gtl=..0}] if items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] at @s run function mg:gta/aim',
               'execute if score $gq2 mg.st matches 0 if score $rp mg.st matches 1 as @a[tag=mg.gtw,scores={mg.gtl=..0}] if items entity @s weapon.mainhand *[custom_data~{rpg:1b}] at @s run function mg:gta/aim',
               # véhicules, police
               'execute as @e[type=minecraft:horse,tag=mg.gcarh] at @s run function mg:gta/car_sync',
               'execute as @e[type=minecraft:happy_ghast,tag=mg.ghel] at @s run function mg:gta/heli_sync',
               'scoreboard players operation $gq mg.st = $gtt mg.st', 'scoreboard players set #20 mg.st 20', 'scoreboard players operation $gq mg.st %= #20 mg.st',
               'execute if score $gq mg.st matches 0 as @e[tag=mg.gcop] at @s if entity @a[tag=mg.gtw,scores={mg.gwl=1..},gamemode=!spectator,distance=..28] run function mg:gta/cop_fire',
               'execute if score $gq mg.st matches 10 as @e[tag=mg.gcop] at @s if entity @a[tag=mg.gtw,scores={mg.gwl=1..},gamemode=!spectator,distance=..28] run function mg:gta/cop_fire',
               # crimes, morts
               'execute as @a[tag=mg.gtw,scores={mg.gkp=1..}] run function mg:gta/kill_player',
               'execute as @a[tag=mg.gtw,scores={mg.gkv=1..}] run function mg:gta/kill_ped',
               'execute as @a[tag=mg.gtw,scores={mg.gks=1..}] run function mg:gta/kill_cop',
               'execute as @a[tag=mg.gtw,scores={mg.gkw=1..}] run function mg:gta/kill_cop',
               f'execute as @a[tag=mg.gtw,scores={{mg.deaths=1..}}] in {DIM} run function mg:gta/wasted',
               'scoreboard players remove @a[tag=mg.gtw,scores={mg.gwt=1..}] mg.gwt 1',
               'execute as @a[tag=mg.gtw,scores={mg.gwl=1..,mg.gwt=0}] run function mg:gta/wanted_down',
               # ramassages, sortie
               'execute as @e[type=minecraft:item_display,tag=mg.gpdi] at @s run tp @s ~ ~ ~ ~5 ~',
               'execute as @e[type=minecraft:item_display,tag=mg.gcash,tag=!mg.gbill] at @s run tp @s ~ ~ ~ ~4 ~',
               'execute as @a[tag=mg.gtw] at @s as @e[type=minecraft:item_display,tag=mg.gcash,distance=..1.6,limit=1] run function mg:gta/cash_take',
               'execute as @a[tag=mg.gtw] at @s if entity @e[type=minecraft:marker,tag=mg.gexit,distance=..1.3] in minecraft:overworld run function mg:gta/leave',
               'scoreboard players operation $gq5t mg.st = $gtt mg.st', 'scoreboard players set #5 mg.st 5', 'scoreboard players operation $gq5t mg.st %= #5 mg.st',
               'execute if score $gq5t mg.st matches 0 as @a[tag=mg.gtw,gamemode=!spectator] if predicate mg:sneak if items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] at @s run function mg:gta/rob',
               'execute if score $gq5t mg.st matches 0 as @a[tag=mg.gtw,gamemode=!spectator] if predicate mg:sneak if items entity @s weapon.mainhand *[custom_data~{rpg:1b}] at @s run function mg:gta/rob',
               'execute if score $gq5t mg.st matches 0 as @a[tag=mg.gtw,scores={mg.grob=1..}] unless predicate mg:sneak run function mg:gta/rob_stop',
               'execute if score $gq5t mg.st matches 0 as @a[tag=mg.gtw,scores={mg.gmt=1..}] at @s run function mg:gta/mis_tick',
               'execute if score $gq5t mg.st matches 0 as @a[tag=mg.gtw,gamemode=!spectator] if predicate mg:sneak at @s if entity @e[type=minecraft:marker,tag=mg.gtraf,distance=..2.6] run function mg:gta/traffic/steal_near',
               'scoreboard players operation $gq4 mg.st = $gtt mg.st', 'scoreboard players set #4 mg.st 4', 'scoreboard players operation $gq4 mg.st %= #4 mg.st',
               'execute if score $gq4 mg.st matches 0 as @a[tag=mg.gtw] if items entity @s weapon.mainhand *[custom_data~{gtamap:1b}] run function mg:gta/map_show',
               'execute as @a[tag=mg.gtw] at @s if entity @e[type=minecraft:marker,tag=mg.glup,distance=..0.8] in mg:gta run function mg:gta/lift_up',
               'execute as @a[tag=mg.gtw] at @s if entity @e[type=minecraft:marker,tag=mg.gldn,distance=..0.8] in mg:gta run function mg:gta/lift_down',
               'execute if score $gq mg.st matches 0 run function mg:gta/second',
               'execute if score $gq mg.st matches 0 run function mg:gta/pads',
               'execute if score $gq mg.st matches 10 run function mg:gta/pads',
               'execute if score $gq mg.st matches 0 run function mg:gta/club_tick', 'execute if score $gq mg.st matches 10 run function mg:gta/club_tick',
               'execute if score $gq mg.st matches 5 run function mg:gta/hud',
               'execute if score $gq mg.st matches 5 run function mg:gta/radio_check',
               'execute if score $gq mg.st matches 15 run function mg:gta/hud'])
w('gta/second', ['# Chaque seconde : véhicules détruits, passants, police, sirènes, valises, ménage',
                 'execute unless score $gsu mg.st matches 1.. run return 0',
                 'execute if score $gsu mg.st matches 1 as @e[type=minecraft:block_display,tag=mg.gvb,tag=!mg.gok] at @s run function mg:gta/wreck',
                 'execute if score $gsu mg.st matches 1 run kill @e[type=minecraft:block_display,tag=mg.gvd,tag=!mg.gok]',
                 'execute if score $gsu mg.st matches 1 run kill @e[type=minecraft:interaction,tag=mg.gcint,tag=!mg.gok]',
                 'tag @e[tag=mg.gok] remove mg.gok', 'scoreboard players set $gsu mg.st 1',
                 'execute store result score $gpn mg.st if entity @e[type=minecraft:villager,tag=mg.gped]',
                 'execute if score $gpn mg.st matches ..39 as @e[type=minecraft:marker,tag=mg.gsw,sort=random,limit=1] at @s unless entity @a[tag=mg.gtw,distance=..12] run function mg:gta/ped_spawn',
                 'execute if score $gpn mg.st matches ..30 as @e[type=minecraft:marker,tag=mg.gsw,sort=random,limit=1] at @s unless entity @a[tag=mg.gtw,distance=..12] run function mg:gta/ped_spawn',
                 'team join mg_gciv @a[tag=mg.gtw,scores={mg.gwl=0}]', 'team leave @a[tag=mg.gtw,scores={mg.gwl=1..}]',
                 'scoreboard players operation $gq3 mg.st = $gtt mg.st', 'scoreboard players set #40 mg.st 40', 'scoreboard players operation $gq3 mg.st %= #40 mg.st',
                 'execute store result score $gca mg.st if entity @e[tag=mg.gcop]',
                 'execute if score $gq3 mg.st matches 0 if score $gca mg.st matches ..44 as @a[tag=mg.gtw,scores={mg.gwl=1..}] at @s run function mg:gta/police_call',
                 'execute if score $gq3 mg.st matches 0 as @e[tag=mg.gcop,tag=!mg.gphel] at @s unless entity @a[tag=mg.gtw,scores={mg.gwl=1..},distance=..60] run function mg:gta/cop_leave',
                 'execute if score $gq3 mg.st matches 0 as @a[tag=mg.gtw,scores={mg.gwl=1..}] at @s run function mg:gta/police_plus',
                 'function mg:gta/police_clean', 'function mg:gta/traffic/second',
                 'scoreboard players operation $gq10 mg.st = $gtt mg.st', 'scoreboard players set #200 mg.st 200', 'scoreboard players operation $gq10 mg.st %= #200 mg.st',
                 f'execute if score $gq10 mg.st matches 0 in {DIM} run kill @e[type=minecraft:item,{AREA}]',
                 f'execute if score $gq10 mg.st matches 0 in {DIM} run kill @e[type=minecraft:item,x={NA[0] - 2},y=50,z={Z + NA[1] - 2},dx={NA[2] - NA[0] + 4},dy=60,dz={NA[3] - NA[1] + 12}]',
                 'execute as @a[tag=mg.gtw,scores={mg.gwl=1..}] at @s run function mg:gta/siren',
                 'function mg:gta/bars_tick', 'scoreboard players enable @a[tag=mg.gtw] mg.gmis',
                 'execute as @e[type=minecraft:marker,tag=mg.gshop,scores={mg.gpc=1..20}] run function mg:gta/shop_reopen',
                 'scoreboard players remove @e[type=minecraft:marker,tag=mg.gshop,scores={mg.gpc=1..}] mg.gpc 20',
                 'execute as @e[type=minecraft:marker,tag=mg.gbank,scores={mg.gpc=1..20}] run function mg:gta/bank_reopen',
                 'scoreboard players remove @e[type=minecraft:marker,tag=mg.gbank,scores={mg.gpc=1..}] mg.gpc 20',
                 'scoreboard players operation $gq5 mg.st = $gtt mg.st', 'scoreboard players set #300 mg.st 300', 'scoreboard players operation $gq5 mg.st %= #300 mg.st',
                 'execute store result score $gcn mg.st if entity @e[type=minecraft:item_display,tag=mg.gcash]',
                 'execute if score $gq5 mg.st matches 0 if score $gcn mg.st matches ..3 at @e[type=minecraft:marker,tag=mg.gsw,sort=random,limit=1] run function mg:gta/cash_spawn',
                 'execute store result score $gvc mg.st if entity @e[type=minecraft:horse,tag=mg.gcarh]',
                 'execute if score $gq5 mg.st matches 100 if score $gvc mg.st matches ..15 as @e[type=minecraft:marker,tag=mg.gix,sort=random,limit=1] at @s unless entity @a[tag=mg.gtw,distance=..20] run function mg:gta/car_random',
                 'execute if score $gq5 mg.st matches 200 if score $gvc mg.st matches ..15 as @e[type=minecraft:marker,tag=mg.gix,sort=random,limit=1] at @s unless entity @a[tag=mg.gtw,distance=..20] run function mg:gta/car_random',
                 'execute store result score $ghc mg.st if entity @e[type=minecraft:happy_ghast,tag=mg.ghel]',
                 'execute if score $gq5 mg.st matches 0 if score $ghc mg.st matches ..3 run function mg:gta/heli_random',
                 'execute as @a[tag=mg.gtw] at @s if entity @s[y=0,dy=60] run function mg:gta/place',
                 f'execute in {DIM} run kill @e[type=#minecraft:arrows,{AREA},nbt={{inGround:1b}}]'])

# ---------------------------------------------------------------- viseur, lunette, radio, étoiles
w('gta/aim', ['# @s tient une arme : viseur au centre, rouge si une cible est dans la ligne de mire (48 blocs) ; sniper accroupi : lunette',
              'execute if items entity @s weapon.mainhand *[custom_data~{gun:5}] if predicate mg:sneak run return run function mg:gta/scope',
              'scoreboard players set $ga mg.st 0', 'scoreboard players set $gar mg.st 48', 'tag @s add mg.gaim',
              'execute anchored eyes positioned ^ ^ ^1 run function mg:gta/aim_ray', 'tag @s remove mg.gaim',
              'title @s times 0 5 2',
              'execute if score $ga mg.st matches 0 run title @s title ' + js({'text': RET_W, 'font': 'mg:gta', 'color': 'white', 'shadow_color': 0}),
              'execute if score $ga mg.st matches 1 run title @s title ' + js({'text': RET_R, 'font': 'mg:gta', 'color': 'white', 'shadow_color': 0})])
w('gta/aim_ray', ['# Un pas (1 bloc) de la ligne de mire',
                  'execute unless block ~ ~ ~ #mg:ray_pass run return 0',
                  'execute positioned ~-0.5 ~-0.5 ~-0.5 if entity @e[tag=mg.gtg,tag=!mg.gaim,dx=0,dy=0,dz=0] run return run scoreboard players set $ga mg.st 1',
                  'scoreboard players remove $gar mg.st 1',
                  'execute if score $gar mg.st matches 1.. positioned ^ ^ ^1 run function mg:gta/aim_ray'])
w('gta/scope', ['# @s vise à la lunette (sniper, accroupi) : cache noir, zoom (lenteur = champ de vision réduit)',
                'tag @s add mg.gscope', 'title @s times 0 5 2', 'title @s title ' + js({'text': SCOPE, 'font': 'mg:gta', 'color': 'white', 'shadow_color': 0}),
                'effect give @s minecraft:slowness 1 6 true'])
w('gta/unscope', ['# @s quitte la lunette', 'tag @s remove mg.gscope', 'effect clear @s minecraft:slowness', 'title @s clear'])
w('gta/radio_check', ['# Toutes les 0,5 s : la radio s\'allume en montant dans une voiture ou un hélico, s\'éteint en descendant',
                      'execute as @e[type=minecraft:horse,tag=mg.gcarh] on passengers run tag @s add mg.gdrn',
                      'execute as @e[type=minecraft:happy_ghast,tag=mg.ghel] on passengers run tag @s add mg.gdrn',
                      'execute as @a[tag=mg.gdrn,tag=!mg.gdrv] at @s run function mg:gta/radio_on',
                      'execute as @a[tag=mg.gdrv,tag=!mg.gdrn] run function mg:gta/radio_off',
                      'tag @a remove mg.gdrn'])
RO = ['# @s monte dans un véhicule : une station au hasard', 'tag @s add mg.gdrv', 'scoreboard players set @s mg.gal 60',
      f'execute store result score $gr mg.st run random value 0..{len(STATIONS) - 1}']
for i, (nm, disc) in enumerate(STATIONS):
    RO += [f'execute if score $gr mg.st matches {i} run playsound minecraft:music_disc.{disc} record @s ~ ~ ~ 0.8 1 0.5',
           f'execute if score $gr mg.st matches {i} run title @s actionbar ' + js([{'text': '📻 ', 'color': 'white'}, {'text': nm, 'color': 'aqua', 'bold': True},
                                                                                {'text': '  ♪', 'color': 'gray'}])]
w('gta/radio_on', RO)
w('gta/radio_off', ['# @s descend : la radio se coupe', 'tag @s remove mg.gdrv', 'stopsound @s record'])
B = ['# Étoiles de recherche : une barre de boss par niveau (1 à 5), haut de l\'écran']
for k in range(1, 6):
    rp = js({'text': THIN.join([STAR_F] * k + [STAR_E] * (5 - k)), 'font': 'mg:gta', 'color': 'white'})
    plain = js([{'text': '★' * k, 'color': 'gold', 'bold': True}, {'text': '☆' * (5 - k), 'color': 'dark_gray', 'bold': True}])
    B += [f'bossbar add mg:gtaw{k} ""', f'bossbar set mg:gtaw{k} color white', f'bossbar set mg:gtaw{k} max 1', f'bossbar set mg:gtaw{k} value 0',
          f'execute if score $rp mg.st matches 1 run bossbar set mg:gtaw{k} name {rp}',
          f'execute unless score $rp mg.st matches 1 run bossbar set mg:gtaw{k} name {plain}']
w('gta/bars', B)
w('gta/bars_tick', ['# Chaque seconde : chaque joueur voit la barre de son niveau'] +
  [f'bossbar set mg:gtaw{k} players @a[tag=mg.gtw,scores={{mg.gwl={k}}}]' for k in range(1, 6)])
w('gta/bars_remove', [f'bossbar remove mg:gtaw{k}' for k in range(1, 6)])

# ---------------------------------------------------------------- dollars, crimes, recherche
def money(n, why, col='green'):
    return [f'scoreboard players add @s mg.gta {n}',
            f'title @s actionbar [{{"text":"+{n} $ ","color":"{col}","bold":true}},{{"text":"{why}","color":"gray"}}]',
            'execute at @s run playsound minecraft:block.note_block.bit player @s ~ ~ ~ 0.7 1.6', 'scoreboard players set @s mg.gal 40']


w('gta/kill_player', ['# @s a tué un joueur'] + money(100, 'joueur éliminé') + ['scoreboard players remove @s mg.gkp 1',
                      'execute if score @s mg.gkp matches 1.. run function mg:gta/kill_player'])
w('gta/kill_ped', ['# @s a tué un passant : +5 $, une étoile de plus'] + money(5, 'passant', 'yellow') +
  ['scoreboard players remove @s mg.gkv 1', 'function mg:gta/wanted_up', 'execute if score @s mg.gkv matches 1.. run function mg:gta/kill_ped'])
w('gta/kill_cop', ['# @s a tué un policier : +25 $, une étoile de plus'] + money(25, 'policier abattu', 'aqua') +
  ['scoreboard players reset @s mg.gks', 'scoreboard players reset @s mg.gkw', 'function mg:gta/wanted_up'])
w('gta/wanted_up', ['# @s : une étoile de plus (5 max), 15 s avant de redescendre',
                    'execute if score @s mg.gwl matches ..4 run scoreboard players add @s mg.gwl 1', 'scoreboard players set @s mg.gwt 300',
                    'team leave @s',
                    'execute at @s run playsound minecraft:block.note_block.pling player @s ~ ~ ~ 0.8 0.6',
                    'execute at @s run playsound minecraft:block.note_block.bell player @s ~ ~ ~ 0.6 1.8'])
w('gta/wanted_down', ['# @s : toutes les 15 s, une étoile de moins', 'scoreboard players remove @s mg.gwl 1', 'scoreboard players set @s mg.gwt 300',
                      'execute if score @s mg.gwl matches 0 run team join mg_gciv @s',
                      'execute if score @s mg.gwl matches 0 run scoreboard players set @s mg.gal 40',
                      'execute if score @s mg.gwl matches 0 run title @s actionbar {"text":"☆ La police a perdu ta trace","color":"green"}'])
w('gta/wasted', ['# @s est mort (contexte : dimension mg:gta) : WASTED, ou BUSTED s\'il était recherché ; -25 % lâchés en liasse',
                 'scoreboard players set @s mg.deaths 0', 'scoreboard players set @s mg.gtl 60',
                 'execute if score @s mg.gwl matches 1.. run tag @s add mg.gbust',
                 'scoreboard players operation $gl mg.st = @s mg.gta', 'scoreboard players set #4 mg.st 4', 'scoreboard players operation $gl mg.st /= #4 mg.st',
                 'scoreboard players operation @s mg.gta -= $gl mg.st',
                 'title @s times 5 45 15',
                 'execute if score @s mg.gwl matches 1.. run title @s title {"text":"BUSTED","color":"#4A7BD8","bold":true}',
                 'execute if score @s mg.gwl matches 1.. run title @s subtitle [{"text":"-","color":"#4A7BD8"},{"score":{"name":"$gl","objective":"mg.st"},"color":"#4A7BD8"},{"text":" $ (caution)","color":"gray"}]',
                 'execute unless score @s mg.gwl matches 1.. run title @s title {"text":"WASTED","color":"#C8102E","bold":true}',
                 'execute unless score @s mg.gwl matches 1.. run title @s subtitle [{"text":"-","color":"#C8102E"},{"score":{"name":"$gl","objective":"mg.st"},"color":"#C8102E"},{"text":" $ (frais d\'hôpital)","color":"gray"}]',
                 'scoreboard players set @s mg.gwl 0', 'scoreboard players set @s mg.gwt 0', 'team join mg_gciv @s',
                 'execute if score $gl mg.st matches 1.. run function mg:gta/drop_cash',
                 'function mg:gta/mis_fail', 'function mg:gta/radio_off', 'function mg:gta/unscope', 'function mg:gta/respawn_at', 'function mg:gta/kit',
                 'execute at @s run playsound minecraft:entity.wither.death player @s ~ ~ ~ 0.4 1.6',
                 'execute at @s run playsound minecraft:block.bell.resonate player @s ~ ~ ~ 0.8 0.5'])
w('gta/drop_cash', ['# @s vient de mourir : les dollars perdus ($gl) tombent en liasse là où il est mort',
                    'data modify storage mg:gta d set value {x:0,y:0,z:0}',
                    'execute store result storage mg:gta d.x int 1 run data get entity @s LastDeathLocation.pos[0]',
                    'execute store result storage mg:gta d.y int 1 run data get entity @s LastDeathLocation.pos[1]',
                    'execute store result storage mg:gta d.z int 1 run data get entity @s LastDeathLocation.pos[2]',
                    'scoreboard players operation $gcv mg.st = $gl mg.st', 'function mg:gta/drop_cash_at with storage mg:gta d'])
w('gta/drop_cash_at', ['# Liasse à la position de la mort (macro : $(x) $(y) $(z))',
                       '$execute positioned $(x) $(y) $(z) align xyz positioned ~0.5 ~0.8 ~0.5 run function mg:gta/cash_new'])
w('gta/siren', ['# @s est recherché : sirène (deux tons) et lumières', 'scoreboard players operation $gs mg.st = $gtt mg.st',
                'scoreboard players set #40 mg.st 40', 'scoreboard players operation $gs mg.st %= #40 mg.st',
                'execute if score $gs mg.st matches 0 run playsound minecraft:block.note_block.bell hostile @a ~ ~ ~ 1.2 1.4',
                'execute if score $gs mg.st matches 20 run playsound minecraft:block.note_block.bell hostile @a ~ ~ ~ 1.2 1.0',
                'execute if score @s mg.gwl matches 3.. run particle minecraft:dust{color:[0.1,0.3,1.0],scale:1.5} ~ ~2.4 ~ 0.3 0.1 0.3 0 3',
                'execute if score @s mg.gwl matches 3.. run particle minecraft:dust{color:[1.0,0.1,0.1],scale:1.5} ~ ~2.4 ~ 0.3 0.1 0.3 0 3'])

# ---------------------------------------------------------------- police
PC = [f'# @s est recherché : renforts toutes les 2 s tant qu\'il y a moins de policiers que voulu dans les 40 blocs {COPS_FOR}',
      'execute store result score $gc mg.st if entity @e[tag=mg.gcop,distance=..40]']
PC += [f'execute if score @s mg.gwl matches {k} run scoreboard players set $gw mg.st {v}' for k, v in COPS_FOR.items()]
PC += ['execute if score $gc mg.st >= $gw mg.st run return 0',
       'execute as @e[type=minecraft:marker,tag=mg.gix,distance=14..45,sort=random,limit=1] at @s run function mg:gta/cop_spawn',
       'execute if score @s mg.gwl matches 2.. as @e[type=minecraft:marker,tag=mg.gix,distance=14..45,sort=random,limit=1] at @s run function mg:gta/cop_spawn',
       'execute if score @s mg.gwl matches 5 as @e[type=minecraft:marker,tag=mg.gix,distance=14..45,sort=random,limit=1] at @s run function mg:gta/cop_spawn',
       'execute if score @s mg.gwl matches 3.. as @e[type=minecraft:marker,tag=mg.gix,distance=14..45,sort=random,limit=1] at @s run function mg:gta/swat_spawn',
       'execute if score @s mg.gwl matches 4.. as @e[type=minecraft:marker,tag=mg.gix,distance=14..45,sort=random,limit=1] at @s run function mg:gta/swat_spawn',
       'execute if score @s mg.gwl matches 5 as @e[type=minecraft:marker,tag=mg.gix,distance=14..45,sort=random,limit=1] at @s run function mg:gta/swat_spawn']
w('gta/police_call', PC)


def cop(model):
    return ('summon minecraft:skeleton ~ ~ ~ {Tags:["mg.gta","mg.gtg","mg.gcop","mg.npc","mg.gcopn"],PersistenceRequired:1b,'
            'CustomName:{"text":"Policier","color":"blue"},'
            'equipment:{head:{id:"minecraft:iron_helmet",count:1},chest:{id:"minecraft:leather_chestplate",count:1,components:{"minecraft:dyed_color":1981031}},'
            'legs:{id:"minecraft:leather_leggings",count:1,components:{"minecraft:dyed_color":1981031}},feet:{id:"minecraft:leather_boots",count:1,components:{"minecraft:dyed_color":1315860}},'
            f'mainhand:{{id:"minecraft:warped_fungus_on_a_stick",count:1,components:{{"minecraft:item_model":"{model}"}}}}}},'
            'drop_chances:{head:0f,chest:0f,legs:0f,feet:0f,mainhand:0f},attributes:[{id:"minecraft:movement_speed",base:0.28}]}')


def swat(model):
    return ('summon minecraft:wither_skeleton ~ ~ ~ {Tags:["mg.gta","mg.gtg","mg.gcop","mg.gswat","mg.npc","mg.gcopn"],PersistenceRequired:1b,'
            'CustomName:{"text":"SWAT","color":"dark_gray","bold":true},'
            'equipment:{head:{id:"minecraft:netherite_helmet",count:1},chest:{id:"minecraft:leather_chestplate",count:1,components:{"minecraft:dyed_color":1315860}},'
            'legs:{id:"minecraft:leather_leggings",count:1,components:{"minecraft:dyed_color":1315860}},'
            f'mainhand:{{id:"minecraft:warped_fungus_on_a_stick",count:1,components:{{"minecraft:item_model":"{model}"}}}}}},'
            'drop_chances:{head:0f,chest:0f,legs:0f,mainhand:0f},attributes:[{id:"minecraft:movement_speed",base:0.3}]}')


w('gta/cop_spawn', ['# Arrivée de deux policiers armés à ce carrefour (gyrophare)',
                    'execute if score $rp mg.st matches 1 run ' + cop('mg:gun_pistol'),
                    'execute if score $rp mg.st matches 1 positioned ~1 ~ ~ run ' + cop('mg:gun_pistol'),
                    'execute unless score $rp mg.st matches 1 run ' + cop('minecraft:crossbow'),
                    'execute unless score $rp mg.st matches 1 positioned ~1 ~ ~ run ' + cop('minecraft:crossbow'),
                    'team join mg_gciv @e[tag=mg.gcopn]', 'tag @e[tag=mg.gcopn] remove mg.gcopn',
                    'particle minecraft:dust{color:[0.1,0.3,1.0],scale:2} ~ ~2 ~ 0.6 0.3 0.6 0 12',
                    'particle minecraft:dust{color:[1.0,0.1,0.1],scale:2} ~ ~2 ~ 0.6 0.3 0.6 0 12',
                    'playsound minecraft:block.note_block.bell hostile @a ~ ~ ~ 2 1.4'])
w('gta/swat_spawn', ['# SWAT (3 ★ et plus) : deux agents au fusil',
                     'execute if score $rp mg.st matches 1 run ' + swat('mg:gun_rifle'),
                     'execute if score $rp mg.st matches 1 positioned ~ ~ ~1 run ' + swat('mg:gun_rifle'),
                     'execute unless score $rp mg.st matches 1 run ' + swat('minecraft:crossbow'),
                     'execute unless score $rp mg.st matches 1 positioned ~ ~ ~1 run ' + swat('minecraft:crossbow'),
                     'team join mg_gciv @e[tag=mg.gcopn]', 'tag @e[tag=mg.gcopn] remove mg.gcopn',
                     'playsound minecraft:entity.iron_golem.attack hostile @a ~ ~ ~ 2 0.6'])
w('gta/cop_fire', ['# @s (policier) : tire sur le joueur recherché le plus proche s\'il le voit (une chance sur trois toutes les 0,5 s)',
                   'execute store result score $gr mg.st run random value 0..3', 'execute if score $gr mg.st matches 1.. run return 0',
                   'tag @s add mg.gcsh', 'scoreboard players set $gcd2 mg.st 2', 'execute if entity @s[tag=mg.gswat] run scoreboard players set $gcd2 mg.st 3',
                   'execute store result storage mg:gta s.a int 1 run random value -6..6', 'execute store result storage mg:gta s.b int 1 run random value -4..4',
                   'execute if entity @s[tag=mg.gswat] store result storage mg:gta s.a int 1 run random value -4..4',
                   'scoreboard players set $gcr mg.st 56', 'function mg:gta/cop_shot with storage mg:gta s', 'tag @s remove mg.gcsh',
                   'playsound minecraft:entity.firework_rocket.blast hostile @a ~ ~ ~ 1.6 1.7',
                   'execute anchored eyes positioned ^-0.3 ^-0.2 ^0.8 run particle minecraft:small_flame ~ ~ ~ 0.02 0.02 0.02 0 3'])
w('gta/cop_shot', ['# Balle du policier vers sa cible, écartée de $(a)° / $(b)°',
                   '$execute anchored eyes facing entity @p[tag=mg.gtw,scores={mg.gwl=1..},gamemode=!spectator,distance=..28] eyes rotated ~$(a) ~$(b) positioned ^ ^ ^0.8 run function mg:gta/cop_ray'])
w('gta/cop_ray', ['# Un pas (0,5 bloc) de la balle du policier',
                  'execute unless block ~ ~ ~ #mg:ray_pass run return run particle minecraft:smoke ~ ~ ~ 0.05 0.05 0.05 0 2',
                  'execute positioned ~-0.5 ~-0.5 ~-0.5 as @a[tag=mg.gtw,gamemode=!spectator,dx=0,dy=0,dz=0,limit=1] run return run function mg:gta/cop_hit',
                  'particle minecraft:crit ~ ~ ~ 0 0 0 0 1',
                  'scoreboard players remove $gcr mg.st 1',
                  'execute if score $gcr mg.st matches 1.. positioned ^ ^ ^0.5 run function mg:gta/cop_ray'])
w('gta/cop_hit', ['# @s touché par une balle de la police',
                  'execute if score $gcd2 mg.st matches 2 run damage @s 2 minecraft:mob_attack by @e[tag=mg.gcsh,limit=1]',
                  'execute if score $gcd2 mg.st matches 3 run damage @s 3 minecraft:mob_attack by @e[tag=mg.gcsh,limit=1]',
                  'particle minecraft:damage_indicator ~ ~1.2 ~ 0.2 0.3 0.2 0 2'])
w('gta/cop_leave', ['# Plus personne de recherché à proximité : le policier s\'en va', 'particle minecraft:poof ~ ~1 ~ 0.3 0.6 0.3 0.02 10', 'execute on vehicle run function mg:gta/veh_remove', 'tp @s ~ -300 ~'])
w('gta/ped_spawn', ['# Un passant sur ce trottoir (habits et prénom au hasard)', 'execute store result score $gr mg.st run random value 0..15'] +
  [f'execute if score $gr mg.st matches {i} run summon minecraft:villager ~ ~ ~ {{Tags:["mg.gta","mg.gtg","mg.gped","mg.npc"],PersistenceRequired:1b,'
   f'VillagerData:{{profession:"minecraft:nitwit",type:"minecraft:{VTYPES[i % len(VTYPES)]}",level:1}},'
   f'CustomName:{{"text":"{nm}","color":"gray"}},CustomNameVisible:0b}}' for i, nm in enumerate(NAMES)])

# ---------------------------------------------------------------- points d'armes
PS = ['# @s (marqueur du point) : objet qui tourne + étiquette']
for t, (n, lab, col, it) in PAD.items():
    if n in GUNM:
        PS.append(f'execute if score @s mg.gpt matches {n} if score $rp mg.st matches 1 run summon minecraft:item_display ~ ~1.1 ~ {{Tags:["mg.gta","mg.gpdi"],'
                  f'item:{{id:"minecraft:warped_fungus_on_a_stick",count:1,components:{{"minecraft:item_model":"mg:gun_{GUNM[n]}"}}}},'
                  f'teleport_duration:1,glow_color_override:16766720,Glowing:1b,{TR % (0, 0, 0, 1.3, 1.3, 1.3)}}}')
        PS.append(f'execute if score @s mg.gpt matches {n} unless score $rp mg.st matches 1 run summon minecraft:item_display ~ ~1.1 ~ {{Tags:["mg.gta","mg.gpdi"],'
                  f'item:{{id:"{it}",count:1}},teleport_duration:1,glow_color_override:16766720,Glowing:1b,{TR % (0, 0, 0, 0.9, 0.9, 0.9)}}}')
    else:
        PS.append(f'execute if score @s mg.gpt matches {n} run summon minecraft:item_display ~ ~1.1 ~ {{Tags:["mg.gta","mg.gpdi"],item:{{id:"{it}",count:1}},'
                  f'teleport_duration:1,glow_color_override:16766720,Glowing:1b,{TR % (0, 0, 0, 0.9, 0.9, 0.9)}}}')
    LBL = [{"text": lab, "color": col, "bold": True}] + ([{"text": f"\n{PRICE[n]} $", "color": "green", "bold": True}] if PRICE.get(n) else []) + \
          ([{"text": "\ngratuit une fois acheté", "color": "gray"}] if n in BASE else [])
    PS.append(f'execute if score @s mg.gpt matches {n} run summon minecraft:text_display ~ ~2 ~ {{Tags:["mg.gta","mg.gpdt"],billboard:"center",'
              f'text:{js(LBL)},background:1073741824,{TR % (0, 0, 0, 0.7, 0.7, 0.7)}}}')
w('gta/pad_show', PS)
w('gta/pads', ['# Présentoirs : réassort, achat par le joueur le plus proche (une fois par passage : tag mg.gbz sur le présentoir, retiré quand plus personne n\'est devant)',
               'scoreboard players remove @e[type=minecraft:marker,tag=mg.gpad,scores={mg.gpc=1..}] mg.gpc 10',
               'execute as @e[type=minecraft:marker,tag=mg.gpad,scores={mg.gpc=0}] at @s unless entity @e[type=minecraft:item_display,tag=mg.gpdi,distance=..1.5] run function mg:gta/pad_show',
               'execute as @e[type=minecraft:marker,tag=mg.gpad,tag=mg.gbz] at @s unless entity @a[tag=mg.gtw,gamemode=!spectator,distance=..2] run tag @s remove mg.gbz',
               'execute as @e[type=minecraft:marker,tag=mg.gpad,tag=!mg.gbz,scores={mg.gpc=..0}] at @s if entity @a[tag=mg.gtw,gamemode=!spectator,distance=..1.6] run function mg:gta/pad_take',
               'tag @a remove mg.gbuy'])
w('gta/pad_take', ['# @s (présentoir) : le joueur le plus proche achète (ou prend, si c\'est gratuit)',
                   'scoreboard players operation $gpt mg.st = @s mg.gpt', 'scoreboard players set $gok mg.st 0', 'tag @s add mg.gbz',
                   'execute as @a[tag=mg.gtw,tag=!mg.gbuy,gamemode=!spectator,distance=..1.6,sort=nearest,limit=1] at @s run function mg:gta/pad_buy',
                   'execute unless score $gok mg.st matches 1 run return 0',
                   'scoreboard players set @s mg.gpc 600', 'execute if entity @s[tag=mg.garm] run scoreboard players set @s mg.gpc 40',
                   'kill @e[type=minecraft:item_display,tag=mg.gpdi,distance=..1.5]', 'kill @e[type=minecraft:text_display,tag=mg.gpdt,distance=..2.5]',
                   'playsound minecraft:entity.villager.yes player @a ~ ~ ~ 0.6 1.2'])
PB_ = ['# @s : achat du contenu du présentoir ($gpt) si assez de dollars (villa : gratuit si déjà acheté)', 'tag @s add mg.gbuy', 'scoreboard players set $gpr mg.st 0',
       'execute if score $gpt mg.st matches 31..49 run return run function mg:gta/villa_take']
PB_ += [f'execute if score $gpt mg.st matches {n} run scoreboard players set $gpr mg.st {v}' for n, v in PRICE.items() if v]
PB_ += ['execute if score @s mg.gta < $gpr mg.st run scoreboard players set @s mg.gal 40',
        'execute if score @s mg.gta < $gpr mg.st run playsound minecraft:entity.villager.no player @s ~ ~ ~ 0.8 1',
        'execute if score @s mg.gta < $gpr mg.st run return run title @s actionbar [{"text":"💸 Pas assez d\'argent : il faut ","color":"red"},'
        '{"score":{"name":"$gpr","objective":"mg.st"},"color":"gold","bold":true},{"text":" $. Braque des passants, des commerces ou la banque !","color":"red"}]',
        'scoreboard players operation @s mg.gta -= $gpr mg.st', 'scoreboard players set $gok mg.st 1', 'function mg:gta/unlock', 'execute if score $gpt mg.st matches 52..57 run scoreboard players remove $gpt mg.st 50', 'function mg:gta/pad_give',
        'execute if score $gpr mg.st matches 1.. run playsound minecraft:block.note_block.chime player @s ~ ~ ~ 0.8 1.4']
w('gta/pad_buy', PB_)
w('gta/unlock', ['# Achat de $gpt : désormais disponible gratuitement à la villa, pour tout le monde'] +
  [f'execute if score $gpt mg.st matches {b} run data modify storage mg:gta unl.t{b} set value 1b' for b in sorted(set(BASE.values()))] +
  ['execute if score $gpt mg.st matches 2..9 run tellraw @s {"text":"🏠 Débloqué : il est aussi au râtelier de la villa, gratuit pour tous.","color":"aqua"}',
   'execute if score $gpt mg.st matches 21..25 run tellraw @s {"text":"🏠 Débloqué : il est aussi au garage de la villa, gratuit pour tous.","color":"aqua"}'])
VT = ['# @s prend un objet à la villa ($gpt) : seulement s\'il a déjà été acheté une fois']
for v, b in BASE.items():
    VT += [f'execute if score $gpt mg.st matches {v} unless data storage mg:gta unl.t{b} run return run function mg:gta/villa_locked',
           f'execute if score $gpt mg.st matches {v} run scoreboard players set $gpt mg.st {b}']
VT += ['scoreboard players set $gvilla mg.st 1', 'scoreboard players set $gok mg.st 1', 'function mg:gta/pad_give', 'scoreboard players set $gvilla mg.st 0']
w('gta/villa_take', VT)
w('gta/villa_locked', ['# Pas encore acheté', 'scoreboard players set @s mg.gal 50', 'playsound minecraft:entity.villager.no player @s ~ ~ ~ 0.8 1',
                       'title @s actionbar {"text":"🔒 Pas encore acheté : achète-le une fois (armurerie ou concession), il sera ici gratuitement pour tous","color":"red"}'])
GV = ['# @s reçoit le contenu du point ($gpt)']
for t, (n, lab, col, it) in PAD.items():
    msg = f'title @s actionbar {js({"text": lab, "color": col, "bold": True})}'
    GV.append(f'execute if score $gpt mg.st matches {n} run scoreboard players set @s mg.gal 40')
    if n in (2, 3, 4):
        GV += [f'execute if score $gpt mg.st matches {n} run {G.give(n, "hotbar.2")}', f'execute if score $gpt mg.st matches {n} run {msg}']
    elif n in (5, 6):
        GV += [f'execute if score $gpt mg.st matches {n} run {G.give(n, "hotbar.3")}', f'execute if score $gpt mg.st matches {n} run {msg}']
    elif n == 7:
        GV += ['execute if score $gpt mg.st matches 7 run function mg:gta/rpg_give', f'execute if score $gpt mg.st matches 7 run {msg}']
    elif n == 8:
        GV += ['execute if score $gpt mg.st matches 8 run effect give @s minecraft:instant_health 1 2 true',
               'execute if score $gpt mg.st matches 8 run effect give @s minecraft:regeneration 8 1 true', f'execute if score $gpt mg.st matches 8 run {msg}']
    elif n == 9:
        GV += ['execute if score $gpt mg.st matches 9 run item replace entity @s armor.chest with minecraft:iron_chestplate[unbreakable={},'
               f'custom_name={js({"text": "🛡 Gilet pare-balles", "color": "gray", "italic": False})}]',
               'execute if score $gpt mg.st matches 9 run effect give @s minecraft:absorption 60 1 true', f'execute if score $gpt mg.st matches 9 run {msg}']
GV += ['execute if score $gpt mg.st matches 70 run function mg:gta/cas_ui_slot', 'execute if score $gpt mg.st matches 71 run function mg:gta/cas_ui_roulette',
       'execute if score $gpt mg.st matches 72 run function mg:gta/cas_ui_dice',
       'execute if score $gpt mg.st matches 60 run function mg:gta/paint',
       'execute if score $gpt mg.st matches 11 run effect give @s minecraft:instant_health 1 1 true',
       'execute if score $gpt mg.st matches 11 run title @s actionbar {"text":"✚ Soigné","color":"red","bold":true}']
GV += [f'execute if score $gpt mg.st matches {PAD[t][0]} run function mg:gta/veh_buy {{t:"{t}"}}' for t in ('moto', 'muscle', 'supercar', 'heli', 'plane')]
w('gta/pad_give', GV)

# ---------------------------------------------------------------- lance-roquettes
RPG_BASE = ('minecraft:warped_fungus_on_a_stick[custom_data={rpg:1b},unbreakable={},'
            f'custom_name={js({"text": "🚀 Lance-roquettes", "color": "red", "bold": True, "italic": False})},'
            f'lore=[{js({"text": "Clic droit : tirer une roquette", "color": "gray", "italic": False})},'
            f'{js({"text": "Roquettes : à l\'armurerie (+5)", "color": "dark_gray", "italic": False})}]')
w('gta/rpg_give', ['# @s : lance-roquettes (+5 roquettes, 15 au plus)',
                   f'execute if score $rp mg.st matches 1 run item replace entity @s hotbar.4 with {RPG_BASE},item_model="mg:gun_rpg"]',
                   f'execute unless score $rp mg.st matches 1 run item replace entity @s hotbar.4 with {RPG_BASE},item_model="minecraft:crossbow"]',
                   'scoreboard players add @s mg.grk 5', 'execute if score @s mg.grk matches 16.. run scoreboard players set @s mg.grk 15'])
w('gta/rpg_fire', ['# @s tire une roquette (cadence 1,25 s)', 'scoreboard players reset @s mg.gqs',
                   'execute if score @s mg.gcd matches 1.. run return 0',
                   'execute unless score @s mg.grk matches 1.. run return run title @s actionbar {"text":"🚀 Plus de roquettes : trouve un point 🚀","color":"red"}',
                   'scoreboard players remove @s mg.grk 1', 'scoreboard players set @s mg.gcd 25',
                   'execute anchored eyes positioned ^-0.2 ^-0.1 ^1 run summon minecraft:item_display ~ ~ ~ {Tags:["mg.gta","mg.grkt","mg.grkn"],'
                   'item:{id:"minecraft:firework_rocket",count:1},teleport_duration:1,'
                   'transformation:{left_rotation:[0.5f,0.5f,-0.5f,0.5f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.4f,1.4f,1.4f]}}',
                   'execute anchored eyes positioned ^-0.2 ^-0.1 ^1 rotated as @s run tp @e[type=minecraft:item_display,tag=mg.grkn] ~ ~ ~ ~ ~',
                   'scoreboard players operation @e[type=minecraft:item_display,tag=mg.grkn] mg.bid = @s mg.bid',
                   'scoreboard players set @e[type=minecraft:item_display,tag=mg.grkn] mg.gpc 0',
                   'tag @e[tag=mg.grkn] remove mg.grkn',
                   'playsound minecraft:entity.firework_rocket.launch player @a ~ ~ ~ 1.5 0.6',
                   'playsound minecraft:entity.blaze.shoot player @a ~ ~ ~ 1 0.5',
                   'particle minecraft:cloud ~ ~1.4 ~ 0.2 0.2 0.2 0.05 10', 'scoreboard players set @s mg.gal 0'])
w('gta/rocket_tick', ['# @s : roquette en vol (âge mg.gpc, tireur mg.bid) : 3 pas de 0,7 bloc par tick',
                      'scoreboard players add @s mg.gpc 1',
                      'execute if score @s mg.gpc matches 60.. run return run function mg:gta/rocket_boom',
                      'execute at @s run function mg:gta/rocket_step', 'execute if entity @s at @s run function mg:gta/rocket_step',
                      'execute if entity @s at @s run function mg:gta/rocket_step',
                      'particle minecraft:flame ~ ~ ~ 0.05 0.05 0.05 0.02 3', 'particle minecraft:large_smoke ~ ~ ~ 0.1 0.1 0.1 0.01 2'])
w('gta/rocket_step', ['# Un pas de la roquette (@s, à sa position, orientée)',
                      'execute unless block ^ ^ ^0.7 #mg:ray_pass positioned ^ ^ ^0.4 run return run function mg:gta/rocket_boom',
                      'scoreboard players operation $bid mg.st = @s mg.bid',
                      'execute positioned ^ ^ ^0.7 positioned ~ ~-0.9 ~ as @e[tag=mg.gtg,distance=..1.3] unless score @s mg.bid = $bid mg.st run tag @s add mg.grhit',
                      'execute if entity @e[tag=mg.grhit] positioned ^ ^ ^0.7 run return run function mg:gta/rocket_boom',
                      'tp @s ^ ^ ^0.7'])
w('gta/rocket_boom', ['# La roquette explose ici : destruction (rayon 3), 16 dégâts dans un rayon de 4, dollars pour les dégâts matériels',
                      'tag @e[tag=mg.grhit] remove mg.grhit',
                      'scoreboard players operation $bid mg.st = @s mg.bid',
                      'function mg:bomber/boom/r3',
                      'execute as @a[tag=mg.gtw] if score @s mg.bid = $bid mg.st run tag @s add mg.gro',
                      'execute as @e[tag=mg.gtg,distance=..4] run damage @s 16 minecraft:player_explosion by @a[tag=mg.gro,limit=1]',
                      'scoreboard players operation $gm mg.st = $bk mg.st', 'scoreboard players set #5 mg.st 5', 'scoreboard players operation $gm mg.st /= #5 mg.st',
                      'scoreboard players operation @a[tag=mg.gro] mg.gta += $gm mg.st',
                      'tag @a remove mg.gro',
                      'particle minecraft:explosion_emitter ~ ~ ~ 0 0 0 0 1 force', 'particle minecraft:flame ~ ~ ~ 1.5 1.2 1.5 0.12 40 force',
                      'particle minecraft:large_smoke ~ ~ ~ 1.6 1.2 1.6 0.06 30 force',
                      'playsound minecraft:entity.generic.explode master @a ~ ~ ~ 5 0.8', 'kill @s'])


# ---------------------------------------------------------------- véhicules : morceaux de carrosserie (block_display liés par mg.gvid)
def DSP(kind, blk, tx, ty, tz, sx, sy, sz, body=False, extra=''):
    tags = f'"mg.gta","mg.gvd","mg.gvn","{kind}"' + (',"mg.gvb"' if body else '')
    return (f'summon minecraft:block_display ~ ~ ~ {{Tags:[{tags}],block_state:{{Name:"minecraft:{blk}"}},teleport_duration:1,'
            f'{TR % (tx, ty, tz, sx, sy, sz)}{extra}}}')


for (n, body, roof, name, spd) in CARS:
    def D(*a, **k): return DSP('mg.gcard', *a, **k)
    L = [f'# Voiture n° {n} : {name} (cheval invisible rapetissé : on est assis dans l\'habitacle)', 'scoreboard players add $gvid mg.st 1',
         'summon minecraft:horse ~ ~ ~ {Tags:["mg.gta","mg.gtg","mg.gcarh","mg.gvn","mg.npc"],Tame:1b,Silent:1b,PersistenceRequired:1b,Health:40f,'
         'equipment:{saddle:{id:"minecraft:saddle",count:1}},drop_chances:{saddle:0f},'
         f'CustomName:{js({"text": name, "color": "yellow"})},CustomNameVisible:0b,'
         'active_effects:[{id:"minecraft:invisibility",duration:-1,amplifier:0,show_particles:0b}],'
         f'attributes:[{{id:"minecraft:movement_speed",base:{spd}}},{{id:"minecraft:jump_strength",base:0.0}},{{id:"minecraft:step_height",base:1.1}},'
         '{id:"minecraft:max_health",base:40},{id:"minecraft:scale",base:0.55}]}',
         D(body, -0.95, 0.05, -1.7, 1.9, 0.75, 3.4, body=True),           # caisse
         D(roof, -0.8, 0.8, -0.9, 1.6, 0.65, 1.7),                         # habitacle
         D('black_concrete', -1.0, 0.0, -1.25, 0.25, 0.45, 0.6), D('black_concrete', 0.75, 0.0, -1.25, 0.25, 0.45, 0.6),   # roues
         D('black_concrete', -1.0, 0.0, 0.85, 0.25, 0.45, 0.6), D('black_concrete', 0.75, 0.0, 0.85, 0.25, 0.45, 0.6),
         D('sea_lantern', -0.8, 0.35, 1.68, 0.35, 0.2, 0.05), D('sea_lantern', 0.45, 0.35, 1.68, 0.35, 0.2, 0.05),       # phares
         D('redstone_block', -0.8, 0.35, -1.73, 0.35, 0.2, 0.05), D('redstone_block', 0.45, 0.35, -1.73, 0.35, 0.2, 0.05),
         D('light_gray_concrete', -0.9, 0.1, 1.7, 1.8, 0.15, 0.1)]                                                          # pare-chocs
    if 'Taxi' in name:
        L.append(D('yellow_concrete', -0.3, 1.45, -0.3, 0.6, 0.2, 0.6))
    if 'police' in name:
        L += [D('blue_stained_glass', -0.55, 1.45, -0.2, 0.5, 0.2, 0.4), D('red_stained_glass', 0.05, 1.45, -0.2, 0.5, 0.2, 0.4)]
    if n == 8:
        L.append(D(body, -0.95, 0.8, -1.7, 1.9, 0.9, 1.9))
    L += ['summon minecraft:interaction ~ ~ ~ {Tags:["mg.gta","mg.gcint","mg.gvn"],width:2.4f,height:1.7f,response:1b}', 'scoreboard players operation @e[tag=mg.gvn] mg.gvid = $gvid mg.st', 'tag @e[tag=mg.gvn] remove mg.gvn']
    w(f'gta/car/spawn_{n}', L)
w('gta/car_random', ['# Une voiture au hasard à ce carrefour (remplace une voiture détruite)',
                     f'execute store result score $gr mg.st run random value 1..{len(CARS)}'] +
  [f'execute if score $gr mg.st matches {n} positioned ~2 ~ ~ run function mg:gta/car/spawn_{n}' for (n, *_) in CARS])
w('gta/car_sync', ['# @s : cheval d\'une voiture. La carrosserie suit ; lancée (> 0,2 bloc/tick), elle renverse ce qu\'elle percute',
                   'scoreboard players operation $gv mg.st = @s mg.gvid',
                   'execute unless predicate mg:has_passenger as @e[type=minecraft:interaction,tag=mg.gcint] if score @s mg.gvid = $gv mg.st run function mg:gta/vd_follow',
                   'execute if predicate mg:has_passenger positioned ~ ~-6 ~ as @e[type=minecraft:interaction,tag=mg.gcint] if score @s mg.gvid = $gv mg.st run function mg:gta/vd_follow',
                   'execute store result score $gx mg.st run data get entity @s Pos[0] 100',
                   'execute store result score $gz mg.st run data get entity @s Pos[2] 100',
                   'scoreboard players operation $gdx mg.st = $gx mg.st', 'scoreboard players operation $gdx mg.st -= @s mg.gpx',
                   'scoreboard players operation $gdz mg.st = $gz mg.st', 'scoreboard players operation $gdz mg.st -= @s mg.gpz',
                   'scoreboard players operation @s mg.gpx = $gx mg.st', 'scoreboard players operation @s mg.gpz = $gz mg.st',
                   'scoreboard players operation $gdx mg.st *= $gdx mg.st', 'scoreboard players operation $gdz mg.st *= $gdz mg.st',
                   'scoreboard players operation $gdx mg.st += $gdz mg.st',
                   # carrosserie : légèrement en avance selon la vitesse (le conducteur voit son cheval bouger sans délai)
                   'execute unless score $gdx mg.st matches 100..100000 as @e[type=minecraft:block_display,tag=mg.gcard] if score @s mg.gvid = $gv mg.st run function mg:gta/vd_follow',
                   'execute if score $gdx mg.st matches 100..899 positioned ^ ^ ^0.3 as @e[type=minecraft:block_display,tag=mg.gcard] if score @s mg.gvid = $gv mg.st run function mg:gta/vd_follow',
                   'execute if score $gdx mg.st matches 900..1599 positioned ^ ^ ^0.6 as @e[type=minecraft:block_display,tag=mg.gcard] if score @s mg.gvid = $gv mg.st run function mg:gta/vd_follow',
                   'execute if score $gdx mg.st matches 1600..100000 positioned ^ ^ ^0.9 as @e[type=minecraft:block_display,tag=mg.gcard] if score @s mg.gvid = $gv mg.st run function mg:gta/vd_follow',
                   'execute if score $gdx mg.st matches 400..100000 on passengers run function mg:gta/car_ram',
                   'execute if score $gdx mg.st matches 400..100000 run particle minecraft:smoke ^ ^0.3 ^-1.8 0.1 0.05 0.1 0.01 1',
                   'execute if score $gdx mg.st matches 100..100000 if score $gq mg.st matches 0 run playsound minecraft:entity.minecart.riding neutral @a ~ ~ ~ 0.35 1.3',
                   'execute if score $gdx mg.st matches 100..100000 if score $gq mg.st matches 10 run playsound minecraft:entity.minecart.riding neutral @a ~ ~ ~ 0.35 1.3'])
w('gta/vd_follow', ['# @s : morceau de carrosserie, colle au véhicule (position et cap du contexte)', 'tp @s ~ ~ ~ ~ 0', 'tag @s add mg.gok'])
w('gta/car_int', ['# @s (zone cliquable d\'une voiture) : le joueur qui a cliqué monte au volant', 'scoreboard players operation $gv mg.st = @s mg.gvid',
                  'execute on target run function mg:gta/car_mount', 'data remove entity @s interaction', 'data remove entity @s attack'])
w('gta/car_mount', ['# @s (joueur) : monte dans la voiture $gv (si personne ne la conduit)',
                    'execute as @e[type=minecraft:horse,tag=mg.gcarh] if score @s mg.gvid = $gv mg.st run tag @s add mg.gmnt',
                    'ride @s mount @e[type=minecraft:horse,tag=mg.gmnt,limit=1]', 'tag @e remove mg.gmnt'])
w('gta/car_ram', ['# @s : conducteur d\'une voiture lancée : renverse (6 dégâts) ce qui est juste devant',
                  'tag @s add mg.grd',
                  'execute on vehicle rotated as @s positioned ^ ^ ^1.8 as @e[tag=mg.gtg,tag=!mg.grd,tag=!mg.gcarh,distance=..1.5] run damage @s 6 minecraft:player_attack by @a[tag=mg.grd,limit=1]',
                  'tag @s remove mg.grd'])
w('gta/wreck', ['# @s : caisse d\'un véhicule détruit (son cheval ou son ghast est mort) : explosion',
                'function mg:bomber/boom/r2',
                'execute as @e[tag=mg.gtg,distance=..3.5] run damage @s 8 minecraft:explosion',
                'particle minecraft:explosion_emitter ~ ~1 ~ 0 0 0 0 1 force', 'particle minecraft:flame ~ ~1 ~ 1.2 0.8 1.2 0.1 50 force',
                'particle minecraft:large_smoke ~ ~1.5 ~ 1 1 1 0.05 40 force', 'particle minecraft:lava ~ ~1 ~ 1 0.5 1 0 15 force',
                'playsound minecraft:entity.generic.explode master @a ~ ~ ~ 5 0.7'])

# hélicos : happy ghast invisible rapetissé (siège à ~2 blocs), modèle autour du pilote
SH = 2.0


def H(blk, tx, ty, tz, sx, sy, sz, body=False):
    return DSP('mg.ghbody', blk, tx, SH + ty, tz, sx, sy, sz, body=body)


HELI = ['# Hélico : happy ghast invisible et rapetissé, carrosserie de couleur $(c), rotors qui tournent', 'scoreboard players add $gvid mg.st 1',
        'summon minecraft:happy_ghast ~ ~ ~ {Tags:["mg.gta","mg.gtg","mg.ghel","mg.gvn","mg.npc"],PersistenceRequired:1b,Health:60f,'
        'equipment:{body:{id:"minecraft:black_harness",count:1}},drop_chances:{body:0f},'
        f'CustomName:{js({"text": "🚁 Hélico", "color": "aqua", "bold": True})},CustomNameVisible:0b,'
        'active_effects:[{id:"minecraft:invisibility",duration:-1,amplifier:0,show_particles:0b}],'
        'attributes:[{id:"minecraft:flying_speed",base:0.12},{id:"minecraft:movement_speed",base:0.12},{id:"minecraft:max_health",base:60},{id:"minecraft:scale",base:0.5}]}']
HELI += ['$' + H('$(c)', -0.9, -0.6, -1.4, 1.8, 1.5, 2.8, body=True),                       # fuselage
         H('light_blue_stained_glass', -0.8, -0.5, 1.4, 1.6, 1.25, 0.9),                    # cockpit
         '$' + H('$(c)', -0.7, 0.75, 1.0, 1.4, 0.15, 0.8),                                    # toit avant
         '$' + H('$(c)', -0.2, 0.1, -5.2, 0.4, 0.4, 3.8),                                     # poutre de queue
         '$' + H('$(c)', -0.06, 0.3, -5.3, 0.12, 1.1, 0.6),                                   # dérive
         H('gray_concrete', 0.1, 0.35, -5.35, 0.06, 1.0, 0.22), H('gray_concrete', 0.1, 0.74, -5.74, 0.06, 0.22, 1.0),   # rotor de queue
         H('gray_concrete', -1.0, -1.25, -1.3, 0.12, 0.12, 3.0), H('gray_concrete', 0.88, -1.25, -1.3, 0.12, 0.12, 3.0),  # patins
         H('gray_concrete', -0.95, -1.15, -0.8, 0.08, 0.55, 0.08), H('gray_concrete', 0.87, -1.15, -0.8, 0.08, 0.55, 0.08),
         H('gray_concrete', -0.95, -1.15, 0.8, 0.08, 0.55, 0.08), H('gray_concrete', 0.87, -1.15, 0.8, 0.08, 0.55, 0.08),
         H('gray_concrete', -0.1, 0.9, -0.1, 0.2, 0.4, 0.2),                                # mât
         H('sea_lantern', -0.1, -0.7, 1.6, 0.2, 0.1, 0.2),                                  # phare
         DSP('mg.ghrot', 'black_concrete', -4.5, SH + 1.3, -0.15, 9, 0.08, 0.3),            # pales du rotor principal
         DSP('mg.ghrot', 'black_concrete', -0.15, SH + 1.3, -4.5, 0.3, 0.08, 9),
         DSP('mg.ghrot', 'gray_concrete', -0.3, SH + 1.25, -0.3, 0.6, 0.2, 0.6),
         'scoreboard players operation @e[tag=mg.gvn] mg.gvid = $gvid mg.st', 'tag @e[tag=mg.gvn] remove mg.gvn']
w('gta/heli_spawn', HELI)
w('gta/heli_random', ['# Un hélico de remplacement sur une des hélisurfaces (contexte : dimension mg:gta)',
                      f'execute store result score $gr mg.st run random value 0..{len(HELI_AT) - 1}'] +
  [f'execute if score $gr mg.st matches {i} in {DIM} positioned {x} 66 {Z + z} unless entity @e[type=minecraft:happy_ghast,tag=mg.ghel,distance=..6] '
   f'run function mg:gta/heli_spawn {{c:"{col}"}}' for i, (x, z, col) in enumerate(HELI_AT)])
w('gta/heli_sync', ['# @s : hélico. La carrosserie suit, les rotors tournent (plus vite avec un pilote)',
                    'scoreboard players operation $gv mg.st = @s mg.gvid',
                    'execute on passengers run tag @s add mg.gpil',
                    'execute as @e[type=minecraft:block_display,tag=mg.ghbody] if score @s mg.gvid = $gv mg.st run function mg:gta/vd_follow',
                    'execute if entity @a[tag=mg.gpil] as @e[type=minecraft:block_display,tag=mg.ghrot] if score @s mg.gvid = $gv mg.st rotated as @s run function mg:gta/rotor_fast',
                    'execute unless entity @a[tag=mg.gpil] as @e[type=minecraft:block_display,tag=mg.ghrot] if score @s mg.gvid = $gv mg.st rotated as @s run function mg:gta/rotor_slow',
                    'execute if entity @a[tag=mg.gpil] run particle minecraft:cloud ~ ~-0.3 ~ 1.5 0.1 1.5 0.02 2',
                    'execute if entity @a[tag=mg.gpil] if score $gq mg.st matches 0 run playsound minecraft:entity.bee.loop neutral @a ~ ~ ~ 1.2 0.5',
                    'execute if entity @a[tag=mg.gpil] if score $gq mg.st matches 10 run playsound minecraft:entity.bee.loop neutral @a ~ ~ ~ 1.2 0.5',
                    'tag @a remove mg.gpil'])
w('gta/rotor_fast', ['tp @s ~ ~ ~ ~45 0', 'tag @s add mg.gok'])
w('gta/rotor_slow', ['tp @s ~ ~ ~ ~6 0', 'tag @s add mg.gok'])

# ---------------------------------------------------------------- liasses de billets, interface
w('gta/cash_new', ['# Une liasse de billets ici, montant $gcv (score mg.gpc de l\'objet)',
                   'execute if score $rp mg.st matches 1 run summon minecraft:item_display ~ ~ ~ {Tags:["mg.gta","mg.gcash","mg.gcnew","mg.gbill"],'
                   'item:{id:"minecraft:paper",count:1,components:{"minecraft:item_model":"mg:cash"}},teleport_duration:1,billboard:"vertical",'
                   f'Glowing:1b,glow_color_override:5635925,{TR % (0, 0, 0, 0.9, 0.9, 0.9)}}}',
                   'execute unless score $rp mg.st matches 1 run summon minecraft:item_display ~ ~ ~ {Tags:["mg.gta","mg.gcash","mg.gcnew"],'
                   f'item:{{id:"minecraft:emerald_block",count:1}},teleport_duration:1,Glowing:1b,glow_color_override:5635925,{TR % (0, 0, 0, 0.6, 0.45, 0.6)}}}',
                   'scoreboard players operation @e[type=minecraft:item_display,tag=mg.gcnew] mg.gpc = $gcv mg.st',
                   'tag @e[tag=mg.gcnew] remove mg.gcnew',
                   'particle minecraft:happy_villager ~ ~0.3 ~ 0.4 0.4 0.4 0 10'])
w('gta/cash_spawn', ['# Une valise de billets (+75 $) sur ce trottoir', 'scoreboard players set $gcv mg.st 75',
                     'execute positioned ~ ~0.8 ~ run function mg:gta/cash_new',
                     'tellraw @a[tag=mg.gtw] {"text":"💰 Une valise de billets est apparue quelque part en ville !","color":"green"}'])
w('gta/cash_take', ['# @s : liasse ramassée par le joueur le plus proche (montant mg.gpc)', 'scoreboard players operation $gcv mg.st = @s mg.gpc',
                    'execute as @p[tag=mg.gtw] run function mg:gta/cash_gain',
                    'execute at @s run playsound minecraft:entity.player.levelup player @a ~ ~ ~ 0.8 1.4', 'kill @s'])
w('gta/cash_gain', ['# @s ramasse $gcv dollars', 'scoreboard players operation @s mg.gta += $gcv mg.st', 'scoreboard players set @s mg.gal 40',
                    'title @s actionbar [{"text":"+","color":"green","bold":true},{"score":{"name":"$gcv","objective":"mg.st"},"color":"green","bold":true},'
                    '{"text":" $ ","color":"green","bold":true},{"text":"billets ramassés","color":"gray"}]'])
MONEY_RP = [{'text': '$', 'font': 'mg:gta_cash'}, {'score': {'name': '@s', 'objective': 'mg.gta'}, 'font': 'mg:gta_cash'}]
MONEY_PL = [{'text': '$ ', 'color': 'green', 'bold': True}, {'score': {'name': '@s', 'objective': 'mg.gta'}, 'color': 'green', 'bold': True}]
GAP = {'text': '      ', 'color': 'gray'}


def hud_lines(money):
    L = []
    for n, g in G.GUNS.items():
        L.append(f'execute if items entity @s weapon.mainhand *[custom_data~{{gun:{n}}}] unless score @s mg.grl matches 1.. run return run title @s actionbar ' +
                 js([{'text': '🔫 ' + g[0] + '  ', 'color': g[8]}, {'score': {'name': '@s', 'objective': f'mg.g{n}'}, 'color': 'white', 'bold': True},
                     {'text': f' / {2 * g[4]}', 'color': 'gray'}, GAP] + money))
    L.append('execute if score @s mg.grl matches 1.. run return run title @s actionbar ' + js([{'text': '⟳ Rechargement…', 'color': 'yellow'}, GAP] + money))
    L.append('execute if items entity @s weapon.mainhand *[custom_data~{rpg:1b}] run return run title @s actionbar ' +
             js([{'text': '🚀 Roquettes  ', 'color': 'red'}, {'score': {'name': '@s', 'objective': 'mg.grk'}, 'color': 'white', 'bold': True}, GAP] + money))
    L.append('title @s actionbar ' + js(money))
    return L


w('gta/hud', ['# Toutes les 0,5 s : munitions et dollars (sauf pendant un message)',
              'execute as @a[tag=mg.gtw,scores={mg.gal=..0}] run function mg:gta/hud_one'])
w('gta/hud_one', ['# @s : barre d\'action (police verte du pack si $rp = 1) ; mission en cours en priorité',
                  'execute if score @s mg.gmt matches 1.. run return run function mg:gta/mis_hud',
                  'execute if score $rp mg.st matches 1 run return run function mg:gta/hud_rp',
                  'function mg:gta/hud_plain'])
w('gta/hud_rp', ['# @s : munitions + dollars en chiffres GTA ; sans arme : mini-carte + dollars'] + hud_lines(MONEY_RP)[:-1] + ['function mg:gta/mini_show'])
w('gta/mini_show', ['# @s : mini-carte (case 30 × 30 de sa position) au-dessus des dollars',
                    'execute store result score $gmi mg.st run data get entity @s Pos[0]', 'execute store result score $gmj mg.st run data get entity @s Pos[2]',
                    f'scoreboard players add $gmi mg.st {HX}', f'scoreboard players remove $gmj mg.st {Z - HX}',
                    'scoreboard players set #30 mg.st 30', 'scoreboard players set #177 mg.st 177',
                    'scoreboard players operation $gmi mg.st *= #30 mg.st', 'scoreboard players operation $gmi mg.st /= #177 mg.st',
                    'scoreboard players operation $gmj mg.st *= #30 mg.st', 'scoreboard players operation $gmj mg.st /= #177 mg.st',
                    'execute if score $gmi mg.st matches ..-1 run scoreboard players set $gmi mg.st 0', 'execute if score $gmi mg.st matches 30.. run scoreboard players set $gmi mg.st 29',
                    'execute if score $gmj mg.st matches ..-1 run scoreboard players set $gmj mg.st 0', 'execute if score $gmj mg.st matches 30.. run scoreboard players set $gmj mg.st 29'] +
  [f'execute if score $gmj mg.st matches {j} run return run function mg:gta/mini/row_{j}' for j in range(30)])
for j in range(30):
    w(f'gta/mini/row_{j}', [f'# Mini-carte, ligne {j}'] +
      [f'execute if score $gmi mg.st matches {i} run return run title @s actionbar ' +
       js([{'text': '\ue600\ue601', 'font': 'mg:gta_mini', 'color': 'white', 'shadow_color': 0},
           {'text': chr(0xE700 + 30 * j + i), 'font': 'mg:gta_mini', 'color': '#FF2A2A', 'shadow_color': 0}, {'text': '   '}] + MONEY_RP)
       for i in range(30)])
w('gta/hud_plain', ['# @s : munitions + dollars (sans pack)'] + hud_lines(MONEY_PL))

# ---------------------------------------------------------------- braquages
def bar(fn, label, col, need):
    L = [f'# @s : jauge de braquage ({label}), mg.grob sur {need}', 'scoreboard players set @s mg.gal 10',
         'scoreboard players operation $gbp mg.st = @s mg.grob', 'scoreboard players set #10 mg.st 10', 'scoreboard players operation $gbp mg.st *= #10 mg.st',
         f'scoreboard players set $gbn mg.st {need}', 'scoreboard players operation $gbp mg.st /= $gbn mg.st']
    for k in range(11):
        L.append(f'execute if score $gbp mg.st matches {k} run title @s actionbar ' + js([{'text': f'💰 {label}  ', 'color': col, 'bold': True},
                                                                                          {'text': '▮' * k, 'color': 'green'}, {'text': '▯' * (10 - k), 'color': 'dark_gray'}]))
    w(f'gta/{fn}', L)


bar('rob_bar_ped', 'Braquage du passant', 'yellow', 40)
bar('rob_bar_shop', 'Caisse du commerce', 'gold', 100)
bar('rob_bar_bank', 'Coffres de la banque', 'red', 300)
w('gta/rob', ['# @s (accroupi, arme en main) : banque, sinon commerce, sinon passant visé (6 blocs)',
              'execute if entity @e[type=minecraft:marker,tag=mg.gbank,distance=..3.5,scores={mg.gpc=..0}] run return run function mg:gta/rob_bank',
              'execute if entity @e[type=minecraft:marker,tag=mg.gshop,distance=..2.6,scores={mg.gpc=..0}] run return run function mg:gta/rob_shop',
              'tag @e[tag=mg.grt] remove mg.grt', 'scoreboard players set $gar mg.st 7', 'tag @s add mg.gaim',
              'execute anchored eyes positioned ^ ^ ^1 run function mg:gta/rob_ray', 'tag @s remove mg.gaim',
              'execute if entity @e[tag=mg.grt] run return run function mg:gta/rob_ped',
              'function mg:gta/rob_stop'])
w('gta/rob_ray', ['# Un pas (1 bloc) vers le passant visé',
                  'execute unless block ~ ~ ~ #mg:ray_pass run return 0',
                  'execute positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=minecraft:villager,tag=mg.gped,tag=!mg.grobbed,dx=0,dy=0,dz=0,limit=1] run return run tag @s add mg.grt',
                  'scoreboard players remove $gar mg.st 1',
                  'execute if score $gar mg.st matches 1.. positioned ^ ^ ^1 run function mg:gta/rob_ray'])
w('gta/rob_stop', ['# @s arrête de braquer', 'execute if score @s mg.grob matches 15.. run title @s actionbar {"text":"✋ Braquage interrompu","color":"gray"}',
                   'scoreboard players set @s mg.grob 0'])
w('gta/rob_ped', ['# @s braque le passant visé (mg.grt) : 2 s', 'effect give @e[tag=mg.grt] minecraft:slowness 1 6 true',
                  'execute as @e[tag=mg.grt] at @s run particle minecraft:angry_villager ~ ~2.2 ~ 0.2 0.1 0.2 0 1',
                  'scoreboard players add @s mg.grob 5', 'function mg:gta/rob_bar_ped',
                  'execute if score @s mg.grob matches 40.. run function mg:gta/rob_ped_ok', 'tag @e[tag=mg.grt] remove mg.grt'])
w('gta/rob_ped_ok', ['# Passant dépouillé : 20 à 80 $, il s\'enfuit ; un témoin peut prévenir la police', 'scoreboard players set @s mg.grob 0',
                     'execute store result score $gcv mg.st run random value 20..80', 'function mg:gta/cash_gain',
                     'tag @e[tag=mg.grt] add mg.grobbed', 'effect give @e[tag=mg.grt] minecraft:speed 15 2 true',
                     'execute as @e[tag=mg.grt] at @s run particle minecraft:happy_villager ~ ~1 ~ 0.3 0.5 0.3 0 8',
                     'execute as @e[tag=mg.grt] at @s run playsound minecraft:entity.villager.hurt neutral @a ~ ~ ~ 1 1.3',
                     'execute store result score $gr mg.st run random value 0..2', 'execute if score $gr mg.st matches 0 run function mg:gta/wanted_up'])
w('gta/lift_up', ['# Ascenseur du manoir : vers le toit-terrasse', f'tp @s {LIFT[0] - 1}.5 {NH["lift_y"][1]} {Z + LIFT[1] + 2}.5', 'playsound minecraft:block.beacon.activate player @s ~ ~ ~ 0.5 2'])
w('gta/lift_down', ['# Ascenseur du manoir : vers le hall', f'tp @s {LIFT[0] - 1}.5 {NH["lift_y"][0]} {Z + LIFT[1] + 2}.5', 'playsound minecraft:block.beacon.deactivate player @s ~ ~ ~ 0.5 2'])
w('gta/rob_shop', ['# @s braque la caisse du commerce : 5 s, alarme ; le caissier lève les mains', 'scoreboard players add @s mg.grob 5', 'function mg:gta/rob_bar_shop',
                   'execute as @e[type=minecraft:villager,tag=mg.gclerk,distance=..5] at @s run particle minecraft:angry_villager ~ ~2.3 ~ 0.2 0.1 0.2 0 1',
                   'execute if score @s mg.grob matches 10 as @e[type=minecraft:villager,tag=mg.gclerk,distance=..5] at @s run playsound minecraft:entity.villager.hurt neutral @a ~ ~ ~ 1 1.4',
                   'execute if score @s mg.grob matches 5 run playsound minecraft:block.bell.use master @a ~ ~ ~ 2 1.2',
                   'execute if score @s mg.grob matches 50 run playsound minecraft:block.bell.use master @a ~ ~ ~ 2 1.2',
                   'execute if score @s mg.grob matches 100.. run function mg:gta/rob_shop_ok'])
w('gta/rob_shop_ok', ['# Caisse vidée : 200 à 450 $, deux étoiles, commerce fermé 3 min', 'scoreboard players set @s mg.grob 0',
                      'execute store result score $gcv mg.st run random value 200..450', 'function mg:gta/cash_gain',
                      'execute as @e[type=minecraft:marker,tag=mg.gshop,distance=..2.6,limit=1,sort=nearest] run function mg:gta/shop_close',
                      'function mg:gta/wanted_up', 'function mg:gta/wanted_up',
                      'title @s title {"text":" ","color":"gold"}', 'title @s subtitle {"text":"💰 Caisse vidée !","color":"gold","bold":true}'])
w('gta/shop_close', ['# @s (caisse) : fermé 3 min', 'scoreboard players set @s mg.gpc 3600', 'scoreboard players operation $gs mg.st = @s mg.gsid',
                     'execute as @e[type=minecraft:text_display,tag=mg.gshl] if score @s mg.gsid = $gs mg.st run data merge entity @s {text:{"text":"🔒 Fermé (braquage)","color":"red","bold":true}}'])
SR = ['# @s (caisse) : le commerce rouvre', 'scoreboard players operation $gs mg.st = @s mg.gsid']
for k, (mx, sz, nm, col) in enumerate(CITY['shops']):
    SR.append(f'execute if score $gs mg.st matches {k} as @e[type=minecraft:text_display,tag=mg.gshl] if score @s mg.gsid matches {k} run data merge entity @s {{text:{js(shop_label(nm))}}}')
w('gta/shop_reopen', SR)
w('gta/rob_bank', ['# @s braque la banque : 15 s dans la salle des coffres, alarme, 4 étoiles d\'un coup', 'scoreboard players add @s mg.grob 5', 'function mg:gta/rob_bar_bank',
                   'execute if score @s mg.grob matches 5 run tellraw @a[tag=mg.gtw] [{"text":"🚨 ","color":"red"},{"selector":"@s","color":"yellow"},{"text":" braque la banque de Neo City !","color":"red","bold":true}]',
                   'execute if score @s mg.grob matches 5 if score @s mg.gwl matches ..3 run scoreboard players set @s mg.gwl 4',
                   'execute if score @s mg.grob matches 5 run scoreboard players set @s mg.gwt 300', 'execute if score @s mg.grob matches 5 run team leave @s',
                   'scoreboard players operation $gbk mg.st = @s mg.grob', 'scoreboard players set #20 mg.st 20', 'scoreboard players operation $gbk mg.st %= #20 mg.st',
                   'execute if score $gbk mg.st matches 5 run playsound minecraft:block.bell.use master @a ~ ~ ~ 4 0.8',
                   'execute if score $gbk mg.st matches 15 run playsound minecraft:block.bell.use master @a ~ ~ ~ 4 1.1',
                   'execute if score @s mg.grob matches 300.. run function mg:gta/rob_bank_ok'])
w('gta/rob_bank_ok', ['# Coffres vidés : 1 500 à 2 500 $, banque fermée 7 min', 'scoreboard players set @s mg.grob 0',
                      'execute store result score $gcv mg.st run random value 1500..2500', 'function mg:gta/cash_gain',
                      'scoreboard players set @e[type=minecraft:marker,tag=mg.gbank] mg.gpc 8400',
                      'execute as @e[type=minecraft:text_display,tag=mg.gbkl] run data merge entity @s {text:{"text":"🔒 Coffres vides","color":"red","bold":true}}',
                      'function mg:gta/wanted_up',
                      'title @s title {"text":"💰 JACKPOT","color":"gold","bold":true}',
                      'tellraw @a[tag=mg.gtw] [{"text":"💰 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a vidé les coffres de la banque : ","color":"gold"},'
                      '{"score":{"name":"$gcv","objective":"mg.st"},"color":"green","bold":true},{"text":" $ !","color":"gold"}]',
                      'execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 1 1'])
w('gta/bank_reopen', ['# Les coffres sont de nouveau pleins',
                      'execute as @e[type=minecraft:text_display,tag=mg.gbkl] run data merge entity @s {text:' + js({"text": "💰 Coffres : accroupi + arme pendant 15 s", "color": "gold"}) + '}',
                      'tellraw @a[tag=mg.gtw] {"text":"🏦 Les coffres de la banque sont de nouveau pleins…","color":"gold"}'])

# ---------------------------------------------------------------- véhicules achetés (un par joueur : l'ancien disparaît)
w('gta/veh_buy', ['# @s achète un véhicule de type $(t) : l\'ancien disparaît, le nouveau est livré',
                  'scoreboard players operation $gv mg.st = @s mg.gveh',
                  'execute if score @s mg.gveh matches 1.. as @e[tag=mg.gta] if score @s mg.gvid = $gv mg.st run kill @s',
                  '$function mg:gta/veh_$(t)',
                  'scoreboard players operation @s mg.gveh = $gvid mg.st',
                  'title @s title {"text":"🔑","color":"gold"}', 'title @s subtitle {"text":"Ton véhicule t\'attend dehors !","color":"yellow"}'])
for (t, n, k) in (('moto', 11, 0), ('muscle', 12, 1), ('supercar', 13, 2)):
    cx, cz = NH['car_drop'][k]
    w(f'gta/veh_{t}', [f'execute if score $gvilla mg.st matches 1 in {DIM} positioned {cx} {VY} {Z + cz} run return run function mg:gta/car/spawn_{n}',
                       f'execute in {DIM} positioned {CAR_DROP[0] + 4 * k - 4} 65 {Z + CAR_DROP[1]} run function mg:gta/car/spawn_{n}'])
w('gta/veh_heli', [f'execute if score $gvilla mg.st matches 1 in {DIM} positioned {NH["heli"][0]} {VY} {Z + NH["heli"][1]} run return run function mg:gta/heli_spawn {{c:"yellow_concrete"}}',
                   f'execute in {DIM} positioned {AIRF[0] - 4} 66 {Z + AIRF[1]} run function mg:gta/heli_spawn {{c:"yellow_concrete"}}'])
w('gta/veh_plane', [f'execute if score $gvilla mg.st matches 1 in {DIM} positioned {NH["plane"][0]} {VY} {Z + NH["plane"][1]} run return run function mg:gta/plane_spawn',
                    f'execute in {DIM} positioned {AIRF[0] + 4} 66 {Z + AIRF[1]} run function mg:gta/plane_spawn'])
BUY_CARS = [  # n°, carrosserie, toit, nom, vitesse, échelle du cheval, modèle
    (11, 'red_concrete', 'black_concrete', '🏍 Moto', 0.46, 0.45, 'moto'),
    (12, 'red_concrete', 'black_concrete', '🚗 Muscle car', 0.44, 0.55, 'muscle'),
    (13, 'purple_concrete', 'black_stained_glass', '🏎 Supercar', 0.52, 0.5, 'super')]
for (n, body, roof, name, spd, sc, kind) in BUY_CARS:
    def D(*a, **k): return DSP('mg.gcard', *a, **k)
    L = [f'# Véhicule acheté n° {n} : {name}', 'scoreboard players add $gvid mg.st 1',
         'summon minecraft:horse ~ ~ ~ {Tags:["mg.gta","mg.gtg","mg.gcarh","mg.gvn","mg.npc"],Tame:1b,Silent:1b,PersistenceRequired:1b,Health:40f,'
         'equipment:{saddle:{id:"minecraft:saddle",count:1}},drop_chances:{saddle:0f},'
         f'CustomName:{js({"text": name, "color": "gold"})},CustomNameVisible:0b,'
         'active_effects:[{id:"minecraft:invisibility",duration:-1,amplifier:0,show_particles:0b}],'
         f'attributes:[{{id:"minecraft:movement_speed",base:{spd}}},{{id:"minecraft:jump_strength",base:0.0}},{{id:"minecraft:step_height",base:1.1}},'
         f'{{id:"minecraft:max_health",base:40}},{{id:"minecraft:scale",base:{sc}}}]}}']
    if kind == 'moto':
        L += [D('black_concrete', -0.12, 0.0, 0.55, 0.24, 0.6, 0.6), D('black_concrete', -0.12, 0.0, -0.95, 0.24, 0.6, 0.6),   # roues
              D(body, -0.2, 0.45, -0.7, 0.4, 0.3, 1.4, body=True), D('gray_concrete', -0.15, 0.3, -0.6, 0.3, 0.2, 1.2),          # réservoir, cadre
              D('black_concrete', -0.2, 0.7, -0.75, 0.4, 0.08, 0.6), D('gray_concrete', -0.4, 0.95, 0.55, 0.8, 0.06, 0.06),     # selle, guidon
              D('sea_lantern', -0.1, 0.65, 0.75, 0.2, 0.15, 0.05), D('redstone_block', -0.08, 0.6, -0.97, 0.16, 0.1, 0.04)]
    elif kind == 'muscle':
        L += [D(body, -0.95, 0.05, -1.8, 1.9, 0.7, 3.6, body=True), D(roof, -0.8, 0.75, -1.0, 1.6, 0.55, 1.5),
              D('white_concrete', -0.25, 0.76, -1.8, 0.18, 0.01, 3.6), D('white_concrete', 0.07, 0.76, -1.8, 0.18, 0.01, 3.6),        # bandes de course
              D('gray_concrete', -0.3, 0.75, 0.6, 0.6, 0.15, 0.6),                                                                  # prise d'air
              D('black_concrete', -1.0, 0.0, -1.3, 0.25, 0.5, 0.65), D('black_concrete', 0.75, 0.0, -1.3, 0.25, 0.5, 0.65),
              D('black_concrete', -1.0, 0.0, 0.9, 0.25, 0.5, 0.65), D('black_concrete', 0.75, 0.0, 0.9, 0.25, 0.5, 0.65),
              D('sea_lantern', -0.8, 0.35, 1.78, 0.35, 0.2, 0.05), D('sea_lantern', 0.45, 0.35, 1.78, 0.35, 0.2, 0.05),
              D('redstone_block', -0.8, 0.35, -1.83, 0.35, 0.2, 0.05), D('redstone_block', 0.45, 0.35, -1.83, 0.35, 0.2, 0.05)]
    else:
        L += [D(body, -1.0, 0.05, -1.9, 2.0, 0.5, 3.8, body=True), D(roof, -0.75, 0.55, -0.9, 1.5, 0.45, 1.5),
              D(body, -0.95, 0.85, -1.95, 1.9, 0.08, 0.45), D('black_concrete', -0.85, 0.55, -1.85, 0.08, 0.3, 0.08),                 # aileron
              D('black_concrete', 0.77, 0.55, -1.85, 0.08, 0.3, 0.08),
              D('black_concrete', -1.05, 0.0, -1.35, 0.25, 0.45, 0.65), D('black_concrete', 0.8, 0.0, -1.35, 0.25, 0.45, 0.65),
              D('black_concrete', -1.05, 0.0, 0.95, 0.25, 0.45, 0.65), D('black_concrete', 0.8, 0.0, 0.95, 0.25, 0.45, 0.65),
              D('sea_lantern', -0.85, 0.25, 1.88, 0.4, 0.12, 0.05), D('sea_lantern', 0.45, 0.25, 1.88, 0.4, 0.12, 0.05),
              D('redstone_block', -0.9, 0.3, -1.93, 1.8, 0.08, 0.04)]
    L += ['summon minecraft:interaction ~ ~ ~ {Tags:["mg.gta","mg.gcint","mg.gvn"],width:2.4f,height:1.7f,response:1b}', 'scoreboard players operation @e[tag=mg.gvn] mg.gvid = $gvid mg.st', 'tag @e[tag=mg.gvn] remove mg.gvn']
    w(f'gta/car/spawn_{n}', L)
PL = ['# Avion : happy ghast invisible et rapetissé, très rapide, fuselage, ailes et dérive', 'scoreboard players add $gvid mg.st 1',
      'summon minecraft:happy_ghast ~ ~ ~ {Tags:["mg.gta","mg.gtg","mg.ghel","mg.gvn","mg.npc"],PersistenceRequired:1b,Health:60f,'
      'equipment:{body:{id:"minecraft:white_harness",count:1}},drop_chances:{body:0f},'
      f'CustomName:{js({"text": "✈ Avion", "color": "aqua", "bold": True})},CustomNameVisible:0b,'
      'active_effects:[{id:"minecraft:invisibility",duration:-1,amplifier:0,show_particles:0b}],'
      'attributes:[{id:"minecraft:flying_speed",base:0.24},{id:"minecraft:movement_speed",base:0.2},{id:"minecraft:max_health",base:60},{id:"minecraft:scale",base:0.5}]}',
      H('white_concrete', -0.6, -0.5, -3.0, 1.2, 1.1, 5.4, body=True), H('red_concrete', -0.45, -0.4, 2.4, 0.9, 0.8, 0.7),       # fuselage, nez
      H('light_blue_stained_glass', -0.5, 0.55, 0.6, 1.0, 0.45, 1.2),                                                            # verrière
      H('red_concrete', -4.6, -0.15, -0.5, 9.2, 0.12, 1.3), H('white_concrete', -4.6, -0.05, -0.5, 0.6, 0.12, 1.3),              # ailes
      H('white_concrete', 4.0, -0.05, -0.5, 0.6, 0.12, 1.3),
      H('red_concrete', -1.7, 0.1, -3.0, 3.4, 0.1, 0.8), H('red_concrete', -0.06, 0.1, -3.1, 0.12, 1.3, 0.9),                    # empennage
      H('black_concrete', -0.05, -0.75, 2.95, 0.1, 1.5, 0.08), H('black_concrete', -0.75, -0.05, 2.95, 1.5, 0.1, 0.08),          # hélice
      H('gray_concrete', -0.6, -1.3, 0.8, 0.1, 0.6, 0.1), H('gray_concrete', 0.5, -1.3, 0.8, 0.1, 0.6, 0.1),                     # train
      H('black_concrete', -0.7, -1.45, 0.65, 0.3, 0.3, 0.4), H('black_concrete', 0.4, -1.45, 0.65, 0.3, 0.3, 0.4),
      'scoreboard players operation @e[tag=mg.gvn] mg.gvid = $gvid mg.st', 'tag @e[tag=mg.gvn] remove mg.gvn']
w('gta/plane_spawn', PL)

# ---------------------------------------------------------------- carte (police mg:gta_map) : plan + point « tu es ici » sur une grille 30 × 30
CELL = ['scoreboard players set #30 mg.st 30', 'scoreboard players set #177 mg.st 177']


def cell(src, si, sj):
    """Case 30 × 30 de la position de src (sélecteur) → scores si / sj, bornés."""
    return [f'execute store result score {si} mg.st run data get entity {src} Pos[0]', f'execute store result score {sj} mg.st run data get entity {src} Pos[2]',
            f'scoreboard players add {si} mg.st {HX}', f'scoreboard players remove {sj} mg.st {Z - HX}',
            f'scoreboard players operation {si} mg.st *= #30 mg.st', f'scoreboard players operation {si} mg.st /= #177 mg.st',
            f'scoreboard players operation {sj} mg.st *= #30 mg.st', f'scoreboard players operation {sj} mg.st /= #177 mg.st',
            f'execute if score {si} mg.st matches ..-1 run scoreboard players set {si} mg.st 0', f'execute if score {si} mg.st matches 30.. run scoreboard players set {si} mg.st 29',
            f'execute if score {sj} mg.st matches ..-1 run scoreboard players set {sj} mg.st 0', f'execute if score {sj} mg.st matches 30.. run scoreboard players set {sj} mg.st 29',
            f'scoreboard players operation {sj} mg.st *= #30 mg.st', f'scoreboard players operation {sj} mg.st += {si} mg.st']


w('gta/dots_init', ['# Les 900 points de la carte (police mg:gta_map), indexés ligne × 30 + colonne',
                    'data modify storage mg:gta dots set value ' + js([chr(0xE500 + k) for k in range(900)])])
w('gta/map_show', ['# @s tient la carte : plan de la ville, sa position (rouge), l\'objectif de sa mission (or)',
                   'execute unless score $rp mg.st matches 1 run return run title @s actionbar [{"text":"🗺 Carte : active le resource pack (/function mg:rp_on)","color":"gray"}]',
                   'execute unless data storage mg:gta dots run function mg:gta/dots_init'] + CELL + cell('@s', '$gmi', '$gmj') +
  ['execute store result storage mg:gta mi.p int 1 run scoreboard players get $gmj mg.st',
   'function mg:gta/map_pick_p with storage mg:gta mi',
   'data modify storage mg:gta mp.t set value "\ue402"',
   'scoreboard players operation $gb mg.st = @s mg.bid', 'tag @e remove mg.gmine',
   'execute as @e[tag=mg.gmo] if score @s mg.bid = $gb mg.st run tag @s add mg.gmine',
   'execute if entity @e[tag=mg.gmine] run function mg:gta/map_target',
   'title @s times 0 6 2', 'scoreboard players set @s mg.gal 6',
   'title @s actionbar [{"text":"● ","color":"red"},{"text":"toi  ","color":"gray"},{"text":"● ","color":"gold"},{"text":"mission  ","color":"gray"},'
   '{"text":"■ ","color":"#9646C8"},{"text":"concession ","color":"gray"},{"text":"■ ","color":"#C82828"},{"text":"armurerie ","color":"gray"},'
   '{"text":"■ ","color":"#E8BA24"},{"text":"banque ","color":"gray"},{"text":"■ ","color":"#F58C1E"},{"text":"commerces","color":"gray"}]',
   'function mg:gta/map_title with storage mg:gta mp'])
w('gta/map_target', ['# Case de l\'objectif de la mission (@e[tag=mg.gmine])'] + cell('@e[tag=mg.gmine,limit=1]', '$gti', '$gtj') +
  ['execute store result storage mg:gta mi.t int 1 run scoreboard players get $gtj mg.st', 'function mg:gta/map_pick_t with storage mg:gta mi'])
w('gta/map_pick_p', ['$data modify storage mg:gta mp.p set from storage mg:gta dots[$(p)]'])
w('gta/map_pick_t', ['$data modify storage mg:gta mp.t set from storage mg:gta dots[$(t)]'])
w('gta/map_title', ['# Titre : plan, puis (retour au bord gauche) le point rouge, puis l\'objectif doré (ou un espace de même largeur)',
                    '$title @s title [{"text":"\ue400\ue401","font":"mg:gta_map","color":"white","shadow_color":0},{"text":"$(p)","font":"mg:gta_map","color":"#FF2A2A","shadow_color":0},'
                    '{"text":"\ue401$(t)","font":"mg:gta_map","color":"#FFC020","shadow_color":0}]'])

w('gta/home', ['# @s : retour à la villa (Neo Hills), refusé si la police le recherche', 'scoreboard players reset @s mg.gqs',
                'execute if score @s mg.gwl matches 1.. run return run title @s actionbar {"text":"🚔 Impossible : la police te recherche !","color":"red"}',
                'execute on vehicle run return 0',
                f'execute in {DIM} run tp @s {VFRONT[0] + 0.5} {VY} {Z + VFRONT[1] + 0.5} 180 0',
                f'execute in {DIM} run spawnpoint @s {VFRONT[0]} {VY} {Z + VFRONT[1]}',
                'execute at @s run playsound minecraft:block.portal.travel player @s ~ ~ ~ 0.2 2',
                'title @s actionbar {"text":"🏠 Neo Hills","color":"aqua","bold":true}'])

exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gta_plus.py'), encoding='utf-8').read())

# ---------------------------------------------------------------- câblage
C.patch('core/tick', 'execute if score $setup mg.st matches 1 run function mg:lobkart/tick',
        ['# Neo City (monde GTA) : portail du lobby et session', 'function mg:gta/lobby_tick'])
C.patch('core/tick', 'function mg:survie/tick', ['function mg:gta/pre_tick'], where='before')
C.patch('survie/leave', '# Retour au lobby des mini-jeux (@s) : tout est sauvegardé, puis remise à zéro façon lobby',
        ['execute if entity @s[tag=mg.gtw] run return run function mg:gta/leave'])
C.patch('core/load', 'execute unless score $rp mg.st matches 0..1 run scoreboard players set $rp mg.st 1',
        ['# Neo City (monde GTA) : construite une fois (dimension mg:gta, 2 min)',
         'execute if score $setup mg.st matches 1 unless data storage mg:gta built run schedule function mg:gta/world_build 45s',
         'scoreboard players set $gtw mg.st 0'])
C.objectives([('mg.gqs', 'minecraft.used:minecraft.warped_fungus_on_a_stick')])
C.patch('core/load', 'scoreboard objectives add mg.bw trigger',
        ['scoreboard objectives modify mg.gta displayname [{"text":"💵 Neo GTA","color":"green","bold":true},{"text":" : les plus riches","color":"gray","bold":false}]'])
C.objectives([('mg.grob', 'dummy'), ('mg.gsid', 'dummy'), ('mg.gveh', 'dummy')])
C.patch('desinstaller', 'scoreboard objectives remove mg.bw',
        ['schedule clear mg:gta/wb_step', 'schedule clear mg:gta/world_build', 'schedule clear mg:gta/session_setup',
         f'execute in {DIM} run forceload remove all', 'kill @e[tag=mg.gtap]', 'team remove mg_gciv', 'data remove storage mg:gta built',
         'data remove storage mg:gta s', 'data remove storage mg:gta unl'])
print(f'GTA OK : {len(INTER)} carrefours, {len(SIDE)} trottoirs, {len(PADS_AT)} points d\'armes, {len(CARS)} voitures, {len(HELI_AT)} hélicos')
