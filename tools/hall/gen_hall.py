"""Hall des scores + classements par mini-jeu : génère data/mg/function/hall/*.mcfunction.

- un objectif de victoires par famille de jeux (mg.wg_<clé>), crédité au retour au lobby
  pour chaque joueur tagué mg.win (le jeu est lu dans $game) ;
- le tableau à droite alterne le classement général (10 s) et le classement d'un jeu (6 s),
  en sautant les jeux encore jamais gagnés (#any) ;
- un petit hall au sud-ouest de la place : le meneur de chaque jeu, le champion général,
  le joueur le plus assidu et le record du parcours d'élytra. Le nom et le score sont
  « figés » au moment du record (composant résolu via un set_name sur un item_display
  tampon), gardés dans storage mg:hall et restaurés à chaque reconstruction.
Lancer depuis la racine du dépôt : python3 tools/hall/gen_hall.py
"""
import os

OUT = os.path.join('data', 'mg', 'function', 'hall')
GAMES = [  # clé, libellé, couleur, plages de $game
    ('spleef', '❄ Spleef', 'aqua', [(1, 1)]),
    ('tntrun', '✷ TNT Run', 'red', [(2, 2)]),
    ('pvp', '⚔ PvP', 'gold', [(3, 3)]),
    ('bedwars', '🛏 Bedwars', 'red', [(4, 4)]),
    ('sheepwar', '🐑 Sheep War', 'white', [(5, 5), (7, 7)]),
    ('mobarena', '☠ Mob Arena', 'dark_green', [(6, 6)]),
    ('splegg', '❍ Splegg', 'yellow', [(20, 21)]),
    ('sumo', '✊ Sumo', 'gold', [(22, 22)]),
    ('dropper', '⬇ Dropper', 'aqua', [(23, 23), (64, 65)]),
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
]
X0, X1, Z0, Z1 = -20, -12, 22, 28          # emprise du hall (sol y 63), ouvert au nord
MARK = (-16, 64, 25)                       # piédestal central (bloc d'or) : témoin de présence
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
    'scoreboard objectives modify mg.wins displayname [{"text":"✦ Victoires","color":"gold","bold":true},{"text":" (tous les jeux)","color":"gray","bold":false}]'])
W('remove', ['# Désinstallation des classements et du hall'] +
  [f'scoreboard objectives remove mg.wg_{k}' for k, *_ in GAMES] +
  ['kill @e[tag=mg.hall]', 'data remove storage mg:hall e', 'data remove storage mg:hall sbon'])

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
    '$function mg:hall/top {obj:"$(obj)",key:"$(key)",lbl:"$(lbl)",col:"$(col)",unit:""}'])
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
BOARDS = [('mg.wins', None), ('mg.stp', None), ('mg.stk', None)] + [(f'mg.wg_{k}', None) for k, *_ in GAMES]
W('rotate', ['# Tableau à droite : affichage suivant',
    'execute if entity @a[scores={mg.wins=1..}] run scoreboard players set #any mg.wins 1',
    'execute if entity @a[scores={mg.stp=1..}] run scoreboard players set #any mg.stp 1',
    'execute if entity @a[scores={mg.stk=1..}] run scoreboard players set #any mg.stk 1',
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

# ---------------------------------------------------------------- construction du hall
b = ['# Hall des scores (sud-ouest de la place) : construction + restauration des meneurs',
     'kill @e[tag=mg.hall]', '',
     f'fill {X0} 63 {Z0} {X1} 63 {Z1} minecraft:smooth_quartz',
     f'fill {X0} 64 {Z0} {X1} 70 {Z1-1} minecraft:air',
     f'fill {X0} 64 {Z1} {X1} 69 {Z1} minecraft:polished_blackstone_bricks',
     f'fill {X0} 70 {Z1} {X1} 70 {Z1} minecraft:gold_block',
     f'fill {X0} 64 {Z0} {X0} 68 {Z0} minecraft:quartz_pillar', f'fill {X1} 64 {Z0} {X1} 68 {Z0} minecraft:quartz_pillar',
     f'setblock {X0} 69 {Z0} minecraft:lantern', f'setblock {X1} 69 {Z0} minecraft:lantern',
     f'fill {X0} 64 {Z1-1} {X0} 66 {Z1-1} minecraft:quartz_pillar', f'fill {X1} 64 {Z1-1} {X1} 66 {Z1-1} minecraft:quartz_pillar',
     f'fill -16 63 {Z0} -16 63 24 minecraft:red_wool',
     'setblock -19 64 25 minecraft:emerald_block', f'setblock {MARK[0]} {MARK[1]} {MARK[2]} minecraft:gold_block', 'setblock -13 64 25 minecraft:lapis_block', '',
     '# Tampon de résolution des noms (invisible)',
     f'summon minecraft:item_display -15.5 64.5 25.5 {{Tags:["mg.hall","mg.hallbuf"],item:{{id:"minecraft:paper"}},{TR % (0.001, 0.001, 0.001)}}}',
     f'summon minecraft:text_display -15.5 71.0 27.5 {{Tags:["mg.hall"],billboard:"center",background:0,text:[{{"text":"🏆 Hall des scores","color":"gold","bold":true}}],{TR % (1.4, 1.4, 1.4)}}}',
     '', '# Piédestaux : objet qui tourne + plaque']
peds = [(-18.5, 'stp', '▶ Le plus assidu', 'green', 'clock'),
        (-15.5, 'wins', '👑 Champion des mini-jeux', 'gold', 'totem_of_undying'),
        (-12.5, 'ely', "🪽 Record petit parcours d'élytra", 'aqua', 'elytra')]
plaques = [(x, 66.9, 25.5, k, l, c, 0.55) for x, k, l, c, _ in peds]
plaques.append((-12.5, 67.6, 25.5, 'ely2', "🪽 Record grand parcours d'élytra", 'light_purple', 0.55))
for x, k, l, c, it in peds:
    b.append(f'summon minecraft:item_display {x} 65.8 25.5 {{Tags:["mg.hall","mg.lspin","mg.lbob"],billboard:"fixed",item:{{id:"minecraft:{it}"}},{TR % (0.9, 0.9, 0.9)}}}')
xs = [-19.3, -17.4, -15.5, -13.6, -11.7]
ys = [68.3, 67.1, 65.9, 64.7]
for i, (k, l, c, _) in enumerate(GAMES):
    plaques.append((xs[i % 5], ys[i // 5], 27.2, k, l, c, 0.42))
b.append('')
b.append('# Plaques : texte par défaut, puis meneur enregistré s\'il existe')
for x, y, z, k, l, c, s in plaques:
    b.append(f'summon minecraft:text_display {x} {y} {z} {{Tags:["mg.hall","mg.h_{k}"],billboard:"vertical",text:[{{"text":"{q(l)}","color":"{c}","bold":true}},{{"text":"\\n— personne —","color":"dark_gray","bold":false}}],{TR % (s, s, s)}}}')
    b.append(f'execute if data storage mg:hall e.{k} run data modify entity @e[type=minecraft:text_display,tag=mg.h_{k},limit=1] text set from storage mg:hall e.{k}')
W('build', b)
W('board_tick', ['# Tableau à droite dans le lobby (classement affiché, pas de vote en cours)',
    'scoreboard players remove $hrt mg.st 1',
    'execute unless score $hrt mg.st matches 1.. run function mg:hall/rotate'])
print(len(GAMES), 'jeux,', len(plaques), 'plaques')
