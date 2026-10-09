"""🦎 Meccha Chameleon (id 198) : cache-cache où les caméléons se peignent pour se fondre dans le décor. Maison colorée en z 26600.

    python tools/arcade/gen_chameleon.py .        (puis tools/resourcepack/gen_rp.py pour les icônes des outils)

Caméléons (cacheurs) : invisibles, ils ont un corps en blocs (tête, corps, bras, jambes) qui les suit. Outils :
  🎨 Palette (fenêtre : partie du corps + 75 matières), 💧 Pipette (copie le bloc regardé sur la partie choisie),
  🧍 Poses (fenêtre : debout, assis, boule, à plat, plaqué au mur, bloc), 👥 Leurre (copie de soi, 2 par manche),
  📢 Narguer (+5 points, recharge 8 s). Immobile 2 s : le corps se cale (angle droit, et sur la grille en pose « bloc »).
  Toutes les 30 s, chaque caméléon siffle (+3 points).
Chasseurs : enfermés et aveugles 45 s, puis 3 min de chasse au lance-peinture (clic droit, 40 blocs) ou à la main.
Un caméléon touché est trouvé (spectateur). Points : chasseur +25 par trouvaille ; caméléon +1 toutes les 5 s, +20 s'il survit.
Plus aucun caméléon → les chasseurs gagnent ; à la fin du temps, les survivants gagnent.
"""
import random
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
GID = 198
Z = 26600
HIDE, HUNT = 900, 3600
Y = 80                                             # sol (on marche à y 81), plafond y 87
X1, X2, Z1, Z2 = -28, 28, Z - 20, Z + 20           # murs extérieurs

# ------------------------------------------------------------------ matières (palette, pipette) : (bloc, couleur du libellé)
DYE = [('white', 'F9FFFE'), ('orange', 'F9801D'), ('magenta', 'C74EBD'), ('light_blue', '3AB3DA'), ('yellow', 'FED83D'), ('lime', '80C71F'),
       ('pink', 'F38BAA'), ('gray', '474F52'), ('light_gray', '9D9D97'), ('cyan', '169C9C'), ('purple', '8932B8'), ('blue', '3C44AA'),
       ('brown', '835432'), ('green', '5E7C16'), ('red', 'B02E26'), ('black', '1D1D21')]
MATS = [(f'{c}_concrete', h) for c, h in DYE] + [(f'{c}_wool', h) for c, h in DYE] + [
    ('terracotta', '985E43'), ('white_terracotta', 'D1B2A1'), ('orange_terracotta', 'A05325'), ('yellow_terracotta', 'BA8523'),
    ('red_terracotta', '8F3D2E'), ('brown_terracotta', '4D3323'), ('light_blue_terracotta', '706C8A'), ('cyan_terracotta', '565B5B'),
    ('green_terracotta', '4C522A'), ('pink_terracotta', 'A14E4E'), ('purple_terracotta', '764656'), ('black_terracotta', '251610'),
    ('oak_planks', 'B8945F'), ('spruce_planks', '7A5A34'), ('birch_planks', 'D7C185'), ('dark_oak_planks', '4F3218'),
    ('jungle_planks', 'B88764'), ('acacia_planks', 'AD5D32'), ('cherry_planks', 'E3B3AD'), ('bookshelf', '6B5131'),
    ('stone', '7E7E7E'), ('stone_bricks', '7A7A7A'), ('bricks', '966253'), ('smooth_quartz', 'ECE6DF'), ('quartz_bricks', 'EAE4DC'),
    ('prismarine', '63A99A'), ('prismarine_bricks', '63AB9E'), ('dark_prismarine', '345C4C'), ('sandstone', 'D8CB9B'),
    ('smooth_stone', 'A0A0A0'), ('deepslate_tiles', '373737'), ('polished_andesite', '848684'), ('calcite', 'DFE0DC'),
    ('oak_leaves', '4E7A28'), ('moss_block', '596E2D'), ('grass_block', '7CBD6B'), ('hay_block', 'A68B0C'), ('pumpkin', 'C67A1B'),
    ('melon', '6F9A2D'), ('dirt', '866043'), ('iron_block', 'DCDCDC'), ('gold_block', 'F6D03D'), ('sea_lantern', 'ACC8BE')]
MID = {b: i + 1 for i, (b, _) in enumerate(MATS)}                     # index 1.. (mats[0] : rien)
assert len(MATS) <= 99


def state(b):
    return '{Name:"minecraft:oak_leaves",Properties:{persistent:"true"}}' if b == 'oak_leaves' else f'{{Name:"minecraft:{b}"}}'


def blk(b):
    return 'oak_leaves[persistent=true]' if b == 'oak_leaves' else b


PARTS = {1: ('Tout', [1, 2, 3, 4, 5, 6]), 2: ('Tête', [1]), 3: ('Corps', [2]), 4: ('Bras', [3, 4]), 5: ('Jambes', [5, 6])}
# poses : (nom, icône, échelle du joueur, largeur et hauteur de la zone touchable, [(translation, échelle)] des 6 morceaux)
H = (0.001, 0.001, 0.001)
POSES = {
    1: ('Debout', '🧍', 1.0, 0.8, 1.9, [((-0.25, 1.4, -0.25), (0.5, 0.5, 0.5)), ((-0.25, 0.7, -0.13), (0.5, 0.7, 0.26)),
                                         ((-0.5, 0.7, -0.12), (0.24, 0.7, 0.24)), ((0.26, 0.7, -0.12), (0.24, 0.7, 0.24)),
                                         ((-0.25, 0.0, -0.12), (0.24, 0.7, 0.24)), ((0.01, 0.0, -0.12), (0.24, 0.7, 0.24))]),
    2: ('Assis', '🪑', 0.7, 0.8, 1.3, [((-0.25, 0.85, -0.25), (0.5, 0.5, 0.5)), ((-0.25, 0.3, -0.13), (0.5, 0.6, 0.26)),
                                       ((-0.5, 0.3, -0.12), (0.24, 0.55, 0.24)), ((0.26, 0.3, -0.12), (0.24, 0.55, 0.24)),
                                       ((-0.25, 0.0, -0.12), (0.24, 0.3, 0.7)), ((0.01, 0.0, -0.12), (0.24, 0.3, 0.7))]),
    3: ('Boule', '⚪', 0.5, 1.0, 1.0, [((-0.3, 0.55, -0.3), (0.6, 0.4, 0.6)), ((-0.45, 0.0, -0.45), (0.9, 0.6, 0.9)),
                                       ((-0.45, 0.0, -0.45), H), ((-0.45, 0.0, -0.45), H), ((-0.45, 0.0, -0.45), H), ((-0.45, 0.0, -0.45), H)]),
    4: ('À plat', '➖', 0.25, 1.4, 0.4, [((-0.25, 0.0, 0.7), (0.5, 0.3, 0.5)), ((-0.25, 0.0, -0.2), (0.5, 0.3, 0.9)),
                                        ((-0.5, 0.0, -0.2), (0.24, 0.24, 0.7)), ((0.26, 0.0, -0.2), (0.24, 0.24, 0.7)),
                                        ((-0.25, 0.0, -1.0), (0.24, 0.24, 0.8)), ((0.01, 0.0, -1.0), (0.24, 0.24, 0.8))]),
    5: ('Plaqué au mur', '🧱', 1.0, 1.0, 1.9, [((-0.25, 1.4, 0.18), (0.5, 0.5, 0.1)), ((-0.4, 0.5, 0.18), (0.8, 0.9, 0.1)),
                                               ((-0.62, 0.6, 0.18), (0.22, 0.8, 0.1)), ((0.4, 0.6, 0.18), (0.22, 0.8, 0.1)),
                                               ((-0.4, 0.0, 0.18), (0.38, 0.5, 0.1)), ((0.02, 0.0, 0.18), (0.38, 0.5, 0.1))]),
    6: ('Bloc', '⬛', 0.5, 1.02, 1.02, [((-0.5, 0.0, -0.5), H), ((-0.5, 0.0, -0.5), (1.0, 1.0, 1.0)),
                                       ((-0.5, 0.0, -0.5), H), ((-0.5, 0.0, -0.5), H), ((-0.5, 0.0, -0.5), H), ((-0.5, 0.0, -0.5), H)]),
}
TOOLS = {1: ('🎨 Palette', 'green', 'Clic droit : choisir la partie du corps et sa matière', 'cham_palette'),
         2: ('💧 Pipette', 'aqua', 'Clic droit sur un bloc : copie sa matière sur la partie choisie', 'cham_pipette'),
         3: ('🧍 Poses', 'yellow', 'Clic droit : debout, assis, boule, à plat, plaqué au mur, bloc', 'cham_pose'),
         4: ('👥 Leurre', 'light_purple', 'Clic droit : pose une copie de toi (2 par manche)', 'cham_decoy'),
         5: ('📢 Narguer', 'gold', 'Clic droit : un sifflet bien fort, +5 points (recharge 8 s)', 'cham_taunt')}


