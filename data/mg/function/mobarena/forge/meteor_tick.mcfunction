# Météorite (@s = marqueur) : chute de 2 blocs par tick
tp @s ~ ~-2 ~
particle minecraft:flame ~ ~ ~ 0.3 0.3 0.3 0.02 8
particle minecraft:lava ~ ~ ~ 0.2 0.2 0.2 0 2
execute positioned ~ 66 ~ run particle minecraft:flame ~ ~0.1 ~ 1.2 0 1.2 0 4
execute at @s if entity @s[y=-1980,dy=2048] run function mg:mobarena/forge/meteor_hit
