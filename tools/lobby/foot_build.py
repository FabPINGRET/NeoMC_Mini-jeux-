"""⚽ Terrain de foot souterrain : site, constantes et construction (importé par gen_foot.py, gen_sit.py et foot_*.py, jamais lancé seul).

Tout est sous la place nord du spawn (overworld), dans la roche de l'île (theme_world.W : pierre de y 46 à 58, terre de 59 à 62) :
- Terrain : intérieur x -13..17, y 48..53, z -40..-22 (sol en y 47, plafond en y 54, coque de briques de deepslate en x -14..18, z -41..-21).
- Buts : ouvertures de 5×3 (z -33..-29, y 48..50) dans les murs courts (x -14 ouest, x 18 est), avec un renfoncement de 2 blocs derrière
  (x -16..-15 et x 19..20) dont le fond est rouge (ouest : le but des Rouges) ou bleu (est : le but des Bleus).
- Vestiaire : intérieur x -3..3, y 48..51, z -19..-15, au sud du terrain, porte de 3×3 (x -1..1, z -21..-20) ; 4 socles de 2×2.
- Entrée : le portail du foot du hub des portails (tools/lobby/gen_hub.py, mg:hub/enter_foot -> foot/go : tp sur le sol du terrain,
  devant le vestiaire). L'ancienne entrée de l'avenue nord (tapis x -7..-5, z -40..-38, but blanc en x -8, haie ouverte en x -4 : OLD_ENTRY)
  et le tapis d'avant (x -19..-17, z -19..-17, OLD_PAD) sont rendus au décor du spawn (theme_world.W) par foot/build.
  Le socle or du vestiaire remonte devant le portail du foot du hub (RETURN).
- Ancien puits (x -2..1, z -18..-15, y 52..66 : trou 2×2, coque, margelle, piquets ; y 52 = plafond du vestiaire, rendu par la coque) : foot/build
  le rebouche avec les blocs du spawn (theme_world.W) et retire les piquets (lignes de migration : la prod en a encore) ; il ne reste que son emplacement (OLD_SHAFT, lu par check_site).
- Bloc témoin : pierre de magnétite en (2, 46, -30), dans la coque sous le rond central ; absent = tout est reconstruit (core/tick).
Constantes de sélecteurs (calculées avec la règle du jeu : le volume va de x à x + dx + 1, sans la case d'arrivée en plus).
Les panneaux (text_display, tag mg.ftd) sont dans foot/labels, sans mg.lby : lobby/deco tue tout ce qui porte mg.lby.
"""
import common as C
import theme_world as TW

# ------------------------------------------------------------------ géométrie
SENT = (2, 46, -30)                      # bloc témoin (l'ancien (2, 46, -31) : retiré de core/tick par gen_foot.py)
CENTRE = '2.5 48 -30.5'                  # point d'engagement de la balle (centre du rond central)
FORCELOAD = '-17 -41 21 -14'             # chunks du terrain, du vestiaire, de l'ancien puits et du tapis (forceload permanent, core/forceloads)
OLD_PAD = (-19, -17, 63, 64, -19, -17)   # tapis d'avant (x1, x2, y1, y2, z1, z2) : rendu à l'herbe par foot/build (la prod en a encore un)
OLD_ENTRY = (-8, -4, 63, 80, -41, -37)   # ancienne entrée de l'avenue nord (tapis, but blanc, haie ouverte) : rendue au décor du spawn
PLOT_RING = {'minecraft:purpur_block': 'minecraft:grass_block', 'minecraft:obsidian': 'minecraft:grass_block',
             'minecraft:crying_obsidian': 'minecraft:grass_block'}   # anneau de l'ancienne place des plots (W) : herbe à la place
