# Tir : Ray Gun (@s = tireur, position/rotation du tireur)
execute if score @s mg.g6 matches ..0 run return run function mg:gun/reload_6
scoreboard players remove @s mg.g6 1
scoreboard players set @s mg.gcd 8
tag @s add mg.gsh
scoreboard players set $gdn mg.st 6
scoreboard players set $grs mg.st 150
scoreboard players set $gstop mg.st 0
execute anchored eyes rotated ~0 ~0 positioned ^ ^ ^0.6 run function mg:gun/ray
tag @s remove mg.gsh
tag @e[tag=mg.ghd] remove mg.ghd
playsound minecraft:block.beacon.power_select player @a ~ ~ ~ 0.9 2.0
execute anchored eyes positioned ^-0.25 ^-0.15 ^0.8 run particle minecraft:happy_villager ~ ~ ~ 0.05 0.05 0.05 0 4
execute if score @s mg.g6 matches 0 run function mg:gun/reload_6
