# Tir : Mitraillette MP5 (@s = tireur, position/rotation du tireur)
execute if score @s mg.g2 matches ..0 run return run function mg:gun/reload_2
scoreboard players remove @s mg.g2 1
scoreboard players set @s mg.gcd 2
tag @s add mg.gsh
scoreboard players set $gdn mg.st 2
scoreboard players set $grs mg.st 125
scoreboard players set $gstop mg.st 0
execute anchored eyes rotated ~0 ~0 positioned ^ ^ ^0.6 run function mg:gun/ray
tag @s remove mg.gsh
tag @e[tag=mg.ghd] remove mg.ghd
playsound minecraft:entity.firework_rocket.blast player @a ~ ~ ~ 0.5 2.0
execute anchored eyes positioned ^-0.25 ^-0.15 ^0.8 run particle minecraft:small_flame ~ ~ ~ 0.02 0.02 0.02 0 3
execute if score @s mg.g2 matches 0 run function mg:gun/reload_2