def tool(n, slot):
    nm, col, lore, model = TOOLS[n]
    return (f'item replace entity @s hotbar.{slot} with minecraft:warped_fungus_on_a_stick[custom_data={{chm:{n}}},item_model="mg:{model}",'
            f'custom_name={js({"text": nm, "color": col, "bold": True, "italic": False})},lore=[{js({"text": lore, "color": "gray", "italic": False})}],unbreakable={{}}]')


GUN = ('item replace entity @s hotbar.0 with minecraft:warped_fungus_on_a_stick[custom_data={chm:10},item_model="mg:gun_raygun",'
       f'custom_name={js({"text": "🔫 Lance-peinture", "color": "red", "bold": True, "italic": False})},'
       f'lore=[{js({"text": "Clic droit : tire (40 blocs). Touche un caméléon pour le trouver !", "color": "gray", "italic": False})}],unbreakable={{}}]')

# ------------------------------------------------------------------ la maison : 6 pièces de 18 × 19, chacune son décor (que des matières de la palette)
rnd = random.Random(198)
L = [f'# 🦎 Maison du Meccha Chameleon : x {X1}..{X2}, z {Z1}..{Z2}, sol y {Y}, plafond y {Y + 7} ; cage des chasseurs sur le toit (généré)']
L += [f'fill {X1 - 3} {y} {Z1 - 3} {X2 + 3} {y} {Z2 + 3} minecraft:air' for y in range(Y + 14, Y - 3, -1)]
L += [f'fill {X1} {Y - 1} {Z1} {X2} {Y - 1} {Z2} minecraft:stone',
      f'fill {X1} {Y} {Z1} {X2} {Y + 7} {Z2} minecraft:white_concrete', f'fill {X1 + 1} {Y + 1} {Z1 + 1} {X2 - 1} {Y + 6} {Z2 - 1} minecraft:air',
      f'fill {X1} {Y + 7} {Z1} {X2} {Y + 7} {Z2} minecraft:smooth_quartz',
      f'fill -9 {Y + 1} {Z1 + 1} -9 {Y + 6} {Z2 - 1} minecraft:white_concrete', f'fill 9 {Y + 1} {Z1 + 1} 9 {Y + 6} {Z2 - 1} minecraft:white_concrete',
      f'fill {X1 + 1} {Y + 1} {Z} {X2 - 1} {Y + 6} {Z} minecraft:white_concrete']
for x in range(X1 + 3, X2, 5):
    for z in range(Z1 + 3, Z2, 5):
        L.append(f'setblock {x} {Y + 7} {z} minecraft:sea_lantern')
ROOMS = {'salon': (-27, -10, Z1 + 1, Z - 1), 'cuisine': (-8, 8, Z1 + 1, Z - 1), 'atelier': (10, 27, Z1 + 1, Z - 1),
         'chambre': (-27, -10, Z + 1, Z2 - 1), 'bain': (-8, 8, Z + 1, Z2 - 1), 'serre': (10, 27, Z + 1, Z2 - 1)}
RAINBOW = ['red_wool', 'orange_wool', 'yellow_wool', 'lime_wool', 'light_blue_wool', 'blue_wool', 'purple_wool', 'pink_wool']
PAINTS = ['red_concrete', 'yellow_concrete', 'blue_concrete', 'lime_concrete', 'magenta_concrete', 'orange_concrete', 'cyan_concrete', 'purple_concrete']


