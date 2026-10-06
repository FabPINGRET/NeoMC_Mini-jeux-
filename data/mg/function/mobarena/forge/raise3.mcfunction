function mg:mobarena/forge/lava_l3
scoreboard players set $lvl mg.st 3
title @a actionbar [{"text":"La lave monte !","color":"gold","bold":true}]
tellraw @a [{"text":"  ⚠ ","color":"gold"},{"text":"Le niveau de lave monte autour du colisée !","color":"red","bold":true}]
execute as @a at @s run playsound minecraft:block.lava.pop master @s ~ ~ ~ 1 0.6
