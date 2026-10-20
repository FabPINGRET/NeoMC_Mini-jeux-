# Terra Nova : boutique, tableau des missions, missions 1 à 4 ; exécuté par gen_terranova.py (exec), à la place exacte de ce bloc.
# Tranche contiguë de l'ancien gen_terranova.py : mêmes globals que la façade, aucun import, aucune copie de w/js/patch.
# Utilise : ARM, CRATES, DIM, HX, LOC_HOME, MEDK, NETL, OUTPOSTS, OUT_H, PAD, RIFLE2, SADDLE, SONIC, TR, TRAP, WF, gain, js, say, top, w

# ================================================================ boutique, tableau des missions
BUY = ['# @s (joueur) achète au présentoir $tvk : prix, conditions, objet',
       'scoreboard players set $tvp mg.st 0'] + [f'execute if score $tvk mg.st matches {c} run scoreboard players set $tvp mg.st {p}' for (c, _, _, p, _) in PAD.values()] + [
       'execute if score $tvk mg.st matches 1 if items entity @s container.* *[custom_data~{tv:4}] run return run function mg:terra/buy_has',
       'execute if score $tvk mg.st matches 2 if score @s mg.trwp matches 2.. run return run function mg:terra/buy_has',
       'execute if score $tvk mg.st matches 3 if items entity @s container.* *[custom_data~{tv:5}] run return run function mg:terra/buy_has_net',
       'execute if score $tvk mg.st matches 4 unless items entity @s container.* *[custom_data~{tv:5}] run return run function mg:terra/buy_need_net',
       'execute if score $tvk mg.st matches 7 if score @s mg.trar matches 1.. run return run function mg:terra/buy_has',
       'execute if score @s mg.tvc < $tvp mg.st run return run function mg:terra/buy_poor',
       'scoreboard players operation @s mg.tvc -= $tvp mg.st',
       'execute if score $tvk mg.st matches 1 run give @s ' + SONIC,
       'execute if score $tvk mg.st matches 2 run clear @s ' + WF + '[minecraft:custom_data~{tv:2}]',
       'execute if score $tvk mg.st matches 2 run give @s ' + RIFLE2, 'execute if score $tvk mg.st matches 2 run scoreboard players set @s mg.trwp 2',
       'execute if score $tvk mg.st matches 3 run give @s ' + NETL,
       'execute if score $tvk mg.st matches 3..4 run scoreboard players add @s mg.tvnet 3',
       'execute if score $tvk mg.st matches 5 unless items entity @s container.* *[custom_data~{tv:6}] run give @s ' + TRAP,
       'execute if score $tvk mg.st matches 5 run scoreboard players add @s mg.tvtr 3',
       'execute if score $tvk mg.st matches 6 run give @s ' + MEDK + ' 2',
       f'execute if score $tvk mg.st matches 7 run item replace entity @s armor.head with {ARM["head"]}',
       f'execute if score $tvk mg.st matches 7 run item replace entity @s armor.chest with {ARM["chest"]}',
       f'execute if score $tvk mg.st matches 7 run item replace entity @s armor.legs with {ARM["legs"]}',
       'execute if score $tvk mg.st matches 7 run scoreboard players set @s mg.trar 1',
       f'execute if score $tvk mg.st matches 8 run give @s {SADDLE}',
       'scoreboard players set @s mg.tval 50',
       'title @s actionbar [{"text":"✔ Acheté ! ","color":"green","bold":true},{"text":"reste ","color":"gray"},{"score":{"name":"@s","objective":"mg.tvc"},"color":"yellow"},{"text":" ₵","color":"yellow"}]',
       'execute at @s run playsound minecraft:entity.villager.yes player @s ~ ~ ~ 0.8 1.1']
w('terra/buy', BUY)
w('terra/buy_int', ['# @s (présentoir) : le colon qui a cliqué achète', 'scoreboard players operation $tvk mg.st = @s mg.tvk',
                    'execute on target if entity @s[tag=mg.tvw] run function mg:terra/buy', 'data remove entity @s interaction'])
w('terra/buy_has', say('Tu l\'as déjà !', 'yellow'))
w('terra/buy_has_net', say('Tu as déjà un lance-filets : prends les filets ×3 à côté', 'yellow'))
w('terra/buy_need_net', say('Il te faut d\'abord un lance-filets', 'yellow'))
w('terra/buy_poor', say('Pas assez de crédits ₵ : fais des missions !', 'red') + ['execute at @s run playsound minecraft:entity.villager.no player @s ~ ~ ~ 0.8 1'])


