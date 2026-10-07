# @s traverse le portail des plots : direction son plot
tag @s add mg.lpz
execute at @s run playsound minecraft:block.portal.travel master @s ~ ~ ~ 0.2 1.8
execute at @s run particle minecraft:reverse_portal ~ ~1 ~ 0.4 0.8 0.4 0.05 40
function mg:plot/enter
