# Explosion de rayon 3 à la position courante : $bk blocs, $bb blocs bonus détruits
scoreboard players set $bk mg.st 0
scoreboard players set $bb mg.st 0
execute store result score $bt mg.st run fill ~-0 ~-3 ~-0 ~0 ~-3 ~0 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-0 ~-3 ~-0 ~0 ~-3 ~0 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-2 ~-2 ~-1 ~2 ~-2 ~1 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-2 ~-2 ~-1 ~2 ~-2 ~1 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-1 ~-2 ~-2 ~1 ~-2 ~2 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-1 ~-2 ~-2 ~1 ~-2 ~2 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-3 ~-1 ~-2 ~3 ~-1 ~2 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-3 ~-1 ~-2 ~3 ~-1 ~2 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-2 ~-1 ~-3 ~2 ~-1 ~3 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-2 ~-1 ~-3 ~2 ~-1 ~3 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-3 ~0 ~-2 ~3 ~0 ~2 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-3 ~0 ~-2 ~3 ~0 ~2 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-2 ~0 ~-3 ~2 ~0 ~3 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-2 ~0 ~-3 ~2 ~0 ~3 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-3 ~1 ~-2 ~3 ~1 ~2 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-3 ~1 ~-2 ~3 ~1 ~2 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-2 ~1 ~-3 ~2 ~1 ~3 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-2 ~1 ~-3 ~2 ~1 ~3 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-2 ~2 ~-1 ~2 ~2 ~1 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-2 ~2 ~-1 ~2 ~2 ~1 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-1 ~2 ~-2 ~1 ~2 ~2 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-1 ~2 ~-2 ~1 ~2 ~2 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-0 ~3 ~-0 ~0 ~3 ~0 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-0 ~3 ~-0 ~0 ~3 ~0 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