def mbtn(label, col, tip, n):
    return {'label': [{'text': label, 'color': col, 'bold': True}], 'tooltip': [{'text': tip, 'color': 'gray'}],
            'action': {'type': 'minecraft:run_command', 'command': f'trigger mg.tvms set {n}'}}


BOARD = {'type': 'minecraft:multi_action', 'title': {'text': '📋 Missions de la colonie', 'color': 'gold', 'bold': True},
         'external_title': {'text': '📋 Missions', 'color': 'gold'}, 'pause': False, 'can_close_with_escape': True, 'columns': 1,
         'body': [{'type': 'minecraft:plain_message', 'contents': [{'text': 'Une mission à la fois. Le 📡 localisateur (case 9) indique l\'objectif.\n'
                                                                                'Les autres colons peuvent t\'aider.', 'color': 'gray'}]}],
         'actions': [mbtn('📦 Récupération de matériel — 150 ₵', 'yellow', 'Une caisse larguée dans la jungle : trouve-la, ramasse-la (accroupi 3 s) et rapporte-la à la colonie', 1),
                     mbtn('🛡 Défense d\'outpost — 250 ₵', 'aqua', 'Rejoins l\'outpost attaqué et protège son générateur pendant 90 s', 2),
                     mbtn('🦖 Chasse : 5 slashers — 200 ₵', 'green', 'Abats 5 slashers dans la jungle', 3),
                     mbtn('🦖 Chasse : le carnotaure — 400 ₵', 'red', 'Un carnotaure rôde : suis le localisateur et abats-le', 4),
                     mbtn('✖ Abandonner ma mission', 'gray', 'Annule la mission en cours', 9)]}
w('terra/board_int', ['# @s (tableau) : le colon qui a cliqué voit les missions',
                      'execute on target if entity @s[tag=mg.tvw] run function mg:terra/board', 'data remove entity @s interaction'])
MLINKS = [{'text': '📋 Missions : ', 'color': 'gold', 'bold': True}] + [
    {'text': f'[{a["label"][0]["text"]}] ', 'color': a['label'][0]['color'], 'bold': False,
     'click_event': {'action': 'run_command', 'command': a['action']['command'].replace('trigger', '/trigger')},
     'hover_event': {'action': 'show_text', 'value': a['tooltip'][0]['text']}} for a in BOARD['actions']]
w('terra/board', ['# @s : fenêtre des missions (sinon liens cliquables dans le chat)', 'scoreboard players enable @s mg.tvms',
                  'scoreboard players set $dlg mg.st 0', f'execute store success score $dlg mg.st run dialog show @s {js(BOARD)}',
                  'execute unless score $dlg mg.st matches 1 run tellraw @s ' + js(MLINKS),
                  'execute at @s run playsound minecraft:item.book.page_turn player @s ~ ~ ~ 0.8 1'])
w('terra/mission_cmd', ['# @s : choix au tableau (trigger mg.tvms)',
                        'execute if score @s mg.tvms matches 9 run function mg:terra/abandon',
                        'execute if score @s mg.tvms matches 1..4 unless score @s mg.tvm matches 1.. at @s run playsound minecraft:block.note_block.bell player @s ~ ~ ~ 0.8 1.2',
                        'execute if score @s mg.tvms matches 1..4 unless score @s mg.tvm matches 1.. run title @s title {"text":"📋 Mission acceptée","color":"gold","bold":true}',
                        'execute if score @s mg.tvms matches 1..4 if score @s mg.tvm matches 1.. run tellraw @s {"text":"Tu as déjà une mission : termine-la ou abandonne-la au tableau.","color":"yellow"}',
                        'execute if score @s mg.tvms matches 1 unless score @s mg.tvm matches 1.. run function mg:terra/m1',
                        'execute if score @s mg.tvms matches 2 unless score @s mg.tvm matches 1.. run function mg:terra/m2',
                        'execute if score @s mg.tvms matches 3 unless score @s mg.tvm matches 1.. run function mg:terra/m3',
                        'execute if score @s mg.tvms matches 4 unless score @s mg.tvm matches 1.. run function mg:terra/m4',
                        'scoreboard players reset @s mg.tvms', 'scoreboard players enable @s mg.tvms'])
