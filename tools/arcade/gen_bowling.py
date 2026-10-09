"""🎳 Bowling façon Wii Sports — id 214, salle de 8 pistes en z 35170 (x -34..33, z 35130..35185, y 62..76).

    flock /home/claude/gen.lock python3 tools/arcade/gen_bowling.py .

Chacun sa piste, tout le monde joue en même temps (8 joueurs max : au-delà, les joueurs en trop regardent en
spectateur — une piste partagée doublerait la durée de la partie). FRAMES frames (5 par défaut, ~5 min ; 10 = partie
réglementaire), 2 lancers par frame, strike = 10 + 2 lancers suivants, spare = 10 + 1 lancer suivant, lancers bonus au
dernier frame. Le meilleur total gagne (égalité = match nul).

Lancer : se placer latéralement derrière la ligne de faute, viser du regard (±8°), clic droit avec la boule quand la
jauge de puissance (barre d'action, oscillante) est au bon niveau ; accroupi pendant le clic = effet (la boule part en
courbe vers le centre après 8 blocs).

Physique (scores ×1000, repère de la piste : bx latéral depuis l'axe, bz depuis la ligne de faute, 2 sous-pas par tick) :
boule → quille par distance (r 0,5), quille projetée → quille (r 0,45) en chaîne, rebond sur les bords (kickbacks),
frottement des quilles. Réglages testés hors jeu (simulateur Python) : ~35-40 % de strikes dans la poche, ~20 % pour un lancer correct,
souvent 7-9 quilles ailleurs.
"""
import math
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js

GID = 214
FRAMES = C.param('frames', 5)              # 5 = format court (~5 min), 10 = règlement
LIMIT = (FRAMES * 60 + 60) * 20            # limite de sécurité (ticks)
ZF = 35160                                 # ligne de faute (début de la piste) ; piste z 35160..35179
NL = 8
CXS = [-25 + 7 * l for l in range(NL)]     # bloc central de chaque piste (axe en x CX + 0,5)
ORDER = [3, 4, 2, 5, 1, 6, 0, 7]           # pistes attribuées d'abord au centre
BALLS = ['ender_pearl', 'magma_cream', 'slime_ball', 'fire_charge', 'snowball', 'ender_eye', 'heart_of_the_sea', 'firework_star']
COLORS = ['purple', 'orange', 'lime', 'red', 'light_blue', 'cyan', 'blue', 'pink']
HEX = ['#B266FF', '#FF9933', '#88FF33', '#FF4444', '#66CCFF', '#33DDDD', '#4477FF', '#FF77CC']
PIN_SP, PIN_RZ, PIN_Z0 = 870, 750, 16000   # quilles : écart latéral, écart entre rangées, quille de tête
RB, RP = 500, 450                          # rayons de contact boule→quille, quille→quille
HOOKZ = 8000                               # l'effet agit après 8 blocs (huile)
Y = 65                                     # surface de la piste
Z0, Z1, X0, X1 = 35130, 35184, -34, 33     # murs de la salle


def Z(lz):
    return ZF + lz


# ───────────────────────────── construction (5 étapes, 2 ticks d'écart) ─────────────────────────────
B1 = ['# 🎳 Bowling — construction 1/5 : vide, dalle, sol']
B1 += [f'fill {X0 - 1} {y} {Z0 - 1} {X1 + 1} {y} {Z1 + 1} minecraft:air' for y in range(62, 78)]
B1 += [f'fill {X0} 63 {Z0} {X1} 63 {Z1} minecraft:smooth_stone',
       f'fill {X0} 64 {Z0} {X1} 64 35153 minecraft:dark_oak_planks',
       f'fill {X0} 64 35154 {X1} 64 35183 minecraft:polished_deepslate',
       # bandes de moquette rétro dans le salon
       f'fill {X0 + 1} 64 35139 {X1 - 1} 64 35139 minecraft:purple_terracotta',
       f'fill {X0 + 1} 64 35145 {X1 - 1} 64 35145 minecraft:cyan_terracotta',
       f'fill {X0 + 1} 64 35153 {X1 - 1} 64 35153 minecraft:purple_terracotta',
       'schedule function mg:bowl/build_2 2t']
w('bowl/build_1', B1)

B2 = ['# 🎳 construction 2/5 : murs, plafond, néons']
B2 += [f'fill {X0} 64 {Z0} {X0} 76 {Z1} minecraft:black_concrete', f'fill {X1} 64 {Z0} {X1} 76 {Z1} minecraft:black_concrete',
       f'fill {X0} 64 {Z0} {X1} 76 {Z0} minecraft:black_concrete', f'fill {X0} 64 {Z1} {X1} 76 {Z1} minecraft:black_concrete',
       f'fill {X0} 76 {Z0} {X1} 76 {Z1} minecraft:black_concrete',
       f'fill {X0} 64 35183 {X1} 75 35183 minecraft:black_concrete',
       # néons : bandes roses et vertes le long des murs, bandeau au-dessus du comptoir
       f'fill {X0} 71 {Z0 + 1} {X0} 71 35182 minecraft:pearlescent_froglight', f'fill {X1} 71 {Z0 + 1} {X1} 71 35182 minecraft:pearlescent_froglight',
       f'fill {X0} 69 {Z0 + 1} {X0} 69 35182 minecraft:verdant_froglight', f'fill {X1} 69 {Z0 + 1} {X1} 69 35182 minecraft:verdant_froglight',
       f'fill {X0 + 1} 72 {Z0} {X1 - 1} 72 {Z0} minecraft:pearlescent_froglight',
       f'fill {X0 + 1} 74 {Z0} {X1 - 1} 74 {Z0} minecraft:ochre_froglight',
       # plafond du salon : rampes lumineuses
       f'fill {X0 + 1} 76 35136 {X1 - 1} 76 35136 minecraft:ochre_froglight',
       f'fill {X0 + 1} 76 35142 {X1 - 1} 76 35142 minecraft:ochre_froglight',
       f'fill {X0 + 1} 76 35148 {X1 - 1} 76 35148 minecraft:ochre_froglight']
B2 += [f'fill {cx} 76 35154 {cx} 76 35178 minecraft:sea_lantern' for cx in CXS]
B2 += ['schedule function mg:bowl/build_3 2t']
w('bowl/build_2', B2)

B3 = ['# 🎳 construction 3/5 : les 8 pistes (parquet, gouttières, ligne de faute, retour de boule, fosse, cache)']
B3 += [f'fill -29 62 35180 28 62 35182 minecraft:black_wool', f'fill -29 63 35180 28 64 35182 minecraft:air']
for l, cx in enumerate(CXS):
    col = COLORS[l]
    B3 += [f'# piste {l + 1}',
           f'fill {cx - 2} 64 35154 {cx + 2} 64 35158 minecraft:birch_planks',
           f'fill {cx - 2} 64 35159 {cx + 2} 64 35159 minecraft:red_concrete',
           f'fill {cx - 1} 64 {ZF} {cx + 1} 64 35179 minecraft:birch_planks',
           # flèches de visée et mouches
           f'setblock {cx} 64 35164 minecraft:dark_oak_planks', f'setblock {cx - 1} 64 35165 minecraft:dark_oak_planks',
           f'setblock {cx + 1} 64 35165 minecraft:dark_oak_planks', f'setblock {cx} 64 35157 minecraft:stripped_dark_oak_wood',
           # gouttières
           f'fill {cx - 2} 64 {ZF} {cx - 2} 64 35179 minecraft:air', f'fill {cx + 2} 64 {ZF} {cx + 2} 64 35179 minecraft:air',
           f'fill {cx - 2} 63 {ZF} {cx - 2} 63 35179 minecraft:polished_blackstone', f'fill {cx + 2} 63 {ZF} {cx + 2} 63 35179 minecraft:polished_blackstone',
           # séparations et kickbacks
           f'fill {cx - 3} 64 35154 {cx - 3} 64 35173 minecraft:polished_deepslate', f'fill {cx + 3} 64 35154 {cx + 3} 64 35173 minecraft:polished_deepslate',
           f'fill {cx - 3} 64 35174 {cx - 3} 66 35182 minecraft:dark_oak_planks', f'fill {cx + 3} 64 35174 {cx + 3} 66 35182 minecraft:dark_oak_planks',
           # retour de boule (à droite de la zone de lancer)
           f'fill {cx + 3} 65 35155 {cx + 3} 65 35157 minecraft:black_concrete', f'setblock {cx + 3} 65 35154 minecraft:polished_blackstone_wall',
           f'setblock {cx + 3} 65 35158 minecraft:{col}_concrete',
           # cache au-dessus des quilles : tableau des scores
           f'fill {cx - 3} 67 35180 {cx + 3} 75 35180 minecraft:black_concrete',
           f'fill {cx - 3} 67 35180 {cx + 3} 67 35180 minecraft:{col}_concrete', f'fill {cx - 3} 74 35180 {cx + 3} 74 35180 minecraft:{col}_concrete',
           # cage invisible de la zone de lancer (on ne marche pas sur la piste)
           f'fill {cx - 3} 65 35153 {cx - 3} 67 35159 minecraft:barrier replace minecraft:air',
           f'fill {cx + 3} 65 35153 {cx + 3} 67 35159 minecraft:barrier replace minecraft:air',
           f'fill {cx - 2} 65 35153 {cx + 2} 67 35153 minecraft:barrier', f'fill {cx - 2} 65 {ZF} {cx + 2} 67 {ZF} minecraft:barrier']
B3 += ['schedule function mg:bowl/build_4 2t']
w('bowl/build_3', B3)

