"""⚽ Terrain de foot souterrain : site, constantes et construction (importé par gen_foot.py, gen_sit.py et foot_*.py, jamais lancé seul).

Tout est sous la place nord du spawn (overworld), dans la roche de l'île (theme_world.W : pierre de y 46 à 58, terre de 59 à 62) :
- Terrain : intérieur x -13..17, y 48..53, z -40..-22 (sol en y 47, plafond en y 54, coque de briques de deepslate en x -14..18, z -41..-21).
- Buts : ouvertures de 5×3 (z -33..-29, y 48..50) dans les murs courts (x -14 ouest, x 18 est), avec un renfoncement de 2 blocs derrière
  (x -16..-15 et x 19..20) dont le fond est rouge (ouest : le but des Rouges) ou bleu (est : le but des Bleus).
- Vestiaire : intérieur x -3..3, y 48..51, z -19..-15, au sud du terrain, porte de 3×3 (x -1..1, z -21..-20) ; 4 socles de 2×2.
- Puits : trou 2×2 en (x -1..0, z -17..-16) dans la place, de y 63 jusqu'au plafond du vestiaire ; on tombe sur du foin.
- Bloc témoin : pierre de magnétite en (2, 46, -31), dans la coque sous le rond central ; absent = tout est reconstruit (core/tick).
Constantes de sélecteurs (calculées avec la règle du jeu : le volume va de x à x + dx + 1, sans la case d'arrivée en plus).
Les panneaux (text_display, tag mg.ftd) sont dans foot/labels, sans mg.lby : lobby/deco tue tout ce qui porte mg.lby.
"""
import common as C

# ------------------------------------------------------------------ géométrie
SENT = (2, 46, -31)                      # bloc témoin
CENTRE = '2.5 48 -30.5'                  # point d'engagement de la balle (centre du rond central)
FORCELOAD = '-17 -41 21 -14'             # chunks du terrain, du vestiaire et du puits (forceload permanent, core/forceloads)
HOLE = (-1, -17)                         # coin nord-ouest du trou 2×2 en surface
HOLE_BOX = f'{HOLE[0]} 63 {HOLE[1]} {HOLE[0] + 1} 63 {HOLE[1] + 1}'
SHELL = (-17, 21, 46, 54, -41, -21)      # boîte englobante de la coque du terrain (x1, x2, y1, y2, z1, z2), buts compris
LOCKER = (-4, 4, 46, 52, -20, -14)       # coque du vestiaire
SHAFT = (-2, 1, 52, 66, -18, -15)        # coque du puits, margelle et piquets (le panneau flotte à 66,6)
# volumes de sélecteur (x, y, z entiers, dx/dy/dz = nombre de cases - 1)
FOOT_ZONE = 'x=-17,y=46,z=-41,dx=38,dy=17,dz=27'        # x -17..21, y 46..63, z -41..-14 : terrain, vestiaire, puits ; PAS la surface (pieds en y 64)
BALL_BOX = 'x=-16,y=47,z=-40,dx=36,dy=6,dz=18'          # intérieur du terrain, buts et renfoncements compris (x -16..20, y 47..53) : sans vestiaire ni puits
GOAL_W = 'x=-16,y=48,z=-33,dx=1,dy=2,dz=4'              # renfoncement ouest (x -16..-15) = but des Rouges
GOAL_E = 'x=19,y=48,z=-33,dx=1,dy=2,dz=4'               # renfoncement est (x 19..20) = but des Bleus
BALLS = '@e[type=minecraft:sulfur_cube,tag=mg.ball]'            # la balle (il n'y en a qu'une ; plusieurs = foot/second les remplace)
BALL1 = '@e[type=minecraft:sulfur_cube,tag=mg.ball,limit=1]'
# socles du vestiaire (2×2) : clé -> (x, z du coin nord-ouest, bloc, texte, couleur)
PADS = {'red': (-3, -19, 'red_concrete', '🔴 Équipe rouge', 'red'),
        'blue': (2, -19, 'blue_concrete', '🔵 Équipe bleue', 'blue'),
        'white': (-3, -16, 'white_concrete', '✖ Quitter l\'équipe', 'white'),
        'gold': (2, -16, 'gold_block', '🏠 Retour au spawn', 'yellow')}
TF = 'transformation:{{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[{s}f,{s}f,{s}f]}}'
WHITE = 'minecraft:white_concrete'