w('terra/abandon', ['# @s abandonne sa mission', 'execute unless score @s mg.tvm matches 1.. run return run tellraw @s {"text":"Pas de mission en cours.","color":"gray"}',
                    'function mg:terra/mis_clear', 'tellraw @s {"text":"✖ Mission abandonnée.","color":"gray"}'])
w('terra/mis_clear', ['# @s : plus de mission (caisse posée ou portée retirée, localisateur vers la colonie)',
                      'scoreboard players operation $own mg.st = @s mg.tvpid',
                      'execute as @e[tag=mg.tvcrate] if score @s mg.tvo = $own mg.st run kill @s',
                      'execute as @e[tag=mg.tvcarry] if score @s mg.tvo = $own mg.st run kill @s',
                      'tag @s remove mg.tvcar', 'effect clear @s minecraft:slowness',
                      'scoreboard players set @s mg.tvm 0', 'scoreboard players set @s mg.tvmp 0', 'scoreboard players set @s mg.tvmo 0',
                      'execute if entity @s[tag=mg.tvw] run function mg:terra/rpg/qloc'])

# ---------------------------------------------------------------- mission 1 : récupération de matériel
M1 = ['# @s : mission « Récupération de matériel » : une caisse sur un point au hasard',
      f'execute store result score $tvr mg.st run random value 0..{len(CRATES) - 1}']
M1 += [f'execute if score $tvr mg.st matches {i} run return run function mg:terra/m1_at {{x:{x},y:{top(x, z)},z:{z}}}' for i, (x, z) in enumerate(CRATES)]
w('terra/m1', M1)
w('terra/m1_at', ['# @s : caisse larguée en $(x) $(y) $(z)', 'scoreboard players operation $own mg.st = @s mg.tvpid',
                  f'$execute in {DIM} positioned $(x) $(y) $(z) run function mg:terra/crate_new',
                  'scoreboard players set @s mg.tvm 1', 'scoreboard players set @s mg.tvmp 0',
                  '$function mg:terra/loc {x:$(x),y:$(y),z:$(z)}',
                  'tellraw @s ' + js([{'text': '📦 Mission : ', 'color': 'yellow', 'bold': True},
                                       {'text': 'une caisse de matériel a été larguée dans la jungle. Suis le 📡, ramasse-la (accroupi 3 s) et rapporte-la à la colonie. ', 'color': 'gray'},
                                       {'text': '+150 ₵', 'color': 'green'}]),
                  'playsound minecraft:block.note_block.bell player @s ~ ~ ~ 0.8 1.2'])
w('terra/crate_new', ['# Caisse de matériel ici (propriétaire $own) : tonneau lumineux, faisceau, étiquette, marqueur',
                      f'summon minecraft:block_display ~ ~ ~ {{Tags:["mg.tv","mg.tvcrate","mg.tvn"],block_state:{{Name:"minecraft:barrel",Properties:{{facing:"up"}}}},Glowing:1b,glow_color_override:16755200,{TR % (-0.45, 0, -0.45, 0.9, 0.9, 0.9)}}}',
                      f'summon minecraft:block_display ~ ~ ~ {{Tags:["mg.tv","mg.tvcrate","mg.tvn"],block_state:{{Name:"minecraft:yellow_stained_glass"}},brightness:{{sky:15,block:15}},view_range:4f,{TR % (-0.1, 0.9, -0.1, 0.2, 30, 0.2)}}}',
                      f'summon minecraft:text_display ~ ~1.6 ~ {{Tags:["mg.tv","mg.tvcrate","mg.tvn"],billboard:"center",text:{js({"text": "📦 Matériel", "color": "yellow", "bold": True})},background:1140850688}}',
                      'summon minecraft:marker ~ ~ ~ {Tags:["mg.tv","mg.tvcrate","mg.tvcrm","mg.tvn"]}',
                      'scoreboard players operation @e[tag=mg.tvn] mg.tvo = $own mg.st', 'tag @e[tag=mg.tvn] remove mg.tvn'])
