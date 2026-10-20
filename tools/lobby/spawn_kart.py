# Spawn : circuit du spawn : tables du moteur kart (t4) et mode kart libre (lobkart) ; exécuté par gen_lobby.py (exec) après les entités de décor et le parkour.
# Utilise : F, G, KCPS, KK, KN, KP, KPAD, ktan, kyaw, os, sx_, sz_, tdisp, wr

# ------------------------------------------------------------------ CIRCUIT DU SPAWN : tables du moteur (kart/t4) et mode kart libre (lobkart/)
KY = G + 1
wr('kart/t4/cp_check', [f'# Circuit du spawn : point de passage attendu (mg.kcp) atteint ? ({KK} points par tour) (généré par tools/lobby/gen_lobby.py)'] +
   [f'execute if score @s mg.kcp matches {k} positioned {x} {KY} {z} if entity @e[type=minecraft:block_display,tag=mg.kk,distance=..9] run return run function mg:kart/cp_pass'
    for k, (x, z, yw) in enumerate(KCPS)])
wr('kart/t4/cp_tp', ['# Circuit du spawn : remise en piste (@s = kart) au point de passage $ki'] +
   [f'execute if score $ki mg.st matches {k} run return run tp @s {x} {KY} {z} {yw} 0' for k, (x, z, yw) in enumerate(KCPS)])
wr('kart/t4/bill_step', ['# Circuit du spawn : Bill Balle (@s = kart) vers le point de passage $ki'] +
   [f'execute if score $ki mg.st matches {k} facing {x} {KY} {z} rotated ~ 0 run return run tp @s ^ ^ ^1.6 ~ ~' for k, (x, z, yw) in enumerate(KCPS)])
