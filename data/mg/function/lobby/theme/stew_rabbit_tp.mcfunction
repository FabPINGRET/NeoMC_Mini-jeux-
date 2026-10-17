# Chaque tick (lobby/theme/tick ; @s = joueur lapin, à sa position) : le lapin se recolle au joueur, dans son axe
scoreboard players operation $thbi mg.st = @s mg.thbn
execute as @e[type=minecraft:rabbit,tag=mg.thbun] if score @s mg.thbn = $thbi mg.st run tp @s ~ ~ ~ ~ 0