PICK = ['# @s (accroupi, mission 1) : ramassage de sa caisse (3 s, 12 × 5 ticks)', 'scoreboard players operation $own mg.st = @s mg.tvpid',
        'scoreboard players set $tvf mg.st 0',
        'execute as @e[type=minecraft:marker,tag=mg.tvcrm,distance=..2.5] if score @s mg.tvo = $own mg.st run scoreboard players set $tvf mg.st 1',
        'execute if score $tvf mg.st matches 0 run return run scoreboard players set @s mg.tvmp 0',
        'scoreboard players add @s mg.tvmp 1', 'scoreboard players set @s mg.tval 10']
for i in range(1, 13):
    PICK.append(f'execute if score @s mg.tvmp matches {i} run title @s actionbar [{{"text":"📦 Ramassage ","color":"yellow"}},{{"text":"{"▮" * i}","color":"green"}},{{"text":"{"▮" * (12 - i)}","color":"dark_gray"}}]')
PICK.append('execute if score @s mg.tvmp matches 12.. run function mg:terra/crate_pick')
w('terra/crate_try', PICK)
w('terra/crate_pick', ['# @s ramasse sa caisse : il la porte (ralenti), une meute flaire l\'odeur',
                       'execute as @e[tag=mg.tvcrate] if score @s mg.tvo = $own mg.st run kill @s',
                       'tag @s add mg.tvcar', 'scoreboard players set @s mg.tvmp 0', 'effect give @s minecraft:slowness infinite 0 true',
                       f'summon minecraft:item_display ~ ~2.2 ~ {{Tags:["mg.tv","mg.tvcarry","mg.tvn"],teleport_duration:1,item:{{id:"minecraft:barrel",count:1}},{TR % (0, 0, 0, 0.7, 0.7, 0.7)}}}',
                       'scoreboard players operation @e[tag=mg.tvn] mg.tvo = $own mg.st',
                       'tag @e[tag=mg.tvn] remove mg.tvn', 'function mg:terra/save_pos', LOC_HOME,
                       'title @s title {"text":"📦 Caisse récupérée","color":"yellow","bold":true}',
                       'title @s subtitle {"text":"Rapporte-la à la colonie !","color":"gray"}',
                       'playsound minecraft:block.barrel.open player @s ~ ~ ~ 1 0.8',
                       'execute as @e[type=minecraft:marker,tag=mg.tvsp,distance=16..48,sort=nearest,limit=1] at @s run function mg:terra/pack',
                       'tellraw @s {"text":"⚠ Des slashers ont flairé la caisse !","color":"red"}'])
w('terra/carry_tick', ['# @s porte sa caisse : elle flotte au-dessus de sa tête', 'scoreboard players operation $own mg.st = @s mg.tvpid',
                         'execute as @e[type=minecraft:item_display,tag=mg.tvcarry] if score @s mg.tvo = $own mg.st run tp @s ~ ~2.2 ~ ~ 0'])
w('terra/m1_done', ['# @s rapporte la caisse à la colonie'] + gain(150, 'matériel livré à la colonie', 'gold') +
  ['function mg:terra/mis_clear', 'title @s title {"text":"✔ Mission accomplie","color":"green","bold":true}',
   'title @s subtitle {"text":"+150 ₵ : matériel livré","color":"gray"}', 'playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1'])
w('terra/save_pos', ['execute store result score @s mg.tvx run data get entity @s Pos[0]', 'execute store result score @s mg.tvy run data get entity @s Pos[1]',
                     'execute store result score @s mg.tvz run data get entity @s Pos[2]'])
w('terra/crate_drop', ['# @s est mort en portant la caisse : elle retombe là où il était (dernière position connue)',
                       'execute store result storage mg:terra d.x int 1 run scoreboard players get @s mg.tvx',
                       'execute store result storage mg:terra d.y int 1 run scoreboard players get @s mg.tvy',
                       'execute store result storage mg:terra d.z int 1 run scoreboard players get @s mg.tvz',
                       'scoreboard players operation $own mg.st = @s mg.tvpid',
                       'execute as @e[tag=mg.tvcarry] if score @s mg.tvo = $own mg.st run kill @s',
                       'function mg:terra/crate_drop_at with storage mg:terra d', 'tag @s remove mg.tvcar', 'effect clear @s minecraft:slowness',
                       'function mg:terra/loc with storage mg:terra d',
                       'tellraw @s {"text":"📦 Tu as lâché la caisse là où tu es tombé (📡).","color":"yellow"}'])
w('terra/crate_drop_at', [f'$execute in {DIM} positioned $(x) $(y) $(z) run function mg:terra/crate_new'])

