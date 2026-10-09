# Tir : Pistolet M1911 (@s = tireur, position/rotation du tireur)
execute if score @s mg.g1 matches ..0 run return run function mg:gun/reload_1
scoreboard players remove @s mg.g1 1
scoreboard players set @s mg.gcd 5
tag @s add mg.gsh
scoreboard players set $gdn mg.st 1
scoreboard players set $grs mg.st 150
scoreboard players set $gstop mg.st 0
execute anchored eyes rotated ~0 ~0 positioned ^ ^ ^0.6 run function mg:gun/ray
tag @s remove mg.gsh
tag @e[tag=mg.ghd] remove mg.ghd
playsound minecraft:entity.firework_rocket.blast player @a ~ ~ ~ 0.9 1.6
execute anchored eyes positioned ^-0.25 ^-0.15 ^0.8 run particle minecraft:small_flame ~ ~ ~ 0.02 0.02 0.02 0 3
execute if score @s mg.g1 matches 0 run function mg:gun/reload_1