B4 = ['# 🎳 construction 4/5 : salon (banquettes, tables), comptoir, casiers à chaussures, râteliers, plantes']
for l, cx in enumerate(CXS):
    B4 += [f'fill {cx - 3} 65 35149 {cx + 3} 65 35152 minecraft:{COLORS[l]}_carpet',
           f'fill {cx - 2} 65 35150 {cx + 2} 65 35150 minecraft:crimson_stairs[facing=north]',
           f'setblock {cx - 3} 65 35150 minecraft:crimson_planks', f'setblock {cx + 3} 65 35150 minecraft:crimson_planks',
           f'setblock {cx} 65 35152 minecraft:dark_oak_fence', f'setblock {cx} 66 35152 minecraft:dark_oak_pressure_plate',
           f'setblock {cx - 3} 66 35150 minecraft:lantern']
B4 += ['fill -14 65 35136 13 65 35136 minecraft:quartz_bricks', 'fill -14 66 35136 13 66 35136 minecraft:smooth_quartz_slab',
       'fill -14 65 35135 -14 66 35132 minecraft:quartz_bricks', 'fill 13 65 35135 13 66 35132 minecraft:quartz_bricks',
       'fill -13 65 35131 12 67 35131 minecraft:barrel[facing=south]', 'fill -13 68 35131 12 68 35131 minecraft:dark_oak_slab',
       'setblock -6 67 35136 minecraft:lantern', 'setblock 5 67 35136 minecraft:lantern', 'setblock 0 67 35136 minecraft:bell[attachment=floor,facing=south]',
       'setblock -10 65 35133 minecraft:jukebox', 'setblock 9 65 35133 minecraft:note_block', 'setblock 8 65 35133 minecraft:brewing_stand']
for x in range(-12, 13, 3):
    B4 += [f'setblock {x} 65 35138 minecraft:dark_oak_fence', f'setblock {x} 66 35138 minecraft:red_carpet']
for x in (-31, 30):          # râteliers à boules
    B4 += [f'fill {x} 65 35134 {x + 1} 65 35147 minecraft:polished_blackstone_slab[type=top]']
for (x, z) in [(-32, 35131), (31, 35131), (-32, 35152), (31, 35152), (-16, 35131), (15, 35131)]:
    B4 += [f'setblock {x} 65 {z} minecraft:potted_bamboo']
for (x, z) in [(-25, 35132), (-20, 35132), (19, 35132), (24, 35132)]:      # bornes d'arcade
    B4 += [f'fill {x} 65 {z} {x + 1} 66 {z} minecraft:black_concrete', f'fill {x} 67 {z} {x + 1} 67 {z} minecraft:magenta_stained_glass',
           f'fill {x} 66 {z + 1} {x + 1} 66 {z + 1} minecraft:light_blue_stained_glass_pane']
B4 += ['schedule function mg:bowl/build_5 2t']
w('bowl/build_4', B4)


def tdisp(x, y, z, yaw, tags, text, scale, extra=''):
    return (f'summon minecraft:text_display {x} {y} {z} {{Tags:["mg.bowl",{",".join(json_tags(tags))}],Rotation:[{yaw}f,0f],'
            f'billboard:"fixed",alignment:"center",line_width:400,{extra}'
            f'transformation:{{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[{scale}f,{scale}f,{scale}f]}},'
            f'text:{text}}}')


def json_tags(tags):
    return [f'"{t}"' for t in tags]


def snbt_text(parts):
    """[(texte, couleur, gras)] → composant SNBT."""
    out = []
    for t, c, b in parts:
        out.append('{text:"' + t + '",color:"' + c + '"' + (',bold:true' if b else '') + '}')
    return '[' + ','.join(out) + ']'


def ball_display(x, y, z, model, tags, scale=0.55):
    return (f'summon minecraft:item_display {x} {y} {z} {{Tags:["mg.bowl",{",".join(json_tags(tags))}],item:{{id:"minecraft:{model}",count:1}},'
            f'billboard:"center",teleport_duration:1,transformation:{{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],'
            f'translation:[0f,0f,0f],scale:[{scale}f,{scale}f,{scale}f]}}}}')


# tableau : FRAMES cases + Total sur 6,4 blocs de large
CELL_W = 6.4 / (FRAMES + 1)
CELL_S = round(min(1.3, CELL_W / 0.8), 2)
B5 = ['# 🎳 construction 5/5 : entités (tableaux des scores, boules décoratives, enseigne) puis quilles des pistes occupées',
      'kill @e[tag=mg.bowl]']
for l, cx in enumerate(CXS):
    for k in range(1, FRAMES + 2):      # vu depuis la zone de lancer (regard vers +z), +x est à gauche
        x = round(cx + 0.5 + 3.2 - CELL_W / 2 - (k - 1) * CELL_W, 3)
        lab = str(k) if k <= FRAMES else 'Total'
        B5.append(tdisp(x, 68.15, 35179.95, 180, ['mg.bbc', f'mg.bbc{l}_{k}'],
                        snbt_text([(lab, 'gray', False), ('\\n ', 'white', True), ('\\n ', 'gold', False)]), CELL_S,
                        'background:-1442840576,'))
    B5.append(tdisp(cx + 0.5, 70.4, 35179.95, 180, ['mg.bbn', f'mg.bbn{l}'], snbt_text([('Piste libre', 'dark_gray', False)]), 2,
                    'background:0,shadow:true,'))
    B5.append(tdisp(cx + 0.5, 72.6, 35179.95, 180, ['mg.bbl'], '{text:"PISTE ' + str(l + 1) + '",color:"' + HEX[l] + '",bold:true}', 1.3,
                    'background:0,brightness:{sky:15,block:15},'))
    B5.append(ball_display(cx + 3.5, 66.3, 35156.5, BALLS[l], ['mg.bdeco']))
for side in (-31, 30):
    for i, z in enumerate(range(35134, 35148)):
        B5.append(ball_display(side + 0.5 + (i % 2), 65.75, z + 0.5, BALLS[(i + side) % NL], ['mg.bdeco'], 0.5))
B5.append(tdisp(0.5, 69.4, Z0 + 2.1, 0, ['mg.bdeco'], snbt_text([('🎳 BOWLING ', '#FF77CC', True), ('NEO', '#66CCFF', True)]), 4,
                'background:0,shadow:true,brightness:{sky:15,block:15},'))
B5.append(tdisp(0.5, 68.7, Z0 + 2.1, 0, ['mg.bdeco'], snbt_text([('Chaussures · Boules · Snacks', 'gray', False)]), 1.5, 'background:0,'))
B5 += ['execute as @a[tag=mg.bwl] run function mg:bowl/rack_me',
       'execute as @a[tag=mg.bwl] run function mg:bowl/name']
w('bowl/build_5', B5)
w('bowl/build', ['# (OP) Construit / remet à neuf la salle de bowling (5 étapes sur 8 ticks)', 'function mg:bowl/build_1'])