# ---------------------------------------------------------------- mission 2 : défense d'outpost
GEN = {}
WAVE = {}
for k, (name, ox, oz) in enumerate(OUTPOSTS, 1):
    GEN[k] = (ox + 0.5, OUT_H[name] + 1, oz + 0.5)
    pts = []
    for dx, dz in [(0, -16), (16, 0), (0, 16), (-16, 0)]:
        x, z = max(-HX + 8, min(HX - 9, ox + dx)), max(-HX + 8, min(HX - 9, oz + dz))
        pts.append((x + 0.5, top(x, z), z + 0.5))
    WAVE[k] = pts
M2 = ['# @s : mission « Défense d\'outpost » : un outpost libre (tiré au sort)', 'execute store result score $tvr mg.st run random value 1..3']
for k in range(1, 4):
    gx, gy, gz = GEN[k]
    M2.append(f'execute if score $tvr mg.st matches {k} if score $tvo{k} mg.st matches 0 run return run function mg:terra/m2_set {{k:{k},x:{int(gx)},y:{gy},z:{int(gz)},n:"{OUTPOSTS[k - 1][0]}"}}')
for k in range(1, 4):
    gx, gy, gz = GEN[k]
    M2.append(f'execute if score $tvo{k} mg.st matches 0 run return run function mg:terra/m2_set {{k:{k},x:{int(gx)},y:{gy},z:{int(gz)},n:"{OUTPOSTS[k - 1][0]}"}}')
M2.append('tellraw @s {"text":"🛡 Tous les outposts sont déjà attaqués : rejoins une défense en cours (barre bleue) !","color":"aqua"}')
w('terra/m2', M2)
w('terra/m2_set', ['scoreboard players set @s mg.tvm 2', '$scoreboard players set @s mg.tvmo $(k)', 'scoreboard players set @s mg.tvmp 0',
                   '$function mg:terra/loc {x:$(x),y:$(y),z:$(z)}',
                   '$tellraw @s [{"text":"🛡 Mission : ","color":"aqua","bold":true},{"text":"l\'outpost $(n) va être attaqué. Rejoins-le (📡) : la défense commence à ton arrivée près du générateur. Tiens 90 s ! ","color":"gray"},{"text":"+250 ₵","color":"green"}]',
                   'playsound minecraft:block.note_block.bell player @s ~ ~ ~ 0.8 1.2'])
