# Explosion de rayon 8 à la position courante : $bk blocs, $bb blocs bonus détruits
scoreboard players set $bk mg.st 0
scoreboard players set $bb mg.st 0
execute store result score $bt mg.st run fill ~-0 ~-8 ~-0 ~0 ~-8 ~0 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-0 ~-8 ~-0 ~0 ~-8 ~0 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-4 ~-7 ~-2 ~4 ~-7 ~2 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-4 ~-7 ~-2 ~4 ~-7 ~2 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-2 ~-7 ~-4 ~2 ~-7 ~4 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-2 ~-7 ~-4 ~2 ~-7 ~4 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-5 ~-6 ~-2 ~5 ~-6 ~2 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-5 ~-6 ~-2 ~5 ~-6 ~2 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-2 ~-6 ~-5 ~2 ~-6 ~5 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-2 ~-6 ~-5 ~2 ~-6 ~5 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-6 ~-5 ~-3 ~6 ~-5 ~3 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-6 ~-5 ~-3 ~6 ~-5 ~3 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-3 ~-5 ~-6 ~3 ~-5 ~6 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-3 ~-5 ~-6 ~3 ~-5 ~6 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-7 ~-4 ~-4 ~7 ~-4 ~4 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-7 ~-4 ~-4 ~7 ~-4 ~4 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-4 ~-4 ~-7 ~4 ~-4 ~7 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-4 ~-4 ~-7 ~4 ~-4 ~7 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-7 ~-3 ~-4 ~7 ~-3 ~4 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-7 ~-3 ~-4 ~7 ~-3 ~4 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-4 ~-3 ~-7 ~4 ~-3 ~7 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-4 ~-3 ~-7 ~4 ~-3 ~7 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-8 ~-2 ~-4 ~8 ~-2 ~4 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-8 ~-2 ~-4 ~8 ~-2 ~4 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-4 ~-2 ~-8 ~4 ~-2 ~8 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-4 ~-2 ~-8 ~4 ~-2 ~8 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-8 ~-1 ~-4 ~8 ~-1 ~4 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-8 ~-1 ~-4 ~8 ~-1 ~4 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-4 ~-1 ~-8 ~4 ~-1 ~8 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-4 ~-1 ~-8 ~4 ~-1 ~8 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-8 ~0 ~-4 ~8 ~0 ~4 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-8 ~0 ~-4 ~8 ~0 ~4 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-4 ~0 ~-8 ~4 ~0 ~8 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-4 ~0 ~-8 ~4 ~0 ~8 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-8 ~1 ~-4 ~8 ~1 ~4 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-8 ~1 ~-4 ~8 ~1 ~4 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-4 ~1 ~-8 ~4 ~1 ~8 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-4 ~1 ~-8 ~4 ~1 ~8 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-8 ~2 ~-4 ~8 ~2 ~4 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-8 ~2 ~-4 ~8 ~2 ~4 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-4 ~2 ~-8 ~4 ~2 ~8 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-4 ~2 ~-8 ~4 ~2 ~8 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-7 ~3 ~-4 ~7 ~3 ~4 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-7 ~3 ~-4 ~7 ~3 ~4 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-4 ~3 ~-7 ~4 ~3 ~7 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-4 ~3 ~-7 ~4 ~3 ~7 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-7 ~4 ~-4 ~7 ~4 ~4 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-7 ~4 ~-4 ~7 ~4 ~4 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-4 ~4 ~-7 ~4 ~4 ~7 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-4 ~4 ~-7 ~4 ~4 ~7 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-6 ~5 ~-3 ~6 ~5 ~3 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-6 ~5 ~-3 ~6 ~5 ~3 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-3 ~5 ~-6 ~3 ~5 ~6 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-3 ~5 ~-6 ~3 ~5 ~6 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-5 ~6 ~-2 ~5 ~6 ~2 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-5 ~6 ~-2 ~5 ~6 ~2 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-2 ~6 ~-5 ~2 ~6 ~5 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-2 ~6 ~-5 ~2 ~6 ~5 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-4 ~7 ~-2 ~4 ~7 ~2 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-4 ~7 ~-2 ~4 ~7 ~2 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-2 ~7 ~-4 ~2 ~7 ~4 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-2 ~7 ~-4 ~2 ~7 ~4 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-0 ~8 ~-0 ~0 ~8 ~0 minecraft:air replace #mg:bomb_bonus
scoreboard players operation $bb mg.st += $bt mg.st
execute store result score $bt mg.st run fill ~-0 ~8 ~-0 ~0 ~8 ~0 minecraft:air replace #mg:bomb_city
scoreboard players operation $bk mg.st += $bt mg.st
