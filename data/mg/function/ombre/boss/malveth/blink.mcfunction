# Malveth, l'archimage : blink
particle minecraft:reverse_portal ~ ~1 ~ 0.5 1 0.5 0.1 60
execute store result score $r mg.st run random value 0..3
execute if score $r mg.st matches 0 run tp @s -164.5 67 183.5
execute if score $r mg.st matches 1 run tp @s -176.5 67 185.5
execute if score $r mg.st matches 2 run tp @s -178.5 67 173.5
execute if score $r mg.st matches 3 run tp @s -166.5 67 171.5
playsound minecraft:entity.enderman.teleport hostile @a ~ ~ ~ 1.5 0.5