DEF_SECOND = []
for k, (name, ox, oz) in enumerate(OUTPOSTS, 1):
    gx, gy, gz = GEN[k]
    at = f'x={gx},y={gy},z={gz}'
    DEF_SECOND += [f'execute if score $tvo{k} mg.st matches 0 if entity @a[tag=mg.tvw,scores={{mg.tvm=2,mg.tvmo={k}}},{at},distance=..8] run function mg:terra/d_start_{k}',
                   f'execute if score $tvo{k} mg.st matches 1 run function mg:terra/d_tick_{k}']
    w(f'terra/d_start_{k}', [f'# Défense de l\'outpost {name} : 90 s, vagues toutes les 15 s, carnotaure à mi-parcours',
                             f'scoreboard players set $tvo{k} mg.st 1', f'scoreboard players set $tvot{k} mg.st 90', f'scoreboard players set $tvoi{k} mg.st 100',
                             f'scoreboard players set $tvow{k} mg.st 3', f'scoreboard players set $tvoa{k} mg.st 0',
                             f'tellraw @a[tag=mg.tvw,{at},distance=..64] ' + js([{'text': f'⚠ Les dinosaures attaquent l\'outpost {name} ! ', 'color': 'red', 'bold': True},
                                                                                  {'text': 'Protège le générateur pendant 90 s.', 'color': 'gray'}]),
                             f'execute positioned {gx} {gy} {gz} as @a[tag=mg.tvw,distance=..64] at @s run playsound minecraft:event.raid.horn hostile @s ~ ~ ~ 0.8 1.2'])
    TICK_D = [f'# Défense de l\'outpost {name} : chaque seconde', f'scoreboard players remove $tvot{k} mg.st 1', f'scoreboard players remove $tvow{k} mg.st 1',
              f'execute if score $tvow{k} mg.st matches ..0 run function mg:terra/d_wave_{k}',
              f'execute if score $tvot{k} mg.st matches 45 unless entity @e[tag=mg.tvcarno] positioned {WAVE[k][0][0]} {WAVE[k][0][1]} {WAVE[k][0][2]} run function mg:terra/d_boss',
              f'execute store result score $tvc2 mg.st if entity @e[tag=mg.tvhos,{at},distance=..3.5]',
              'scoreboard players operation $tvc2 mg.st *= #4 mg.st', f'scoreboard players operation $tvoi{k} mg.st -= $tvc2 mg.st',
              f'execute if score $tvc2 mg.st matches 1.. run particle minecraft:electric_spark {gx} {gy + 1.5} {gz} 0.3 0.6 0.3 0.4 25',
              f'execute if score $tvc2 mg.st matches 1.. run playsound minecraft:entity.iron_golem.damage hostile @a {gx} {gy} {gz} 0.8 1.4',
              f'execute store result bossbar mg:tvo{k} value run scoreboard players get $tvoi{k} mg.st',
              f'bossbar set mg:tvo{k} name [{{"text":"🛡 Outpost {name} : générateur ","color":"aqua"}},{{"score":{{"name":"$tvoi{k}","objective":"mg.st"}},"color":"white","bold":true}},{{"text":" %  ·  ","color":"gray"}},{{"score":{{"name":"$tvot{k}","objective":"mg.st"}},"color":"yellow","bold":true}},{{"text":" s","color":"yellow"}}]',
              f'bossbar set mg:tvo{k} players @a[tag=mg.tvw,{at},distance=..56]',
              f'execute unless entity @a[tag=mg.tvw,{at},distance=..56] run scoreboard players add $tvoa{k} mg.st 1',
              f'execute if entity @a[tag=mg.tvw,{at},distance=..56] run scoreboard players set $tvoa{k} mg.st 0',
              f'execute if score $tvoa{k} mg.st matches 15.. run return run function mg:terra/d_fail_{k}',
              f'execute if score $tvoi{k} mg.st matches ..0 run return run function mg:terra/d_fail_{k}',
              f'execute if score $tvot{k} mg.st matches ..0 run function mg:terra/d_win_{k}']
    w(f'terra/d_tick_{k}', TICK_D)
    WV = [f'# Vague sur l\'outpost {name} : 2 slashers + 1 par colon présent (5 au plus)', f'scoreboard players set $tvow{k} mg.st 15',
          f'execute store result score $tvn mg.st if entity @a[tag=mg.tvw,{at},distance=..40]', 'scoreboard players add $tvn mg.st 2',
          'execute if score $tvn mg.st matches 6.. run scoreboard players set $tvn mg.st 5', f'function mg:terra/d_wave_one_{k}']
    w(f'terra/d_wave_{k}', WV)
    W1 = ['execute store result score $tvr mg.st run random value 0..3']
    W1 += [f'execute if score $tvr mg.st matches {i} positioned {x} {y} {z} run function mg:terra/d_raptor' for i, (x, y, z) in enumerate(WAVE[k])]
    W1 += ['scoreboard players remove $tvn mg.st 1', f'execute if score $tvn mg.st matches 1.. run function mg:terra/d_wave_one_{k}']
    w(f'terra/d_wave_one_{k}', W1)
    win = [f'# Outpost {name} tenu : récompenses, outpost réparé', f'scoreboard players set $tvo{k} mg.st 0', f'bossbar set mg:tvo{k} players',
           f'execute as @a[tag=mg.tvw,{at},distance=..40] unless entity @s[scores={{mg.tvm=2,mg.tvmo={k}}}] run function mg:terra/m2_help',
           f'execute as @a[tag=mg.tvw,scores={{mg.tvm=2,mg.tvmo={k}}},{at},distance=..40] run function mg:terra/m2_done',
           f'execute as @a[tag=mg.tvw,scores={{mg.tvm=2,mg.tvmo={k}}}] run function mg:terra/m2_late',
           f'function mg:terra/out_build_{k}',
           f'execute positioned {gx} {gy} {gz} run playsound minecraft:ui.toast.challenge_complete player @a[tag=mg.tvw,distance=..48] ~ ~ ~ 0.6 1']
    w(f'terra/d_win_{k}', win)
    fail = [f'# Outpost {name} perdu', f'scoreboard players set $tvo{k} mg.st 0', f'bossbar set mg:tvo{k} players',
            f'particle minecraft:explosion_emitter {gx} {gy + 1} {gz} 0 0 0 0 1 force', f'playsound minecraft:entity.generic.explode hostile @a {gx} {gy} {gz} 2 0.8',
            f'tellraw @a[tag=mg.tvw,{at},distance=..64] {js({"text": f"💥 Le générateur de l’outpost {name} est détruit !", "color": "red", "bold": True})}',
            f'execute as @a[tag=mg.tvw,scores={{mg.tvm=2,mg.tvmo={k}}}] run function mg:terra/m2_fail',
            f'function mg:terra/out_build_{k}']
    w(f'terra/d_fail_{k}', fail)
