# Capteurs du kart (@s = kart, à sa position)
scoreboard players set $kg mg.st 0
execute unless block ~ ~-0.2 ~ #mg:kart_pass run scoreboard players set $kg mg.st 1
scoreboard players set $kro mg.st 0
execute if block ~ ~-0.5 ~ #mg:kart_road run scoreboard players set $kro mg.st 1
execute if score $klob mg.st matches 1 run scoreboard players set $kro mg.st 1
scoreboard players set $kju mg.st 0
execute if block ~ ~-0.5 ~ minecraft:lime_concrete run scoreboard players set $kju mg.st 1
scoreboard players set $kbp mg.st 0
execute if block ~ ~-0.5 ~ minecraft:orange_glazed_terracotta run scoreboard players set $kbp mg.st 1
scoreboard players set $kwa mg.st 0
execute if block ~ ~0.3 ~ minecraft:water run scoreboard players set $kwa mg.st 1
execute if block ~ ~-0.5 ~ minecraft:lava run scoreboard players set $kwa mg.st 1
execute store result score $kyy mg.st run data get entity @s Pos[1] 100
execute store result score $kyaw mg.st run data get entity @s Rotation[0] 10
