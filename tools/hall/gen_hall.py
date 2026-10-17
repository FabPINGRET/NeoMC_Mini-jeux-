"""Hall des scores + classements par mini-jeu : génère data/mg/function/hall/*.mcfunction.

- un objectif de victoires par famille de jeux (mg.wg_<clé>), crédité au retour au lobby
  pour chaque joueur tagué mg.win (le jeu est lu dans $game) ;
- le tableau à droite alterne le classement général (10 s) et le classement d'un jeu (6 s),
  en sautant les jeux encore jamais gagnés (#any) ;
- un petit hall au sud-ouest de la place : le meneur de chaque jeu, le champion général,
  le joueur le plus assidu et le record du parcours d'élytra. Le nom et le score sont
  « figés » au moment du record (composant résolu via un set_name sur un item_display
  tampon), gardés dans storage mg:hall et restaurés à chaque reconstruction.
Lancer de n'importe où : python3 tools/hall/gen_hall.py (la sortie est dérivée de l'emplacement du script).
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data', 'mg', 'function', 'hall')
GAMES = [  # clé, libellé, couleur, plages de $game
    ('spleef', '❄ Spleef', 'aqua', [(1, 1)]),
    ('tntrun', '✷ TNT Run', 'red', [(2, 2), (244, 245)]),
    ('pvp', '⚔ PvP', 'gold', [(3, 3)]),
    ('bedwars', '🛏 Bedwars', 'red', [(4, 4)]),
    ('sheepwar', '🐑 Sheep War', 'white', [(5, 5), (7, 7)]),
    ('mobarena', '☠ Mob Arena', 'dark_green', [(6, 6)]),
    ('splegg', '❍ Splegg', 'yellow', [(20, 21)]),
    ('sumo', '✊ Sumo', 'gold', [(22, 22)]),
    ('dropper', '⬇ Dropper', 'aqua', [(23, 23), (64, 65), (228, 228)]),
    ('oitc', '➶ One in the Chamber', 'gold', [(26, 26)]),
    ('tnttag', '✹ TNT Tag', 'red', [(27, 27)]),
    ('blockparty', '▦ Block Party', 'light_purple', [(28, 28)]),
    ('anvil', "⚓ Pluie d'enclumes", 'gray', [(29, 29)]),
    ('turf', '▮ Turf Wars', 'gold', [(30, 30)]),
    ('quake', '⚡ Quakecraft', 'aqua', [(31, 31)]),
    ('paintball', '▓ Paintball', 'gold', [(36, 36)]),
    ('icerace', '⛵ Course de bateaux', 'aqua', [(56, 56)]),
    ('bb', '✎ Build Battle', 'green', [(57, 58)]),
    ('party', '★ Mini Party', 'gold', [(59, 60)]),
    ('kart', '🏎 Kart', 'red', [(61, 63)]),
    ('elyrace', "🪽 Course d'élytres", 'aqua', [(66, 66)]),
    ('elytra', '🪽 Élytra (3 modes)', 'aqua', [(75, 75)]),
    ('telephone', '📞 Téléphone', 'gold', [(83, 83)]),
    ('tron', '⚡ Tron', 'aqua', [(84, 85), (200, 201)]),
    ('koth', '👑 King of the Hill', 'gold', [(86, 87), (206, 209)]),
    ('tower', '🏰 The Towers', 'gold', [(88, 88)]),
    ('convoy', '🚚 Convoi', 'gold', [(89, 90)]),
    ('ctf', '🚩 Capture the Flag', 'red', [(93, 93), (242, 243)]),
    ('uhc', '⛏ Mini UHC Run', 'gold', [(94, 94), (202, 202), (204, 204)]),
    ('hg', '🏹 Mini Hunger Games', 'gold', [(95, 95), (203, 203), (205, 205)]),
    ('prophunt', '🎭 Prop Hunt', 'gold', [(96, 96)]),
    ('zombies', '🧟 Zombies', 'dark_green', [(97, 97), (210, 210), (212, 212), (229, 229), (231, 231), (235, 235), (237, 237)]),
    ('infection', '🧪 Infection', 'green', [(98, 98), (211, 211), (213, 213), (217, 219), (230, 230), (232, 232), (236, 236), (238, 238)]),
    ('bomber', '💣 Bombardier', 'red', [(99, 99)]),
    ('chameleon', '🦎 Meccha Chameleon', 'green', [(198, 198)]),
    ('wii', '🎾 Wii Sports', 'aqua', [(214, 216)]),
    ('soleil', '🔴 1, 2, 3 Soleil', 'red', [(220, 220)]),
    ('autotamp', '🚗 Autos tamponneuses', 'aqua', [(221, 223)]),
    ('slimejump', '🟩 Slime Jump', 'green', [(224, 224)]),
    ('lab', '🙈 Labyrinthe aveugle', 'light_purple', [(225, 225)]),
    ('master', '👑 Master dit', 'gold', [(226, 226)]),
    ('murder', '🔪 Murder Mystery', 'red', [(227, 227)]),
    ('bman', '💣 Bomberman', 'red', [(239, 240)]),
    ('maze', '🌀 Labyrinthe géant', 'light_purple', [(241, 241)]),
]
# Hall v15 : grand bâtiment compartimenté au sud-ouest de la place (x -60..-12, z 15..36, sol y 63), entrée à l'est
# (côté avenue sud). Une nef est-ouest, 44 stands (2 rangées × 2 niveaux × 11) : chaque jeu a son stand avec son podium et le
# top 3 de ses victoires. Galerie à l'étage (y 68) reliée par un escalier au fond ; salle d'honneur sous le palier (ouest).
HX0, HX1, HZ0, HZ1 = -60, -12, 15, 36      # murs extérieurs compris
NAVE = (22, 29)                            # nef (z) ; balcons de l'étage : z 22..24 et 27..29, vide central z 25..26
BX0, BP, NB = -59, 4, 11                   # 1er stand en x -59, un stand tous les 4 blocs (3 d'intérieur + cloison), 11 par rangée
FL = (63, 68)                              # sols : rez-de-chaussée y 63, étage y 68 ; toit y 73
OLD = (-24, -6, 11, 25)                    # hall v14 (x1, x2, z1, z2), effacé une fois
MARK = (-58, 64, 26)                       # piédestal du champion (bloc d'or) : témoin de présence
VERSION = 15
TR = 'transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[%sf,%sf,%sf]}'

def W(name, lines):
    with open(os.path.join(OUT, name + '.mcfunction'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')

def q(s): return s.replace('"', '\\"')
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- objectifs (appelé par core/load)
W('objectives', ['# Objectifs des classements par jeu (généré par tools/hall/gen_hall.py)'] + [
    f'scoreboard objectives add mg.wg_{k} dummy [{{"text":"{q(l)}","color":"{c}","bold":true}},{{"text":" — victoires","color":"gray","bold":false}}]'
    for k, l, c, _ in GAMES] + [
    'scoreboard objectives modify mg.stp displayname [{"text":"▶ Parties jouées","color":"green","bold":true}]',
    'scoreboard objectives modify mg.stk displayname [{"text":"⚔ Kills","color":"red","bold":true},{"text":" (toutes parties)","color":"gray","bold":false}]',
    'scoreboard objectives modify mg.wins displayname [{"text":"✦ Victoires","color":"gold","bold":true},{"text":" (tous les jeux)","color":"gray","bold":false}]',
    'scoreboard objectives add mg.gen dummy [{"text":"🏅 Score général","color":"aqua","bold":true}]',
    'scoreboard objectives add mg.lvl dummy [{"text":"🏅 Classement général","color":"aqua","bold":true},{"text":" (niveau)","color":"gray","bold":false}]',
    'scoreboard objectives add mg.genc dummy'])
W('remove', ['# Désinstallation des classements et du hall'] +
  [f'scoreboard objectives remove mg.wg_{k}' for k, *_ in GAMES] +
  ['kill @e[tag=mg.hall]', 'schedule clear mg:hall/build', 'data remove storage mg:hall e', 'data remove storage mg:hall t3', 'data remove storage mg:hall t3x', 'data remove storage mg:hall v15', 'data remove storage mg:hall sbon', 'data remove storage mg:hall v2', 'data remove storage mg:hall v3', 'data remove storage mg:hall v4', 'data remove storage mg:hall v5', 'data remove storage mg:hall v6', 'data remove storage mg:hall v7', 'data remove storage mg:hall v8', 'data remove storage mg:hall v9', 'data remove storage mg:hall v10', 'data remove storage mg:hall v11', 'data remove storage mg:hall v12', 'data remove storage mg:hall v13', 'data remove storage mg:hall v14',
   'scoreboard objectives remove mg.gen', 'scoreboard objectives remove mg.lvl', 'scoreboard objectives remove mg.genc'])

# ---------------------------------------------------------------- crédit des vainqueurs
cr = ['# Vainqueur (@s, tag mg.win) au retour au lobby : classement du jeu + hall des scores',
      'function mg:hall/top {obj:"mg.wins",key:"wins",lbl:"👑 Champion des mini-jeux",col:"gold",unit:" victoire(s)"}']
for k, l, c, rngs in GAMES:
    for a, b in rngs:
        m = f'{a}' if a == b else f'{a}..{b}'
        cr.append(f'execute if score $game mg.st matches {m} run function mg:hall/game {{obj:"mg.wg_{k}",key:"{k}",lbl:"{q(l)}",col:"{c}"}}')
W('credit', cr)
W('game', ['# +1 victoire dans le classement d\'un jeu (@s) — macro',
    '$scoreboard players add @s $(obj) 1',
    '$scoreboard players set #any $(obj) 1',
    '$function mg:hall/top {obj:"$(obj)",key:"$(key)",lbl:"$(lbl)",col:"$(col)",unit:""}',
    '$function mg:hall/t3 {k:"$(key)",obj:"$(obj)",lbl:"$(lbl)",col:"$(col)"}'])
W('top', ['# Nouveau meneur d\'un classement ? (@s) — fige « libellé / pseudo — score » dans le hall — macro',
    '$execute unless score #top $(obj) matches 0.. run scoreboard players set #top $(obj) 0',
    '$execute unless score @s $(obj) > #top $(obj) run return 0',
    '$scoreboard players operation #top $(obj) = @s $(obj)',
    '$item modify entity @e[type=minecraft:item_display,tag=mg.hallbuf,limit=1] contents {function:"minecraft:set_name",entity:"this",target:"custom_name",name:[{text:"$(lbl)",color:"$(col)",bold:true},{text:"\\n",bold:false},{selector:"@s",color:"white",bold:false},{text:" — ",color:"gray",bold:false},{score:{name:"@s",objective:"$(obj)"},color:"gold",bold:false},{text:"$(unit)",color:"gray",bold:false}]}',
    '$data modify storage mg:hall e.$(key) set from entity @e[type=minecraft:item_display,tag=mg.hallbuf,limit=1] item.components."minecraft:custom_name"',
    '$data modify entity @e[type=minecraft:text_display,tag=mg.h_$(key),limit=1] text set from storage mg:hall e.$(key)'])
def ely(pad):
    zero = '{text:"0",color:"gold",bold:false},' if pad else ''
    return ('$item modify entity @e[type=minecraft:item_display,tag=mg.hallbuf,limit=1] contents {function:"minecraft:set_name",entity:"this",target:"custom_name",name:['
            '{text:"$(lbl)",color:"aqua",bold:true},{text:"\\n",bold:false},{selector:"@s",color:"white",bold:false},{text:" — ",color:"gray",bold:false},'
            '{score:{name:"$es",objective:"mg.st"},color:"gold",bold:false},{text:",",color:"gold",bold:false},' + zero +
            '{score:{name:"$ecs",objective:"mg.st"},color:"gold",bold:false},{text:" s",color:"gold",bold:false}]}')
W('ely', ['# Record d\'un parcours d\'élytra (@s, temps dans $es / $ecs) → hall — macro {key, lbl}',
    ely(True).replace('$item modify', '$execute if score $ecs mg.st matches ..9 run item modify', 1),
    ely(False).replace('$item modify', '$execute if score $ecs mg.st matches 10.. run item modify', 1),
    '$data modify storage mg:hall e.$(key) set from entity @e[type=minecraft:item_display,tag=mg.hallbuf,limit=1] item.components."minecraft:custom_name"',
    '$data modify entity @e[type=minecraft:text_display,tag=mg.h_$(key),limit=1] text set from storage mg:hall e.$(key)'])

# ---------------------------------------------------------------- tableau à droite : rotation
# Lobby, hors partie : un tableau toutes les 8 s — victoires, parties jouées, kills, puis chaque
# jeu déjà gagné. Pendant des votes, le tableau des votes revient un affichage sur deux.
BOARDS = [('mg.lvl', None), ('mg.wins', None), ('mg.stp', None), ('mg.stk', None), ('mg.gta', None)] + [(f'mg.wg_{k}', None) for k, *_ in GAMES]   # mg.gta : les plus riches de Neo GTA
W('rotate', ['# Tableau à droite : affichage suivant',
    'execute if entity @a[scores={mg.wins=1..}] run scoreboard players set #any mg.wins 1',
    'execute if entity @a[scores={mg.lvl=1..}] run scoreboard players set #any mg.lvl 1',
    'execute if entity @a[scores={mg.stp=1..}] run scoreboard players set #any mg.stp 1',
    'execute if entity @a[scores={mg.stk=1..}] run scoreboard players set #any mg.stk 1',
    'execute if entity @a[scores={mg.gta=1..}] run scoreboard players set #any mg.gta 1',
    'execute if score $vn mg.st matches 1.. unless score $rph mg.st matches 1 run return run function mg:hall/rot_votes',
    'scoreboard players set $rph mg.st 0',
    'scoreboard players set $hrt mg.st 160',
    'scoreboard players set $rtry mg.st 0',
    'function mg:hall/rot_next'])
W('rot_votes', ['scoreboard players set $rph mg.st 1', 'scoreboard players set $hrt mg.st 120',
    'scoreboard objectives setdisplay sidebar mg.vb'])
W('rot_game', ['function mg:hall/rotate'])
rn = ['# Tableau suivant ayant au moins un score (sinon victoires)',
      'scoreboard players add $rot mg.st 1',
      f'execute unless score $rot mg.st matches 1..{len(BOARDS)} run scoreboard players set $rot mg.st 1',
      'scoreboard players add $rtry mg.st 1',
      f'execute if score $rtry mg.st matches {len(BOARDS)+1}.. run return run scoreboard objectives setdisplay sidebar mg.wins']
for i, (obj, _) in enumerate(BOARDS, 1):
    rn.append(f'execute if score $rot mg.st matches {i} if score #any {obj} matches 1.. run return run scoreboard objectives setdisplay sidebar {obj}')
rn.append('function mg:hall/rot_next')
W('rot_next', rn)

# ---------------------------------------------------------------- construction du hall (v15)
CONC = {'gold': 'yellow', 'aqua': 'light_blue', 'red': 'red', 'white': 'white', 'dark_green': 'green', 'yellow': 'yellow',
        'light_purple': 'magenta', 'gray': 'gray', 'green': 'lime'}
# stands : (x0 = 1re colonne intérieure, côté 'n' | 's', étage 0 | 1) ; ordre : rez nord, rez sud, étage nord, étage sud
STANDS = [(BX0 + BP * i, side, lv) for lv in (0, 1) for side in ('n', 's') for i in range(NB)]
assert len(GAMES) <= len(STANDS), f'agrandir le hall : {len(GAMES)} jeux pour {len(STANDS)} stands'
NZ1, NZ2 = NAVE
x0h, x1h = HX0 + 1, HX1 - 1                # intérieur (x)
b = ['# Hall des scores v15 (sud-ouest de la place) : construction + restauration des top 3 (généré par tools/hall/gen_hall.py)',
     '# Chunks du hall pas encore chargés (démarrage du serveur) : on réessaie dans 1 s, 60 fois au plus',
     f'execute store success score #hl mg.st unless block {HX0 + 2} 300 {HZ0 + 3} minecraft:bedrock',
     f'execute if score #hl mg.st matches 1 store success score #hl mg.st unless block {HX1 - 2} 300 {HZ1 - 3} minecraft:bedrock',
     'execute if score #hl mg.st matches 0 run scoreboard players add #hlr mg.st 1',
     'execute if score #hl mg.st matches 0 if score #hlr mg.st matches 60.. run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Hall des scores : chunks pas chargés, construction abandonnée (relance /function mg:hall/build).","color":"red"}]',
     'execute if score #hl mg.st matches 0 if score #hlr mg.st matches 60.. run return run scoreboard players set #hlr mg.st 0',
     'execute if score #hl mg.st matches 0 run return run schedule function mg:hall/build 20t',
     'scoreboard players set #hlr mg.st 0',
     'kill @e[tag=mg.hall]',
     'execute unless data storage mg:hall v15 run function mg:hall/clear_old', '',
     '# gros œuvre : terrain dégagé (arbres, ancienne fontaine), dalle, murs, étage, toit',
     f'fill {HX0} 64 {HZ0} {HX1} 84 {HZ1} minecraft:air',
     f'fill {HX0} 62 {HZ0} {HX1} 62 {HZ1} minecraft:stone',
     f'fill {HX0} 63 {HZ0} {HX1} 63 {HZ1} minecraft:polished_andesite',
     # murs (pas de « hollow » : il remplirait aussi le sol et le plafond)
     *[f'fill {xa} 64 {za} {xb} 72 {zb} minecraft:stone_bricks' for xa, za, xb, zb in ((HX0, HZ0, HX1, HZ0), (HX0, HZ1, HX1, HZ1), (HX0, HZ0, HX0, HZ1), (HX1, HZ0, HX1, HZ1))],
     f'fill {HX0} 73 {HZ0} {HX1} 73 {HZ1} minecraft:dark_oak_planks',
     f'fill {HX0 - 1} 73 {HZ0 - 1} {HX1 + 1} 73 {HZ0 - 1} minecraft:dark_oak_slab[type=bottom]',
     f'fill {HX0 - 1} 73 {HZ1 + 1} {HX1 + 1} 73 {HZ1 + 1} minecraft:dark_oak_slab[type=bottom]',
     f'fill {HX0 - 1} 73 {HZ0} {HX0 - 1} 73 {HZ1} minecraft:dark_oak_slab[type=bottom]',
     f'fill {HX1 + 1} 73 {HZ0} {HX1 + 1} 73 {HZ1} minecraft:dark_oak_slab[type=bottom]',
     # bandeaux (soubassement en pierre moussue, cordon sculpté à l'étage) : les 4 murs seulement
     *[f'fill {xa} {y} {za} {xb} {y} {zb} minecraft:{blk}' for y, blk in ((64, 'mossy_stone_bricks'), (FL[1], 'chiseled_stone_bricks'))
       for xa, za, xb, zb in ((HX0, HZ0, HX1, HZ0), (HX0, HZ1, HX1, HZ1), (HX0, HZ0, HX0, HZ1), (HX1, HZ0, HX1, HZ1))],
     f'fill {x0h} {FL[1]} {HZ0 + 1} {x1h} {FL[1]} {HZ1 - 1} minecraft:dark_oak_planks',
     # vide central de la nef + salle d'honneur et vestibule sans étage
     f'fill {x0h} {FL[1]} {NZ1 + 3} {x1h} {FL[1]} {NZ2 - 3} minecraft:air',
     f'fill {HX1 - 3} {FL[1]} {NZ1} {x1h} {FL[1]} {NZ2} minecraft:air',
     # garde-corps de la galerie (sauf au-dessus de l'escalier, côté ouest)
     f'fill -51 {FL[1] + 1} {NZ1 + 2} {HX1 - 4} {FL[1] + 1} {NZ1 + 2} minecraft:dark_oak_fence',
     f'fill -51 {FL[1] + 1} {NZ2 - 2} {HX1 - 4} {FL[1] + 1} {NZ2 - 2} minecraft:dark_oak_fence',
     f'fill {HX1 - 4} {FL[1] + 1} {NZ1} {HX1 - 4} {FL[1] + 1} {NZ2} minecraft:dark_oak_fence',
     f'fill {HX1 - 4} {FL[1] + 1} {NZ1 + 3} {HX1 - 4} {FL[1] + 1} {NZ2 - 3} minecraft:air']
# escalier (vide central, x -51 → -55) vers le palier ouest (y 68, x -59..-56)
for k in range(1, 5):
    x = -50 - k
    b.append(f'fill {x} {63 + k} {NZ1 + 3} {x} {63 + k} {NZ2 - 3} minecraft:dark_oak_stairs[facing=west]')
    if k > 1:
        b.append(f'fill {x} 64 {NZ1 + 3} {x} {62 + k} {NZ2 - 3} minecraft:dark_oak_planks')
b += [f'fill {x0h} {FL[1]} {NZ1} -55 {FL[1]} {NZ2} minecraft:dark_oak_planks',
      # nef : tapis rouge jusqu'à la salle d'honneur, entrée à l'est (portail 6 × 4)
      f'fill -50 63 {NZ1 + 3} {x1h} 63 {NZ2 - 3} minecraft:red_wool',
      f'fill {HX1} 64 {NZ1 + 1} {HX1} 67 {NZ2 - 1} minecraft:air',
      f'fill {HX1} 68 {NZ1 + 1} {HX1} 68 {NZ2 - 1} minecraft:chiseled_stone_bricks',
      f'fill {HX1 + 1} 63 {NZ1 + 1} -6 63 {NZ2 - 1} minecraft:polished_andesite',
      f'fill {HX1 + 1} 64 {NZ1 + 1} -6 70 {NZ2 - 1} minecraft:air',
      # fenêtres hautes (murs nord et sud, étage) et lustres de la nef
      ] + [f'fill {x} 70 {z} {x + 1} 71 {z} minecraft:glass_pane' for x in range(-57, -14, 4) for z in (HZ0, HZ1)] + \
     [f'setblock {x} 72 {z} minecraft:lantern[hanging=true]' for x in range(-50, -14, 6) for z in (25, 26)] + \
     [f'setblock {x} 72 {z} minecraft:sea_lantern' for x in range(-57, -13, 4) for z in (18, 33)]
# stands : cloisons, sol coloré, podium, éclairage
for i, (x0, side, lv) in enumerate(STANDS):
    y0 = FL[lv]                                         # sol du stand
    za, zb = (HZ0 + 1, NZ1 - 1) if side == 'n' else (NZ2 + 1, HZ1 - 1)
    back = HZ0 + 1 if side == 'n' else HZ1 - 1        # rangée du fond (côté mur)
    sgn = 1 if side == 'n' else -1
    xw = x0 + 3                                         # cloison
    if xw <= x1h:
        b.append(f'fill {xw} {y0 + 1} {za} {xw} {y0 + 4} {zb} minecraft:{"stripped_dark_oak_log[axis=y]" if lv == 0 else "stripped_spruce_log[axis=y]"}')
    if i >= len(GAMES):
        continue
    k, l, c, _ = GAMES[i]
    cc = CONC.get(c, 'white')
    b += [f'fill {x0} {y0} {za} {x0 + 2} {y0} {zb} minecraft:{cc}_concrete',
          f'fill {x0} {y0 + 1} {back} {x0 + 2} {y0 + 1} {back} minecraft:polished_andesite',
          f'setblock {x0 + 1} {y0 + 1} {back + sgn} minecraft:gold_block', f'setblock {x0 + 1} {y0 + 2} {back} minecraft:gold_block',
          f'setblock {x0} {y0 + 1} {back + sgn} minecraft:iron_block', f'setblock {x0 + 2} {y0 + 1} {back + sgn} minecraft:copper_block',
          f'setblock {x0 + 1} {y0 + 4} {za + 2} minecraft:light[level=15]',
          f'setblock {x0 + 1} {y0 + 4} {zb - 1} minecraft:light[level=12]']
b += ['', '# salle d\'honneur (sous le palier ouest) et ses piédestaux',
      f'fill -58 63 {NZ1} -56 63 {NZ2} minecraft:smooth_quartz',
      f'setblock -58 64 23 minecraft:emerald_block', f'setblock {MARK[0]} {MARK[1]} {MARK[2]} minecraft:gold_block', f'setblock -58 64 29 minecraft:lapis_block',
      f'fill -59 67 {NZ1} -59 67 {NZ2} minecraft:sea_lantern', '',
      '# Tampon de résolution des noms (invisible)',
      f'summon minecraft:item_display -57.5 64.5 26.5 {{Tags:["mg.hall","mg.hallbuf"],item:{{id:"minecraft:paper"}},{TR % (0.001, 0.001, 0.001)}}}',
      f'summon minecraft:text_display {HX1 + 0.6} 69.6 {(NZ1 + NZ2) / 2 + 0.5} {{Tags:["mg.hall"],billboard:"vertical",background:0,text:[{{"text":"🏆 Hall des scores","color":"gold","bold":true}}],{TR % (2.2, 2.2, 2.2)}}}',
      f'summon minecraft:text_display -35 72.2 {(NZ1 + NZ2) / 2 + 0.5} {{Tags:["mg.hall"],billboard:"vertical",background:0,text:[{{"text":"🏆 Hall des scores","color":"gold","bold":true}},{{"text":"\\n🥇 🥈 🥉 le top 3 de chaque jeu — étage par l\'escalier du fond","color":"gray","bold":false}}],{TR % (1.4, 1.4, 1.4)}}}',
      '', '# Piédestaux : objet qui tourne + plaque']
peds = [(-57.5, 23.5, 'stp', '▶ Le plus assidu', 'green', 'clock'),
        (-57.5, 26.5, 'wins', '👑 Champion des mini-jeux', 'gold', 'totem_of_undying'),
        (-57.5, 29.5, 'ely', "🪽 Record petit parcours d'élytra", 'aqua', 'elytra')]
plaques = [(x, 66.6, z, k, l, c, 0.9) for x, z, k, l, c, _ in peds]
plaques.append((-58.6, 70.4, 23.5, 'ely2', "🪽 Record grand parcours d'élytra", 'light_purple', 0.9))
plaques.append((-58.6, 70.4, 29.5, 'elyg', '🪽 Record Élytra : course', 'aqua', 0.9))
plaques.append((-58.6, 71.4, 26.5, 'gen', '🏅 Meilleur niveau général', 'aqua', 1.1))
for x, z, k, l, c, it in peds:
    b.append(f'summon minecraft:item_display {x} 65.8 {z} {{Tags:["mg.hall","mg.lspin","mg.lbob"],billboard:"fixed",item:{{id:"minecraft:{it}"}},{TR % (0.8, 0.8, 0.8)}}}')
b.append('')
b.append('# Plaques d\'honneur : texte par défaut, puis meneur enregistré s\'il existe')
for x, y, z, k, l, c, s in plaques:
    lw = 200 if k == 'gen' else int(2.6 / (0.025 * s))
    b.append(f'summon minecraft:text_display {x} {y} {z} {{Tags:["mg.hall","mg.h_{k}"],billboard:"vertical",line_width:{lw},text:[{{"text":"{q(l)}","color":"{c}","bold":true}},{{"text":"\\n— personne —","color":"dark_gray","bold":false}}],{TR % (s, s, s)}}}')
    b.append(f'execute if data storage mg:hall e.{k} run data modify entity @e[type=minecraft:text_display,tag=mg.h_{k},limit=1] text set from storage mg:hall e.{k}')
b.append('')
b.append('# Stands : top 3 de chaque jeu (texte par défaut, puis top 3 enregistré)')
for i, (k, l, c, _) in enumerate(GAMES):
    x0, side, lv = STANDS[i]
    y0 = FL[lv]
    z = (HZ0 + 1.6) if side == 'n' else (HZ1 - 0.6)
    b.append(f'summon minecraft:text_display {x0 + 1.5} {y0 + 3.0} {z} {{Tags:["mg.hall","mg.h3_{k}"],billboard:"vertical",line_width:110,'
             f'text:[{{"text":"{q(l)}","color":"{c}","bold":true}},{{"text":"\\n— personne —","color":"dark_gray","bold":false}}],{TR % (0.62, 0.62, 0.62)}}}')
    b.append(f'execute if data storage mg:hall t3x.{k} run data modify entity @e[type=minecraft:text_display,tag=mg.h3_{k},limit=1] text set from storage mg:hall t3x.{k}')
# Version du hall : core/load reconstruit le hall (une fois) sur les mondes dont le hall est plus ancien
b += [f'data modify storage mg:hall v{v} set value 1b' for v in range(2, VERSION + 1)]
W('build', b)
ox1, ox2, oz1, oz2 = OLD
W('clear_old', ['# Ancien hall (v14 : x %d..%d, z %d..%d) : ce qui dépasse du nouveau est rendu à la pelouse (une fois)' % OLD,
                f'fill {ox1} 64 {oz1} {ox2} 79 {HZ0 - 1} minecraft:air', f'fill {ox1} 63 {oz1} {ox2} 63 {HZ0 - 1} minecraft:grass_block',
                f'fill {HX1 + 1} 64 {HZ0} {ox2} 79 {oz2} minecraft:air', f'fill {HX1 + 1} 63 {HZ0} {ox2} 63 {oz2} minecraft:grass_block'])

# ---------------------------------------------------------------- top 3 par jeu (storage mg:hall t3.<clé> = [{u, n, s}], t3x.<clé> = texte)
W('t3', ['# @s : sa place dans le top 3 du jeu $(k) (score dans $(obj)) — macro {k, obj, lbl, col}',
         '$execute store result score #t3s mg.st run scoreboard players get @s $(obj)',
         'execute unless score #t3s mg.st matches 1.. run return 0',
         'data modify storage mg:hall t3w set value {}', 'data modify storage mg:hall t3w.u set from entity @s UUID',
         'execute store result storage mg:hall t3w.s int 1 run scoreboard players get #t3s mg.st',
         'item modify entity @e[type=minecraft:item_display,tag=mg.hallbuf,limit=1] contents {function:"minecraft:set_name",entity:"this",target:"custom_name",name:{selector:"@s"}}',
         'data modify storage mg:hall t3w.n set from entity @e[type=minecraft:item_display,tag=mg.hallbuf,limit=1] item.components."minecraft:custom_name"',
         'data modify storage mg:hall t3c set value []', '$data modify storage mg:hall t3c set from storage mg:hall t3.$(k)',
         'function mg:hall/t3_merge',
         '$execute store success score #t3d mg.st run data modify storage mg:hall t3.$(k) set from storage mg:hall t3c',
         '$execute if score #t3d mg.st matches 1 run function mg:hall/t3_show {k:"$(k)",lbl:"$(lbl)",col:"$(col)"}'])
M = ['# Insère t3w dans t3c (liste triée, 3 au plus) en retirant d\'abord l\'ancienne entrée du même joueur']
for i in (2, 1, 0):
    M += [f'execute if data storage mg:hall t3c[{i}] run data modify storage mg:hall t3q set from storage mg:hall t3c[{i}].u',
          f'execute if data storage mg:hall t3c[{i}] store success score #t3d mg.st run data modify storage mg:hall t3q set from storage mg:hall t3w.u',
          f'execute if data storage mg:hall t3c[{i}] if score #t3d mg.st matches 0 run data remove storage mg:hall t3c[{i}]']
M.append('scoreboard players set #t3i mg.st -1')
for i in range(3):
    M += [f'execute if score #t3i mg.st matches -1 if data storage mg:hall t3c[{i}] store result score #t3v mg.st run data get storage mg:hall t3c[{i}].s',
          f'execute if score #t3i mg.st matches -1 if data storage mg:hall t3c[{i}] if score #t3s mg.st > #t3v mg.st run scoreboard players set #t3i mg.st {i}']
M += [f'execute if score #t3i mg.st matches {i} run data modify storage mg:hall t3c insert {i} from storage mg:hall t3w' for i in range(3)]
M += ['execute if score #t3i mg.st matches -1 unless data storage mg:hall t3c[2] run data modify storage mg:hall t3c append from storage mg:hall t3w',
      'data remove storage mg:hall t3c[3]']
W('t3_merge', M)
MED = [('🥇', 'gold'), ('🥈', 'gray'), ('🥉', 'gold')]


def line(k, i):
    m, mc = MED[i]
    return (f'{{text:"\\n{m} ",color:"{mc}",bold:false}},{{nbt:"t3.$(k)[{i}].n",storage:"mg:hall",interpret:true,color:"white",bold:false}},'
            f'{{text:" — ",color:"dark_gray",bold:false}},{{nbt:"t3.$(k)[{i}].s",storage:"mg:hall",color:"yellow",bold:false}}')


SH = ['# Texte du stand $(k) : libellé + top 3 (résolu sur le tampon, gardé dans t3x.$(k)) — macro {k, lbl, col}']
for n in (3, 2, 1):
    cond = f'if data storage mg:hall t3.$(k)[{n - 1}]' + (f' unless data storage mg:hall t3.$(k)[{n}]' if n < 3 else '')
    SH.append(f'$execute {cond} run item modify entity @e[type=minecraft:item_display,tag=mg.hallbuf,limit=1] contents '
              '{function:"minecraft:set_name",entity:"this",target:"custom_name",name:[{text:"$(lbl)",color:"$(col)",bold:true},'
              + ','.join(line('k', i) for i in range(n)) + ']}')
SH += ['$data modify storage mg:hall t3x.$(k) set from entity @e[type=minecraft:item_display,tag=mg.hallbuf,limit=1] item.components."minecraft:custom_name"',
       '$data modify entity @e[type=minecraft:text_display,tag=mg.h3_$(k),limit=1] text set from storage mg:hall t3x.$(k)']
W('t3_show', SH)
W('t3_all', ['# @s (joueur en ligne) : ses victoires de chaque jeu reportées dans les top 3 (toutes les minutes ; remplit les top 3 au fil des connexions)'] +
  [f'execute if score @s mg.wg_{k} matches 1.. run function mg:hall/t3 {{k:"{k}",obj:"mg.wg_{k}",lbl:"{q(l)}",col:"{c}"}}' for k, l, c, _ in GAMES])

# câblage hors du hall : témoin de présence (core/tick), version (core/load), suivi de mg:setup
_F = os.path.join(OUT, '..')
def _sub(rel, a, c):
    p = os.path.join(_F, rel + '.mcfunction'); s = open(p, encoding='utf-8').read()
    if a in s: open(p, 'w', encoding='utf-8', newline='\n').write(s.replace(a, c))
_sub('core/tick', 'unless block -16 64 25 minecraft:gold_block run function mg:hall/build', f'unless block {MARK[0]} {MARK[1]} {MARK[2]} minecraft:gold_block run function mg:hall/build')
_sub('core/load', 'unless data storage mg:hall v8 run schedule function mg:hall/build', 'unless data storage mg:hall v11 run schedule function mg:hall/build')
_sub('core/load', 'unless data storage mg:hall v10 run schedule function mg:hall/build', 'unless data storage mg:hall v14 run schedule function mg:hall/build')
_sub('core/load', 'unless data storage mg:hall v11 run schedule function mg:hall/build', 'unless data storage mg:hall v14 run schedule function mg:hall/build')
_sub('core/load', 'unless data storage mg:hall v12 run schedule function mg:hall/build', 'unless data storage mg:hall v14 run schedule function mg:hall/build')
_sub('core/load', 'unless data storage mg:hall v13 run schedule function mg:hall/build', 'unless data storage mg:hall v14 run schedule function mg:hall/build')
_sub('core/load', 'unless data storage mg:hall v9 run schedule function mg:hall/build', 'unless data storage mg:hall v10 run schedule function mg:hall/build')
_sub('core/load', 'unless data storage mg:hall v14 run schedule function mg:hall/build', f'unless data storage mg:hall v{VERSION} run schedule function mg:hall/build')
_sub('core/tick', 'unless block -16 64 15 minecraft:gold_block run function mg:hall/build', f'unless block {MARK[0]} {MARK[1]} {MARK[2]} minecraft:gold_block run function mg:hall/build')
_T3 = 'execute if score $setup mg.st matches 1 if score $lan mg.t matches 12 run function mg:hall/t3_tick'
_hb = f'execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 unless block {MARK[0]} {MARK[1]} {MARK[2]} minecraft:gold_block run function mg:hall/build'
if _T3 not in open(os.path.join(_F, 'core/tick.mcfunction'), encoding='utf-8').read():
    _sub('core/tick', _hb, _hb + '\n' + _T3)
W('t3_tick', ['# Chaque seconde : toutes les 60 s, les joueurs en ligne hors partie reportent leurs victoires dans les top 3 du hall',
              'scoreboard players add #t3t mg.st 1', 'execute if score #t3t mg.st matches ..59 run return 0', 'scoreboard players set #t3t mg.st 0',
              'execute unless entity @e[type=minecraft:item_display,tag=mg.hallbuf] run return 0',
              'execute as @a[tag=!mg.play] run function mg:hall/t3_all'])
W('board_tick', ['# Tableau à droite dans le lobby (classement affiché, pas de vote en cours)',
    'scoreboard players remove $hrt mg.st 1',
    'execute unless score $hrt mg.st matches 1.. run function mg:hall/rotate'])
print(len(GAMES), 'jeux,', len(plaques), 'plaques')
