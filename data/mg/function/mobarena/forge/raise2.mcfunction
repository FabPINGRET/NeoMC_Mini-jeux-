function mg:mobarena/forge/lava_l2
scoreboard players set $lvl mg.st 2
title @a[tag=!mg.surv] actionbar [{"text":"La lave monte !","color":"gold","bold":true}]
tellraw @a [{"text":"  ⚠ ","color":"gold"},{"text":"Le niveau de lave monte autour du colisée !","color":"red","bold":true}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.lava.pop master @s ~ ~ ~ 1 0.6