def wall_block(room, x, y, z, k):
    """Bloc de la peau intérieure du mur (k : position le long du mur)."""
    if room == 'salon':
        return 'dark_oak_planks' if y == Y + 1 else ('light_blue_wool' if (k // 2) % 2 else 'white_wool')
    if room == 'cuisine':
        if y <= Y + 2:
            return 'white_terracotta'
        return 'cyan_terracotta' if (k + y) % 2 else 'light_blue_terracotta'
    if room == 'atelier':
        return rnd.choice(PAINTS) if rnd.random() < 0.45 else 'white_concrete'
    if room == 'chambre':
        return RAINBOW[k % len(RAINBOW)] if y > Y + 1 else 'birch_planks'
    if room == 'bain':
        return 'prismarine_bricks' if y <= Y + 2 else ('smooth_quartz' if (k + y) % 2 else 'calcite')
    return 'oak_leaves' if k % 4 else 'jungle_planks'


def floor_block(room, x, z):
    if room == 'salon':
        return 'oak_planks'
    if room == 'cuisine':
        return 'black_concrete' if (x + z) % 2 else 'white_concrete'
    if room == 'atelier':
        return rnd.choice(PAINTS) if rnd.random() < 0.12 else 'white_concrete'
    if room == 'chambre':
        return 'pink_wool' if (x + z) % 2 else 'yellow_wool'
    if room == 'bain':
        return 'white_concrete' if (x // 2 + z // 2) % 2 else 'light_blue_concrete'
    return 'moss_block' if rnd.random() < 0.35 else 'grass_block'


for room, (x1, x2, z1, z2) in ROOMS.items():
    for x in range(x1, x2 + 1):
        for z in range(z1, z2 + 1):
            L.append(f'setblock {x} {Y} {z} minecraft:{blk(floor_block(room, x, z))}')
    ring = [(x, z1) for x in range(x1, x2 + 1)] + [(x2, z) for z in range(z1 + 1, z2 + 1)] + \
           [(x, z2) for x in range(x2 - 1, x1 - 1, -1)] + [(x1, z) for z in range(z2 - 1, z1, -1)]
    for k, (x, z) in enumerate(ring):
        for y in range(Y + 1, Y + 7):
            L.append(f'setblock {x} {y} {z} minecraft:{blk(wall_block(room, x, y, z, k))}')


def fl(x1, y1, z1, x2, y2, z2, b):
    L.append(f'fill {x1} {y1} {z1} {x2} {y2} {z2} minecraft:{blk(b)}')


def st(x, y, z, b):
    L.append(f'setblock {x} {y} {z} minecraft:{blk(b)}')


y1 = Y + 1
# salon : tapis à damier, canapé d'angle, fauteuil, bibliothèque, télé, table basse, plantes
for x in range(-22, -15):
    for z in range(Z - 14, Z - 7):
        st(x, Y, z, 'red_wool' if (x + z) % 2 else 'white_wool')
fl(-26, y1, Z - 18, -20, y1, Z - 18, 'red_wool'); fl(-26, y1 + 1, Z - 19 + 1, -20, y1 + 1, Z - 18, 'red_wool')
fl(-26, y1, Z - 17, -26, y1, Z - 13, 'red_wool')
fl(-17, y1, Z - 18, -16, y1, Z - 17, 'yellow_wool'); st(-16, y1 + 1, Z - 18, 'yellow_wool')
fl(-14, y1, Z - 19, -11, y1 + 3, Z - 19, 'bookshelf')
fl(-25, y1 + 1, Z - 2, -21, y1 + 2, Z - 2, 'black_concrete'); fl(-25, y1, Z - 2, -21, y1, Z - 2, 'dark_oak_planks')
fl(-21, y1, Z - 12, -20, y1, Z - 11, 'dark_oak_planks')
for (x, z) in [(-11, Z - 2), (-26, Z - 2), (-11, Z - 9)]:
    st(x, y1, z, 'moss_block'); fl(x, y1 + 1, z, x, y1 + 2, z, 'oak_leaves')
st(-13, y1, Z - 5, 'sea_lantern')
# cuisine : plans de travail, frigo, îlot, table et chaises, tabourets colorés
fl(-7, y1, Z - 19, 3, y1, Z - 19, 'lime_terracotta' if False else 'green_terracotta'); fl(-7, y1 + 1, Z - 19, 3, y1 + 1, Z - 19, 'smooth_stone')
fl(5, y1, Z - 19, 6, y1 + 2, Z - 19, 'iron_block')
fl(-7, y1 + 3, Z - 19, 3, y1 + 4, Z - 19, 'white_terracotta')
fl(-3, y1, Z - 12, 2, y1, Z - 11, 'quartz_bricks')
for x, c in zip(range(-3, 3), ['red_concrete', 'yellow_concrete', 'lime_concrete', 'light_blue_concrete', 'pink_concrete', 'orange_concrete']):
    st(x, y1, Z - 9, c)
fl(-6, y1, Z - 5, -2, y1, Z - 3, 'spruce_planks')
for (x, z) in [(-7, Z - 4), (-1, Z - 4), (-4, Z - 6), (-4, Z - 2)]:
    st(x, y1, z, 'birch_planks')
fl(6, y1, Z - 4, 7, y1, Z - 2, 'oak_planks'); st(7, y1 + 1, Z - 3, 'melon'); st(6, y1 + 1, Z - 2, 'pumpkin')
# atelier : chevalets et toiles, seaux de peinture, grande fresque, palettes empilées
for (x, z) in [(13, Z - 15), (18, Z - 15), (23, Z - 15), (15, Z - 8), (21, Z - 8)]:
    st(x, y1, z, 'spruce_planks'); st(x, y1 + 1, z, 'spruce_planks')
    c1, c2 = rnd.sample(PAINTS, 2)
    fl(x - 1, y1 + 2, z, x + 1, y1 + 3, z, c1.replace('concrete', 'wool')); st(x, y1 + 3, z, c2)
for _ in range(14):
    x, z = rnd.randint(11, 26), rnd.randint(Z - 18, Z - 2)
    st(x, y1, z, rnd.choice(PAINTS))
fl(12, y1 + 1, Z - 2, 25, y1 + 4, Z - 2, 'white_wool')
for x in range(12, 26):
    for y in range(y1 + 1, y1 + 5):
        if rnd.random() < 0.6:
            st(x, y, Z - 2, rnd.choice(PAINTS).replace('concrete', 'wool'))
fl(25, y1, Z - 18, 26, y1 + 1, Z - 17, 'acacia_planks')
# chambre d'enfant : lit, armoire, cubes de jouets, ballon, bureau
fl(-26, y1, Z + 15, -25, y1, Z + 18, 'red_wool'); fl(-26, y1, Z + 18, -25, y1, Z + 18, 'white_wool')
fl(-12, y1, Z + 16, -11, y1 + 2, Z + 18, 'birch_planks')
for _ in range(16):
    x, z = rnd.randint(-24, -13), rnd.randint(Z + 4, Z + 14)
    h = rnd.randint(1, 2)
    for k in range(h):
        st(x, y1 + k, z, rnd.choice(['red_concrete', 'yellow_concrete', 'blue_concrete', 'lime_concrete', 'orange_concrete', 'magenta_concrete']))
st(-18, y1, Z + 17, 'lime_concrete')
fl(-22, y1, Z + 2, -19, y1, Z + 2, 'cherry_planks')
# salle de bain : baignoire, lavabos, serviettes, tapis de bain
fl(-7, y1, Z + 14, 0, y1, Z + 18, 'smooth_quartz'); fl(-6, y1, Z + 15, -1, y1, Z + 17, 'water')
for x in (3, 6):
    st(x, y1, Z + 18, 'calcite'); st(x, y1 + 1, Z + 18, 'smooth_quartz')
for (x, c) in [(-6, 'pink_wool'), (-3, 'cyan_wool'), (0, 'yellow_wool')]:
    fl(x, y1 + 2, Z + 1, x, y1 + 3, Z + 1, c)
fl(2, Y, Z + 8, 5, Y, Z + 10, 'light_blue_wool')
st(7, y1, Z + 2, 'white_concrete'); st(7, y1 + 1, Z + 2, 'quartz_bricks')
# serre : bottes de foin, citrouilles, melons, potager, arbre, caisses
for (x, z) in [(12, Z + 3), (13, Z + 3), (12, Z + 4), (24, Z + 17), (25, Z + 17)]:
    st(x, y1, z, 'hay_block')
st(12, y1 + 1, Z + 3, 'hay_block')
for _ in range(10):
    st(rnd.randint(11, 26), y1, rnd.randint(Z + 6, Z + 18), rnd.choice(['pumpkin', 'melon']))
fl(15, Y, Z + 12, 22, Y, Z + 13, 'dirt')
fl(19, y1, Z + 6, 19, y1 + 3, Z + 6, 'spruce_planks'); fl(17, y1 + 3, Z + 4, 21, y1 + 5, Z + 8, 'oak_leaves'); st(19, y1 + 3, Z + 6, 'spruce_planks')
fl(25, y1, Z + 2, 26, y1 + 1, Z + 3, 'oak_planks')
# portes (2 de large, 3 de haut) entre les pièces
for (xa, xb, za, zb) in [(-10, -8, Z - 11, Z - 9), (8, 10, Z - 11, Z - 9), (-10, -8, Z + 9, Z + 11), (8, 10, Z + 9, Z + 11),
                         (-19, -18, Z - 1, Z + 1), (-1, 0, Z - 1, Z + 1), (17, 18, Z - 1, Z + 1)]:
    fl(xa, y1, za, xb, y1 + 2, zb, 'air')
# cage des chasseurs (sur le toit)
L += [f'fill -3 {Y + 8} {Z - 3} 3 {Y + 12} {Z + 3} minecraft:black_stained_glass', f'fill -2 {Y + 9} {Z - 2} 2 {Y + 11} {Z + 2} minecraft:air',
      f'fill -2 {Y + 8} {Z - 2} 2 {Y + 8} {Z + 2} minecraft:black_concrete']
w('cham/build', L)

# ------------------------------------------------------------------ fenêtres (dialogues) : palette, poses, aide
D = C.D
import os
os.makedirs(os.path.join(D, 'dialog'), exist_ok=True)


DLG = {}                                           # fenêtres en ligne (dialog show @s {...}) : pas de redémarrage du serveur à l'ajout


def dialog(name, d):
    DLG[name] = 'dialog show @s ' + js(d)
    if os.path.exists(os.path.join(D, 'dialog', name + '.json')):
        os.remove(os.path.join(D, 'dialog', name + '.json'))


PART_IN = {'type': 'minecraft:single_option', 'key': 'partie', 'label': {'text': 'Partie du corps', 'color': 'gold'}, 'label_visible': True,
           'options': [{'id': str(k), 'display': {'text': nm, 'color': 'yellow'}, **({'initial': True} if k == 1 else {})} for k, (nm, _) in PARTS.items()]}
dialog('cham_palette', {
    'type': 'minecraft:multi_action', 'title': {'text': '🎨 Palette du caméléon', 'color': 'green', 'bold': True}, 'pause': False,
    'after_action': 'none',
    'can_close_with_escape': True, 'columns': 5,
    'body': [{'type': 'minecraft:plain_message', 'width': 400, 'contents': [
        {'text': 'Choisis la partie du corps, puis clique une matière pour la peindre. ', 'color': 'gray'},
        {'text': '💧 Pipette', 'color': 'aqua'}, {'text': ' : copie directement un bloc du décor sur la partie choisie.', 'color': 'gray'}]}],
    'inputs': [PART_IN],
    'actions': [{'label': {'text': '💧 Pipette sur cette partie', 'color': 'aqua', 'bold': True}, 'width': 150,
                 'action': {'type': 'minecraft:dynamic/run_command', 'template': 'trigger mg.cmp set $(partie)00'}}] +
               [{'label': [{'text': '■ ', 'color': f'#{h}'}, {'translate': f'block.minecraft.{b}', 'color': 'white'}], 'width': 110,
                 'action': {'type': 'minecraft:dynamic/run_command', 'template': f'trigger mg.cmp set $(partie){MID[b]:02d}'}} for b, h in MATS],
    'exit_action': {'label': {'text': 'Fermer', 'color': 'gray'}}})
dialog('cham_poses', {
    'type': 'minecraft:multi_action', 'title': {'text': '🧍 Poses', 'color': 'yellow', 'bold': True}, 'pause': False, 'can_close_with_escape': True,
    'columns': 2,
    'body': [{'type': 'minecraft:plain_message', 'contents': [{'text': 'Immobile 2 s, ton corps se cale à angle droit. En « Bloc », il se cale aussi sur la grille : peins-le avec la pipette et deviens un bloc du décor !', 'color': 'gray'}]}],
    'actions': [{'label': {'text': f'{ic} {nm}', 'color': 'yellow'}, 'width': 140, 'action': {'type': 'minecraft:run_command', 'command': f'trigger mg.cmo set {n}'}}
                for n, (nm, ic, *_r) in POSES.items()],
    'exit_action': {'label': {'text': 'Fermer', 'color': 'gray'}}})
HELP_H = [{'text': 'Tu es un CAMÉLÉON 🦎\n\n', 'color': 'green', 'bold': True},
          {'text': '🎨 Palette', 'color': 'green'}, {'text': ' : peins chaque partie de ton corps (tête, corps, bras, jambes).\n', 'color': 'gray'},
          {'text': '💧 Pipette', 'color': 'aqua'}, {'text': ' : vise un bloc du décor et copie-le sur toi.\n', 'color': 'gray'},
          {'text': '🧍 Poses', 'color': 'yellow'}, {'text': ' : debout, assis, boule, à plat, plaqué au mur, bloc.\n', 'color': 'gray'},
          {'text': '👥 Leurre', 'color': 'light_purple'}, {'text': ' : laisse une copie de toi pour piéger les chasseurs (2).\n', 'color': 'gray'},
          {'text': '📢 Narguer', 'color': 'gold'}, {'text': ' : siffle pour +5 points… mais ça s\'entend !\n\n', 'color': 'gray'},
          {'text': 'Tu as 45 s pour te cacher. Immobile 2 s, tu te cales. Toutes les 30 s, tu siffles malgré toi. Survis 3 minutes !', 'color': 'white'}]
HELP_S = [{'text': 'Tu es un CHASSEUR 🔍\n\n', 'color': 'red', 'bold': True},
          {'text': 'Les caméléons se peignent aux couleurs du décor et prennent des poses. Tu es enfermé 45 s, puis tu as 3 minutes.\n\n', 'color': 'gray'},
          {'text': '🔫 Lance-peinture', 'color': 'red'}, {'text': ' : clic droit pour tirer, ou frappe à la main. Un caméléon touché est trouvé (+25 points).\n', 'color': 'gray'},
          {'text': '👥 Attention aux leurres', 'color': 'light_purple'}, {'text': ' : en toucher un te ralentit 3 s.\n', 'color': 'gray'},
          {'text': '👂 Écoute les sifflets', 'color': 'gold'}, {'text': ' : les caméléons sifflent toutes les 30 s.', 'color': 'gray'}]
for nm, body, col in (('cham_help_hider', HELP_H, 'green'), ('cham_help_seeker', HELP_S, 'red')):
    dialog(nm, {'type': 'minecraft:notice', 'title': {'text': '🦎 MECCHA CHAMELEON', 'color': col, 'bold': True}, 'pause': False,
                'can_close_with_escape': True, 'body': [{'type': 'minecraft:plain_message', 'width': 320, 'contents': body}],
                'action': {'label': {'text': 'C\'est parti !', 'color': col, 'bold': True}}})

# ------------------------------------------------------------------ fonctions
def tr(t, s):
    return f'translation:[{t[0]}f,{t[1]}f,{t[2]}f],scale:[{s[0]}f,{s[1]}f,{s[2]}f]'


ROT0 = 'left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]'
w('cham/prepare', ['# 🦎 Meccha Chameleon : préparation (maison, rôles, cage)', 'function mg:cham/build', 'function mg:cham/kill_all',
                   'data modify storage mg:cham mats set value [' + ','.join(['{Name:"minecraft:air"}'] + [state(b) for b, _ in MATS]) + ']',
                   'clear @a[tag=mg.play]', 'gamemode adventure @a[tag=mg.play]', 'tag @a[tag=mg.play] add mg.cmx',
                   'execute store result score $cmn mg.st if entity @a[tag=mg.play]', 'scoreboard players set #4 mg.st 4',
                   'scoreboard players set $cmsolo mg.st 0', 'execute if score $cmn mg.st matches ..1 run scoreboard players set $cmsolo mg.st 1',
                   'scoreboard players operation $cmn mg.st /= #4 mg.st', 'execute if score $cmn mg.st matches ..0 run scoreboard players set $cmn mg.st 1',
                   'execute if score $cmsolo mg.st matches 0 run function mg:cham/pick', 'execute as @a[tag=mg.play,tag=!mg.cms] run tag @s add mg.cmh',
                   'team join mg_red @a[tag=mg.cms]', 'team join mg_cm @a[tag=mg.cmh]',
                   f'tp @a[tag=mg.cms] 0.5 {Y + 9} {Z}.5', 'execute as @a[tag=mg.cms] at @s run spawnpoint @s ~ ~ ~',
                   f'spreadplayers 0 {Z} 2 18 under {Y + 5} false @a[tag=mg.cmh]', 'execute as @a[tag=mg.cmh] at @s run spawnpoint @s ~ ~ ~',
                   'scoreboard players set @a[tag=mg.cmx] mg.cmpts 0', 'scoreboard players set @a[tag=mg.cmx] mg.cmf 0'])
w('cham/pick', ['execute as @a[tag=mg.play,tag=!mg.cms,sort=random,limit=1] run tag @s add mg.cms',
                'scoreboard players remove $cmn mg.st 1', 'execute if score $cmn mg.st matches 1.. run function mg:cham/pick'])
w('cham/kill_all', ['kill @e[tag=mg.cmd]', 'kill @e[tag=mg.cmi]', 'kill @e[tag=mg.cmdd]', 'kill @e[tag=mg.cmdi]', 'bossbar remove mg:cham'])
w('cham/go', ['# Départ : 45 s pour se cacher', 'scoreboard players set $cmt mg.st 0', 'scoreboard players set $cmc mg.st 0', 'scoreboard players set $cmdc mg.st 0',
              'execute as @a[tag=mg.cmh] run function mg:cham/become', 'execute as @a[tag=mg.cms] run function mg:cham/seeker_kit',
              f'effect give @a[tag=mg.cms] minecraft:blindness {HIDE // 20 + 1} 0 true',
              'bossbar add mg:cham {"text":"🦎 Meccha Chameleon"}', 'bossbar set mg:cham color green', f'bossbar set mg:cham max {HIDE}',
              'bossbar set mg:cham players @a[tag=mg.cmx]',
              'execute as @a[tag=mg.cmh] run function mg:cham/help_hider', 'execute as @a[tag=mg.cms] run function mg:cham/help_seeker',
              'title @a[tag=mg.cmh] title {"text":"🦎 Cache-toi !","color":"green","bold":true}',
              'title @a[tag=mg.cmh] subtitle {"text":"Peins-toi aux couleurs du décor","color":"gray"}',
              'title @a[tag=mg.cms] title {"text":"🔍 Chasseur","color":"red","bold":true}',
              'title @a[tag=mg.cms] subtitle {"text":"Libéré dans 45 s","color":"gray"}',
              'execute if score $cmsolo mg.st matches 1 run tellraw @a[tag=mg.cmx] {"text":"🦎 Mode entraînement (seul) : tu es caméléon, essaie la palette, la pipette et les poses. Il faut au moins 2 joueurs pour une vraie partie.","color":"yellow"}'])
B = ['# @s devient caméléon : invisible, corps en blocs (6 morceaux) et zone touchable',
     'clear @s', 'scoreboard players add $cmc mg.st 1', 'scoreboard players operation @s mg.cmid = $cmc mg.st',
     'effect give @s minecraft:invisibility infinite 0 true', 'effect give @s minecraft:saturation infinite 0 true',
     'effect give @s minecraft:resistance infinite 3 true', 'effect give @s minecraft:regeneration infinite 2 true',
     'scoreboard players set @s mg.cmpo 1', 'scoreboard players set @s mg.cmpt 1', 'scoreboard players set @s mg.cmdl 2',
     'scoreboard players set @s mg.cmtc 0', 'scoreboard players set @s mg.cmst 0', 'scoreboard players set @s mg.cmq 0',
     'scoreboard players enable @s mg.cmp', 'scoreboard players enable @s mg.cmo']
for k, b in enumerate(['green_concrete', 'lime_concrete', 'lime_concrete', 'lime_concrete', 'green_concrete', 'green_concrete'], 1):
    t, s = POSES[1][5][k - 1]
    B.append(f'execute at @s run summon minecraft:block_display ~ ~ ~ {{Tags:["mg.cmd","mg.cmk{k}","mg.cmnew"],teleport_duration:1,'
             f'block_state:{state(b)},transformation:{{{ROT0},{tr(t, s)}}}}}')
B += ['execute at @s run summon minecraft:interaction ~ ~ ~ {Tags:["mg.cmi","mg.cmnew"],width:0.8f,height:1.9f}',
      'scoreboard players operation @e[tag=mg.cmnew] mg.cmid = @s mg.cmid', 'tag @e[tag=mg.cmnew] remove mg.cmnew',
      'attribute @s minecraft:scale base set 1'] + [tool(n, n - 1) for n in TOOLS]
w('cham/become', B)
w('cham/seeker_kit', ['# @s : chasseur', 'clear @s', 'effect clear @s minecraft:invisibility', 'attribute @s minecraft:scale base set 1', GUN,
                      'item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=16711680,unbreakable={}]',
                      'item replace entity @s armor.head with minecraft:leather_helmet[dyed_color=16711680,unbreakable={}]',
                      'effect give @s minecraft:saturation infinite 0 true', 'effect give @s minecraft:speed infinite 0 true',
                      'scoreboard players set @s mg.cmgc 0', 'scoreboard players set @s mg.cmq 0'])
# outils (clic droit)
w('cham/use', ['# @s a fait un clic droit avec un outil', 'scoreboard players set @s mg.cmq 0'] +
  [f'execute if items entity @s weapon.mainhand *[custom_data~{{chm:{n}}}] run return run function mg:cham/tool_{n}' for n in list(TOOLS) + [10]])
w('cham/tool_1', ['scoreboard players enable @s mg.cmp', DLG['cham_palette']])
w('cham/tool_3', ['scoreboard players enable @s mg.cmo', DLG['cham_poses']])
w('cham/help_hider', [DLG['cham_help_hider']])
w('cham/help_seeker', [DLG['cham_help_seeker']])
w('cham/tool_2', ['# Pipette : premier bloc solide regardé (6 blocs)', 'scoreboard players set $cmf mg.st 0', 'scoreboard players set $cmr mg.st 30',
                  'execute anchored eyes positioned ^ ^ ^0.2 run function mg:cham/pip_ray',
                  'execute if score $cmf mg.st matches 0 run title @s actionbar {"text":"💧 Rien à copier ici : vise un mur, un sol ou un meuble","color":"gray"}'])
PR = ['# Un pas (0,2 bloc) de la pipette', 'execute if block ~ ~ ~ #mg:ray_pass run scoreboard players remove $cmr mg.st 1',
      'execute if block ~ ~ ~ #mg:ray_pass if score $cmr mg.st matches 1.. positioned ^ ^ ^0.2 run return run function mg:cham/pip_ray']
PR += [f'execute if block ~ ~ ~ minecraft:{b} run return run function mg:cham/pip_got {{m:{MID[b]}}}' for b, _ in MATS]
w('cham/pip_ray', PR)
w('cham/pip_got', ['# @s : la pipette a trouvé la matière $(m)', 'scoreboard players set $cmf mg.st 1',
                   '$scoreboard players set $cmm mg.st $(m)', 'scoreboard players operation $cmpp mg.st = @s mg.cmpt', 'function mg:cham/paint_do',
                   'particle minecraft:dust{color:[0.3,0.9,1.0],scale:1} ~ ~ ~ 0.15 0.15 0.15 0 8',
                   'execute at @s run playsound minecraft:item.bottle.fill player @s ~ ~ ~ 0.8 1.4'])
PD = ['# @s : peint la partie $cmpp (1 tout, 2 tête, 3 corps, 4 bras, 5 jambes) avec la matière $cmm',
      'scoreboard players operation $cmid mg.st = @s mg.cmid', 'execute store result storage mg:cham p.m int 1 run scoreboard players get $cmm mg.st']
for p, (nm, ks) in PARTS.items():
    for k in ks:
        PD.append(f'execute if score $cmpp mg.st matches {p} run data modify storage mg:cham p.k{k} set value 1b')
PD += ['function mg:cham/paint_apply with storage mg:cham p', 'data remove storage mg:cham p',
       'execute at @s run playsound minecraft:block.honey_block.place player @s ~ ~ ~ 0.8 1.3', 'function mg:cham/hud']
w('cham/paint_do', PD)
PA = []
for k in range(1, 7):
    PA.append(f'$execute if data storage mg:cham p.k{k} as @e[type=minecraft:block_display,tag=mg.cmk{k}] if score @s mg.cmid = $cmid mg.st '
              f'run data modify entity @s block_state set from storage mg:cham mats[$(m)]')
w('cham/paint_apply', ['# Macro {m} : matière des morceaux cochés (p.k1..k6)'] + PA)
w('cham/palette_cmd', ['# @s a choisi dans la palette (mg.cmp = partie × 100 + matière)', 'scoreboard players operation $cmv mg.st = @s mg.cmp',
                       'scoreboard players reset @s mg.cmp', 'scoreboard players enable @s mg.cmp', 'scoreboard players set #100 mg.st 100',
                       'scoreboard players operation $cmm mg.st = $cmv mg.st', 'scoreboard players operation $cmm mg.st %= #100 mg.st',
                       'scoreboard players operation $cmpp mg.st = $cmv mg.st', 'scoreboard players operation $cmpp mg.st /= #100 mg.st',
                       'execute unless score $cmpp mg.st matches 1..5 run return 0', 'scoreboard players operation @s mg.cmpt = $cmpp mg.st',
                       'execute if score $cmm mg.st matches 0 run return run function mg:cham/hud',
                       f'execute if score $cmm mg.st matches 1..{len(MATS)} run function mg:cham/paint_do'])
# poses
PS = ['# @s a choisi une pose (mg.cmo)', 'scoreboard players operation $cmv mg.st = @s mg.cmo', 'scoreboard players reset @s mg.cmo',
      'scoreboard players enable @s mg.cmo', f'execute unless score $cmv mg.st matches 1..{len(POSES)} run return 0',
      'scoreboard players operation @s mg.cmpo = $cmv mg.st', 'scoreboard players set @s mg.cmst 0', 'scoreboard players operation $cmid mg.st = @s mg.cmid']
PS += [f'execute if score $cmv mg.st matches {n} run function mg:cham/pose_{n}' for n in POSES]
PS += ['execute at @s run playsound minecraft:entity.armor_stand.place player @s ~ ~ ~ 0.7 1.2', 'function mg:cham/hud']
w('cham/pose_cmd', PS)
for n, (nm, ic, sc, wd, ht, parts) in POSES.items():
    P = [f'# Pose {nm}', f'attribute @s minecraft:scale base set {sc}']
    for k, (t, s) in enumerate(parts, 1):
        P.append(f'execute as @e[type=minecraft:block_display,tag=mg.cmk{k}] if score @s mg.cmid = $cmid mg.st run data merge entity @s '
                 f'{{interpolation_duration:4,start_interpolation:0,transformation:{{{ROT0},{tr(t, s)}}}}}')
    P.append(f'execute as @e[type=minecraft:interaction,tag=mg.cmi] if score @s mg.cmid = $cmid mg.st run data merge entity @s {{width:{wd}f,height:{ht}f}}')
    w(f'cham/pose_{n}', P)
# suivi du corps, calage à l'arrêt
w('cham/follow', ['# @s (caméléon) : son corps le suit ; immobile 2 s → calé (angle droit, grille en pose « bloc »)',
                  'scoreboard players operation $cmid mg.st = @s mg.cmid',
                  'execute store result score $cmx mg.st run data get entity @s Pos[0] 20', 'execute store result score $cmz mg.st run data get entity @s Pos[2] 20',
                  'execute store result score $cmy mg.st run data get entity @s Pos[1] 20',
                  'execute if score $cmx mg.st = @s mg.cmlx if score $cmz mg.st = @s mg.cmlz if score $cmy mg.st = @s mg.cmly run scoreboard players add @s mg.cmst 1',
                  'execute unless score $cmx mg.st = @s mg.cmlx run scoreboard players set @s mg.cmst 0',
                  'execute unless score $cmz mg.st = @s mg.cmlz run scoreboard players set @s mg.cmst 0',
                  'execute unless score $cmy mg.st = @s mg.cmly run scoreboard players set @s mg.cmst 0',
                  'scoreboard players operation @s mg.cmlx = $cmx mg.st', 'scoreboard players operation @s mg.cmlz = $cmz mg.st', 'scoreboard players operation @s mg.cmly = $cmy mg.st',
                  'execute if score @s mg.cmst matches ..39 as @e[type=minecraft:block_display,tag=mg.cmd] if score @s mg.cmid = $cmid mg.st run tp @s ~ ~ ~ ~ 0',
                  'execute if score @s mg.cmst matches ..39 as @e[type=minecraft:interaction,tag=mg.cmi] if score @s mg.cmid = $cmid mg.st run tp @s ~ ~ ~',
                  'execute if score @s mg.cmst matches 40 run function mg:cham/snap',
                  'execute if score @s mg.cmst matches 41.. run scoreboard players set @s mg.cmst 41'])
w('cham/snap', ['# @s : calage (angle droit le plus proche ; en pose « bloc », centre du bloc)',
                'execute store result score $cmr mg.st run data get entity @s Rotation[0]', 'scoreboard players add $cmr mg.st 405',
                'scoreboard players set #90 mg.st 90', 'scoreboard players set #360 mg.st 360',
                'scoreboard players operation $cmr mg.st /= #90 mg.st', 'scoreboard players operation $cmr mg.st *= #90 mg.st',
                'scoreboard players operation $cmr mg.st %= #360 mg.st', 'execute store result storage mg:cham s.y int 1 run scoreboard players get $cmr mg.st',
                'execute if score @s mg.cmpo matches 6 align xz positioned ~0.5 ~ ~0.5 run function mg:cham/snap_at with storage mg:cham s',
                'execute unless score @s mg.cmpo matches 6 run function mg:cham/snap_at with storage mg:cham s',
                'title @s actionbar {"text":"🔒 Calé : ne bouge plus !","color":"green"}',
                'execute at @s run playsound minecraft:block.wool.place player @s ~ ~ ~ 0.5 0.8'])
w('cham/snap_at', ['$execute as @e[type=minecraft:block_display,tag=mg.cmd] if score @s mg.cmid = $cmid mg.st run tp @s ~ ~ ~ $(y) 0',
                   'execute as @e[type=minecraft:interaction,tag=mg.cmi] if score @s mg.cmid = $cmid mg.st run tp @s ~ ~ ~'])
# leurre : copie du corps
w('cham/tool_4', ['# Leurre : une copie du corps, là où on est', 'execute unless score @s mg.cmdl matches 1.. run return run title @s actionbar {"text":"👥 Plus de leurre pour cette manche","color":"gray"}',
                  'scoreboard players remove @s mg.cmdl 1', 'scoreboard players add $cmdc mg.st 1', 'scoreboard players operation $cmid mg.st = @s mg.cmid',
                  'execute as @e[type=minecraft:block_display,tag=mg.cmd] if score @s mg.cmid = $cmid mg.st at @s run function mg:cham/decoy_part',
                  'execute at @s run summon minecraft:interaction ~ ~ ~ {Tags:["mg.cmdi","mg.cmnew"],width:0.9f,height:1.6f}',
                  'scoreboard players operation @e[tag=mg.cmnew] mg.cmdn = $cmdc mg.st', 'tag @e[tag=mg.cmnew] remove mg.cmnew',
                  'title @s actionbar [{"text":"👥 Leurre posé ! Reste : ","color":"light_purple"},{"score":{"name":"@s","objective":"mg.cmdl"},"color":"white"}]',
                  'execute at @s run particle minecraft:poof ~ ~1 ~ 0.3 0.5 0.3 0.02 12',
                  'execute at @s run playsound minecraft:entity.illusioner.mirror_move player @s ~ ~ ~ 0.8 1.2'])
w('cham/decoy_part', ['# @s : un morceau du corps, recopié en leurre',
                      'summon minecraft:block_display ~ ~ ~ {Tags:["mg.cmdd","mg.cmnew"]}',
                      'data modify entity @e[tag=mg.cmnew,limit=1] block_state set from entity @s block_state',
                      'data modify entity @e[tag=mg.cmnew,limit=1] transformation set from entity @s transformation',
                      'data modify entity @e[tag=mg.cmnew,limit=1] Rotation set from entity @s Rotation',
                      'scoreboard players operation @e[tag=mg.cmnew] mg.cmdn = $cmdc mg.st', 'tag @e[tag=mg.cmnew] remove mg.cmnew'])
w('cham/decoy_pop', ['# @s (zone d\'un leurre) touchée par un chasseur ($cmhunt) : le leurre éclate, le chasseur est ralenti 3 s',
                     'scoreboard players operation $cmv mg.st = @s mg.cmdn',
                     'execute as @e[type=minecraft:block_display,tag=mg.cmdd] if score @s mg.cmdn = $cmv mg.st run kill @s',
                     'particle minecraft:poof ~ ~1 ~ 0.4 0.6 0.4 0.05 25', 'particle minecraft:witch ~ ~1 ~ 0.4 0.6 0.4 0 15',
                     'playsound minecraft:entity.illusioner.cast_spell player @a ~ ~ ~ 1 1.4',
                     'effect give @a[tag=mg.cmhunt] minecraft:slowness 3 2 true',
                     'title @a[tag=mg.cmhunt] actionbar {"text":"👥 C\'était un leurre !","color":"light_purple","bold":true}', 'kill @s'])
# narguer, sifflets
w('cham/tool_5', ['# Narguer : sifflet fort, +5 points (recharge 8 s)',
                  'execute if score @s mg.cmtc matches 1.. run return run title @s actionbar [{"text":"📢 Recharge : ","color":"gray"},{"score":{"name":"@s","objective":"mg.cmtc"},"color":"white"},{"text":" ticks","color":"gray"}]',
                  'scoreboard players set @s mg.cmtc 160', 'scoreboard players add @s mg.cmpts 5',
                  'execute at @s run playsound minecraft:entity.parrot.ambient player @a ~ ~ ~ 2 1.6',
                  'execute at @s run playsound minecraft:block.note_block.flute player @a ~ ~ ~ 2 2',
                  'execute at @s run particle minecraft:note ~ ~1.5 ~ 0.3 0.3 0.3 1 6',
                  'title @s actionbar {"text":"📢 Tu nargues les chasseurs : +5 points","color":"gold"}'])
w('cham/whistle', ['# Toutes les 30 s : chaque caméléon siffle malgré lui (+3 points)',
                   'execute as @a[tag=mg.cmh,tag=!mg.cmout] at @s run function mg:cham/whistle_one'])
w('cham/whistle_one', ['execute store result score $cmq mg.st run random value 0..2',
                       'execute if score $cmq mg.st matches 0 run playsound minecraft:block.note_block.flute player @a ~ ~ ~ 1.3 1.6',
                       'execute if score $cmq mg.st matches 1 run playsound minecraft:block.note_block.chime player @a ~ ~ ~ 1.3 1.2',
                       'execute if score $cmq mg.st matches 2 run playsound minecraft:entity.parrot.ambient player @a ~ ~ ~ 1.3 1.3',
                       'particle minecraft:note ~ ~1 ~ 0.2 0.2 0.2 1 3', 'scoreboard players add @s mg.cmpts 3'])
# lance-peinture
w('cham/tool_10', ['# Lance-peinture : rayon de 40 blocs (cadence 0,6 s)', 'execute if score @s mg.cmgc matches 1.. run return 0',
                   'scoreboard players set @s mg.cmgc 12', 'tag @s add mg.cmhunt', 'scoreboard players set $cmr mg.st 160',
                   'execute at @s run playsound minecraft:entity.slime.squish player @a ~ ~ ~ 1 1.6',
                   'execute anchored eyes positioned ^ ^ ^0.3 run function mg:cham/shot_ray', 'tag @s remove mg.cmhunt'])
SR = ['# Un pas (0,25 bloc) du tir', 'scoreboard players remove $cmr mg.st 1',
      'execute positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=minecraft:interaction,tag=mg.cmi,dx=0,dy=0,dz=0,limit=1] positioned ~0.5 ~0.5 ~0.5 run return run function mg:cham/shot_hit',
      'execute positioned ~-0.5 ~-0.5 ~-0.5 as @e[type=minecraft:interaction,tag=mg.cmdi,dx=0,dy=0,dz=0,limit=1] at @s run return run function mg:cham/decoy_pop',
      'execute unless block ~ ~ ~ #mg:ray_pass run return run function mg:cham/shot_miss',
      'particle minecraft:dust{color:[1.0,0.3,0.6],scale:0.6} ~ ~ ~ 0 0 0 0 1',
      'execute if score $cmr mg.st matches 1.. positioned ^ ^ ^0.25 run function mg:cham/shot_ray']
w('cham/shot_ray', SR)
w('cham/shot_miss', ['particle minecraft:dust{color:[1.0,0.3,0.6],scale:1.4} ~ ~ ~ 0.15 0.15 0.15 0 10',
                     'playsound minecraft:block.honey_block.hit player @a ~ ~ ~ 0.7 1.2'])
w('cham/shot_hit', ['# @s : zone touchable d\'un caméléon touchée par le tir', 'scoreboard players operation $cmv mg.st = @s mg.cmid',
                    'execute as @a[tag=mg.cmh,tag=!mg.cmout] if score @s mg.cmid = $cmv mg.st run function mg:cham/found'])
w('cham/hit_int', ['# @s : zone touchable frappée à la main', 'execute on attacker if entity @s[tag=mg.cms] run tag @s add mg.cmhunt',
                   'data remove entity @s attack', 'execute if entity @a[tag=mg.cmhunt] run function mg:cham/shot_hit', 'tag @a remove mg.cmhunt'])
w('cham/hit_dec', ['# @s : leurre frappé à la main', 'execute on attacker if entity @s[tag=mg.cms] run tag @s add mg.cmhunt',
                   'data remove entity @s attack', 'execute if entity @a[tag=mg.cmhunt] at @s run function mg:cham/decoy_pop', 'tag @a remove mg.cmhunt'])
w('cham/hit_adv', ['# Récompense de mg:cham_hit : @s (chasseur) a frappé un joueur', 'advancement revoke @s only mg:cham_hit',
                   'execute unless entity @s[tag=mg.cms] run return 0', 'tag @s add mg.cmhunt',
                   'execute as @a[tag=mg.cmh,tag=!mg.cmout] if data entity @s {HurtTime:10s} run function mg:cham/found', 'tag @s remove mg.cmhunt'])
w('cham/found', ['# @s (caméléon) trouvé par @a[tag=mg.cmhunt]', 'tag @s add mg.cmout', 'scoreboard players operation $cmid mg.st = @s mg.cmid',
                 'execute at @s run particle minecraft:dust{color:[1.0,0.3,0.6],scale:2} ~ ~0.8 ~ 0.4 0.6 0.4 0 40',
                 'execute at @s run particle minecraft:totem_of_undying ~ ~1 ~ 0.3 0.5 0.3 0.3 20',
                 'execute as @e[tag=mg.cmd] if score @s mg.cmid = $cmid mg.st run kill @s', 'execute as @e[tag=mg.cmi] if score @s mg.cmid = $cmid mg.st run kill @s',
                 'scoreboard players add @a[tag=mg.cmhunt] mg.cmf 1', 'scoreboard players add @a[tag=mg.cmhunt] mg.cmpts 25',
                 'clear @s', 'effect clear @s', 'attribute @s minecraft:scale base set 1', 'gamemode spectator @s',
                 'title @s title {"text":"🔍 Trouvé !","color":"red","bold":true}',
                 'title @s subtitle [{"text":"par ","color":"gray"},{"selector":"@a[tag=mg.cmhunt]","color":"red"}]',
                 'title @a[tag=mg.cmhunt] actionbar [{"text":"🎯 Trouvé : ","color":"green","bold":true},{"selector":"@s","color":"yellow"},{"text":"  +25","color":"gold"}]',
                 'tellraw @a[tag=mg.cmx] [{"text":"🦎 ","color":"green"},{"selector":"@s","color":"yellow"},{"text":" a été trouvé par ","color":"gray"},{"selector":"@a[tag=mg.cmhunt]","color":"red"}]',
                 'execute as @a[tag=mg.cmx] at @s run playsound minecraft:entity.player.levelup player @s ~ ~ ~ 0.6 1.6'])
# phases, HUD
w('cham/release', ['# Fin de la cachette : les chasseurs entrent', 'effect clear @a[tag=mg.cms] minecraft:blindness',
                   f'spreadplayers 0 {Z} 1 6 under {Y + 5} false @a[tag=mg.cms]', 'execute as @a[tag=mg.cms] at @s run spawnpoint @s ~ ~ ~',
                   'bossbar set mg:cham color red', f'bossbar set mg:cham max {HUNT}',
                   'title @a[tag=mg.cmx] title {"text":"🔍 La chasse commence !","color":"red","bold":true}',
                   'title @a[tag=mg.cmx] subtitle {"text":"3 minutes","color":"gray"}',
                   'execute as @a[tag=mg.cmx] at @s run playsound minecraft:event.raid.horn master @s ~ ~ ~ 0.6 1.2'])
w('cham/hud', ['# @s (caméléon) : barre d\'action (partie choisie, pose, leurres)',
               'execute if score @s mg.cmst matches 40.. run return 0'] +
  [f'execute if score @s mg.cmpt matches {p} if score @s mg.cmpo matches {n} run title @s actionbar [{{"text":"🎨 {pn}","color":"green"}},'
   f'{{"text":"   {ic} {nm}","color":"yellow"}},{{"text":"   👥 ","color":"light_purple"}},{{"score":{{"name":"@s","objective":"mg.cmdl"}},"color":"white"}},'
   f'{{"text":"   ⭐ ","color":"gold"}},{{"score":{{"name":"@s","objective":"mg.cmpts"}},"color":"white"}}]'
   for p, (pn, _) in PARTS.items() for n, (nm, ic, *_r) in POSES.items()])
w('cham/second', ['# Chaque seconde : barre de boss, points de survie, sifflets',
                  'scoreboard players operation $cml mg.st = $cmt mg.st', 'scoreboard players set #20 mg.st 20',
                  f'execute if score $cmt mg.st matches ..{HIDE} run scoreboard players set $cmk mg.st {HIDE}',
                  f'execute if score $cmt mg.st matches {HIDE + 1}.. run scoreboard players set $cmk mg.st {HIDE + HUNT}',
                  'scoreboard players operation $cmk mg.st -= $cmt mg.st', 'execute store result bossbar mg:cham value run scoreboard players get $cmk mg.st',
                  'scoreboard players operation $cmk mg.st /= #20 mg.st', 'scoreboard players set #60 mg.st 60',
                  'scoreboard players operation $cmm2 mg.st = $cmk mg.st', 'scoreboard players operation $cmm2 mg.st /= #60 mg.st',
                  'scoreboard players operation $cms2 mg.st = $cmk mg.st', 'scoreboard players operation $cms2 mg.st %= #60 mg.st',
                  'execute store result score $cmh mg.st if entity @a[tag=mg.cmh,tag=!mg.cmout]',
                  f'execute if score $cmt mg.st matches ..{HIDE} if score $cms2 mg.st matches 10.. run bossbar set mg:cham name [{{"text":"🦎 Cachez-vous !  ","color":"green","bold":true}},{{"score":{{"name":"$cmm2","objective":"mg.st"}},"color":"white"}},{{"text":":","color":"white"}},{{"score":{{"name":"$cms2","objective":"mg.st"}},"color":"white"}}]',
                  f'execute if score $cmt mg.st matches ..{HIDE} if score $cms2 mg.st matches ..9 run bossbar set mg:cham name [{{"text":"🦎 Cachez-vous !  ","color":"green","bold":true}},{{"score":{{"name":"$cmm2","objective":"mg.st"}},"color":"white"}},{{"text":":0","color":"white"}},{{"score":{{"name":"$cms2","objective":"mg.st"}},"color":"white"}}]',
                  f'execute if score $cmt mg.st matches {HIDE + 1}.. if score $cms2 mg.st matches 10.. run bossbar set mg:cham name [{{"text":"🔍 Chasse  ","color":"red","bold":true}},{{"score":{{"name":"$cmm2","objective":"mg.st"}},"color":"white"}},{{"text":":","color":"white"}},{{"score":{{"name":"$cms2","objective":"mg.st"}},"color":"white"}},{{"text":"   🦎 ","color":"green"}},{{"score":{{"name":"$cmh","objective":"mg.st"}},"color":"white"}},{{"text":" caché(s)","color":"gray"}}]',
                  f'execute if score $cmt mg.st matches {HIDE + 1}.. if score $cms2 mg.st matches ..9 run bossbar set mg:cham name [{{"text":"🔍 Chasse  ","color":"red","bold":true}},{{"score":{{"name":"$cmm2","objective":"mg.st"}},"color":"white"}},{{"text":":0","color":"white"}},{{"score":{{"name":"$cms2","objective":"mg.st"}},"color":"white"}},{{"text":"   🦎 ","color":"green"}},{{"score":{{"name":"$cmh","objective":"mg.st"}},"color":"white"}},{{"text":" caché(s)","color":"gray"}}]',
                  'execute as @a[tag=mg.cmh,tag=!mg.cmout] run function mg:cham/hud',
                  'scoreboard players operation $cmq mg.st = $cmt mg.st', 'scoreboard players set #100 mg.st 100', 'scoreboard players operation $cmq mg.st %= #100 mg.st',
                  f'execute if score $cmt mg.st matches {HIDE + 1}.. if score $cmq mg.st matches 0 run scoreboard players add @a[tag=mg.cmh,tag=!mg.cmout] mg.cmpts 1',
                  'scoreboard players operation $cmq mg.st = $cmt mg.st', 'scoreboard players set #600 mg.st 600', 'scoreboard players operation $cmq mg.st %= #600 mg.st',
                  f'execute if score $cmt mg.st matches {HIDE + 1}.. if score $cmq mg.st matches 0 run function mg:cham/whistle',
                  f'execute if score $cmt mg.st matches {HIDE - 200}..{HIDE - 20} run title @a[tag=mg.cms] actionbar [{{"text":"🔍 Libéré dans ","color":"red"}},{{"score":{{"name":"$cms2","objective":"mg.st"}},"color":"white","bold":true}},{{"text":" s","color":"red"}}]',
                  f'execute if score $cmt mg.st matches {HIDE - 200}..{HIDE - 20} as @a[tag=mg.cms] at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 0.6 1.4'])
w('cham/tick', ['# 🦎 Meccha Chameleon : tick', 'scoreboard players add $cmt mg.st 1',
                f'execute if score $cmt mg.st matches ..{HIDE - 1} run tp @a[tag=mg.cms] 0.5 {Y + 9} {Z}.5',
                f'execute if score $cmt mg.st matches {HIDE} run function mg:cham/release',
                'execute as @a[tag=mg.cmx,scores={mg.cmq=1..}] at @s run function mg:cham/use',
                'execute as @a[tag=mg.cmh,tag=!mg.cmout,scores={mg.cmp=1..}] run function mg:cham/palette_cmd',
                'execute as @a[tag=mg.cmh,tag=!mg.cmout,scores={mg.cmo=1..}] run function mg:cham/pose_cmd',
                'execute as @a[tag=mg.cmh,tag=!mg.cmout] at @s run function mg:cham/follow',
                'scoreboard players remove @a[tag=mg.cmx,scores={mg.cmtc=1..}] mg.cmtc 1', 'scoreboard players remove @a[tag=mg.cmx,scores={mg.cmgc=1..}] mg.cmgc 1',
                'execute as @e[type=minecraft:interaction,tag=mg.cmi] if data entity @s attack run function mg:cham/hit_int',
                'execute as @e[type=minecraft:interaction,tag=mg.cmdi] if data entity @s attack run function mg:cham/hit_dec',
                'execute as @e[type=minecraft:interaction,tag=mg.cmi] if data entity @s interaction run data remove entity @s interaction',
                'execute as @e[type=minecraft:interaction,tag=mg.cmdi] if data entity @s interaction run data remove entity @s interaction',
                'scoreboard players operation $cmq mg.st = $cmt mg.st', 'scoreboard players set #20 mg.st 20', 'scoreboard players operation $cmq mg.st %= #20 mg.st',
                'execute if score $cmq mg.st matches 0 run function mg:cham/second',
                'execute store result score $cmh mg.st if entity @a[tag=mg.play,tag=mg.cmh,tag=!mg.cmout]',
                'execute store result score $cmk mg.st if entity @a[tag=mg.play,tag=mg.cms]',
                'execute if score $cmsolo mg.st matches 0 if score $state mg.st matches 2 if score $cmh mg.st matches 0 run return run function mg:cham/seekers_win',
                'execute if score $cmsolo mg.st matches 0 if score $state mg.st matches 2 if score $cmk mg.st matches 0 run return run function mg:cham/hiders_win',
                f'execute if score $state mg.st matches 2 if score $cmt mg.st matches {HIDE + HUNT}.. run function mg:cham/hiders_win'])
REC = ['# Récapitulatif de fin de manche (points de chacun, meilleur joueur)',
       'tellraw @a[tag=mg.cmx] {"text":"━━━━━━━━ 🦎 MECCHA CHAMELEON ━━━━━━━━","color":"green","bold":true}',
       'execute if entity @a[tag=mg.cmh,tag=!mg.cmout] run tellraw @a[tag=mg.cmx] [{"text":"🦎 Jamais trouvés : ","color":"green"},{"selector":"@a[tag=mg.cmh,tag=!mg.cmout]","color":"yellow"}]',
       'execute as @a[tag=mg.cms] run tellraw @a[tag=mg.cmx] [{"text":"🔍 ","color":"red"},{"selector":"@s","color":"white"},{"text":" : ","color":"gray"},{"score":{"name":"@s","objective":"mg.cmf"},"color":"yellow"},{"text":" trouvé(s), ","color":"gray"},{"score":{"name":"@s","objective":"mg.cmpts"},"color":"gold"},{"text":" pts","color":"gray"}]',
       'execute as @a[tag=mg.cmh] run tellraw @a[tag=mg.cmx] [{"text":"🦎 ","color":"green"},{"selector":"@s","color":"white"},{"text":" : ","color":"gray"},{"score":{"name":"@s","objective":"mg.cmpts"},"color":"gold"},{"text":" pts","color":"gray"}]',
       'scoreboard players set $cmbest mg.st -1', 'execute as @a[tag=mg.cmx] run scoreboard players operation $cmbest mg.st > @s mg.cmpts',
       'execute as @a[tag=mg.cmx] if score @s mg.cmpts = $cmbest mg.st run tellraw @a[tag=mg.cmx] [{"text":"⭐ Meilleur joueur : ","color":"gold","bold":true},{"selector":"@s","color":"yellow"},{"text":" (","color":"gray"},{"score":{"name":"@s","objective":"mg.cmpts"},"color":"gold"},{"text":" pts)","color":"gray"}]']
w('cham/recap', REC)
w('cham/hiders_win', ['# Les caméléons encore cachés gagnent', 'scoreboard players add @a[tag=mg.cmh,tag=!mg.cmout] mg.cmpts 20', 'function mg:cham/recap',
                      'tag @a[tag=mg.play,tag=mg.cmh,tag=!mg.cmout] add mg.win', 'scoreboard players add @a[tag=mg.play,tag=mg.cmh,tag=!mg.cmout] mg.wins 1',
                      'scoreboard players set $state mg.st 3', 'scoreboard players set $timer mg.st 120',
                      'title @a[tag=!mg.surv] title {"text":"Les CAMÉLÉONS gagnent !","color":"green","bold":true}',
                      'tellraw @a [{"text":"★ Victoire des caméléons : ","color":"gold"},{"selector":"@a[tag=mg.play,tag=mg.cmh,tag=!mg.cmout]","color":"yellow"}]',
                      'execute as @a[tag=!mg.surv] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1'])
w('cham/seekers_win', ['# Plus aucun caméléon', 'function mg:cham/recap', 'tellraw @a {"text":"🔍 Tous les caméléons ont été trouvés !","color":"red","bold":true}',
                       'function mg:core/win_red'])
w('cham/cleanup', ['function mg:cham/kill_all', 'execute as @a[tag=mg.cmx] run attribute @s minecraft:scale base set 1',
                   'effect clear @a[tag=mg.cmx]', 'team leave @a[team=mg_cm]',
                   'tag @a remove mg.cmh', 'tag @a remove mg.cms', 'tag @a remove mg.cmout', 'tag @a remove mg.cmhunt', 'tag @a remove mg.cmx',
                   'scoreboard players reset @a mg.cmp', 'scoreboard players reset @a mg.cmo'])

# avancement : un chasseur frappe un joueur
os.makedirs(os.path.join(D, 'advancement'), exist_ok=True)
with open(os.path.join(D, 'advancement', 'cham_hit.json'), 'w', encoding='utf-8', newline='\n') as f:
    import json
    json.dump({'criteria': {'hit': {'trigger': 'minecraft:player_hurt_entity'}},
               'rewards': {'function': 'mg:cham/hit_adv'}}, f, indent=2)
    f.write('\n')

C.register([GID], 'cham', [C.announce(GID, '', '🦎 MECCHA CHAMELEON', 'green', 'peignez-vous aux couleurs du décor, les chasseurs arrivent dans 45 s !')])
C.objectives([('mg.cmid', 'dummy'), ('mg.cmq', 'minecraft.used:minecraft.warped_fungus_on_a_stick'), ('mg.cmp', 'trigger'), ('mg.cmo', 'trigger'),
              ('mg.cmpo', 'dummy'), ('mg.cmpt', 'dummy'), ('mg.cmst', 'dummy'), ('mg.cmlx', 'dummy'), ('mg.cmly', 'dummy'), ('mg.cmlz', 'dummy'),
              ('mg.cmdl', 'dummy'), ('mg.cmdn', 'dummy'), ('mg.cmtc', 'dummy'), ('mg.cmgc', 'dummy'), ('mg.cmpts', 'dummy'), ('mg.cmf', 'dummy')])
C.patch('core/load', 'scoreboard objectives add mg.bw trigger', ['team add mg_cm', 'team modify mg_cm nametagVisibility never',
                                                                 'team modify mg_cm friendlyFire false', 'team modify mg_cm collisionRule never',
                                                                 'team modify mg_cm color green'])
C.patch('desinstaller', 'scoreboard objectives remove mg.bw', ['team remove mg_cm', 'bossbar remove mg:cham', 'data remove storage mg:cham mats'])
C.forceload([f'# Meccha Chameleon (z {Z})', f'forceload add {X1 - 3} {Z1 - 3} {X2 + 3} {Z2 + 3}'])
print(f'Meccha Chameleon OK : {len(L)} commandes de construction, {len(MATS)} matières')
