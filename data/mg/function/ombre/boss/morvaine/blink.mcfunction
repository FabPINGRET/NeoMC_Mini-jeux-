# Morvaine, la mère-sorcière : blink
particle minecraft:witch ~ ~1 ~ 0.5 1 0.5 0 40
execute store result score $r mg.st run random value 0..3
execute if score $r mg.st matches 0 run tp @s ~8 ~ ~0
execute if score $r mg.st matches 1 run tp @s ~0 ~ ~8
execute if score $r mg.st matches 2 run tp @s ~-8 ~ ~0
execute if score $r mg.st matches 3 run tp @s ~0 ~ ~-8
execute at @s run particle minecraft:witch ~ ~1 ~ 0.5 1 0.5 0 40
playsound minecraft:entity.enderman.teleport hostile @a ~ ~ ~ 1.5 0.6