RETURN = (7.5, 64, -43.5)                # arrivée du socle or : devant le portail du foot du hub (x 9, z -44)
SHELL = (-17, 21, 46, 54, -41, -21)      # boîte englobante de la coque du terrain (x1, x2, y1, y2, z1, z2), buts compris
LOCKER = (-4, 4, 46, 52, -20, -14)       # coque du vestiaire
OLD_SHAFT = (-2, 1, 52, 66, -18, -15)    # emplacement de l'ancien puits (coque y 52..62, margelle y 63, piquets y 64..65) : rebouché
# volumes de sélecteur (x, y, z entiers, dx/dy/dz = nombre de cases - 1)
FOOT_ZONE = 'x=-17,y=46,z=-41,dx=38,dy=8,dz=27'         # x -17..21, y 46..54, z -41..-14 : terrain et vestiaire ; PAS la surface (pieds en y 64)
BALL_BOX = 'x=-16,y=47,z=-40,dx=36,dy=6,dz=18'          # intérieur du terrain, buts et renfoncements compris (x -16..20, y 47..53) : sans vestiaire
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
    la hitbox du joueur (±0,3) ne touche pas le bord du socle voisin (x ou z dès ce bord), donc un joueur qui arrive ou passe à côté ne rejoint pas une équipe."""
    x, z = PADS[key][:2]
    return f'x={x + 0.3:.1f},y=48,z={z + 0.3:.1f},dx=0.4,dy=0.5,dz=0.4'


# ------------------------------------------------------------------ fonctions écrites
def refill_lines(W):
    """Rebouche l'ancien puits (y 53..63, x -2..1, z -18..-15) avec les blocs du spawn (W, l'air n'y est pas stocké) : un fill par couche
    identique sur les 16 cases, sinon un setblock par case. y 52 est le plafond du vestiaire (coque LOCKER) : on n'y touche pas."""
    x1, x2, _, _, z1, z2 = OLD_SHAFT
    return ['# ancien puits : rebouché avec les blocs du spawn (roche, terre, avenue)'] + TW.restore_lines(W, (x1, x2, 53, 63, z1, z2))