w('terra/d_raptor', ['# Slasher de vague (ici) lancé sur le colon le plus proche', 'function mg:terra/dino/raptor', 'tag @e[tag=mg.tvlast] add mg.tvwave',
                     'execute as @e[tag=mg.tvlast] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.tvw,gamemode=adventure,distance=..60]'])
w('terra/d_boss', ['# Carnotaure de défense (ici)', 'function mg:terra/dino/carno', 'scoreboard players set $tvcc mg.st 240',
                   'execute as @e[tag=mg.tvlast] at @s run damage @s 0.01 minecraft:generic by @p[tag=mg.tvw,gamemode=adventure,distance=..60]',
                   'tellraw @a[tag=mg.tvw,distance=..80] {"text":"🦖 Un carnotaure fonce sur l\'outpost !","color":"red","bold":true}',
                   'execute as @a[tag=mg.tvw,distance=..80] at @s run playsound minecraft:entity.ravager.roar hostile @s ~ ~ ~ 1 0.55'])
w('terra/m2_done', ['# @s a tenu l\'outpost'] + gain(250, 'outpost défendu', 'aqua') +
  ['function mg:terra/mis_clear', 'title @s title {"text":"✔ Outpost défendu","color":"aqua","bold":true}', 'title @s subtitle {"text":"+250 ₵","color":"green"}'])
w('terra/m2_help', ['# @s a aidé à défendre un outpost'] + gain(60, 'renfort à l\'outpost', 'aqua'))
w('terra/m2_late', ['# @s avait la mission mais était trop loin à la fin', 'function mg:terra/mis_clear',
                    'tellraw @s {"text":"🛡 L\'outpost a tenu sans toi : mission terminée sans récompense.","color":"gray"}'])
w('terra/m2_fail', ['function mg:terra/mis_clear', 'title @s title {"text":"✖ Mission échouée","color":"red","bold":true}',
                    'title @s subtitle {"text":"Le générateur est détruit","color":"gray"}'])

# ---------------------------------------------------------------- missions 3 et 4 : chasse
w('terra/m3', ['# @s : mission « Chasse : 5 slashers »', 'scoreboard players set @s mg.tvm 3', 'scoreboard players set @s mg.tvmp 0',
               'execute as @e[type=minecraft:marker,tag=mg.tvfar,sort=random,limit=1] run function mg:terra/mark_loc',
               'function mg:terra/loc with storage mg:terra h',
               'tellraw @s ' + js([{'text': '🦖 Mission : ', 'color': 'green', 'bold': True}, {'text': 'abats 5 slashers dans la jungle (le 📡 indique une zone de chasse). ', 'color': 'gray'},
                                    {'text': '+200 ₵', 'color': 'green'}])])
w('terra/mark_loc', ['# @s (entité) : sa position dans storage mg:terra h', 'execute store result storage mg:terra h.x int 1 run data get entity @s Pos[0]',
                     'execute store result storage mg:terra h.y int 1 run data get entity @s Pos[1]', 'execute store result storage mg:terra h.z int 1 run data get entity @s Pos[2]'])
w('terra/m3_done', ['# @s a abattu ses 5 slashers'] + gain(200, 'chasse réussie', 'green') +
  ['function mg:terra/mis_clear', 'title @s title {"text":"✔ Chasse réussie","color":"green","bold":true}', 'title @s subtitle {"text":"+200 ₵","color":"green"}'])
w('terra/m4', ['# @s : mission « Chasse : le carnotaure » (un carnotaure traqué, apparu loin de la colonie si besoin)', 'scoreboard players set @s mg.tvm 4',
               'execute unless entity @e[tag=mg.tvhunt] as @e[type=minecraft:marker,tag=mg.tvfar,sort=random,limit=1] at @s run function mg:terra/hunt_spawn',
               'function mg:terra/hunt_loc',
               'tellraw @s ' + js([{'text': '🦖 Mission : ', 'color': 'red', 'bold': True}, {'text': 'un carnotaure rôde. Suis le 📡 et abats-le (prends du renfort !). ', 'color': 'gray'},
                                    {'text': '+400 ₵', 'color': 'green'}])])