wr('kart/t4/const', ['# Circuit du spawn : constantes', f'scoreboard players set $kK mg.st {KK}', 'scoreboard players set $kLaps mg.st 999'])
grid = ['# Place @s (le pilote) sur une des 6 places de départ ($lgi 0..5), tourné vers la piste']
for g in range(6):
    back, side = 3 + (g // 2) * 4, (-2 if g % 2 == 0 else 2)
    i = (-back * 2) % KN; tx, tz = ktan(i)
    x, z = KP[i][0] + -tz * side, KP[i][1] + tx * side
    grid.append(f'execute if score $lgi mg.st matches {g} run return run tp @s {round(x, 1)} {KY} {round(z, 1)} {kyaw(tx, tz)} 0')
wr('lobkart/grid_tp', grid)
LKC = ['scoreboard players set #km1 mg.st -1'] + [f'scoreboard players set #k{v} mg.st {v}' for v in (2, 3, 4, 5, 8, 10, 12, 20, 60, 65, 100, 120, 1000)] + \
      ['scoreboard players set #kt85 mg.st 85', 'scoreboard players set #kt120 mg.st 120', 'scoreboard players set #kt90 mg.st 90', 'scoreboard players set #kkmh mg.st 108']
wr('lobkart/consts', ['# Constantes du moteur du kart (les mêmes qu\'en course)'] + LKC)
RESET = ['ksp', 'kdr', 'krc', 'kbo', 'khi', 'kst', 'kit', 'kic', 'kgd', 'kbill', 'kboo', 'kmg', 'kcp', 'klp', 'kvy', 'kfp', 'kps', 'kbl', 'krl', 'klt']
BTN = ('tellraw @s [{"text":"🏎 ","color":"gold"},{"text":"Circuit du spawn : ","color":"gray"},'
       '{"text":"[Descendre]","color":"red","bold":true,"click_event":{"action":"run_command","command":"trigger mg.opt set 27"},"hover_event":{"action":"show_text","value":"Ranger le kart et revenir au garage (/trigger mg.opt set 27)"}},'
       '{"text":" ","color":"gray"},{"text":"[Vue assise]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.kv set 2"}},'
       '{"text":" ","color":"gray"},{"text":"[Caméra de poursuite]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.kv set 1"}},'
       '{"text":" ","color":"gray"},{"text":"[⛑ Je suis coincé]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.opt set 26"},"hover_event":{"action":"show_text","value":"Te remet sur la piste au dernier point de passage (ou /trigger mg.opt set 26)"}},'
       '{"text":"  (Shift = descendre ; on peut rouler sur tout le spawn)","color":"dark_gray"}]')
wr('lobkart/enter', ['# @s marche sur le tapis du garage : il monte dans un kart sur la ligne de départ du circuit du spawn',
                     'tag @s add mg.lkz',
                     'execute unless score $state mg.st matches 0 run return run tellraw @s [{"text":"⚠ Le kart libre n\'est pas disponible pendant une partie.","color":"red"}]',
                     'execute store result score $lkn mg.st if entity @a[tag=mg.lk]',
                     'execute if score $lkn mg.st matches 12.. run return run tellraw @s [{"text":"⚠ Trop de karts sur le circuit, réessaie dans un instant.","color":"red"}]',
                     'function mg:parkour/quit', 'clear @s', 'effect clear @s', 'function mg:core/heal', 'function mg:lobkart/consts',
                     'tag @s remove mg.kfin', 'tag @s remove mg.kout', 'tag @s remove mg.kok',
                     'scoreboard players add $lri mg.st 1', 'execute unless score $lri mg.st matches 100..999 run scoreboard players set $lri mg.st 100',
                     'scoreboard players operation @s mg.ri = $lri mg.st'] +
   [f'scoreboard players set @s mg.{k} 0' for k in RESET] +
   ['execute unless score @s mg.kvm matches 0..1 run scoreboard players set @s mg.kvm 1', 'scoreboard players reset @s mg.qs', 'scoreboard players enable @s mg.kv',
    'scoreboard players add $lgi mg.st 1', 'execute unless score $lgi mg.st matches 0..5 run scoreboard players set $lgi mg.st 0',
    'function mg:lobkart/grid_tp', 'tag @s add mg.lk',
    'execute at @s run function mg:kart/kart_new', 'function mg:kart/kk', 'tag @e[tag=mg.kk] add mg.lkart', 'function mg:kart/seat',
    'tag @e[tag=mg.kk] remove mg.kk', 'tag @e[tag=mg.kcamc] remove mg.kcamc',
    'title @s title [{"text":"🏁 CIRCUIT DU SPAWN","color":"gold","bold":true}]',
    'title @s subtitle [{"text":"Z avancer, Q / D tourner, Espace = dérapage, Shift = descendre","color":"yellow"}]',
    'execute at @s run playsound minecraft:block.note_block.bell master @s ~ ~ ~ 1 1.4', BTN])
wr('lobkart/remove', ['# Range le kart de @s (et sa caméra, sa tête) sans le déplacer',
                      'function mg:kart/kk', 'ride @s dismount',
                      'execute as @e[type=minecraft:block_display,tag=mg.kk] on passengers unless entity @s[type=minecraft:player] run kill @s',
                      'kill @e[tag=mg.kk]', 'kill @e[tag=mg.kcamc]',
                      'execute as @e[type=minecraft:item_display,tag=mg.khead] if score @s mg.ri = $me mg.st run kill @s',
                      'tag @s remove mg.lk', 'tag @s remove mg.kfin', 'tag @s remove mg.kout', 'scoreboard players set @s mg.ri 0',
                      'execute if entity @s[gamemode=spectator] run gamemode adventure @s'])
wr('lobkart/leave', ['# @s quitte le circuit du spawn sans être ramené au garage (plot, survie, reconnexion)', 'execute if entity @s[tag=mg.lk] run function mg:lobkart/remove'])
wr('lobkart/exit', ['# @s descend du kart : retour au garage',
                    'execute unless entity @s[tag=mg.lk] run return 0',
                    'function mg:lobkart/remove', 'tag @s add mg.lkz',
                    f'tp @s 0.5 64 {KPAD[1] - 2.5} 180 0', 'function mg:core/give_menu', 'function mg:core/heal',
                    'title @s actionbar [{"text":"🏎 Kart rangé. À bientôt sur le circuit !","color":"gold"}]'])
wr('lobkart/stop_all', ['# Une partie commence : karts du spawn rangés (participant déjà sorti par core/request, filet de sécurité : sur place ; les autres : au garage)',
                        'execute as @a[tag=mg.lk,tag=mg.play] run function mg:lobkart/leave', 'execute as @a[tag=mg.lk] run function mg:lobkart/exit'])
wr('lobkart/claim', ['# @s (pilote du spawn) garde son kart et sa caméra (pas orphelins)', 'function mg:kart/kk', 'tag @e[tag=mg.kk] remove mg.lko', 'tag @e[tag=mg.kcamc] remove mg.lko',
                     'tag @e[tag=mg.kk] remove mg.kk', 'tag @e[tag=mg.kcamc] remove mg.kcamc'])
wr('lobkart/orphans', ['# Karts du spawn dont le pilote est parti (déconnexion) : rangés',
                       'tag @e[type=minecraft:block_display,tag=mg.lkart] add mg.lko',
                       'execute as @e[type=minecraft:item_display,tag=mg.kcam] if score @s mg.ri matches 100.. run tag @s add mg.lko',
                       'execute as @a[tag=mg.lk] run function mg:lobkart/claim',
                       'execute as @e[type=minecraft:block_display,tag=mg.lko] on passengers run kill @s',
                       'kill @e[tag=mg.lko]'])
wr('lobkart/tick', ['# Kart libre au spawn (chaque tick) : moteur du kart pour les pilotes mg.lk, sur le circuit du spawn',
                    f'execute as @a[tag=mg.lkz] unless entity @s[x={KPAD[0]},y=63,z={KPAD[1]},dx=2.99,dy=2.5,dz=2.99] run tag @s remove mg.lkz',
                    f'execute if score $state mg.st matches 0 as @a[tag=!mg.lk,tag=!mg.lkz,tag=!mg.play,tag=!mg.surv,tag=!mg.inplot,gamemode=adventure,x={KPAD[0]},y=63,z={KPAD[1]},dx=2.99,dy=2.5,dz=2.99] run function mg:lobkart/enter',
                    'scoreboard players add $lko mg.st 1',
                    'execute if score $lko mg.st matches 100.. run function mg:lobkart/orphans',
                    'execute if score $lko mg.st matches 100.. run scoreboard players set $lko mg.st 0',
                    'execute unless entity @a[tag=mg.lk] run return 0',
                    'execute unless score $state mg.st matches 0 run return run function mg:lobkart/stop_all',
                    'execute as @a[tag=mg.lk,gamemode=creative] run function mg:lobkart/leave',
                    'execute as @a[tag=mg.lk] if predicate mg:sneak run function mg:lobkart/exit',
                    'execute as @a[tag=mg.lk,tag=mg.surv] run function mg:lobkart/leave',
                    'scoreboard players operation $lkb mg.st = $kbat mg.st', 'scoreboard players set $kbat mg.st 0',
                    'scoreboard players set $klob mg.st 1', 'function mg:kart/t4/const',
                    'execute if score $rp mg.st matches 1 as @e[type=minecraft:block_display,tag=mg.lkart,tag=!mg.rps] at @s run function mg:kart/rp_skin',
                    'execute if score $rp mg.st matches 1 as @e[tag=mg.fx,tag=!mg.rps] at @s run function mg:kart/rp_skin',
                    'scoreboard players add @a[tag=mg.lk,scores={mg.klp=1..}] mg.klt 1',
                    'execute as @a[tag=mg.lk] run function mg:kart/drive',
                    'tag @e[tag=mg.kk] remove mg.kk', 'tag @e[tag=mg.kcamc] remove mg.kcamc',
                    'execute as @e[type=minecraft:block_display,tag=mg.kart,tag=!mg.lkart] if score @s mg.ri matches 100.. run tag @s add mg.lkart',
                    'scoreboard players add $kph mg.st 1', 'execute if score $kph mg.st matches 4.. run scoreboard players set $kph mg.st 0',
                    'execute if score $kph mg.st matches 0 as @a[tag=mg.lk] run function mg:lobkart/hud',
                    'scoreboard players set $klob mg.st 0', 'scoreboard players operation $kbat mg.st = $lkb mg.st', 'function mg:kart/const'])
def tsd(score):   # secondes.dixièmes d'un score en ticks → $s, $d
    return [f'scoreboard players operation $s mg.st = {score}', 'scoreboard players operation $s mg.st /= #k20 mg.st',
            f'scoreboard players operation $d mg.st = {score}', 'scoreboard players operation $d mg.st %= #k20 mg.st', 'scoreboard players operation $d mg.st /= #k2 mg.st']
wr('lobkart/hud', ['# Barre du bas du pilote du spawn (@s) : tour, chrono, meilleur tour, vitesse',
                   'scoreboard players operation $kmh mg.st = @s mg.ksp', 'scoreboard players operation $kmh mg.st *= #kkmh mg.st', 'scoreboard players operation $kmh mg.st /= #k100 mg.st',
                   'execute if score $kmh mg.st matches ..-1 run scoreboard players operation $kmh mg.st *= #km1 mg.st',
                   'execute if score @s mg.klp matches 0 run return run title @s actionbar [{"text":"🏁 Passe la ligne de départ pour lancer le chrono  ","color":"gold"},{"score":{"name":"$kmh","objective":"mg.st"},"color":"aqua"},{"text":" km/h","color":"dark_aqua"}]']
   + tsd('@s mg.klt') + ['scoreboard players operation $bs mg.st = @s mg.klb', 'scoreboard players operation $bs mg.st /= #k20 mg.st',
                         'scoreboard players operation $bd mg.st = @s mg.klb', 'scoreboard players operation $bd mg.st %= #k20 mg.st', 'scoreboard players operation $bd mg.st /= #k2 mg.st',
                         'execute unless score @s mg.klb matches 1.. run title @s actionbar [{"text":"🏁 Tour ","color":"gold"},{"score":{"name":"@s","objective":"mg.klp"},"color":"yellow","bold":true},{"text":"   ⏱ ","color":"gold"},{"score":{"name":"$s","objective":"mg.st"},"color":"white","bold":true},{"text":".","color":"white"},{"score":{"name":"$d","objective":"mg.st"},"color":"white"},{"text":" s   ","color":"gray"},{"score":{"name":"$kmh","objective":"mg.st"},"color":"aqua"},{"text":" km/h","color":"dark_aqua"}]',
                         'execute if score @s mg.klb matches 1.. run title @s actionbar [{"text":"🏁 Tour ","color":"gold"},{"score":{"name":"@s","objective":"mg.klp"},"color":"yellow","bold":true},{"text":"   ⏱ ","color":"gold"},{"score":{"name":"$s","objective":"mg.st"},"color":"white","bold":true},{"text":".","color":"white"},{"score":{"name":"$d","objective":"mg.st"},"color":"white"},{"text":" s   ★ ","color":"gold"},{"score":{"name":"$bs","objective":"mg.st"},"color":"yellow"},{"text":".","color":"yellow"},{"score":{"name":"$bd","objective":"mg.st"},"color":"yellow"},{"text":" s   ","color":"gray"},{"score":{"name":"$kmh","objective":"mg.st"},"color":"aqua"},{"text":" km/h","color":"dark_aqua"}]'])
wr('lobkart/lap', ['# Ligne d\'arrivée franchie par un pilote du spawn (@s) : tour chronométré, record perso et record du circuit',
                   'scoreboard players add @s mg.klp 1',
                   'execute if score @s mg.klp matches 1 run scoreboard players set @s mg.klt 0',
                   'execute if score @s mg.klp matches 1 run return run title @s actionbar [{"text":"🏁 C\'est parti, le chrono tourne !","color":"green","bold":true}]']
   + tsd('@s mg.klt') +
   ['tellraw @s [{"text":"🏁 Tour en ","color":"gold"},{"score":{"name":"$s","objective":"mg.st"},"color":"white","bold":true},{"text":".","color":"white"},{"score":{"name":"$d","objective":"mg.st"},"color":"white"},{"text":" s","color":"gold"}]',
    'execute at @s run playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1.2',
    'execute if score @s mg.klb matches 1.. if score @s mg.klt < @s mg.klb run tellraw @s [{"text":"★ Nouveau record perso !","color":"aqua","bold":true}]',
    'execute unless score @s mg.klb matches 1.. run scoreboard players operation @s mg.klb = @s mg.klt',
    'execute if score @s mg.klt < @s mg.klb run scoreboard players operation @s mg.klb = @s mg.klt',
    'execute unless score $klrec mg.st matches 1.. run function mg:lobkart/record',
    'execute if score $klrec mg.st matches 1.. if score @s mg.klt < $klrec mg.st run function mg:lobkart/record',
    'scoreboard players set @s mg.klt 0'])
wr('lobkart/record', ['# Nouveau record du circuit du spawn (@s ; $s / $d déjà calculés)',
                      'scoreboard players operation $klrec mg.st = @s mg.klt',
                      'tellraw @a[tag=!mg.surv] [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow","bold":true},{"text":" bat le record du circuit du spawn : ","color":"gray"},{"score":{"name":"$s","objective":"mg.st"},"color":"gold","bold":true},{"text":".","color":"gold"},{"score":{"name":"$d","objective":"mg.st"},"color":"gold"},{"text":" s !","color":"gold"}]',
                      'execute store result storage mg:lk s int 1 run scoreboard players get $s mg.st', 'execute store result storage mg:lk d int 1 run scoreboard players get $d mg.st',
                      'function mg:lobkart/board with storage mg:lk'])
wr('lobkart/board', ['# Panneau du record (macro $(s), $(d))', '$data modify entity @e[type=minecraft:text_display,tag=mg.lkboard,limit=1] text set value {text:"🏆 Record du tour : $(s).$(d) s",color:"gold"}'])
wr('lobkart/board_refresh', ['# Réaffiche le record sur le panneau (après reconstruction du décor)', 'function mg:lobkart/consts'] + tsd('$klrec mg.st') +
   ['execute store result storage mg:lk s int 1 run scoreboard players get $s mg.st', 'execute store result storage mg:lk d int 1 run scoreboard players get $d mg.st',
    'function mg:lobkart/board with storage mg:lk'])
KDECO = [tdisp(KPAD[0] + 1.5, 66.6, KPAD[1] + 1.5, '[{"text":"🏎 KART LIBRE","color":"gold","bold":true}]', 1.6),
         tdisp(KPAD[0] + 1.5, 66.1, KPAD[1] + 1.5, '[{"text":"Marche sur le tapis pour monter dans un kart","color":"gray"}]', 0.9),
         tdisp(round(sx_, 1) + 0.5, 74.5, round(sz_, 1) + 0.5, '[{"text":"🏁 CIRCUIT DU SPAWN","color":"gold","bold":true}]', 2.4),
         tdisp(round(sx_, 1) + 0.5, 73.8, round(sz_, 1) + 0.5, '[{"text":"🏆 Record du tour : aucun","color":"gold"}]', 1.4).replace('Tags:["mg.lby"', 'Tags:["mg.lby","mg.lkboard"')]
with open(os.path.join(F, 'lobby', 'deco_common.mcfunction'), 'a', encoding='utf-8', newline='\n') as f:
    f.write('\n'.join(['# Circuit du spawn : panneaux'] + KDECO + ['execute if score $klrec mg.st matches 1.. run function mg:lobkart/board_refresh']) + '\n')

