# Tir : Fusil à pompe (@s = tireur, position/rotation du tireur)
execute if score @s mg.g3 matches ..0 run return run function mg:gun/reload_3
scoreboard players remove @s mg.g3 1
scoreboard players set @s mg.gcd 16
tag @s add mg.gsh
scoreboard players set $gdn mg.st 3
scoreboard players set $grs mg.st 40
scoreboard players set $gstop mg.st 0
execute anchored eyes rotated ~0 ~0 positioned ^ ^ ^0.6 run function mg:gun/ray
scoreboard players set $grs mg.st 40
scoreboard players set $gstop mg.st 0
execute anchored eyes rotated ~-4 ~0 positioned ^ ^ ^0.6 run function mg:gun/ray
scoreboard players set $grs mg.st 40
scoreboard players set $gstop mg.st 0
execute anchored eyes rotated ~4 ~0 positioned ^ ^ ^0.6 run function mg:gun/ray
scoreboard players set $grs mg.st 40
scoreboard players set $gstop mg.st 0
execute anchored eyes rotated ~0 ~-3 positioned ^ ^ ^0.6 run function mg:gun/ray
scoreboard players set $grs mg.st 40
scoreboard players set $gstop mg.st 0
execute anchored eyes rotated ~0 ~3 positioned ^ ^ ^0.6 run function mg:gun/ray
scoreboard players set $grs mg.st 40
scoreboard players set $gstop mg.st 0
execute anchored eyes rotated ~-3 ~2 positioned ^ ^ ^0.6 run function mg:gun/ray
scoreboard players set $grs mg.st 40
scoreboard players set $gstop mg.st 0
execute anchored eyes rotated ~3 ~-2 positioned ^ ^ ^0.6 run function mg:gun/ray
tag @s remove mg.gsh
tag @e[tag=mg.ghd] remove mg.ghd
playsound minecraft:entity.generic.explode player @a ~ ~ ~ 0.9 1.8
execute anchored eyes positioned ^-0.25 ^-0.15 ^0.8 run particle minecraft:small_flame ~ ~ ~ 0.02 0.02 0.02 0 3
execute if score @s mg.g3 matches 0 run function mg:gun/reload_3