# ───────────────────────────── quilles ─────────────────────────────
PINS = []
for r in range(4):
    for k in range(r + 1):
        PINS.append(((2 * k - r) * PIN_SP // 2, PIN_Z0 + r * PIN_RZ))
SC = 3.0                                    # bougie blanche ×3 : 0,375 × 1,125 bloc
RAD = 0.1875


def pin_tf(q, t):
    return ('{left_rotation:[%sf,%sf,%sf,%sf],right_rotation:[0f,0f,0f,1f],translation:[%sf,%sf,%sf],scale:[%sf,%sf,%sf]}'
            % tuple([round(v, 4) for v in q] + [round(v, 4) for v in t] + [SC] * 3))


STAND = pin_tf((0, 0, 0, 1), (-1.5, 0, -1.5))
s45 = math.sqrt(0.5)
c = (1.5, 0, 1.5)
FALL = {  # direction : (quaternion, matrice appliquée à c)
    'zp': ((s45, 0, 0, s45), lambda x, y, z: (x, -z, y)),
    'zm': ((-s45, 0, 0, s45), lambda x, y, z: (x, z, -y)),
    'xp': ((0, 0, -s45, s45), lambda x, y, z: (y, -x, z)),
    'xm': ((0, 0, s45, s45), lambda x, y, z: (-y, x, z)),
}
FALL_TF = {}
for d, (q, R) in FALL.items():
    rc = R(*c)
    FALL_TF[d] = pin_tf(q, (-rc[0], RAD - rc[1], -rc[2]))

for l, cx in enumerate(CXS):
    L = [f'# Quilles de la piste {l + 1} (10 en triangle)']
    base = cx * 1000 + 500
    for (px, pz) in PINS:
        L += [f'summon minecraft:block_display {(base + px) / 1000} {Y} {(ZF * 1000 + pz) / 1000} {{Tags:["mg.bowl","mg.bpin","mg.bnew"],'
              f'teleport_duration:1,block_state:{{Name:"minecraft:white_candle",Properties:{{candles:"1",lit:"false"}}}},transformation:{STAND}}}',
              f'scoreboard players set @e[type=minecraft:block_display,tag=mg.bnew] mg.bx {px}',
              f'scoreboard players set @e[type=minecraft:block_display,tag=mg.bnew] mg.bz {pz}',
              'tag @e[type=minecraft:block_display,tag=mg.bnew] remove mg.bnew']
    L += [f'scoreboard players set @e[type=minecraft:block_display,tag=mg.bpin,x={cx - 3},y=63,z=35174,dx=7,dy=4,dz=10] mg.bln {l}',
          f'scoreboard players set @e[type=minecraft:block_display,tag=mg.bpin,x={cx - 3},y=63,z=35174,dx=7,dy=4,dz=10] mg.bcx {base}',
          f'particle minecraft:cloud {cx + 0.5} 66 {ZF + 17} 1 0.3 1 0.02 12',
          f'playsound minecraft:block.wooden_trapdoor.close master @a[tag=!mg.surv,x={cx},y=65,z=35160,distance=..30] {cx + 0.5} 65 {ZF + 17} 1 0.6']
    w(f'bowl/rack_{l}', L)
w('bowl/rack', ['# Remet 10 quilles sur la piste #ln (les anciennes de la piste sont retirées)',
                'execute as @e[type=minecraft:block_display,tag=mg.bpin] if score @s mg.bln = #ln mg.st run kill @s'] +
  [f'execute if score #ln mg.st matches {l} run function mg:bowl/rack_{l}' for l in range(NL)])
w('bowl/rack_me', ['# @s (joueur) : quilles de sa piste', 'scoreboard players operation #ln mg.st = @s mg.bln', 'function mg:bowl/rack'])

# ───────────────────────────── préparation / départ ─────────────────────────────
w('bowl/prepare', [
    '# 🎳 Bowling — préparation : salle (asynchrone), pistes attribuées, joueurs en trop spectateurs',
    'function mg:bowl/build_1',
    'scoreboard players set $px mg.st 0', 'scoreboard players set $py mg.st 72', 'scoreboard players set $pz mg.st 35146',
    'scoreboard players set $bt mg.st 0', 'scoreboard players set $bend mg.st 0',
    'tag @a remove mg.bwl', 'tag @a remove mg.bnr', 'scoreboard players reset * mg.bln',
    'gamemode adventure @a[tag=mg.play]', 'clear @a[tag=mg.play]',
    'scoreboard players set #km1 mg.st -1'] +
    [f'execute as @a[tag=mg.play,tag=!mg.bwl,limit=1,sort=random] run function mg:bowl/assign {{l:{l},c:"{CXS[l] + 0.5}",b:{CXS[l] * 1000 + 500}}}' for l in ORDER] +
    ['execute as @a[tag=mg.play,tag=!mg.bwl] run function mg:bowl/extra'])
w('bowl/assign', ['# @s : piste $(l) (axe x $(c))',
                  'tag @s add mg.bwl',
                  '$scoreboard players set @s mg.bln $(l)', '$scoreboard players set @s mg.bcx $(b)',
                  '$tp @s $(c) 65 35156.5 0 0',
                  '$data modify storage mg:bowl L$(l) set value {l:$(l),f:1,a:"",b:"",c:"",t:0,' +
                  ','.join([f'f{k}:" "' for k in range(1, FRAMES + 1)] + [f'c{k}:" "' for k in range(1, FRAMES + 1)]) + '}',
                  'scoreboard players set @s mg.bph 8', 'scoreboard players set @s mg.btm 0',
                  'scoreboard players set @s mg.bfr 1', 'scoreboard players set @s mg.brl 1', 'scoreboard players set @s mg.bsc 0',
                  'scoreboard players set @s mg.bcu 0', 'scoreboard players set @s mg.bfs 0', 'scoreboard players set @s mg.bxs 0',
                  'scoreboard players set @s mg.bp1n 0', 'scoreboard players set @s mg.bp2n 0', 'scoreboard players set @s mg.bp1f 0',
                  'scoreboard players set @s mg.bp2f 0', 'scoreboard players set @s mg.bp1s 0', 'scoreboard players set @s mg.bp2s 0',
                  'scoreboard players set @s mg.br1 0', 'scoreboard players set @s mg.br2 0', 'scoreboard players set @s mg.bpw 0',
                  'scoreboard players set @s mg.bpd 1'])
w('bowl/extra', ['# @s : plus de piste libre → spectateur de la partie',
                 'tag @s remove mg.play', 'tag @s add mg.out', 'gamemode spectator @s',
                 'tp @s 0.5 72 35146.5 0 20',
                 'tellraw @s ' + js([{'text': '🎳 Les 8 pistes sont prises : tu regardes cette partie en spectateur.', 'color': 'gray'}])])
w('bowl/name', ['# @s : son nom sur le tableau de sa piste (résolu par set_name sur un objet temporaire)',
                'item replace entity @s hotbar.8 with minecraft:paper',
                'item modify entity @s hotbar.8 {function:"minecraft:set_name",entity:"this",target:"custom_name",name:{selector:"@s"}}',
                'data modify storage mg:bowl n set value {text:"?"}',
                'data modify storage mg:bowl n set from entity @s Inventory[{Slot:8b}].components."minecraft:custom_name"',
                'item replace entity @s hotbar.8 with minecraft:air',
                'execute store result storage mg:bowl q.l int 1 run scoreboard players get @s mg.bln',
                'function mg:bowl/name_set with storage mg:bowl q'])
w('bowl/name_set', ['$data modify entity @e[type=minecraft:text_display,tag=mg.bbn$(l),limit=1] text set from storage mg:bowl n'])

BALL_ITEMS = []
for l in range(NL):
    BALL_ITEMS.append(f'execute if score @s mg.bln matches {l} run item replace entity @s hotbar.0 with minecraft:warped_fungus_on_a_stick['
                      f'minecraft:item_model="minecraft:{BALLS[l]}",minecraft:custom_data={{mg_bowl:1b}},minecraft:unbreakable={{}},'
                      'minecraft:custom_name={"text":"Boule de bowling","color":"' + HEX[l] + '","italic":false},'
                      'minecraft:lore=[{"text":"Clic droit : lancer (puissance de la jauge)","color":"gray","italic":false},'
                      '{"text":"Accroupi en lançant : effet","color":"gray","italic":false}]]')
w('bowl/give', ['# @s : boule en main (modèle de la couleur de sa piste)', 'clear @s minecraft:warped_fungus_on_a_stick[minecraft:custom_data={mg_bowl:1b}]'] +
  BALL_ITEMS + ['scoreboard players reset @s mg.blu',
                'execute at @s run playsound minecraft:block.piston.extend master @s ~ ~ ~ 0.5 0.7'])

w('bowl/go', ['# 🎳 Départ',
              'scoreboard players set $bt mg.st 0',
              'scoreboard objectives setdisplay sidebar mg.bsc',
              'effect give @a[tag=mg.play] minecraft:saturation infinite 0 true',
              'effect give @a[tag=mg.play] minecraft:resistance infinite 4 true',
              'execute as @a[tag=mg.bwl] run function mg:bowl/name',
              'execute as @a[tag=mg.bwl] run function mg:bowl/to_aim',
              'tellraw @a[tag=mg.play] ' + js([{'text': '🎳 BOWLING : ', 'color': 'light_purple', 'bold': True},
                                               {'text': f'{FRAMES} frames, chacun sur sa piste. Place-toi derrière la ligne rouge, vise du regard, '
                                                        'et fais clic droit avec la boule quand la jauge de puissance est au bon niveau. '
                                                        'Accroupi en lançant = effet. Strike = 10 + les 2 lancers suivants, spare = 10 + le suivant.',
                                                'color': 'gray'}]),
              'execute as @a[tag=!mg.surv,tag=mg.play] at @s run playsound minecraft:music_disc.cat record @s ~ ~ ~ 0.25 1'])

# ───────────────────────────── tick ─────────────────────────────
w('bowl/tick', ['# 🎳 Bowling — tick', 'scoreboard players add $bt mg.st 1', 'scoreboard players set #km1 mg.st -1',
                'scoreboard players set $bsub mg.st 0', 'function mg:bowl/phys',
                'scoreboard players set $bsub mg.st 1', 'function mg:bowl/phys',
                'execute as @e[type=minecraft:item_display,tag=mg.bball] run function mg:bowl/pos',
                'execute as @e[type=minecraft:block_display,tag=mg.bpmv] run function mg:bowl/pos_pin',
                'execute as @a[tag=mg.play,tag=mg.bwl] at @s run function mg:bowl/ptick',
                'scoreboard players reset @a[scores={mg.blu=1..}] mg.blu',
                'scoreboard players reset @a[tag=mg.play,scores={mg.qs=1..}] mg.qs',
                f'kill @e[type=minecraft:item,x={X0},y=60,z={Z0},dx={X1 - X0},dy=20,dz={Z1 - Z0}]',
                f'execute if score $bt mg.st matches {LIMIT - 1200} run tellraw @a[tag=mg.play] {{"text":"🎳 Plus qu\'une minute !","color":"gold"}}',
                f'execute if score $state mg.st matches 2 if score $bt mg.st matches {LIMIT}.. run return run function mg:bowl/finish',
                # tout le monde a fini → résultats 3 s plus tard
                'execute store result score $alive mg.st if entity @a[tag=mg.play]',
                'execute store result score #n mg.st if entity @a[tag=mg.play,tag=mg.bwl,scores={mg.bph=..8}]',
                'execute if score $alive mg.st matches 1.. if score #n mg.st matches 0 run scoreboard players add $bend mg.st 1',
                'execute if score $state mg.st matches 2 if score $bend mg.st matches 60.. run return run function mg:bowl/finish',
                'execute if score $state mg.st matches 2 if score $alive mg.st matches 0 run function mg:core/draw'])
w('bowl/phys', ['# Un sous-pas de physique (2 par tick) : boules puis quilles en mouvement',
                'execute as @e[type=minecraft:item_display,tag=mg.bball] run function mg:bowl/ball_step',
                'execute as @e[type=minecraft:block_display,tag=mg.bpmv] run function mg:bowl/pin_step'])
w('bowl/pos', ['# @s (boule ou quille) : position du monde = repère de la piste (×1000)',
               'scoreboard players operation #w mg.st = @s mg.bcx', 'scoreboard players operation #w mg.st += @s mg.bx',
               'execute store result entity @s Pos[0] double 0.001 run scoreboard players get #w mg.st',
               f'scoreboard players set #w mg.st {ZF * 1000}', 'scoreboard players operation #w mg.st += @s mg.bz',
               'execute store result entity @s Pos[2] double 0.001 run scoreboard players get #w mg.st'])
w('bowl/pos_pin', ['# @s (quille tombée) : position, hauteur (fosse / gouttière / piste)', 'function mg:bowl/pos',
                   'execute if score @s mg.bz matches 19600.. run return run data modify entity @s Pos[1] set value 63.0d',
                   'execute unless score @s mg.bx matches -1600..1600 run return run data modify entity @s Pos[1] set value 64.0d',
                   'data modify entity @s Pos[1] set value 65.0d'])

# boule
w('bowl/ball_step', ['# @s : boule, un sous-pas',
                     'scoreboard players operation #ln mg.st = @s mg.bln',
                     f'execute if score $bsub mg.st matches 0 if score @s mg.bz matches {HOOKZ}.. unless entity @s[tag=mg.bgut] run scoreboard players operation @s mg.bvx += @s mg.bsp',
                     'scoreboard players operation @s mg.bx += @s mg.bvx', 'scoreboard players operation @s mg.bz += @s mg.bvz',
                     'execute unless entity @s[tag=mg.bgut] unless score @s mg.bx matches -1500..1500 run function mg:bowl/gutter',
                     'execute unless entity @s[tag=mg.bgut] if score @s mg.bz matches 14000..20000 run function mg:bowl/ball_pins',
                     'execute if score @s mg.bz matches 20600.. run function mg:bowl/ball_pit'])
w('bowl/gutter', ['# @s : boule dans la gouttière (plus d\'effet, plus de quilles)', 'tag @s add mg.bgut',
                  'execute if score @s mg.bx matches 1.. run scoreboard players set @s mg.bx 2000',
                  'execute if score @s mg.bx matches ..0 run scoreboard players set @s mg.bx -2000',
                  'scoreboard players set @s mg.bvx 0', 'data modify entity @s Pos[1] set value 64.3d',
                  'execute at @s run playsound minecraft:block.note_block.didgeridoo master @a[tag=!mg.surv,distance=..30] ~ ~ ~ 1 0.6'])
w('bowl/ball_pit', ['# @s : la boule tombe dans la fosse', 'execute at @s run particle minecraft:poof ~ ~ ~ 0.2 0.2 0.2 0.02 6',
                    'execute at @s run playsound minecraft:block.wool.fall master @a[tag=!mg.surv,distance=..30] ~ ~ ~ 1 0.6', 'kill @s'])
w('bowl/ball_pins', ['# @s : boule près des quilles → tests de contact avec les quilles debout de sa piste',
                     'scoreboard players operation #bx mg.st = @s mg.bx', 'scoreboard players operation #bz mg.st = @s mg.bz',
                     'scoreboard players operation #bvx mg.st = @s mg.bvx', 'scoreboard players operation #bvz mg.st = @s mg.bvz',
                     'execute as @e[type=minecraft:block_display,tag=mg.bpin,tag=!mg.bpdn] if score @s mg.bln = #ln mg.st run function mg:bowl/ball_test',
                     'scoreboard players operation @s mg.bvx = #bvx mg.st', 'scoreboard players operation @s mg.bvz = #bvz mg.st'])
w('bowl/ball_test', ['# @s : quille debout ; contact si distance à la boule < 0,5',
                     'scoreboard players operation #dx mg.st = @s mg.bx', 'scoreboard players operation #dx mg.st -= #bx mg.st',
                     f'execute unless score #dx mg.st matches -{RB}..{RB} run return 0',
                     'scoreboard players operation #dz mg.st = @s mg.bz', 'scoreboard players operation #dz mg.st -= #bz mg.st',
                     f'execute unless score #dz mg.st matches -{RB}..{RB} run return 0',
                     'scoreboard players operation #d2 mg.st = #dx mg.st', 'scoreboard players operation #d2 mg.st *= #dx mg.st',
                     'scoreboard players operation #q mg.st = #dz mg.st', 'scoreboard players operation #q mg.st *= #dz mg.st',
                     'scoreboard players operation #d2 mg.st += #q mg.st',
                     f'execute if score #d2 mg.st matches {RB * RB}.. run return 0',
                     'function mg:bowl/ball_hit'])
w('bowl/ball_hit', ['# @s : quille percutée par la boule → part dans l\'axe du choc (+ un peu de hasard), la boule ralentit et dévie',
                    f'scoreboard players set #k mg.st {RB}',
                    'scoreboard players operation @s mg.bvx = #dx mg.st', 'scoreboard players operation @s mg.bvx *= #bvz mg.st',
                    'scoreboard players operation @s mg.bvx /= #k mg.st',
                    'execute store result score #r mg.st run random value -60..60', 'scoreboard players operation @s mg.bvx += #r mg.st',
                    'scoreboard players operation @s mg.bvz = #dz mg.st', 'scoreboard players operation @s mg.bvz *= #bvz mg.st',
                    'scoreboard players operation @s mg.bvz /= #k mg.st',
                    'scoreboard players set #k mg.st 4', 'scoreboard players operation #q mg.st = #bvz mg.st', 'scoreboard players operation #q mg.st /= #k mg.st',
                    'scoreboard players operation @s mg.bvz += #q mg.st',
                    'scoreboard players set #k mg.st 8', 'scoreboard players operation #q mg.st = #bvz mg.st', 'scoreboard players operation #q mg.st /= #k mg.st',
                    'scoreboard players operation #bvz mg.st -= #q mg.st',
                    'scoreboard players set #k mg.st 5', 'scoreboard players operation #q mg.st = @s mg.bvx', 'scoreboard players operation #q mg.st /= #k mg.st',
                    'scoreboard players operation #bvx mg.st -= #q mg.st',
                    'execute at @s run playsound minecraft:entity.zombie.attack_wooden_door master @a[tag=!mg.surv,distance=..30] ~ ~ ~ 0.7 1.4',
                    'function mg:bowl/pin_fall'])
w('bowl/pin_fall', ['# @s : la quille tombe (côté de sa vitesse dominante) et glisse',
                    'tag @s add mg.bpdn', 'tag @s add mg.bpmv',
                    'scoreboard players operation #ax mg.st = @s mg.bvx', 'execute if score #ax mg.st matches ..-1 run scoreboard players operation #ax mg.st *= #km1 mg.st',
                    'scoreboard players operation #az mg.st = @s mg.bvz', 'execute if score #az mg.st matches ..-1 run scoreboard players operation #az mg.st *= #km1 mg.st',
                    f'execute if score #az mg.st >= #ax mg.st if score @s mg.bvz matches 0.. run return run data merge entity @s {{start_interpolation:0,interpolation_duration:6,transformation:{FALL_TF["zp"]}}}',
                    f'execute if score #az mg.st >= #ax mg.st run return run data merge entity @s {{start_interpolation:0,interpolation_duration:6,transformation:{FALL_TF["zm"]}}}',
                    f'execute if score @s mg.bvx matches 0.. run return run data merge entity @s {{start_interpolation:0,interpolation_duration:6,transformation:{FALL_TF["xp"]}}}',
                    f'data merge entity @s {{start_interpolation:0,interpolation_duration:6,transformation:{FALL_TF["xm"]}}}'])
w('bowl/pin_step', ['# @s : quille tombée en mouvement, un sous-pas (frottement, rebond sur les kickbacks, chocs en chaîne)',
                    'scoreboard players operation #ln mg.st = @s mg.bln',
                    'scoreboard players operation @s mg.bx += @s mg.bvx', 'scoreboard players operation @s mg.bz += @s mg.bvz',
                    'execute if score @s mg.bx matches 2300.. if score @s mg.bvx matches 1.. run function mg:bowl/kick',
                    'execute if score @s mg.bx matches ..-2300 if score @s mg.bvx matches ..-1 run function mg:bowl/kick',
                    'scoreboard players set #k mg.st 16',
                    'scoreboard players operation #q mg.st = @s mg.bvx', 'scoreboard players operation #q mg.st /= #k mg.st', 'scoreboard players operation @s mg.bvx -= #q mg.st',
                    'scoreboard players operation #q mg.st = @s mg.bvz', 'scoreboard players operation #q mg.st /= #k mg.st', 'scoreboard players operation @s mg.bvz -= #q mg.st',
                    # vitesse ≈ max + min/2
                    'scoreboard players operation #ax mg.st = @s mg.bvx', 'execute if score #ax mg.st matches ..-1 run scoreboard players operation #ax mg.st *= #km1 mg.st',
                    'scoreboard players operation #az mg.st = @s mg.bvz', 'execute if score #az mg.st matches ..-1 run scoreboard players operation #az mg.st *= #km1 mg.st',
                    'scoreboard players operation #S mg.st = #ax mg.st', 'scoreboard players operation #S mg.st > #az mg.st',
                    'scoreboard players operation #q mg.st = #ax mg.st', 'scoreboard players operation #q mg.st < #az mg.st',
                    'scoreboard players set #k mg.st 2', 'scoreboard players operation #q mg.st /= #k mg.st', 'scoreboard players operation #S mg.st += #q mg.st',
                    'execute if score #S mg.st matches ..24 run return run function mg:bowl/pin_stop',
                    'execute if score @s mg.bz matches 19501.. run return run function mg:bowl/pin_stop',
                    'scoreboard players operation #px mg.st = @s mg.bx', 'scoreboard players operation #pz mg.st = @s mg.bz',
                    'scoreboard players operation #mvx mg.st = @s mg.bvx', 'scoreboard players operation #mvz mg.st = @s mg.bvz',
                    'execute as @e[type=minecraft:block_display,tag=mg.bpin,tag=!mg.bpdn] if score @s mg.bln = #ln mg.st run function mg:bowl/pin_test',
                    'scoreboard players operation @s mg.bvx = #mvx mg.st', 'scoreboard players operation @s mg.bvz = #mvz mg.st'])
w('bowl/kick', ['# @s : rebond sur le côté (kickback), perd la moitié de sa vitesse latérale',
                'scoreboard players operation @s mg.bvx *= #km1 mg.st', 'scoreboard players set #k mg.st 2', 'scoreboard players operation @s mg.bvx /= #k mg.st',
                'execute at @s run playsound minecraft:block.wood.hit master @a[tag=!mg.surv,distance=..30] ~ ~ ~ 0.6 1.2'])
w('bowl/pin_stop', ['# @s : la quille s\'immobilise', 'tag @s remove mg.bpmv', 'scoreboard players set @s mg.bvx 0', 'scoreboard players set @s mg.bvz 0',
                    'function mg:bowl/pos_pin'])
w('bowl/pin_test', ['# @s : quille debout ; touchée par la quille en mouvement (#px #pz, vitesse #S) si distance < 0,45',
                    'scoreboard players operation #dx mg.st = @s mg.bx', 'scoreboard players operation #dx mg.st -= #px mg.st',
                    f'execute unless score #dx mg.st matches -{RP}..{RP} run return 0',
                    'scoreboard players operation #dz mg.st = @s mg.bz', 'scoreboard players operation #dz mg.st -= #pz mg.st',
                    f'execute unless score #dz mg.st matches -{RP}..{RP} run return 0',
                    'scoreboard players operation #d2 mg.st = #dx mg.st', 'scoreboard players operation #d2 mg.st *= #dx mg.st',
                    'scoreboard players operation #q mg.st = #dz mg.st', 'scoreboard players operation #q mg.st *= #dz mg.st',
                    'scoreboard players operation #d2 mg.st += #q mg.st',
                    f'execute if score #d2 mg.st matches {RP * RP}.. run return 0',
                    f'scoreboard players set #k mg.st {RP}', 'scoreboard players set #k3 mg.st 3', 'scoreboard players set #k4 mg.st 4',
                    'scoreboard players operation @s mg.bvx = #dx mg.st', 'scoreboard players operation @s mg.bvx *= #S mg.st',
                    'scoreboard players operation @s mg.bvx /= #k mg.st', 'scoreboard players operation @s mg.bvx *= #k3 mg.st', 'scoreboard players operation @s mg.bvx /= #k4 mg.st',
                    'scoreboard players operation @s mg.bvz = #dz mg.st', 'scoreboard players operation @s mg.bvz *= #S mg.st',
                    'scoreboard players operation @s mg.bvz /= #k mg.st', 'scoreboard players operation @s mg.bvz *= #k3 mg.st', 'scoreboard players operation @s mg.bvz /= #k4 mg.st',
                    # la quille qui frappe perd 2/5 de sa vitesse et recule d'un tiers de l'élan donné
                    'scoreboard players set #k mg.st 5',
                    'scoreboard players operation #mvx mg.st *= #k3 mg.st', 'scoreboard players operation #mvx mg.st /= #k mg.st',
                    'scoreboard players operation #mvz mg.st *= #k3 mg.st', 'scoreboard players operation #mvz mg.st /= #k mg.st',
                    'scoreboard players operation #q mg.st = @s mg.bvx', 'scoreboard players operation #q mg.st /= #k3 mg.st', 'scoreboard players operation #mvx mg.st -= #q mg.st',
                    'scoreboard players operation #q mg.st = @s mg.bvz', 'scoreboard players operation #q mg.st /= #k3 mg.st', 'scoreboard players operation #mvz mg.st -= #q mg.st',
                    'execute at @s run playsound minecraft:block.wood.break master @a[tag=!mg.surv,distance=..30] ~ ~ ~ 0.6 1.6',
                    'function mg:bowl/pin_fall'])

# ───────────────────────────── joueur : visée, lancer, attente, résultat ─────────────────────────────
w('bowl/ptick', ['# @s : joueur sur sa piste, selon sa phase (0 visée, 1 boule en route, 2 quilles qui bougent, 3 requilleur, 8 attente, 9 fini)',
                 'scoreboard players add @s mg.btm 1',
                 'execute if score @s mg.bph matches 0 run return run function mg:bowl/aim',
                 'execute if score @s mg.bph matches 1 run return run function mg:bowl/rolling',
                 'execute if score @s mg.bph matches 2 run return run function mg:bowl/settle',
                 'execute if score @s mg.bph matches 3 run return run function mg:bowl/reset',
                 'execute if score @s mg.bph matches 9 run title @s actionbar [{"text":"🎳 Partie terminée : ","color":"gray"},{"score":{"name":"@s","objective":"mg.bsc"},"color":"gold","bold":true},{"text":" points — on attend les autres…","color":"gray"}]'])
w('bowl/to_aim', ['# @s : prêt à lancer', 'scoreboard players set @s mg.bph 0', 'scoreboard players set @s mg.btm 0',
                  'scoreboard players set @s mg.bpw 0', 'scoreboard players set @s mg.bpd 1', 'function mg:bowl/give'])

# jauge : 0..100 (pas de 4 par tick, aller-retour en 2,5 s)
GAUGE = []
for i in range(21):
    lo, hi = i * 5, i * 5 + 4 if i < 20 else 100
    col = 'green' if i < 9 else ('yellow' if i < 16 else 'red')
    bar = '█' * i
    rest = '░' * (20 - i)
    GAUGE.append(f'execute if score @s mg.bpw matches {lo}..{hi} run title @s actionbar [{{"text":"Puissance ","color":"gray"}},{{"text":"{bar}","color":"{col}"}},'
                 f'{{"text":"{rest}","color":"dark_gray"}},{{"text":"  Frame ","color":"gray"}},{{"score":{{"name":"@s","objective":"mg.bfr"}},"color":"white"}},'
                 f'{{"text":"/{FRAMES} · lancer ","color":"gray"}},{{"score":{{"name":"@s","objective":"mg.brl"}},"color":"white"}} ]')
w('bowl/aim', ['# @s : visée — jauge oscillante, aperçu de la trajectoire, clic droit = lancer',
               'scoreboard players operation @s mg.bpw += @s mg.bpd', 'scoreboard players operation @s mg.bpw += @s mg.bpd',
               'scoreboard players operation @s mg.bpw += @s mg.bpd', 'scoreboard players operation @s mg.bpw += @s mg.bpd',
               'execute if score @s mg.bpw matches 100.. run scoreboard players set @s mg.bpd -1',
               'execute if score @s mg.bpw matches ..0 run scoreboard players set @s mg.bpd 1',
               'execute unless items entity @s weapon.mainhand *[minecraft:custom_data~{mg_bowl:1b}] unless items entity @s weapon.offhand *[minecraft:custom_data~{mg_bowl:1b}] unless items entity @s hotbar.* *[minecraft:custom_data~{mg_bowl:1b}] unless items entity @s inventory.* *[minecraft:custom_data~{mg_bowl:1b}] run function mg:bowl/give',
               'execute store result score #yw mg.st run data get entity @s Rotation[0] 100',
               'execute if score #yw mg.st matches 18001.. run scoreboard players remove #yw mg.st 36000',
               'execute if score #yw mg.st matches ..-18001 run scoreboard players add #yw mg.st 36000',
               'execute unless items entity @s weapon.mainhand *[minecraft:custom_data~{mg_bowl:1b}] run title @s actionbar {"text":"🎳 Prends la boule en main (barre d\'outils)","color":"yellow"}',
               'execute if items entity @s weapon.mainhand *[minecraft:custom_data~{mg_bowl:1b}] unless score #yw mg.st matches -800..800 run title @s actionbar {"text":"🎳 Vise la piste ! (le lancer sera redressé)","color":"red"}',
               'execute if items entity @s weapon.mainhand *[minecraft:custom_data~{mg_bowl:1b}] if score #yw mg.st matches -800..800 run function mg:bowl/gauge',
               'scoreboard players operation #q mg.st = @s mg.btm', 'scoreboard players set #k mg.st 3', 'scoreboard players operation #q mg.st %= #k mg.st',
               'execute if score #q mg.st matches 0 if score #yw mg.st matches -800..800 run function mg:bowl/preview',
               'execute if score @s mg.blu matches 1.. if items entity @s weapon.mainhand *[minecraft:custom_data~{mg_bowl:1b}] run return run function mg:bowl/throw',
               'execute if score @s mg.btm matches 500 run title @s actionbar {"text":"🎳 Lance vite : lancer automatique dans 5 s !","color":"red"}',
               'execute if score @s mg.btm matches 600.. run function mg:bowl/throw'])
w('bowl/gauge', GAUGE)
w('bowl/preview', ['# @s : aperçu de la trajectoire en ligne droite (pour lui seul)',
                   'execute rotated ~ 0 run particle minecraft:dust{color:[1.0,0.85,0.2],scale:0.8} ^ ^0.1 ^5 0 0 0 0 1 force @s',
                   'execute rotated ~ 0 run particle minecraft:dust{color:[1.0,0.85,0.2],scale:0.8} ^ ^0.1 ^9 0 0 0 0 1 force @s',
                   'execute rotated ~ 0 run particle minecraft:dust{color:[1.0,0.85,0.2],scale:0.8} ^ ^0.1 ^13 0 0 0 0 1 force @s',
                   'execute rotated ~ 0 run particle minecraft:dust{color:[1.0,0.6,0.2],scale:1.0} ^ ^0.1 ^17 0 0 0 0 1 force @s'])
w('bowl/throw', ['# @s : lancer — position latérale, angle (±8°), puissance de la jauge, effet si accroupi',
                 'scoreboard players operation #ln mg.st = @s mg.bln',
                 'execute store result score #lx mg.st run data get entity @s Pos[0] 1000',
                 'scoreboard players operation #lx mg.st -= @s mg.bcx',
                 'execute if score #lx mg.st matches 1300.. run scoreboard players set #lx mg.st 1300',
                 'execute if score #lx mg.st matches ..-1300 run scoreboard players set #lx mg.st -1300',
                 'execute store result score #yw mg.st run data get entity @s Rotation[0] 100',
                 'execute if score #yw mg.st matches 18001.. run scoreboard players remove #yw mg.st 36000',
                 'execute if score #yw mg.st matches ..-18001 run scoreboard players add #yw mg.st 36000',
                 'execute if score #yw mg.st matches 800.. run scoreboard players set #yw mg.st 800',
                 'execute if score #yw mg.st matches ..-800 run scoreboard players set #yw mg.st -800',
                 # vz = 150 + 1,9 × puissance (par sous-pas) ; vx = -lacet × vz / 5730 (petits angles)
                 'scoreboard players operation #vz mg.st = @s mg.bpw', 'scoreboard players set #k mg.st 19', 'scoreboard players operation #vz mg.st *= #k mg.st',
                 'scoreboard players set #k mg.st 10', 'scoreboard players operation #vz mg.st /= #k mg.st', 'scoreboard players add #vz mg.st 150',
                 'scoreboard players operation #vx mg.st = #yw mg.st', 'scoreboard players operation #vx mg.st *= #km1 mg.st',
                 'scoreboard players operation #vx mg.st *= #vz mg.st', 'scoreboard players set #k mg.st 5730', 'scoreboard players operation #vx mg.st /= #k mg.st',
                 'scoreboard players set #sp mg.st 0',
                 'execute if predicate mg:sneak run function mg:bowl/spin',
                 'scoreboard players operation #cx mg.st = @s mg.bcx',
                 'execute positioned ~ 65.32 35160.2 run summon minecraft:item_display ~ ~ ~ {Tags:["mg.bowl","mg.bball","mg.bnew"],item:{id:"minecraft:ender_pearl",count:1},billboard:"center",teleport_duration:1,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}',
                 'execute as @e[type=minecraft:item_display,tag=mg.bnew] run function mg:bowl/ball_init',
                 # quilles debout au départ du lancer
                 'scoreboard players set #pc mg.st 0',
                 'execute as @e[type=minecraft:block_display,tag=mg.bpin,tag=!mg.bpdn] if score @s mg.bln = #ln mg.st run scoreboard players add #pc mg.st 1',
                 'scoreboard players operation @s mg.bk = #pc mg.st',
                 'clear @s minecraft:warped_fungus_on_a_stick[minecraft:custom_data={mg_bowl:1b}]',
                 'scoreboard players set @s mg.bph 1', 'scoreboard players set @s mg.btm 0', 'scoreboard players reset @s mg.blu',
                 'playsound minecraft:entity.player.attack.sweep master @s ~ ~ ~ 0.8 0.6',
                 'execute if score #sp mg.st matches 0 run title @s actionbar {"text":"🎳 Lancer droit !","color":"aqua"}',
                 'execute unless score #sp mg.st matches 0 run title @s actionbar {"text":"🎳 Lancer avec effet !","color":"light_purple"}'])
w('bowl/spin', ['# effet : la boule revient vers le centre (si lancée au centre : à l\'opposé de sa direction)',
                'execute if score #lx mg.st matches 1.. run return run scoreboard players set #sp mg.st -1',
                'execute if score #lx mg.st matches ..-1 run return run scoreboard players set #sp mg.st 1',
                'execute if score #vx mg.st matches ..-1 run return run scoreboard players set #sp mg.st 1',
                'scoreboard players set #sp mg.st -1'])
w('bowl/ball_init', ['# @s : nouvelle boule (repère de la piste #ln)', 'tag @s remove mg.bnew',
                     'scoreboard players operation @s mg.bln = #ln mg.st',
                     'scoreboard players operation @s mg.bcx = #cx mg.st',
                     'scoreboard players operation @s mg.bx = #lx mg.st', 'scoreboard players set @s mg.bz 0',
                     'scoreboard players operation @s mg.bvx = #vx mg.st', 'scoreboard players operation @s mg.bvz = #vz mg.st',
                     'scoreboard players operation @s mg.bsp = #sp mg.st'] +
  [f'execute if score #ln mg.st matches {l} run data modify entity @s item.id set value "minecraft:{BALLS[l]}"' for l in range(NL)] +
  ['function mg:bowl/pos'])
w('bowl/rolling', ['# @s : la boule roule (bruit de roulement), fin quand elle est dans la fosse',
                   'scoreboard players operation #ln mg.st = @s mg.bln', 'scoreboard players set #n mg.st 0',
                   'execute as @e[type=minecraft:item_display,tag=mg.bball] if score @s mg.bln = #ln mg.st run scoreboard players add #n mg.st 1',
                   'scoreboard players operation #q mg.st = @s mg.btm', 'scoreboard players set #k mg.st 4', 'scoreboard players operation #q mg.st %= #k mg.st',
                   'execute if score #q mg.st matches 0 as @e[type=minecraft:item_display,tag=mg.bball] if score @s mg.bln = #ln mg.st at @s run playsound minecraft:block.wood.step master @a[tag=!mg.surv,distance=..24] ~ ~ ~ 0.5 0.5',
                   'execute if score @s mg.btm matches 300.. as @e[type=minecraft:item_display,tag=mg.bball] if score @s mg.bln = #ln mg.st run kill @s',
                   'execute if score #n mg.st matches 0 run scoreboard players set @s mg.btm 0',
                   'execute if score #n mg.st matches 0 run scoreboard players set @s mg.bph 2'])
w('bowl/settle', ['# @s : on attend que les quilles s\'immobilisent (1,25 s mini, 6 s maxi) puis on compte',
                  'scoreboard players operation #ln mg.st = @s mg.bln', 'scoreboard players set #n mg.st 0',
                  'execute as @e[type=minecraft:block_display,tag=mg.bpmv] if score @s mg.bln = #ln mg.st run scoreboard players add #n mg.st 1',
                  'execute if score @s mg.btm matches 25.. if score #n mg.st matches 0 run return run function mg:bowl/count',
                  'execute if score @s mg.btm matches 120.. run function mg:bowl/count'])
w('bowl/count', ['# @s : quilles renversées par ce lancer → score',
                 'scoreboard players set #pc mg.st 0',
                 'execute as @e[type=minecraft:block_display,tag=mg.bpin,tag=!mg.bpdn] if score @s mg.bln = #ln mg.st run scoreboard players add #pc mg.st 1',
                 'scoreboard players operation #k mg.st = @s mg.bk', 'scoreboard players operation #k mg.st -= #pc mg.st',
                 'execute as @e[type=minecraft:block_display,tag=mg.bpmv] if score @s mg.bln = #ln mg.st run function mg:bowl/pin_stop',
                 'function mg:bowl/result'])

# ───────────────────────────── score (vraies règles) ─────────────────────────────
# Lancer de #k quilles : les frames en attente de bonus (strike : 2 lancers, spare : 1) reçoivent #k ; un frame
# se « ferme » quand son score est connu → cumul écrit dans sa case. Total provisoire (barre latérale) = cumul + attentes + frame en cours.
w('bowl/result', ['# @s : joueur, #k quilles renversées (#ln piste)',
                  'execute store result storage mg:bowl q.l int 1 run scoreboard players get @s mg.bln',
                  'function mg:bowl/w_load with storage mg:bowl q',
                  'tag @s remove mg.bnr', 'scoreboard players set #ev mg.st 0',
                  # bonus des frames en attente
                  'execute if score @s mg.bp1n matches 1.. run scoreboard players operation @s mg.bp1s += #k mg.st',
                  'execute if score @s mg.bp1n matches 1.. run scoreboard players remove @s mg.bp1n 1',
                  'execute if score @s mg.bp2n matches 1.. run scoreboard players operation @s mg.bp2s += #k mg.st',
                  'execute if score @s mg.bp2n matches 1.. run scoreboard players remove @s mg.bp2n 1',
                  'execute if score @s mg.bp1n matches 0 if score @s mg.bp1f matches 1.. run function mg:bowl/p1_close',
                  'execute if score @s mg.bp1n matches 0 if score @s mg.bp1f matches 1.. run function mg:bowl/p1_close',
                  'scoreboard players operation @s mg.bfs += #k mg.st',
                  'execute store result storage mg:bowl w.f int 1 run scoreboard players get @s mg.bfr',
                  # (dernier frame testé d'abord : r_frame passe au frame suivant)
                  f'execute if score @s mg.bfr matches {FRAMES} run function mg:bowl/r_last',
                  f'execute if score @s mg.bfr matches ..{FRAMES - 1} run function mg:bowl/r_frame',
                  # total provisoire
                  'scoreboard players operation @s mg.bsc = @s mg.bcu',
                  'execute if score @s mg.bp1f matches 1.. run scoreboard players operation @s mg.bsc += @s mg.bp1s',
                  'execute if score @s mg.bp2f matches 1.. run scoreboard players operation @s mg.bsc += @s mg.bp2s',
                  'scoreboard players operation @s mg.bsc += @s mg.bfs',
                  'execute store result storage mg:bowl w.t int 1 run scoreboard players get @s mg.bsc',
                  'function mg:bowl/render with storage mg:bowl w',
                  'function mg:bowl/w_save with storage mg:bowl w',
                  'function mg:bowl/announce',
                  'scoreboard players set @s mg.bph 3', 'scoreboard players set @s mg.btm 0'])
w('bowl/w_load', ['$data modify storage mg:bowl w set from storage mg:bowl L$(l)'])
w('bowl/w_save', ['$data modify storage mg:bowl L$(l) set from storage mg:bowl w'])
w('bowl/p1_close', ['# @s : le plus ancien frame en attente est complet → cumul, case remplie, l\'attente suivante remonte',
                    'scoreboard players operation @s mg.bcu += @s mg.bp1s',
                    'execute store result storage mg:bowl q.f int 1 run scoreboard players get @s mg.bp1f',
                    'execute store result storage mg:bowl q.v int 1 run scoreboard players get @s mg.bcu',
                    'function mg:bowl/cw with storage mg:bowl q',
                    'scoreboard players operation @s mg.bp1f = @s mg.bp2f', 'scoreboard players operation @s mg.bp1s = @s mg.bp2s',
                    'scoreboard players operation @s mg.bp1n = @s mg.bp2n',
                    'scoreboard players set @s mg.bp2f 0', 'scoreboard players set @s mg.bp2s 0', 'scoreboard players set @s mg.bp2n 0'])
w('bowl/cw', ['$data modify storage mg:bowl w.c$(f) set value $(v)'])
w('bowl/mw', ['$data modify storage mg:bowl w.f$(f) set value "$(a) $(b) $(c)"'])
w('bowl/push', ['# @s : le frame en cours attend #pn lancers de bonus (valeur 10)',
                'execute if score @s mg.bp1f matches 1.. run return run function mg:bowl/push2',
                'scoreboard players operation @s mg.bp1f = @s mg.bfr', 'scoreboard players set @s mg.bp1s 10',
                'scoreboard players operation @s mg.bp1n = #pn mg.st'])
w('bowl/push2', ['scoreboard players operation @s mg.bp2f = @s mg.bfr', 'scoreboard players set @s mg.bp2s 10',
                 'scoreboard players operation @s mg.bp2n = #pn mg.st'])
for slot in 'abc':
    w(f'bowl/mk_{slot}', [f'# marque du lancer #k dans la case ({slot}) : X, - ou le nombre',
                          f'execute if score #k mg.st matches 10 run return run data modify storage mg:bowl w.{slot} set value "X"',
                          f'execute if score #k mg.st matches 0 run return run data modify storage mg:bowl w.{slot} set value "-"',
                          f'execute store result storage mg:bowl w.{slot} int 1 run scoreboard players get #k mg.st'])
w('bowl/r_frame', ['# @s : lancer dans un frame normal',
                   'execute if score @s mg.brl matches 1 if score #k mg.st matches 10 run return run function mg:bowl/r_strike',
                   'execute if score @s mg.brl matches 1 run return run function mg:bowl/r_first',
                   'scoreboard players operation #q mg.st = @s mg.br1', 'scoreboard players operation #q mg.st += #k mg.st',
                   'execute if score #q mg.st matches 10 run return run function mg:bowl/r_spare',
                   'function mg:bowl/mk_b', 'function mg:bowl/mw with storage mg:bowl w',
                   'scoreboard players set #ev mg.st 0', 'execute if score #k mg.st matches 0 run scoreboard players set #ev mg.st 4',
                   'scoreboard players operation @s mg.bcu += @s mg.bfs',
                   'execute store result storage mg:bowl q.f int 1 run scoreboard players get @s mg.bfr',
                   'execute store result storage mg:bowl q.v int 1 run scoreboard players get @s mg.bcu',
                   'function mg:bowl/cw with storage mg:bowl q',
                   'scoreboard players set @s mg.bxs 0',
                   'function mg:bowl/next_frame'])
w('bowl/r_first', ['# 1er lancer sans strike', 'scoreboard players operation @s mg.br1 = #k mg.st',
                   'function mg:bowl/mk_a', 'data modify storage mg:bowl w.b set value ""', 'data modify storage mg:bowl w.c set value ""',
                   'function mg:bowl/mw with storage mg:bowl w', 'scoreboard players set @s mg.brl 2',
                   'execute if score #k mg.st matches 0 run scoreboard players set #ev mg.st 4'])
w('bowl/r_strike', ['# STRIKE (frame normal)', 'data modify storage mg:bowl w.a set value ""', 'data modify storage mg:bowl w.b set value "X"',
                    'data modify storage mg:bowl w.c set value ""', 'function mg:bowl/mw with storage mg:bowl w',
                    'scoreboard players set #pn mg.st 2', 'function mg:bowl/push', 'scoreboard players set @s mg.bfs 0',
                    'scoreboard players add @s mg.bxs 1', 'scoreboard players set #ev mg.st 1', 'function mg:bowl/next_frame'])
w('bowl/r_spare', ['# SPARE (frame normal)', 'data modify storage mg:bowl w.b set value "/"', 'function mg:bowl/mw with storage mg:bowl w',
                   'scoreboard players set #pn mg.st 1', 'function mg:bowl/push', 'scoreboard players set @s mg.bfs 0',
                   'scoreboard players set @s mg.bxs 0', 'scoreboard players set #ev mg.st 2', 'function mg:bowl/next_frame'])
w('bowl/next_frame', ['scoreboard players add @s mg.bfr 1', 'scoreboard players set @s mg.brl 1', 'scoreboard players set @s mg.bfs 0',
                      'tag @s add mg.bnr', 'data modify storage mg:bowl w.a set value ""', 'data modify storage mg:bowl w.b set value ""',
                      'data modify storage mg:bowl w.c set value ""'])
w('bowl/r_last', ['# @s : dernier frame (jusqu\'à 3 lancers : strike ou spare donnent les lancers bonus)',
                  'execute if score @s mg.brl matches 1 run return run function mg:bowl/l1',
                  'execute if score @s mg.brl matches 2 run return run function mg:bowl/l2',
                  'function mg:bowl/l3'])
w('bowl/l1', ['scoreboard players operation @s mg.br1 = #k mg.st', 'function mg:bowl/mk_a', 'function mg:bowl/mw with storage mg:bowl w',
              'scoreboard players set @s mg.brl 2',
              'execute if score #k mg.st matches 10 run tag @s add mg.bnr',
              'execute if score #k mg.st matches 10 run scoreboard players add @s mg.bxs 1',
              'execute if score #k mg.st matches 10 run scoreboard players set #ev mg.st 1',
              'execute if score #k mg.st matches 0 run scoreboard players set #ev mg.st 4',
              'execute unless score #k mg.st matches 10 run scoreboard players set @s mg.bxs 0'])
w('bowl/l2', ['scoreboard players operation @s mg.br2 = #k mg.st',
              'execute if score @s mg.br1 matches 10 run return run function mg:bowl/l2_after_x',
              'scoreboard players operation #q mg.st = @s mg.br1', 'scoreboard players operation #q mg.st += #k mg.st',
              'execute if score #q mg.st matches 10 run data modify storage mg:bowl w.b set value "/"',
              'execute unless score #q mg.st matches 10 run function mg:bowl/mk_b',
              'function mg:bowl/mw with storage mg:bowl w',
              'execute if score #q mg.st matches 10 run scoreboard players set #ev mg.st 2',
              'execute if score #q mg.st matches 10 run tag @s add mg.bnr',
              'execute if score #q mg.st matches 10 run return run scoreboard players set @s mg.brl 3',
              'execute if score #k mg.st matches 0 run scoreboard players set #ev mg.st 4',
              'function mg:bowl/last_end'])
w('bowl/l2_after_x', ['# 2e lancer après un strike au dernier frame (lancer bonus)', 'function mg:bowl/mk_b', 'function mg:bowl/mw with storage mg:bowl w',
                      'scoreboard players set @s mg.brl 3',
                      'execute if score #k mg.st matches 10 run tag @s add mg.bnr',
                      'execute if score #k mg.st matches 10 run scoreboard players add @s mg.bxs 1',
                      'execute if score #k mg.st matches 10 run scoreboard players set #ev mg.st 1',
                      'execute unless score #k mg.st matches 10 run scoreboard players set @s mg.bxs 0'])
w('bowl/l3', ['# 3e lancer (bonus) du dernier frame',
              'scoreboard players operation #q mg.st = @s mg.br2', 'scoreboard players operation #q mg.st += #k mg.st',
              'execute if score @s mg.br1 matches 10 unless score @s mg.br2 matches 10 if score #q mg.st matches 10 run data modify storage mg:bowl w.c set value "/"',
              'execute if score @s mg.br1 matches 10 unless score @s mg.br2 matches 10 if score #q mg.st matches 10 run scoreboard players set #ev mg.st 2',
              'execute unless data storage mg:bowl w{c:"/"} run function mg:bowl/mk_c',
              'execute unless data storage mg:bowl w{c:"/"} if score #k mg.st matches 10 run scoreboard players add @s mg.bxs 1',
              'execute unless data storage mg:bowl w{c:"/"} if score #k mg.st matches 10 run scoreboard players set #ev mg.st 1',
              'function mg:bowl/mw with storage mg:bowl w',
              'function mg:bowl/last_end'])
w('bowl/last_end', ['# @s : partie finie pour ce joueur (le cumul du dernier frame est écrit)',
                    'scoreboard players operation @s mg.bcu += @s mg.bfs', 'scoreboard players set @s mg.bfs 0',
                    'execute store result storage mg:bowl q.f int 1 run scoreboard players get @s mg.bfr',
                    'execute store result storage mg:bowl q.v int 1 run scoreboard players get @s mg.bcu',
                    'function mg:bowl/cw with storage mg:bowl q',
                    'scoreboard players set @s mg.brl 4',
                    'tellraw @a[tag=mg.play] ' + js([{'text': '🎳 ', 'color': 'light_purple'}, {'selector': '@s', 'color': 'yellow'},
                                                     {'text': ' termine avec ', 'color': 'gray'},
                                                     {'score': {'name': '@s', 'objective': 'mg.bcu'}, 'color': 'gold', 'bold': True},
                                                     {'text': ' points.', 'color': 'gray'}])])

RENDER = ['# Tableau de la piste $(l) (cases frames + total)']
for k in range(1, FRAMES + 1):
    RENDER.append(f'$data modify entity @e[type=minecraft:text_display,tag=mg.bbc$(l)_{k},limit=1] text set value '
                  f'[{{text:"{k}",color:"gray"}},{{text:"\\n$(f{k})",color:"white",bold:true}},{{text:"\\n$(c{k})",color:"gold"}}]')
RENDER.append(f'$data modify entity @e[type=minecraft:text_display,tag=mg.bbc$(l)_{FRAMES + 1},limit=1] text set value '
              '[{text:"Total",color:"gray"},{text:"\\n$(t)",color:"yellow",bold:true},{text:"\\n ",color:"gold"}]')
w('bowl/render', RENDER)

w('bowl/announce', ['# @s : annonce du lancer (#ev : 1 strike, 2 spare, 4 zéro) — titre, sons, particules',
                    'scoreboard players operation #ln mg.st = @s mg.bln',
                    'execute if score #ev mg.st matches 1 if score @s mg.bxs matches 3.. run return run function mg:bowl/fx_turkey',
                    'execute if score #ev mg.st matches 1 run return run function mg:bowl/fx_strike',
                    'execute if score #ev mg.st matches 2 run return run function mg:bowl/fx_spare',
                    'execute if score #ev mg.st matches 4 run title @s actionbar {"text":"🎳 Aucune quille…","color":"gray"}',
                    'execute if score #ev mg.st matches 4 run return run playsound minecraft:entity.villager.no master @s ~ ~ ~ 0.8 1',
                    'title @s actionbar [{"text":"🎳 ","color":"gray"},{"score":{"name":"#k","objective":"mg.st"},"color":"white","bold":true},{"text":" quille(s) — total ","color":"gray"},{"score":{"name":"@s","objective":"mg.bsc"},"color":"gold"}]',
                    'playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.6 1'])


def fx_lines(particle, count):
    out = []
    for l, cx in enumerate(CXS):
        out.append(f'execute if score #ln mg.st matches {l} run particle {particle} {cx + 0.5} 66 {ZF + 17} 1.2 0.6 1.2 0.15 {count} force')
    return out


w('bowl/fx_strike', ['title @s times 5 30 10', 'title @s title {"text":"STRIKE !","color":"gold","bold":true}',
                     'title @s subtitle {"text":"✖ toutes les quilles d\'un coup","color":"yellow"}',
                     'tellraw @a[tag=mg.play] ' + js([{'text': '🎳 ', 'color': 'gold'}, {'selector': '@s', 'color': 'yellow'},
                                                      {'text': ' fait un ', 'color': 'gray'}, {'text': 'STRIKE', 'color': 'gold', 'bold': True}, {'text': ' !', 'color': 'gray'}]),
                     'playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 0.8 1.2',
                     'execute at @s run playsound minecraft:entity.firework_rocket.twinkle master @a[tag=!mg.surv,distance=..30] ~ ~ ~ 1 1'] +
  fx_lines('minecraft:firework', 60) + fx_lines('minecraft:totem_of_undying', 40))
w('bowl/fx_turkey', ['function mg:bowl/fx_strike', 'title @s title {"text":"🦃 TURKEY !","color":"gold","bold":true}',
                     'title @s subtitle [{"score":{"name":"@s","objective":"mg.bxs"},"color":"yellow"},{"text":" strikes d\'affilée !","color":"yellow"}]',
                     'execute at @s run playsound minecraft:entity.turtle.egg_hatch master @a[tag=!mg.surv,distance=..30] ~ ~ ~ 1 0.6'])
w('bowl/fx_spare', ['title @s times 5 25 10', 'title @s title {"text":"SPARE !","color":"aqua","bold":true}',
                    'title @s subtitle {"text":"/ toutes les quilles en 2 lancers","color":"gray"}',
                    'tellraw @a[tag=mg.play] ' + js([{'text': '🎳 ', 'color': 'aqua'}, {'selector': '@s', 'color': 'yellow'},
                                                     {'text': ' fait un ', 'color': 'gray'}, {'text': 'SPARE', 'color': 'aqua', 'bold': True}, {'text': ' !', 'color': 'gray'}]),
                    'playsound minecraft:entity.player.levelup master @s ~ ~ ~ 0.7 1.4'] + fx_lines('minecraft:happy_villager', 30))

w('bowl/reset', ['# @s : requilleur — balaye les quilles tombées, remet un jeu complet si besoin, rend la boule',
                 'scoreboard players operation #ln mg.st = @s mg.bln',
                 'execute if score @s mg.btm matches 20 as @e[type=minecraft:block_display,tag=mg.bpdn] if score @s mg.bln = #ln mg.st at @s run particle minecraft:poof ~ ~0.2 ~ 0.1 0.1 0.1 0.01 2',
                 'execute if score @s mg.btm matches 20 as @e[type=minecraft:block_display,tag=mg.bpdn] if score @s mg.bln = #ln mg.st run kill @s',
                 'execute if score @s mg.btm matches 20 at @s run playsound minecraft:block.piston.contract master @s ~ ~ ~ 0.4 0.8',
                 'execute if score @s mg.btm matches 28 if entity @s[tag=mg.bnr] unless score @s mg.brl matches 4 run function mg:bowl/rack',
                 'execute if score @s mg.btm matches 40.. if score @s mg.brl matches 4 run return run function mg:bowl/done',
                 'execute if score @s mg.btm matches 40.. run function mg:bowl/to_aim'])
w('bowl/done', ['# @s : ses frames sont joués', 'scoreboard players set @s mg.bph 9', 'scoreboard players set @s mg.btm 0',
                'clear @s minecraft:warped_fungus_on_a_stick[minecraft:custom_data={mg_bowl:1b}]'])

w('bowl/finish', ['# Fin : meilleur total (barre latérale) ; égalité = match nul ; seul = résultat sans victoire',
                  'scoreboard players set $bx mg.st -1', 'scoreboard players operation $bx mg.st > @a[tag=mg.play] mg.bsc',
                  'scoreboard players set $bc mg.st 0', 'execute as @a[tag=mg.play] if score @s mg.bsc = $bx mg.st run scoreboard players add $bc mg.st 1',
                  'tellraw @a[tag=mg.play] ' + js([{'text': '🎳 Meilleur score : ', 'color': 'light_purple'},
                                                   {'score': {'name': '$bx', 'objective': 'mg.st'}, 'color': 'gold', 'bold': True}]),
                  'execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw',
                  'execute if score $bc mg.st matches 2.. run return run function mg:core/draw',
                  'execute as @a[tag=mg.play] if score @s mg.bsc = $bx mg.st run return run function mg:core/win_player',
                  'function mg:core/draw'])
w('bowl/cleanup', ['# 🎳 Nettoyage', 'kill @e[tag=mg.bowl]',
                   'clear @a minecraft:warped_fungus_on_a_stick[minecraft:custom_data={mg_bowl:1b}]',
                   'tag @a remove mg.bwl', 'tag @a remove mg.bnr', 'data remove storage mg:bowl w', 'stopsound @a record minecraft:music_disc.cat',
                   'schedule clear mg:bowl/build_2', 'schedule clear mg:bowl/build_3', 'schedule clear mg:bowl/build_4', 'schedule clear mg:bowl/build_5',
                   'effect clear @a[tag=mg.play] minecraft:resistance',
                   'scoreboard players reset * mg.bsc', 'scoreboard players reset * mg.bph', 'scoreboard players reset * mg.bln'])

C.register([GID], 'bowl', [C.announce(GID, '', '🎳 BOWLING', 'light_purple', f'chacun sa piste, {FRAMES} frames, le meilleur total gagne !')])
C.objectives([('mg.blu', 'minecraft.used:minecraft.warped_fungus_on_a_stick')] +
             [(f'mg.{n}', 'dummy') for n in ('bln', 'bcx', 'bx', 'bz', 'bvx', 'bvz', 'bsp', 'bph', 'btm', 'bfr', 'brl', 'bpw', 'bpd', 'bk',
                                             'br1', 'br2', 'bfs', 'bcu', 'bp1f', 'bp1s', 'bp1n', 'bp2f', 'bp2s', 'bp2n', 'bxs')] +
             [('mg.bsc', 'dummy {"text":"🎳 Bowling","color":"light_purple"}')])
C.patch('desinstaller', 'scoreboard objectives remove mg.bw',
        [f'schedule clear mg:bowl/build_{i}' for i in range(2, 6)])
C.forceload([f'# 🎳 Bowling (z 35170)', f'forceload add {X0 - 1} {Z0 - 1} {X1 + 1} {Z1 + 1}'])
print('Bowling OK')
