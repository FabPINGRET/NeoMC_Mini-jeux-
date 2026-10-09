# @s braque le passant visé (mg.grt) : 2 s
effect give @e[tag=mg.grt] minecraft:slowness 1 6 true
execute as @e[tag=mg.grt] at @s run particle minecraft:angry_villager ~ ~2.2 ~ 0.2 0.1 0.2 0 1
scoreboard players add @s mg.grob 5
function mg:gta/rob_bar_ped
execute if score @s mg.grob matches 40.. run function mg:gta/rob_ped_ok
tag @e[tag=mg.grt] remove mg.grt
