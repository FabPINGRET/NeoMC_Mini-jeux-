# @s marche sur le tapis du garage : il monte dans un kart sur la ligne de départ du circuit du spawn
tag @s add mg.lkz
execute unless score $state mg.st matches 0 run return run tellraw @s [{"text":"⚠ Le kart libre n'est pas disponible pendant une partie.","color":"red"}]
execute store result score $lkn mg.st if entity @a[tag=mg.lk]
execute if score $lkn mg.st matches 12.. run return run tellraw @s [{"text":"⚠ Trop de karts sur le circuit, réessaie dans un instant.","color":"red"}]
function mg:parkour/quit
clear @s
effect clear @s
function mg:lobkart/consts
scoreboard players add $lri mg.st 1
execute unless score $lri mg.st matches 100..999 run scoreboard players set $lri mg.st 100
scoreboard players operation @s mg.ri = $lri mg.st
scoreboard players set @s mg.ksp 0
scoreboard players set @s mg.kdr 0
scoreboard players set @s mg.krc 0
scoreboard players set @s mg.kbo 0
scoreboard players set @s mg.khi 0
scoreboard players set @s mg.kst 0
scoreboard players set @s mg.kit 0
scoreboard players set @s mg.kic 0
scoreboard players set @s mg.kgd 0
scoreboard players set @s mg.kbill 0
scoreboard players set @s mg.kboo 0
scoreboard players set @s mg.kmg 0
scoreboard players set @s mg.kcp 0
scoreboard players set @s mg.klp 0
scoreboard players set @s mg.kvy 0
scoreboard players set @s mg.kfp 0
scoreboard players set @s mg.kps 0
scoreboard players set @s mg.kbl 0
scoreboard players set @s mg.krl 0
scoreboard players set @s mg.klt 0
execute unless score @s mg.kvm matches 0..1 run scoreboard players set @s mg.kvm 1
scoreboard players reset @s mg.qs
scoreboard players enable @s mg.kv
scoreboard players add $lgi mg.st 1
execute unless score $lgi mg.st matches 0..5 run scoreboard players set $lgi mg.st 0
function mg:lobkart/grid_tp
tag @s add mg.lk
execute at @s run function mg:kart/kart_new
function mg:kart/kk
tag @e[tag=mg.kk] add mg.lkart
function mg:kart/seat
tag @e[tag=mg.kk] remove mg.kk
tag @e[tag=mg.kcamc] remove mg.kcamc
title @s title [{"text":"🏁 CIRCUIT DU SPAWN","color":"gold","bold":true}]
title @s subtitle [{"text":"Z avancer, Q / D tourner, Espace en tournant = dérapage","color":"yellow"}]
execute at @s run playsound minecraft:block.note_block.bell master @s ~ ~ ~ 1 1.4
tellraw @s [{"text":"🏎 ","color":"gold"},{"text":"Circuit du spawn : ","color":"gray"},{"text":"[Descendre]","color":"red","bold":true,"click_event":{"action":"run_command","command":"trigger mg.opt set 27"},"hover_event":{"action":"show_text","value":"Ranger le kart et revenir au garage (/trigger mg.opt set 27)"}},{"text":" ","color":"gray"},{"text":"[Vue assise]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.kv set 2"}},{"text":" ","color":"gray"},{"text":"[Caméra de poursuite]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.kv set 1"}},{"text":"  (T pour ouvrir le chat)","color":"dark_gray"}]
