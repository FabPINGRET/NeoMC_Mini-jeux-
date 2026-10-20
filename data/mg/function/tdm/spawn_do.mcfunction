# Apparition de @s (participant, $tma = arène, #tms = départ) : PV neufs, 3 s de protection (mg.tmp), tir impossible
scoreboard players set @s mg.tmhp 2
function mg:tdm/unscope
tag @s add mg.tmp
execute if items entity @s hotbar.0 minecraft:warped_fungus_on_a_stick[custom_data~{mg_tm:1b}] run item modify entity @s hotbar.0 {function:"minecraft:set_components",components:{"!minecraft:use_cooldown":{}}}
execute if items entity @s hotbar.1 minecraft:warped_fungus_on_a_stick[custom_data~{mg_tm:1b}] run item modify entity @s hotbar.1 {function:"minecraft:set_components",components:{"!minecraft:use_cooldown":{}}}
execute if items entity @s hotbar.2 minecraft:warped_fungus_on_a_stick[custom_data~{mg_tm:1b}] run item modify entity @s hotbar.2 {function:"minecraft:set_components",components:{"!minecraft:use_cooldown":{}}}
execute if items entity @s hotbar.3 minecraft:warped_fungus_on_a_stick[custom_data~{mg_tm:1b}] run item modify entity @s hotbar.3 {function:"minecraft:set_components",components:{"!minecraft:use_cooldown":{}}}
execute if items entity @s hotbar.4 minecraft:warped_fungus_on_a_stick[custom_data~{mg_tm:1b}] run item modify entity @s hotbar.4 {function:"minecraft:set_components",components:{"!minecraft:use_cooldown":{}}}
execute if items entity @s hotbar.5 minecraft:warped_fungus_on_a_stick[custom_data~{mg_tm:1b}] run item modify entity @s hotbar.5 {function:"minecraft:set_components",components:{"!minecraft:use_cooldown":{}}}
execute if items entity @s hotbar.6 minecraft:warped_fungus_on_a_stick[custom_data~{mg_tm:1b}] run item modify entity @s hotbar.6 {function:"minecraft:set_components",components:{"!minecraft:use_cooldown":{}}}
execute if items entity @s hotbar.7 minecraft:warped_fungus_on_a_stick[custom_data~{mg_tm:1b}] run item modify entity @s hotbar.7 {function:"minecraft:set_components",components:{"!minecraft:use_cooldown":{}}}
execute if items entity @s hotbar.8 minecraft:warped_fungus_on_a_stick[custom_data~{mg_tm:1b}] run item modify entity @s hotbar.8 {function:"minecraft:set_components",components:{"!minecraft:use_cooldown":{}}}
scoreboard players set @s mg.tmx 60
scoreboard players set @s mg.tmcd 0
scoreboard players set @s mg.tmkc 0
title @s actionbar {"text":"3","color":"yellow","bold":true}
execute if score $tma mg.st matches 1 positioned 0.5 89 40000.5 run function mg:tdm/spawn_slot
execute if score $tma mg.st matches 2 positioned 0.5 81 40400.5 run function mg:tdm/spawn_slot
execute if score $tma mg.st matches 3 positioned 0.5 81 40800.5 run function mg:tdm/spawn_slot
