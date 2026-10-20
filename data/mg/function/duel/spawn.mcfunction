# Départ de manche (@s = duelliste) : défieur au nord, invité au sud ; 3 s de protection (mg.dlp), tir impossible
scoreboard players set @s mg.dlhp 2
function mg:duel/unscope
tag @s add mg.dlp
execute if items entity @s hotbar.0 minecraft:warped_fungus_on_a_stick[custom_data~{mg_dl:1b}] run item modify entity @s hotbar.0 {function:"minecraft:set_components",components:{"!minecraft:use_cooldown":{}}}
execute if items entity @s hotbar.1 minecraft:warped_fungus_on_a_stick[custom_data~{mg_dl:1b}] run item modify entity @s hotbar.1 {function:"minecraft:set_components",components:{"!minecraft:use_cooldown":{}}}
execute if items entity @s hotbar.2 minecraft:warped_fungus_on_a_stick[custom_data~{mg_dl:1b}] run item modify entity @s hotbar.2 {function:"minecraft:set_components",components:{"!minecraft:use_cooldown":{}}}
execute if items entity @s hotbar.3 minecraft:warped_fungus_on_a_stick[custom_data~{mg_dl:1b}] run item modify entity @s hotbar.3 {function:"minecraft:set_components",components:{"!minecraft:use_cooldown":{}}}
execute if items entity @s hotbar.4 minecraft:warped_fungus_on_a_stick[custom_data~{mg_dl:1b}] run item modify entity @s hotbar.4 {function:"minecraft:set_components",components:{"!minecraft:use_cooldown":{}}}
execute if items entity @s hotbar.5 minecraft:warped_fungus_on_a_stick[custom_data~{mg_dl:1b}] run item modify entity @s hotbar.5 {function:"minecraft:set_components",components:{"!minecraft:use_cooldown":{}}}
execute if items entity @s hotbar.6 minecraft:warped_fungus_on_a_stick[custom_data~{mg_dl:1b}] run item modify entity @s hotbar.6 {function:"minecraft:set_components",components:{"!minecraft:use_cooldown":{}}}
execute if items entity @s hotbar.7 minecraft:warped_fungus_on_a_stick[custom_data~{mg_dl:1b}] run item modify entity @s hotbar.7 {function:"minecraft:set_components",components:{"!minecraft:use_cooldown":{}}}
execute if items entity @s hotbar.8 minecraft:warped_fungus_on_a_stick[custom_data~{mg_dl:1b}] run item modify entity @s hotbar.8 {function:"minecraft:set_components",components:{"!minecraft:use_cooldown":{}}}
scoreboard players set @s mg.dlx 60
scoreboard players set @s mg.dlcd 0
scoreboard players set @s mg.dlkc 0
title @s actionbar {"text":"3","color":"yellow","bold":true}
execute if entity @s[tag=mg.dla,scores={mg.dli=1}] run tp @s 0.5 89 39934.5 0 0
execute if entity @s[tag=!mg.dla,scores={mg.dli=1}] run tp @s 0.5 89 40066.5 180 0
execute if entity @s[tag=mg.dla,scores={mg.dli=2}] run tp @s 0.5 81 40334.5 0 0
execute if entity @s[tag=!mg.dla,scores={mg.dli=2}] run tp @s 0.5 81 40466.5 180 0
execute if entity @s[tag=mg.dla,scores={mg.dli=3}] run tp @s 0.5 81 40734.5 0 0
execute if entity @s[tag=!mg.dla,scores={mg.dli=3}] run tp @s 0.5 81 40866.5 180 0
