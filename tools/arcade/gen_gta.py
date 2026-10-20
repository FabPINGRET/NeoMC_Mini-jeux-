"""🚓 Neo GTA : la ville de Neo City, monde libre (dimension mg:gta) relié au lobby par un portail, hors mini-jeux.

    python tools/arcade/gen_gta.py .          (après gen_bomber.py : réutilise sa ville et ses explosions ; avant tools/duel/gen_duel.py,
                                         qui ajoute une garde à gta/menu_go, réécrit en entier ici)

Monde
- Dimension mg:gta (data/mg/dimension/gta.json) : vide, biome the_void (aucun monstre naturel). La ville du Bombardier y est
  construite une fois (mg:gta/world_build, ~2 min au premier chargement), puis réparée en tâche de fond quand le dernier
  joueur s'en va (mg:gta/session_end). Ajouter la dimension demande un redémarrage du serveur (pas un simple /reload).
- Portail au lobby (nord-est de la place, x 9 z -33), reconstruit s'il disparaît. Sortie : panneau 🚪 au carrefour de départ,
  ou le menu (les joueurs du GTA portent mg.surv, comme la survie : exclus des mini-jeux, menu « retour au lobby »).
- Session : démarre au premier joueur (forceload + entités), s'arrête au dernier. Les dollars (mg.gta) sont gardés.

Jeu
- Batte et pistolet au départ, 16 points d'armes (mitraillette, fusil à pompe, fusil, sniper avec lunette au clic droit,
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
PRICE = {2: 150, 3: 200, 4: 300, 5: 450, 6: 800, 7: 650, 8: 50, 9: 120, 11: 0, 21: 400, 22: 900, 23: 1800, 24: 3000, 25: 4500}
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
NZ = NH['runway'][1]                                            # bord nord : la piste d'aviation derrière le domaine
FL2 = f'{NA[0]} {Z + NZ} {NA[2]} {Z + NA[3] + 4}'            # chargement forcé du domaine
PAD.update({'slot': (70, '🎰 Machine à sous', 'gold', 'minecraft:gold_ingot'), 'roulette': (71, '🎡 Roulette', 'red', 'minecraft:clock'),
            'dice': (72, '🎲 Dés', 'aqua', 'minecraft:white_concrete'),
            'paint': (60, '🎨 Peinture', 'light_purple', 'minecraft:magenta_dye'), 'g_moto': (31, '🏍 Moto', 'gold', 'minecraft:saddle'), 'g_muscle': (32, '🚗 Muscle car', 'red', 'minecraft:minecart'),
            'g_super': (33, '🏎 Supercar', 'light_purple', 'minecraft:golden_horse_armor'), 'g_heli': (34, '🚁 Hélico', 'yellow', 'minecraft:feather'),
            'g_plane': (35, '✈ Avion', 'aqua', 'minecraft:elytra'), 'g_smg': (42, '🔫 Mitraillette', 'aqua', 'minecraft:crossbow'),
            'g_shotgun': (43, '🔫 Fusil à pompe', 'gold', 'minecraft:crossbow'), 'g_rifle': (44, '🔫 Fusil M14', 'yellow', 'minecraft:crossbow'),
            'g_sniper': (45, '🎯 Sniper', 'light_purple', 'minecraft:spyglass'), 'g_raygun': (46, '✦ Ray Gun', 'green', 'minecraft:heart_of_the_sea'),
            'g_rpg': (47, '🚀 Lance-roquettes', 'red', 'minecraft:firework_rocket'), 'g_armor': (49, '🛡 Gilet pare-balles', 'gray', 'minecraft:iron_chestplate'),
            'atm': (80, '💵 Distributeur (gratuit)', 'green', 'minecraft:paper')})
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
HELI_AT = [(4, 48, 'red_concrete'), (-3, 60, 'blue_concrete'), (52, -78, 'black_concrete'), (-76, 66, 'white_concrete')]
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

# Découpe en parts exécutées dans l'ordre (même idiome que gta_plus.py) : elles partagent les globals de ce fichier.
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gta_world.py'), encoding='utf-8').read())

exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gta_session.py'), encoding='utf-8').read())

exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gta_police.py'), encoding='utf-8').read())

exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gta_drive.py'), encoding='utf-8').read())

exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gta_heists.py'), encoding='utf-8').read())

exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gta_plus.py'), encoding='utf-8').read())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gta_city.py'), encoding='utf-8').read())

# ---------------------------------------------------------------- câblage
C.patch('core/tick', 'execute if score $setup mg.st matches 1 run function mg:lobkart/tick',
        ['# Neo City (monde GTA) : portail du lobby et session', 'function mg:gta/lobby_tick'])
C.patch('core/tick', 'function mg:survie/tick', ['function mg:gta/pre_tick'], where='before')
C.patch('survie/leave', '# Retour au lobby des mini-jeux (@s) : tout est sauvegardé, puis remise à zéro façon lobby',
        ['execute if entity @s[tag=mg.gtw] run return run function mg:gta/leave'])
C.patch('core/load', 'execute unless score $rp mg.st matches 0..1 run scoreboard players set $rp mg.st 1',
        ['# Neo City (monde GTA) : construite une fois (dimension mg:gta, 2 min)',
         'execute if score $setup mg.st matches 1 unless data storage mg:gta built run schedule function mg:gta/world_build 45s',
         'execute if score $setup mg.st matches 1 unless data storage mg:lobby gtaclean run schedule function mg:gta/spawn_clean 8s',
         'scoreboard players set $gtw mg.st 0'])
C.objectives([('mg.gqs', 'minecraft.used:minecraft.warped_fungus_on_a_stick')])
C.patch('core/load', 'scoreboard objectives add mg.bw trigger',
        ['scoreboard objectives add mg.gta dummy {"text":"💵 Dollars","color":"green"}',
         'scoreboard objectives modify mg.gta displayname [{"text":"💵 Neo GTA","color":"green","bold":true},{"text":" : les plus riches","color":"gray","bold":false}]'])
C.objectives([('mg.grob', 'dummy'), ('mg.gsid', 'dummy'), ('mg.gveh', 'dummy')])
C.patch('desinstaller', 'scoreboard objectives remove mg.bw',
        ['schedule clear mg:gta/wb_step', 'schedule clear mg:gta/world_build', 'schedule clear mg:gta/session_setup',
         f'execute in {DIM} run forceload remove all', 'kill @e[tag=mg.gtap]', 'team remove mg_gciv', 'data remove storage mg:gta built',
         'data remove storage mg:gta s', 'data remove storage mg:gta unl', 'data remove storage mg:lobby gtaclean', 'schedule clear mg:gta/spawn_clean'])
print(f'GTA OK : {len(INTER)} carrefours, {len(SIDE)} trottoirs, {len(PADS_AT)} points d\'armes, {len(CARS)} voitures, {len(HELI_AT)} hélicos')