w('terra/hunt_spawn', ['function mg:terra/dino/carno', 'tag @e[tag=mg.tvlast] add mg.tvhunt', 'scoreboard players set $tvcc mg.st 240'])
w('terra/hunt_loc', ['# Localisateurs des chasseurs de carnotaure : vers le carnotaure traqué',
                     'execute as @e[tag=mg.tvhunt,limit=1] run function mg:terra/mark_loc',
                     'execute if entity @e[tag=mg.tvhunt] as @a[tag=mg.tvw,scores={mg.tvm=4}] run function mg:terra/loc with storage mg:terra h'])
w('terra/k_raptor', ['# @s a abattu mg.tvkr slasher(s) : 12 ₵ chacun, progression de la chasse', 'function mg:terra/rpg/k_raptor',
                     'scoreboard players operation $tvk2 mg.st = @s mg.tvkr', 'scoreboard players operation $tvk2 mg.st *= #12 mg.st',
                     'scoreboard players operation @s mg.tvc += $tvk2 mg.st', 'scoreboard players set @s mg.tval 30',
                     'title @s actionbar [{"text":"+","color":"green","bold":true},{"score":{"name":"$tvk2","objective":"mg.st"},"color":"green","bold":true},{"text":" ₵ ","color":"green","bold":true},{"text":"slasher abattu","color":"gray"}]',
                     'execute if score @s mg.tvm matches 3 run scoreboard players operation @s mg.tvmp += @s mg.tvkr',
                     'execute if score @s mg.tvm matches 3 if score @s mg.tvmp matches ..4 run tellraw @s [{"text":"🦖 Chasse : ","color":"green"},{"score":{"name":"@s","objective":"mg.tvmp"},"color":"yellow","bold":true},{"text":" / 5","color":"yellow"}]',
                     'scoreboard players set @s mg.tvkr 0',
                     'execute if score @s mg.tvm matches 3 if score @s mg.tvmp matches 5.. run function mg:terra/m3_done'])
w('terra/k_carno', ['# @s a abattu un carnotaure : 120 ₵ (+ mission de chasse), les autres chasseurs ont une part',
                    'scoreboard players set @s mg.tvkc 0', 'function mg:terra/rpg/k_carno'] + gain(120, 'carnotaure abattu !', 'gold') +
  ['tellraw @a[tag=mg.tvw] [{"text":"🦖 ","color":"red"},{"selector":"@s","color":"yellow"},{"text":" a abattu le carnotaure !","color":"red","bold":true}]',
   'execute if entity @e[tag=mg.tvhunt] run return 0',
   'tag @s add mg.tvkill',
   'execute if score @s mg.tvm matches 4 run function mg:terra/m4_done',
   'execute as @a[tag=mg.tvw,tag=!mg.tvkill,scores={mg.tvm=4}] run function mg:terra/m4_share', 'tag @s remove mg.tvkill'])
w('terra/m4_done', ['# @s a abattu le carnotaure traqué'] + gain(400, 'chasse au carnotaure réussie', 'gold') +
  ['function mg:terra/mis_clear', 'title @s title {"text":"✔ Carnotaure abattu","color":"gold","bold":true}', 'title @s subtitle {"text":"+400 ₵","color":"green"}',
   'execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.7 1'])
w('terra/m4_share', ['# @s chassait aussi le carnotaure : une part de la prime'] + gain(150, 'part de la chasse au carnotaure', 'gold') + ['function mg:terra/mis_clear'])
w('terra/k_herb', ['# @s a tué un herbivore : braconnage, -25 ₵', 'scoreboard players set @s mg.tvkb 0', 'scoreboard players set @s mg.tvkg 0',
                   'scoreboard players remove @s mg.tvc 25', 'execute if score @s mg.tvc matches ..-1 run scoreboard players set @s mg.tvc 0',
                   'scoreboard players set @s mg.tval 50',
                   'title @s actionbar [{"text":"-25 ₵ ","color":"red","bold":true},{"text":"braconnage : les herbivores sont protégés","color":"gray"}]'])
