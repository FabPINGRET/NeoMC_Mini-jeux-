# @s a bu une potion de mana
scoreboard players set @s mg.olhb 0
clear @s minecraft:glass_bottle 1
scoreboard players add @s mg.olmp 60
execute if score @s mg.olmp > @s mg.olmm run scoreboard players operation @s mg.olmp = @s mg.olmm
function mg:ombre/mana_bar
execute at @s run particle minecraft:glow ~ ~1 ~ 0.4 0.6 0.4 0 20
