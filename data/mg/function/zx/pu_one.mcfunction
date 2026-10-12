# @s : bonus au sol (30 s), tourne, pris par le premier joueur qui marche dessus
scoreboard players add @s mg.zpl 1
tp @s ~ ~ ~ ~8 ~
particle minecraft:end_rod ~ ~ ~ 0.2 0.2 0.2 0.01 1
execute if score @s mg.zpl matches 600.. run return run kill @s
execute if entity @a[tag=mg.play,tag=!mg.zdead,distance=..1.8] run function mg:zx/pu_take
