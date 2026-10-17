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
# Hall v18 : « Allée des champions » à ciel ouvert au sud-ouest de la place : une seule allée est-ouest (z 24..27) bordée
# de chaque côté par une rangée d'étals de marché (22 par côté, 2 blocs chacun) : auvent rayé, top 3 sur fond sombre, objet et bloc du jeu sur le comptoir. Bordure
# basse (1 bloc) autour, place d'entrée à l'est (x -11..-6) avec les piédestaux d'honneur.
HX0, HX1, HZ0, HZ1 = -60, -12, 19, 31      # bordure comprise
CX0, CZ0, CZ1 = -60, 15, 36                # zone dégagée (anciennes versions du hall)
BX0, BP, NB = -59, 2, 22                   # 1er stand en x -59, un stand tous les 2 blocs, 22 par côté
OLD = (-24, -6, 11, 25)                    # hall v14 (x1, x2, z1, z2), effacé une fois
MARK = (-9, 64, 25)                        # piédestal du champion (bloc d'or) : témoin de présence
VERSION = 21
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
  ['kill @e[tag=mg.hall]', 'schedule clear mg:hall/build', 'data remove storage mg:hall e', 'data remove storage mg:hall t3', 'data remove storage mg:hall t3x', 'data remove storage mg:hall v15', 'data remove storage mg:hall v16', 'data remove storage mg:hall v17', 'data remove storage mg:hall v18', 'data remove storage mg:hall v19', 'data remove storage mg:hall v20', 'data remove storage mg:hall v21', 'data remove storage mg:hall sbon', 'data remove storage mg:hall v2', 'data remove storage mg:hall v3', 'data remove storage mg:hall v4', 'data remove storage mg:hall v5', 'data remove storage mg:hall v6', 'data remove storage mg:hall v7', 'data remove storage mg:hall v8', 'data remove storage mg:hall v9', 'data remove storage mg:hall v10', 'data remove storage mg:hall v11', 'data remove storage mg:hall v12', 'data remove storage mg:hall v13', 'data remove storage mg:hall v14',
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

# ---------------------------------------------------------------- construction du hall (v18 : une allée, les stands de chaque côté)
CONC = {'gold': 'yellow', 'aqua': 'light_blue', 'red': 'red', 'white': 'white', 'dark_green': 'green', 'yellow': 'yellow',
        'light_purple': 'magenta', 'gray': 'gray', 'green': 'lime'}
AZ1, AZ2 = 23, 27                          # allée (z) : 5 blocs, centrée sur le piédestal du champion (z 25)
# côtés : (z intérieur 1, z intérieur 2, z du fond / podium, sens vers l'allée)
SIDES = [(HZ0 + 1, AZ1 - 1, HZ0 + 1, 1), (AZ2 + 1, HZ1 - 1, HZ1 - 1, -1)]
STANDS = [(BX0 + BP * i, sd) for sd in SIDES for i in range(NB)]
assert len(GAMES) <= len(STANDS), f'allonger l\'allée : {len(GAMES)} jeux pour {len(STANDS)} stands'
b = ['# Allée des champions (Hall des scores v18, à ciel ouvert, sud-ouest de la place) : construction + top 3 (généré par tools/hall/gen_hall.py)',
     '# Chunks pas encore chargés (démarrage du serveur) : on réessaie dans 1 s, 60 fois au plus',
     f'execute store success score #hl mg.st unless block {HX0 + 2} 300 {HZ0 + 3} minecraft:bedrock',
     f'execute if score #hl mg.st matches 1 store success score #hl mg.st unless block {HX1 - 2} 300 {HZ1 - 3} minecraft:bedrock',
     'execute if score #hl mg.st matches 0 run scoreboard players add #hlr mg.st 1',
     'execute if score #hl mg.st matches 0 if score #hlr mg.st matches 60.. run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Hall des scores : chunks pas chargés, construction abandonnée (relance /function mg:hall/build).","color":"red"}]',
     'execute if score #hl mg.st matches 0 if score #hlr mg.st matches 60.. run return run scoreboard players set #hlr mg.st 0',
     'execute if score #hl mg.st matches 0 run return run schedule function mg:hall/build 20t',
     'scoreboard players set #hlr mg.st 0',
     'kill @e[tag=mg.hall]',
     'execute unless data storage mg:hall v15 run function mg:hall/clear_old', '',
     '# terrain des versions précédentes rendu à la pelouse, puis l\'allée et ses deux rangées de stands',
     f'fill {CX0} 64 {CZ0} {HX1 + 6} 84 {CZ1} minecraft:air',
     # débord du toit du bâtiment v15 (dalles en y 73, une rangée hors de la zone) : retiré
     f'fill -61 73 14 -11 73 14 minecraft:air replace minecraft:dark_oak_slab', f'fill -61 73 37 -11 73 37 minecraft:air replace minecraft:dark_oak_slab',
     f'fill -61 73 14 -61 73 37 minecraft:air replace minecraft:dark_oak_slab', f'fill -11 73 14 -11 73 37 minecraft:air replace minecraft:dark_oak_slab',
     f'fill {CX0} 62 {CZ0} {HX1 + 6} 62 {CZ1} minecraft:dirt',
     f'fill {CX0} 63 {CZ0} {HX1 + 6} 63 {CZ1} minecraft:grass_block',
     f'fill {HX0 + 1} 63 {AZ1} {HX1 + 6} 63 {AZ2} minecraft:dirt_path',
     f'fill {HX1 - 1} 63 {HZ0} {HX1 + 6} 63 {HZ1} minecraft:polished_andesite',
     # bordure basse (1 bloc) autour des stands, ouverte à l'est sur l'allée
     *[f'fill {xa} 64 {za} {xb} 64 {zb} minecraft:moss_block' for xa, za, xb, zb in ((HX0, HZ0, HX1, HZ0), (HX0, HZ1, HX1, HZ1), (HX0, HZ0, HX0, HZ1), (HX1, HZ0, HX1, HZ1))],
     f'fill {HX1} 64 {AZ1} {HX1} 64 {AZ2} minecraft:air',
     # fond de l'allée ouvert à l'ouest, raccordé au chemin du pont (sortie de l'île)
     f'fill {HX0} 64 {AZ1} {HX0} 64 {AZ2} minecraft:air', f'fill {HX0} 63 {AZ1} {HX0} 63 {AZ2} minecraft:dirt_path',
     f'fill {HX0 - 3} 63 {AZ1} {HX0 - 1} 63 {AZ2} minecraft:dirt_path replace minecraft:grass_block',
     f'fill {HX0 - 3} 64 {AZ1} {HX0 - 1} 65 {AZ2} minecraft:air replace #minecraft:replaceable',
     *[f'setblock {x} 65 {z} minecraft:lantern' for x in range(HX0, HX1 + 1, 6) for z in (HZ0, HZ1)]]
# étals du marché : fond en planches, comptoir côté allée (un poteau + un bloc rappelant le jeu, l'objet du jeu posé dessus),
# auvent rayé rouge / blanc ; chaque étal fait 2 blocs, poteau à gauche
DECO = {'spleef': ('diamond_shovel', 'snow_block'), 'tntrun': ('tnt', 'tnt'), 'pvp': ('iron_sword', 'chiseled_stone_bricks'),
        'bedwars': ('red_bed', 'red_wool'), 'sheepwar': ('shears', 'white_wool'), 'mobarena': ('zombie_head', 'mossy_cobblestone'),
        'splegg': ('egg', 'hay_block'), 'sumo': ('slime_ball', 'slime_block'), 'dropper': ('feather', 'blue_ice'),
        'oitc': ('bow', 'target'), 'tnttag': ('tnt', 'red_concrete'), 'blockparty': ('music_disc_cat', 'jukebox'),
        'anvil': ('anvil', 'anvil'), 'turf': ('bow', 'red_terracotta'), 'quake': ('diamond_hoe', 'target'),
        'paintball': ('snowball', 'lime_concrete'), 'icerace': ('oak_boat', 'packed_ice'), 'bb': ('brick', 'crafting_table'),
        'party': ('cake', 'cake'), 'kart': ('minecart', 'redstone_block'), 'elyrace': ('elytra', 'end_stone_bricks'),
        'elytra': ('firework_rocket', 'purpur_block'), 'telephone': ('writable_book', 'bookshelf'), 'tron': ('blaze_rod', 'sea_lantern'),
        'koth': ('golden_helmet', 'gold_block'), 'tower': ('golden_apple', 'quartz_block'), 'convoy': ('chest_minecart', 'barrel'),
        'ctf': ('red_banner', 'blue_wool'), 'uhc': ('golden_apple', 'grass_block'), 'hg': ('iron_axe', 'chest'),
        'prophunt': ('armor_stand', 'pumpkin'), 'zombies': ('rotten_flesh', 'mossy_stone_bricks'), 'infection': ('zombie_head', 'green_concrete'),
        'bomber': ('fire_charge', 'tnt'), 'chameleon': ('lime_dye', 'moss_block'), 'wii': ('snowball', 'white_concrete'),
        'soleil': ('red_dye', 'red_concrete'), 'autotamp': ('oak_boat', 'blue_ice'), 'slimejump': ('slime_ball', 'slime_block'),
        'lab': ('ink_sac', 'black_concrete'), 'master': ('clock', 'gold_block'), 'murder': ('iron_sword', 'redstone_block'),
        'bman': ('tnt', 'stone_bricks'), 'maze': ('compass', 'moss_block')}
BG = (0xC8 << 24 | 0x1A1410) - (1 << 32)   # fond sombre des panneaux (ARGB)
for i, (k, l, c, _) in enumerate(GAMES):
    x0, (za, zb, back, sgn) = STANDS[i]
    front = back + 2 * sgn
    it, blk = DECO.get(k, ('paper', 'spruce_planks'))
    b += [f'fill {x0} 63 {za} {x0 + 1} 63 {zb} minecraft:spruce_planks',
          f'fill {x0} 64 {back} {x0 + 1} 66 {back} minecraft:stripped_spruce_wood',
          f'setblock {x0} 64 {front} minecraft:spruce_planks', f'setblock {x0 + 1} 64 {front} minecraft:{blk}',
          f'fill {x0} 65 {front} {x0} 66 {front} minecraft:spruce_fence',
          f'fill {x0} 67 {back} {x0 + 1} 67 {front} minecraft:{"red_wool" if i % 2 == 0 else "white_wool"}',
          f'setblock {x0 + 1} 66 {back + sgn} minecraft:light[level=13]']
for (za, zb, back, sgn) in SIDES:                     # dernier poteau de chaque rangée
    xe = BX0 + BP * NB
    b += [f'setblock {xe} 64 {back + 2 * sgn} minecraft:spruce_planks', f'fill {xe} 65 {back + 2 * sgn} {xe} 66 {back + 2 * sgn} minecraft:spruce_fence']
# ------- décor autour de l'allée (comme le reste du spawn) : arches, arbres, massifs fleuris, réverbères, bancs
import random as _rnd
_r = _rnd.Random(2026)
b += ['', '# Décor : arches d\'entrée (est) et de sortie (ouest)']
for xa in (HX1, HX0):
    b += [f'fill {xa} 64 {AZ1 - 1} {xa} 68 {AZ1 - 1} minecraft:stripped_spruce_log', f'fill {xa} 64 {AZ2 + 1} {xa} 68 {AZ2 + 1} minecraft:stripped_spruce_log',
          f'fill {xa} 69 {AZ1 - 1} {xa} 69 {AZ2 + 1} minecraft:spruce_planks', f'fill {xa} 70 {AZ1 - 1} {xa} 70 {AZ2 + 1} minecraft:spruce_slab[type=bottom]',
          f'setblock {xa} 70 {(AZ1 + AZ2) // 2} minecraft:spruce_planks', f'setblock {xa} 71 {(AZ1 + AZ2) // 2} minecraft:lantern',
          f'setblock {xa} 68 {AZ1 + 1} minecraft:lantern[hanging=true]', f'setblock {xa} 68 {AZ2 - 1} minecraft:lantern[hanging=true]']
b.append('# Décor : arbres de part et d\'autre (chênes et bouleaux)')


def tree(x, z, kind):
    log, lv = (('oak_log', 'oak_leaves[persistent=true]') if kind == 0 else ('birch_log', 'birch_leaves[persistent=true]'))
    return [f'fill {x - 2} 67 {z - 2} {x + 2} 68 {z + 2} minecraft:{lv}', f'fill {x - 2} 67 {z - 2} {x - 2} 68 {z - 2} minecraft:air',
            f'fill {x + 2} 67 {z - 2} {x + 2} 68 {z - 2} minecraft:air', f'fill {x - 2} 67 {z + 2} {x - 2} 68 {z + 2} minecraft:air',
            f'fill {x + 2} 67 {z + 2} {x + 2} 68 {z + 2} minecraft:air',
            f'fill {x - 1} 69 {z} {x + 1} 69 {z} minecraft:{lv}', f'fill {x} 69 {z - 1} {x} 69 {z + 1} minecraft:{lv}', f'setblock {x} 70 {z} minecraft:{lv}',
            f'fill {x} 64 {z} {x} 69 {z} minecraft:{log}']


for i, x in enumerate(range(HX0 + 4, HX1 - 2, 12)):
    b += tree(x, HZ0 - 3, i % 2) + tree(x + 6, HZ1 + 3, (i + 1) % 2)
b.append('# Décor : massifs fleuris le long de la bordure, herbes et buissons')
FLW = ['poppy', 'dandelion', 'cornflower', 'allium', 'azure_bluet', 'oxeye_daisy', 'red_tulip', 'white_tulip', 'lily_of_the_valley']
for z in (HZ0 - 1, HZ1 + 1):
    for x in range(HX0, HX1 + 1):
        if (x - HX0) % 6 == 3:
            b.append(f'setblock {x} 64 {z} minecraft:{_r.choice(["azalea", "flowering_azalea"])}')
        else:
            b.append(f'setblock {x} 64 {z} minecraft:{_r.choice(FLW)}')
for z in list(range(CZ0, HZ0 - 1)) + list(range(HZ1 + 2, CZ1 + 1)):
    for x in range(HX0 - 3, HX1 + 7):
        if _r.random() < 0.18:
            b.append(f'execute if block {x} 64 {z} minecraft:air if block {x} 63 {z} minecraft:grass_block run setblock {x} 64 {z} minecraft:{_r.choice(["short_grass", "short_grass", "fern"] + FLW[:3])}')
b.append('# Décor : réverbères et bancs de la place d\'entrée')
for (x, z) in ((HX1 + 1, HZ0), (HX1 + 6, HZ0), (HX1 + 1, HZ1), (HX1 + 6, HZ1)):
    b += [f'fill {x} 64 {z} {x} 66 {z} minecraft:dark_oak_fence', f'setblock {x} 67 {z} minecraft:lantern']
b += [f'fill {HX1 + 2} 64 {HZ0} {HX1 + 5} 64 {HZ0} minecraft:spruce_stairs[facing=north]',
      f'fill {HX1 + 2} 64 {HZ1} {HX1 + 5} 64 {HZ1} minecraft:spruce_stairs[facing=south]']
b += ['', '# Place d\'entrée (est) : piédestaux d\'honneur',
      f'setblock -9 64 20 minecraft:emerald_block', f'setblock {MARK[0]} {MARK[1]} {MARK[2]} minecraft:gold_block', f'setblock -9 64 30 minecraft:lapis_block',
      '', '# Tampon de résolution des noms (invisible)',
      f'summon minecraft:item_display -8.5 64.5 25.5 {{Tags:["mg.hall","mg.hallbuf"],item:{{id:"minecraft:paper"}},{TR % (0.001, 0.001, 0.001)}}}',
      f'summon minecraft:text_display -8.5 70.8 25.5 {{Tags:["mg.hall"],billboard:"vertical",background:0,text:[{{"text":"🏆 Allée des champions","color":"gold","bold":true}},{{"text":"\\n🥇 🥈 🥉 le top 3 de chaque jeu, de chaque côté de l\'allée","color":"gray","bold":false}}],{TR % (1.6, 1.6, 1.6)}}}',
      '', '# Piédestaux : objet qui tourne + plaque']
peds = [(-8.5, 20.5, 'stp', '▶ Le plus assidu', 'green', 'clock'),
        (-8.5, 25.5, 'wins', '👑 Champion des mini-jeux', 'gold', 'totem_of_undying'),
        (-8.5, 30.5, 'ely', "🪽 Record petit parcours d'élytra", 'aqua', 'elytra')]
plaques = [(x, 66.7, z, k, l, c, 0.9) for x, z, k, l, c, _ in peds]
plaques.append((-8.5, 68.1, 30.5, 'ely2', "🪽 Record grand parcours d'élytra", 'light_purple', 0.9))
plaques.append((-8.5, 69.5, 30.5, 'elyg', '🪽 Record Élytra : course', 'aqua', 0.9))
plaques.append((-8.5, 68.6, 25.5, 'gen', '🏅 Meilleur niveau général', 'aqua', 1.1))
for x, z, k, l, c, it in peds:
    b.append(f'summon minecraft:item_display {x} 65.8 {z} {{Tags:["mg.hall","mg.lspin","mg.lbob"],billboard:"fixed",item:{{id:"minecraft:{it}"}},{TR % (0.8, 0.8, 0.8)}}}')
b.append('')
b.append('# Plaques d\'honneur : texte par défaut, puis meneur enregistré s\'il existe')
for x, y, z, k, l, c, s in plaques:
    lw = 200 if k == 'gen' else int(2.6 / (0.025 * s))
    b.append(f'summon minecraft:text_display {x} {y} {z} {{Tags:["mg.hall","mg.h_{k}"],billboard:"vertical",line_width:{lw},text:[{{"text":"{q(l)}","color":"{c}","bold":true}},{{"text":"\\n— personne —","color":"dark_gray","bold":false}}],{TR % (s, s, s)}}}')
    b.append(f'execute if data storage mg:hall e.{k} run data modify entity @e[type=minecraft:text_display,tag=mg.h_{k},limit=1] text set from storage mg:hall e.{k}')
b.append('')
b.append('# Étals : top 3 de chaque jeu sur fond sombre (texte par défaut, puis top 3 enregistré), objet du jeu sur le comptoir')
for i, (k, l, c, _) in enumerate(GAMES):
    x0, (za, zb, back, sgn) = STANDS[i]
    it, blk = DECO.get(k, ('paper', 'spruce_planks'))
    b.append(f'summon minecraft:text_display {x0 + 1.0} 65.35 {back + 0.5 + sgn} {{Tags:["mg.hall","mg.h3_{k}"],billboard:"vertical",line_width:120,background:{BG},'
             f'text:[{{"text":"{q(l)}","color":"{c}","bold":true}},{{"text":"\\n— personne —","color":"dark_gray","bold":false}}],{TR % (0.45, 0.45, 0.45)}}}')
    b.append(f'summon minecraft:item_display {x0 + 1.5} 65.45 {back + 2 * sgn + 0.5} {{Tags:["mg.hall","mg.lspin"],billboard:"fixed",item:{{id:"minecraft:{it}"}},{TR % (0.55, 0.55, 0.55)}}}')
    b.append(f'execute if data storage mg:hall t3x.{k} run data modify entity @e[type=minecraft:text_display,tag=mg.h3_{k},limit=1] text set from storage mg:hall t3x.{k}')
b += [f'data modify storage mg:hall v{v} set value 1b' for v in range(2, VERSION + 1)]
W('build', b)
ox1, ox2, oz1, oz2 = OLD
W('clear_old', ['# Ancien hall (v14 : x %d..%d, z %d..%d) : ce qui dépasse du nouveau est rendu à la pelouse (une fois)' % OLD,
                f'fill {ox1} 64 {oz1} {ox2} 79 {CZ0 - 1} minecraft:air', f'fill {ox1} 63 {oz1} {ox2} 63 {CZ0 - 1} minecraft:grass_block'])

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
_sub('core/load', 'unless data storage mg:hall v15 run schedule function mg:hall/build', f'unless data storage mg:hall v{VERSION} run schedule function mg:hall/build')
_sub('core/load', 'unless data storage mg:hall v16 run schedule function mg:hall/build', f'unless data storage mg:hall v{VERSION} run schedule function mg:hall/build')
_sub('core/load', 'unless data storage mg:hall v17 run schedule function mg:hall/build', f'unless data storage mg:hall v{VERSION} run schedule function mg:hall/build')
_sub('core/load', 'unless data storage mg:hall v18 run schedule function mg:hall/build', f'unless data storage mg:hall v{VERSION} run schedule function mg:hall/build')
_sub('core/load', 'unless data storage mg:hall v19 run schedule function mg:hall/build', f'unless data storage mg:hall v{VERSION} run schedule function mg:hall/build')
_sub('core/load', 'unless data storage mg:hall v20 run schedule function mg:hall/build', f'unless data storage mg:hall v{VERSION} run schedule function mg:hall/build')
_sub('core/tick', 'unless block -9 64 27 minecraft:gold_block run function mg:hall/build', f'unless block {MARK[0]} {MARK[1]} {MARK[2]} minecraft:gold_block run function mg:hall/build')
_sub('core/tick', 'unless block -16 64 15 minecraft:gold_block run function mg:hall/build', f'unless block {MARK[0]} {MARK[1]} {MARK[2]} minecraft:gold_block run function mg:hall/build')
_sub('core/tick', 'unless block -58 64 26 minecraft:gold_block run function mg:hall/build', f'unless block {MARK[0]} {MARK[1]} {MARK[2]} minecraft:gold_block run function mg:hall/build')
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