def build_lines(W):
    """foot/build : coque, creux, sol, buts, vestiaire, lumières, rebouchage de l'ancien puits, ancien tapis rendu à l'herbe, tapis d'entrée,
    haie ouverte, but blanc, bloc témoin (en dernier), panneaux, drapeau foot2 (storage mg:lobby ; foot1 = tapis d'avant, x -19..-17).
    W = theme_world.W (les blocs du spawn, pour le rebouchage)."""
    x1, x2 = -14, 18
    B = ['# ⚽ Terrain de foot souterrain : terrain, buts, vestiaire, tapis d\'entrée (généré par tools/lobby/gen_foot.py)',
         # coques (la roche de l'île est remplie sur place : tout est posé par-dessus)
         f'fill {x1} 46 -41 {x2} 54 -21 minecraft:deepslate_bricks',
         'fill -17 46 -34 -14 51 -28 minecraft:deepslate_bricks', 'fill 18 46 -34 21 51 -28 minecraft:deepslate_bricks',
         'fill -4 46 -20 4 52 -14 minecraft:deepslate_bricks',
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
    # lumière : lanternes de mer au plafond (tout est éclairé, rien n'apparaît), sol du vestiaire
    B += [f'setblock {x} 54 {z} minecraft:sea_lantern' for x in (-11, -6, -1, 4, 9, 14) for z in (-38, -33, -28, -23)]
    B += ['setblock -16 51 -31 minecraft:sea_lantern', 'setblock 20 51 -31 minecraft:sea_lantern',
          'fill -3 47 -19 3 47 -15 minecraft:deepslate_tiles',
          'setblock -3 52 -19 minecraft:sea_lantern', 'setblock 3 52 -19 minecraft:sea_lantern',
          'setblock -3 52 -15 minecraft:sea_lantern', 'setblock 3 52 -15 minecraft:sea_lantern']
    for key, (px, pz, blk, _, _) in PADS.items():
        B.append(f'fill {px} 47 {pz} {px + 1} 47 {pz + 1} minecraft:{blk}')
    B += refill_lines(W)
    # piquets de l'ancien puits (y 64..65, avec leur lanterne) : la prod en a encore ; jamais lues par theme_world.load (lignes « execute »)
    B += [f'execute if block {x} 64 {z} minecraft:polished_blackstone_wall run fill {x} 64 {z} {x} 65 {z} minecraft:air'
          for x in (-2, 1) for z in (-18, -15)]
    # tapis d'avant (x -19..-17, z -19..-17) : l'herbe et les fleurs du spawn reviennent
    B += ['# tapis d\'avant : rendu à l\'herbe'] + TW.restore_lines(W, OLD_PAD)
    # ancienne entrée de l'avenue nord (tapis, but blanc, haie ouverte) : décor du spawn rendu, l'anneau de l'ancienne place des plots en herbe
    B += ['# ancienne entrée de l\'avenue nord : décor du spawn rendu']
    B += [' '.join(l.split(' ')[:-1] + [PLOT_RING.get(TW.bid(l.split(' ')[-1]), l.split(' ')[-1])]) for l in TW.restore_lines(W, OLD_ENTRY)]
    # le bloc témoin est posé en TOUT DERNIER (juste avant les panneaux) : une construction interrompue ne le laisse jamais en place
    return B + [f'setblock {SENT[0]} {SENT[1]} {SENT[2]} minecraft:lodestone', 'function mg:foot/labels',
                'execute if score $ftoff mg.st matches 1 run function mg:foot/entry_close',
                'data modify storage mg:lobby foot2 set value 1b']


FIXED_E = 'billboard:"fixed",Rotation:[-90f,0f]'      # panneau fixe, face à l'est (l'avenue)


def _text(pos, parts, scale, bg, extra='billboard:"center"'):
    return (f'summon minecraft:text_display {pos} {{Tags:["mg.ftd"],{extra},background:{bg},text:{C.js(parts)},' + TF.format(s=scale) + '}')


def labels_lines():
    """foot/labels : panneaux du but blanc (tapis d'entrée), des socles et du vestiaire (tag mg.ftd)."""
    L = ['# Panneaux du terrain de foot (tag mg.ftd, sans mg.lby : lobby/deco tuerait tout ce qui le porte)',
         'kill @e[type=minecraft:text_display,tag=mg.ftd]',
         ]
    for key, (px, pz, blk, txt, col) in PADS.items():
        L.append(_text(f'{px + 1}.0 49.6 {pz + 1}.0', [{'text': txt, 'color': col, 'bold': True}], 0.8, 1342177280))
    L.append(_text('0.5 50.9 -14.1', [
        {'text': '⚽ TERRAIN DE FOOT', 'color': 'green', 'bold': True},
        {'text': '\nSocle rouge ou bleu : choisis ton équipe · blanc : la quitter · or : retour au spawn.', 'color': 'white'},
        {'text': '\nLe point va à l\'équipe adverse du but, quel que soit le tireur.', 'color': 'gray'}],
        0.5, 1342177280, extra='billboard:"fixed",Rotation:[180f,0f],line_width:300'))
    return L


def write(W):
    """Écrit foot/build, labels, pad, go, entry_open, entry_close, build_start, build_go. W = theme_world.W (rebouchage de l'ancien puits)."""
    w = C.w
    w('foot/build', build_lines(W))
    w('foot/labels', labels_lines())
    w('foot/go', ['# @s passe le portail du foot du hub (mg:hub/enter_foot) : descend sur le terrain, devant la porte du vestiaire, face au terrain',
                  'tp @s 0.5 48 -16.5 facing 0.5 48 -22.5',
                  'execute at @s run playsound minecraft:block.portal.travel master @s ~ ~ ~ 0.2 1.8',
                  'execute at @s run particle minecraft:portal ~ ~1 ~ 0.3 0.6 0.3 0.5 30'])
    w('foot/entry_close', ['# Terrain désactivé (le portail du hub refuse l\'entrée : $ftoff), panneaux retirés', 'kill @e[type=minecraft:text_display,tag=mg.ftd]'])
    w('foot/entry_open', ['# Terrain réactivé : panneaux reposés', 'function mg:foot/labels'])
    w('foot/build_start', ['# Charge la zone puis construit (2 s plus tard)', f'forceload add {FORCELOAD}', 'schedule function mg:foot/build_go 2s'])
    w('foot/build_go', ['function mg:foot/build', f'forceload remove {FORCELOAD}', 'function mg:core/forceloads',
                        'tellraw @a[tag=mg.admin] {"text":"⚽ Terrain de foot souterrain construit (entrée : portail du foot du hub des portails).","color":"gold"}'])
