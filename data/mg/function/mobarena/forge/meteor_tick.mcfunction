# Météorite (@s = marqueur) : chute de 2 blocs par tick
tp @s ~ ~-2 ~
particle minecraft:flame ~ ~ ~ 0.3 0.3 0.3 0.02 8
particle minecraft:lava ~ ~ ~ 0.2 0.2 0.2 0 2
execute positioned ~ 66 ~ run particle minecraft:flame ~ ~0.1 ~ 1.2 0 1.2 0 4
execute store result score @s mg.t run data get entity @s Pos[1]
execute if score @s mg.t matches ..68 run function mg:mobarena/forge/meteor_hit