def pad_box(key):
    """Sélecteur de la zone où l'on se tient sur un socle (pieds en y 48). Volume [x+0,3 ; x+1,7] (dx 0,4 = x+0,3 jusqu'à x+0,3+0,4+1) :
    la hitbox du joueur (±0,3) ne touche pas le foin voisin (x ou z dès le bord du socle), donc un joueur qui atterrit ne rejoint pas une équipe."""
    x, z = PADS[key][:2]
    return f'x={x + 0.3:.1f},y=48,z={z + 0.3:.1f},dx=0.4,dy=0.5,dz=0.4'


# ------------------------------------------------------------------ fonctions écrites
def build_lines():
    """foot/build : coque, creux, sol, buts, vestiaire, puits, lumières, bloc témoin (en dernier), panneaux, drapeau foot1 (storage mg:lobby)."""
    x1, x2 = -14, 18
    B = ['# ⚽ Terrain de foot souterrain : terrain, buts, vestiaire, puits (généré par tools/lobby/gen_foot.py)',
         # coques (la roche de l'île est remplie sur place : tout est posé par-dessus)
         f'fill {x1} 46 -41 {x2} 54 -21 minecraft:deepslate_bricks',
         'fill -17 46 -34 -14 51 -28 minecraft:deepslate_bricks', 'fill 18 46 -34 21 51 -28 minecraft:deepslate_bricks',
         'fill -4 46 -20 4 52 -14 minecraft:deepslate_bricks',
         'fill -2 52 -18 1 62 -15 minecraft:deepslate_bricks',
         # creux : terrain, renfoncements, ouvertures des buts, vestiaire, porte
         'fill -13 48 -40 17 53 -22 minecraft:air',
         'fill -16 48 -33 -14 50 -29 minecraft:air', 'fill 18 48 -33 20 50 -29 minecraft:air',
         'fill -3 48 -19 3 51 -15 minecraft:air', 'fill -1 48 -21 1 50 -20 minecraft:air',
         # sol du terrain : pelouse, ligne médiane, rond central
         'fill -13 47 -40 17 47 -22 minecraft:green_concrete',
         f'fill 2 47 -40 2 47 -22 {WHITE}',
         f'fill 0 47 -33 4 47 -33 {WHITE}', f'fill 0 47 -29 4 47 -29 {WHITE}',
         f'fill 0 47 -33 0 47 -29 {WHITE}', f'fill 4 47 -33 4 47 -29 {WHITE}',
         # buts : cadre blanc, fond rouge (ouest) ou bleu (est)
         'fill -17 48 -33 -17 50 -29 minecraft:red_concrete', 'fill 21 48 -33 21 50 -29 minecraft:blue_concrete']
    for gx in (x1, x2):
        B += [f'fill {gx} 48 -34 {gx} 50 -34 {WHITE}', f'fill {gx} 48 -28 {gx} 50 -28 {WHITE}',
              f'fill {gx} 51 -34 {gx} 51 -28 {WHITE}']
    # lumière : lanternes de mer au plafond (tout est éclairé, rien n'apparaît), sol du vestiaire, foin sous le puits
    B += [f'setblock {x} 54 {z} minecraft:sea_lantern' for x in (-11, -6, -1, 4, 9, 14) for z in (-38, -33, -28, -23)]
    B += ['setblock -16 51 -31 minecraft:sea_lantern', 'setblock 20 51 -31 minecraft:sea_lantern',
          'fill -3 47 -19 3 47 -15 minecraft:deepslate_tiles',
          'setblock -3 52 -19 minecraft:sea_lantern', 'setblock 3 52 -19 minecraft:sea_lantern',
          'setblock -3 52 -15 minecraft:sea_lantern', 'setblock 3 52 -15 minecraft:sea_lantern',
          'setblock -2 57 -17 minecraft:sea_lantern', 'setblock 1 57 -16 minecraft:sea_lantern',
          'setblock -2 61 -16 minecraft:sea_lantern', 'setblock 1 61 -17 minecraft:sea_lantern']
    for key, (px, pz, blk, _, _) in PADS.items():
        B.append(f'fill {px} 47 {pz} {px + 1} 47 {pz + 1} minecraft:{blk}')
    hx, hz = HOLE
    B += [f'fill {hx} 47 {hz} {hx + 1} 47 {hz + 1} minecraft:hay_block',
          # entrée en surface : margelle en briques noires, piquets avec lanternes, puits 2×2 ouvert jusqu'au vestiaire
          f'fill {hx - 1} 63 {hz - 1} {hx + 2} 63 {hz + 2} minecraft:polished_blackstone_bricks',
          f'fill {hx} 52 {hz} {hx + 1} 63 {hz + 1} minecraft:air',
          # colonne du trou au-dessus de la margelle (y 64..66) : dégagée pour que les décors saisonniers (neige de Noël) n'y posent rien
          # (jamais le bloc light en (0, 65, -18) : il est sur la margelle, hors de la colonne 2×2)
          f'fill {hx} 64 {hz} {hx + 1} 66 {hz + 1} minecraft:air']
    for dx, dz in ((-1, -1), (2, -1), (-1, 2), (2, 2)):
        B += [f'setblock {hx + dx} 64 {hz + dz} minecraft:polished_blackstone_wall', f'setblock {hx + dx} 65 {hz + dz} minecraft:lantern']
    # le bloc témoin est posé en TOUT DERNIER (juste avant les panneaux) : une construction interrompue ne le laisse jamais en place
    return B + [f'setblock {SENT[0]} {SENT[1]} {SENT[2]} minecraft:lodestone', 'function mg:foot/labels',
                'execute if score $ftoff mg.st matches 1 run function mg:foot/hole_close',
                'data modify storage mg:lobby foot1 set value 1b']


