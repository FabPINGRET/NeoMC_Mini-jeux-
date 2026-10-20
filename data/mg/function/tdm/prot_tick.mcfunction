# Réapparition protégée (@s = joueur mg.tmp ; mg.tmx = décompte en ticks)
scoreboard players remove @s mg.tmx 1
execute if score @s mg.tmx matches 40 run title @s actionbar [{"text":"2","color":"yellow","bold":true}]
execute if score @s mg.tmx matches 20 run title @s actionbar [{"text":"1","color":"yellow","bold":true}]
execute if score @s mg.tmx matches ..0 run title @s actionbar [{"text":"🎯 FEU !","color":"red","bold":true}]
execute if score @s mg.tmx matches ..0 at @s run playsound minecraft:entity.firework_rocket.blast master @s ~ ~ ~ 0.6 1.4
# l'overlay de recharge du sniper (use_cooldown) n'est posé qu'ici : sinon un clic protégé verrouillerait le tir
execute if score @s mg.tmx matches ..0 if items entity @s hotbar.0 minecraft:warped_fungus_on_a_stick[custom_data~{mg_tm:1b}] run item modify entity @s hotbar.0 {function:"minecraft:set_components",components:{"minecraft:use_cooldown":{seconds:2f,cooldown_group:"mg:tmsn"}}}
execute if score @s mg.tmx matches ..0 if items entity @s hotbar.1 minecraft:warped_fungus_on_a_stick[custom_data~{mg_tm:1b}] run item modify entity @s hotbar.1 {function:"minecraft:set_components",components:{"minecraft:use_cooldown":{seconds:2f,cooldown_group:"mg:tmsn"}}}
execute if score @s mg.tmx matches ..0 if items entity @s hotbar.2 minecraft:warped_fungus_on_a_stick[custom_data~{mg_tm:1b}] run item modify entity @s hotbar.2 {function:"minecraft:set_components",components:{"minecraft:use_cooldown":{seconds:2f,cooldown_group:"mg:tmsn"}}}
execute if score @s mg.tmx matches ..0 if items entity @s hotbar.3 minecraft:warped_fungus_on_a_stick[custom_data~{mg_tm:1b}] run item modify entity @s hotbar.3 {function:"minecraft:set_components",components:{"minecraft:use_cooldown":{seconds:2f,cooldown_group:"mg:tmsn"}}}
execute if score @s mg.tmx matches ..0 if items entity @s hotbar.4 minecraft:warped_fungus_on_a_stick[custom_data~{mg_tm:1b}] run item modify entity @s hotbar.4 {function:"minecraft:set_components",components:{"minecraft:use_cooldown":{seconds:2f,cooldown_group:"mg:tmsn"}}}
execute if score @s mg.tmx matches ..0 if items entity @s hotbar.5 minecraft:warped_fungus_on_a_stick[custom_data~{mg_tm:1b}] run item modify entity @s hotbar.5 {function:"minecraft:set_components",components:{"minecraft:use_cooldown":{seconds:2f,cooldown_group:"mg:tmsn"}}}
execute if score @s mg.tmx matches ..0 if items entity @s hotbar.6 minecraft:warped_fungus_on_a_stick[custom_data~{mg_tm:1b}] run item modify entity @s hotbar.6 {function:"minecraft:set_components",components:{"minecraft:use_cooldown":{seconds:2f,cooldown_group:"mg:tmsn"}}}
execute if score @s mg.tmx matches ..0 if items entity @s hotbar.7 minecraft:warped_fungus_on_a_stick[custom_data~{mg_tm:1b}] run item modify entity @s hotbar.7 {function:"minecraft:set_components",components:{"minecraft:use_cooldown":{seconds:2f,cooldown_group:"mg:tmsn"}}}
execute if score @s mg.tmx matches ..0 if items entity @s hotbar.8 minecraft:warped_fungus_on_a_stick[custom_data~{mg_tm:1b}] run item modify entity @s hotbar.8 {function:"minecraft:set_components",components:{"minecraft:use_cooldown":{seconds:2f,cooldown_group:"mg:tmsn"}}}
execute if score @s mg.tmx matches ..0 run tag @s remove mg.tmp
execute if score @s mg.tmx matches ..0 run scoreboard players reset @s mg.tmx
