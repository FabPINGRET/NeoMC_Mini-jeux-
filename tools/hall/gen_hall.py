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
    ('elyrace', "🪽 Course d'élytres", 'aqua', [(66, 66)]),
    ('elytra', '🪽 Élytra (3 modes)', 'aqua', [(75, 75)]),
    ('telephone', '📞 Téléphone', 'gold', [(83, 83)]),
    ('tron', '⚡ Tron', 'aqua', [(84, 85), (200, 201)]),
    ('koth', '👑 King of the Hill', 'gold', [(86, 87), (206, 209)]),
    ('tower', '🏰 The Towers', 'gold', [(88, 88)]),
    ('convoy', '🚚 Convoi', 'gold', [(89, 90)]),
    ('ctf', '🚩 Capture the Flag', 'red', [(93, 93)]),
    ('uhc', '⛏ Mini UHC Run', 'gold', [(94, 94), (202, 202), (204, 204)]),
    ('hg', '🏹 Mini Hunger Games', 'gold', [(95, 95), (203, 203), (205, 205)]),
    ('prophunt', '🎭 Prop Hunt', 'gold', [(96, 96)]),
    ('zombies', '🧟 Zombies', 'dark_green', [(97, 97), (210, 210), (212, 212)]),
    ('infection', '🧪 Infection', 'green', [(98, 98), (211, 211), (213, 213), (217, 219)]),
    ('bomber', '💣 Bombardier', 'red', [(99, 99)]),
    ('chameleon', '🦎 Meccha Chameleon', 'green', [(198, 198)]),
    ('wii', '🎾 Wii Sports', 'aqua', [(214, 216)]),
    ('soleil', '🔴 1, 2, 3 Soleil', 'red', [(220, 220)]),
    ('autotamp', '🚗 Autos tamponneuses', 'aqua', [(221, 223)]),
    ('slimejump', '🟩 Slime Jump', 'green', [(224, 224)]),
    ('lab', '🙈 Labyrinthe aveugle', 'light_purple', [(225, 225)]),
    ('master', '👑 Master dit', 'gold', [(226, 226)]),
]
X0, X1, Z0, Z1 = -24, -6, 11, 25           # emprise du hall (sol y 63), ouvert au nord, juste au sud-ouest de la place
OLD_Z0, OLD_Z1 = 21, 35                    # ancien emplacement (v8 et avant), nettoyé une fois
PZ = Z0 + 4                                # rangée des piédestaux
MARK = (-16, 64, PZ)                       # piédestal central (bloc d'or) : témoin de présence
WALL_TOP = 74                              # haut du mur des plaques (6 rangées)
VERSION = 9
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
  ['kill @e[tag=mg.hall]', 'schedule clear mg:hall/build', 'data remove storage mg:hall e', 'data remove storage mg:hall sbon', 'data remove storage mg:hall v2', 'data remove storage mg:hall v3', 'data remove storage mg:hall v4', 'data remove storage mg:hall v5', 'data remove storage mg:hall v6', 'data remove storage mg:hall v7', 'data remove storage mg:hall v8', 'data remove storage mg:hall v9', 'data remove storage mg:hall v10', 'data remove storage mg:hall v11', 'data remove storage mg:hall v12', 'data remove storage mg:hall v13', 'data remove storage mg:hall v14',
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

# ---------------------------------------------------------------- construction du hall
b = ['# Hall des scores (sud-ouest de la place) : construction + restauration des meneurs',
     '# Chunks du hall pas encore chargés (démarrage du serveur) : on réessaie dans 1 s, 60 fois au plus (motif de mg:dropadv/loaded_all :',
     '# « unless block … bedrock » ne réussit que si le chunk est chargé, il n\'y a jamais de bedrock à y 300). #hl = 1 : les 2 chunks sont chargés',
     f'execute store success score #hl mg.st unless block {X0 + 2} 300 {Z0 + 3} minecraft:bedrock',
     f'execute if score #hl mg.st matches 1 store success score #hl mg.st unless block {X1 - 2} 300 {Z0 + 3} minecraft:bedrock',
     'execute if score #hl mg.st matches 0 run scoreboard players add #hlr mg.st 1',
     'execute if score #hl mg.st matches 0 if score #hlr mg.st matches 60.. run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Hall des scores : chunks pas chargés, construction abandonnée (relance /function mg:hall/build).","color":"red"}]',
     'execute if score #hl mg.st matches 0 if score #hlr mg.st matches 60.. run return run scoreboard players set #hlr mg.st 0',
     'execute if score #hl mg.st matches 0 run return run schedule function mg:hall/build 20t',
     'scoreboard players set #hlr mg.st 0',
     'kill @e[tag=mg.hall]',
     'execute unless data storage mg:hall v9 run function mg:hall/clear_old', '',
     f'fill {X0} 63 {Z0} {X1} 63 {Z1} minecraft:smooth_quartz',
     f'fill {X0} 64 {Z0} {X1} 79 {Z1} minecraft:air',
     # mur du fond (plaques des jeux) : pierre taillée comme les murets du spawn, un peu de mousse et de fissures,
     # soubassement et corniche en dalles ; les plaques ont leur fond sombre, lisibles sur ce gris moyen
     f'fill {X0} 64 {Z1} {X1} {WALL_TOP} {Z1} minecraft:stone_bricks',
     ] + [f'setblock {x} {y} {Z1} minecraft:{"mossy_stone_bricks" if (x * 7 + y * 3) % 5 == 0 else "cracked_stone_bricks"}'
          for x in range(X0, X1 + 1) for y in range(64, WALL_TOP + 1) if (x * 7 + y * 3) % 5 in (0, 3) and (x + y) % 2 == 0] + [
     f'fill {X0} 64 {Z1} {X1} 64 {Z1} minecraft:mossy_stone_bricks',
     f'fill {X0} {WALL_TOP + 1} {Z1} {X1} {WALL_TOP + 1} {Z1} minecraft:stone_brick_slab[type=bottom]',
     # tapis rouge de l'entrée au fond, bancs, lustres
     f'fill -16 63 {Z0} -15 63 {Z1 - 1} minecraft:red_wool',
     # l'arbre planté juste devant l'entrée masquait le hall
     f'fill -20 64 {Z0 - 6} -11 74 {Z0 - 1} minecraft:air replace #minecraft:logs', f'fill -20 64 {Z0 - 6} -11 74 {Z0 - 1} minecraft:air replace #minecraft:leaves',
     f'fill {X0 + 2} 64 {Z1 - 7} {X0 + 4} 64 {Z1 - 7} minecraft:dark_oak_stairs[facing=south]', f'fill {X1 - 4} 64 {Z1 - 7} {X1 - 2} 64 {Z1 - 7} minecraft:dark_oak_stairs[facing=south]',
     f'fill {X0 + 2} 64 {Z1 - 10} {X0 + 4} 64 {Z1 - 10} minecraft:dark_oak_stairs[facing=south]', f'fill {X1 - 4} 64 {Z1 - 10} {X1 - 2} 64 {Z1 - 10} minecraft:dark_oak_stairs[facing=south]',
     f'fill {X0 + 1} 63 {Z0 + 1} {X0 + 1} 63 {Z1 - 1} minecraft:gold_block', f'fill {X1 - 1} 63 {Z0 + 1} {X1 - 1} 63 {Z1 - 1} minecraft:gold_block',
     f'setblock -19 64 {PZ} minecraft:emerald_block', f'setblock {MARK[0]} {MARK[1]} {MARK[2]} minecraft:gold_block', f'setblock -13 64 {PZ} minecraft:lapis_block', '',
     '# Tampon de résolution des noms (invisible)',
     f'summon minecraft:item_display -15.5 64.5 {PZ}.5 {{Tags:["mg.hall","mg.hallbuf"],item:{{id:"minecraft:paper"}},{TR % (0.001, 0.001, 0.001)}}}',
     f'summon minecraft:text_display -15.5 {WALL_TOP + 1.6} {Z1 - 0.4} {{Tags:["mg.hall"],billboard:"center",background:0,text:[{{"text":"🏆 Hall des scores","color":"gold","bold":true}}],{TR % (4.5, 4.5, 4.5)}}}',
     '', '# Piédestaux : objet qui tourne + plaque']
peds = [(-18.5, 'stp', '▶ Le plus assidu', 'green', 'clock'),
        (-15.5, 'wins', '👑 Champion des mini-jeux', 'gold', 'totem_of_undying'),
        (-12.5, 'ely', "🪽 Record petit parcours d'élytra", 'aqua', 'elytra')]
plaques = [(x, 66.9, PZ + 0.5, k, l, c, 1.35) for x, k, l, c, _ in peds]   # textes ×1,5
plaques.append((-12.5, 68.4, PZ + 0.5, 'ely2', "🪽 Record grand parcours d'élytra", 'light_purple', 1.35))
plaques.append((-12.5, 69.9, PZ + 0.5, 'elyg', '🪽 Record Élytra : course', 'aqua', 1.35))
plaques.append((-15.5, 73.9, Z1 - 0.7, 'gen', '🏅 Meilleur niveau général', 'aqua', 1.5))   # juste au-dessus du tableau
for x, k, l, c, it in peds:
    b.append(f'summon minecraft:item_display {x} 65.8 {PZ}.5 {{Tags:["mg.hall","mg.lspin","mg.lbob"],billboard:"fixed",item:{{id:"minecraft:{it}"}},{TR % (0.9, 0.9, 0.9)}}}')
xs = [-22.5 + 3.0 * i for i in range(6)]   # 6 colonnes × 6 rangées sur le mur du fond (36 plaques), texte plus grand
ys = [72.6, 71.3, 70.0, 68.7, 67.4, 66.1, 64.8]   # 7 rangées (42 places)   # plus bas (à hauteur des yeux) et texte plus grand
assert len(GAMES) <= len(xs) * len(ys), 'agrandir la grille de plaques'
for i, (k, l, c, _) in enumerate(GAMES):
    plaques.append((xs[i % 6], ys[i // 6], Z1 - 0.8, k, l, c, 1.125))
b.append('')
b.append('# Plaques : texte par défaut, puis meneur enregistré s\'il existe')
for x, y, z, k, l, c, s in plaques:
    lw = 200 if k == 'gen' else int(2.8 / (0.025 * s))   # retour à la ligne : pas de chevauchement avec la plaque voisine (3 blocs)
    b.append(f'summon minecraft:text_display {x} {y} {z} {{Tags:["mg.hall","mg.h_{k}"],billboard:"vertical",line_width:{lw},text:[{{"text":"{q(l)}","color":"{c}","bold":true}},{{"text":"\\n— personne —","color":"dark_gray","bold":false}}],{TR % (s, s, s)}}}')
    b.append(f'execute if data storage mg:hall e.{k} run data modify entity @e[type=minecraft:text_display,tag=mg.h_{k},limit=1] text set from storage mg:hall e.{k}')
# Version du hall : core/load reconstruit le hall (une fois) sur les mondes dont les plaques sont plus anciennes (nouveau jeu ajouté)
b.append('data modify storage mg:hall v2 set value 1b')
b.append('data modify storage mg:hall v3 set value 1b')
b.append('data modify storage mg:hall v4 set value 1b')
b.append('data modify storage mg:hall v5 set value 1b')
b.append('data modify storage mg:hall v6 set value 1b')
b.append('data modify storage mg:hall v7 set value 1b')
b.append('data modify storage mg:hall v8 set value 1b')
b.append('data modify storage mg:hall v9 set value 1b')
b.append('data modify storage mg:hall v10 set value 1b')
b.append('data modify storage mg:hall v11 set value 1b')
b.append('data modify storage mg:hall v12 set value 1b')
b.append('data modify storage mg:hall v13 set value 1b')
b.append('data modify storage mg:hall v14 set value 1b')
W('build', b)
W('clear_old', ['# Ancien emplacement du hall (z %d..%d) : mur et sol retirés, pelouse (une fois, avant la v9)' % (OLD_Z0, OLD_Z1),
                f'fill {X0} 64 {Z1 + 1} {X1} 74 {OLD_Z1} minecraft:air',
                f'fill {X0} 63 {Z1 + 1} {X1} 63 {OLD_Z1} minecraft:grass_block'])
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
W('board_tick', ['# Tableau à droite dans le lobby (classement affiché, pas de vote en cours)',
    'scoreboard players remove $hrt mg.st 1',
    'execute unless score $hrt mg.st matches 1.. run function mg:hall/rotate'])
print(len(GAMES), 'jeux,', len(plaques), 'plaques')