def _text(pos, parts, scale, bg, extra='billboard:"center"'):
    return (f'summon minecraft:text_display {pos} {{Tags:["mg.ftd"],{extra},background:{bg},text:{C.js(parts)},' + TF.format(s=scale) + '}')


def labels_lines():
    """foot/labels : panneaux du puits, des socles et du vestiaire (tag mg.ftd)."""
    L = ['# Panneaux du terrain de foot (tag mg.ftd, sans mg.lby : lobby/deco tuerait tout ce qui le porte)',
         'kill @e[type=minecraft:text_display,tag=mg.ftd]',
         _text(f'{HOLE[0] + 1} 66.6 {HOLE[1] + 1}', [{'text': '⚽ Terrain de foot', 'color': 'green', 'bold': True},
                                                      {'text': '\nsaute dans le trou ↓', 'color': 'gray'}], 1.4, 0)]
    for key, (px, pz, blk, txt, col) in PADS.items():
        L.append(_text(f'{px + 1}.0 49.6 {pz + 1}.0', [{'text': txt, 'color': col, 'bold': True}], 0.8, 1342177280))
    L.append(_text('0.5 50.9 -14.1', [
        {'text': '⚽ TERRAIN DE FOOT', 'color': 'green', 'bold': True},
        {'text': '\nSocle rouge ou bleu : choisis ton équipe · blanc : la quitter · or : retour au spawn.', 'color': 'white'},
        {'text': '\nLe point va à l\'équipe adverse du but, quel que soit le tireur.', 'color': 'gray'}],
        0.5, 1342177280, extra='billboard:"fixed",Rotation:[180f,0f],line_width:300'))
    return L


def write():
    """Écrit foot/build, labels, hole_open, hole_close, build_start, build_go."""
    w = C.w
    w('foot/build', build_lines())
    w('foot/labels', labels_lines())
    w('foot/hole_close', ['# Terrain désactivé : trou refermé (margelle pleine), panneaux retirés', f'fill {HOLE_BOX} minecraft:polished_blackstone_bricks',
                          'kill @e[type=minecraft:text_display,tag=mg.ftd]'])
    w('foot/hole_open', ['# Terrain réactivé : trou rouvert, panneaux reposés', f'fill {HOLE_BOX} minecraft:air', 'function mg:foot/labels'])
    w('foot/build_start', ['# Charge la zone puis construit (2 s plus tard)', f'forceload add {FORCELOAD}', 'schedule function mg:foot/build_go 2s'])
    w('foot/build_go', ['function mg:foot/build', f'forceload remove {FORCELOAD}', 'function mg:core/forceloads',
                        'tellraw @a[tag=mg.admin] {"text":"⚽ Terrain de foot souterrain construit (trou à côté du portail de Terra Nova, au nord de la place).","color":"gold"}'])
