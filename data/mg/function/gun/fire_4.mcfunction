# Tir : Fusil M14 (@s = tireur, position/rotation du tireur)
execute if score @s mg.g4 matches ..0 run return run function mg:gun/reload_4
scoreboard players remove @s mg.g4 1
scoreboard players set @s mg.gcd 7
tag @s add mg.gsh
scoreboard players set $gdn mg.st 4
scoreboard players set $grs mg.st 200
scoreboard players set $gstop mg.st 0
execute anchored eyes rotated ~0 ~0 positioned ^ ^ ^0.6 run function mg:gun/ray
tag @s remove mg.gsh
tag @e[tag=mg.ghd] remove mg.ghd
playsound minecraft:entity.firework_rocket.large_blast player @a ~ ~ ~ 0.9 1.4
execute anchored eyes positioned ^-0.25 ^-0.15 ^0.8 run particle minecraft:small_flame ~ ~ ~ 0.02 0.02 0.02 0 3
execute if score @s mg.g4 matches 0 run function mg:gun/reload_4
