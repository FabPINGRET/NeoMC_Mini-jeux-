# Tir : Revolver Python (@s = tireur, position/rotation du tireur)
execute unless score @s mg.g8 = @s mg.g8 run scoreboard players set @s mg.g8 6
execute if score @s mg.g8 matches ..0 run return run function mg:gun/reload_8
scoreboard players remove @s mg.g8 1
scoreboard players set @s mg.gcd 10
execute if entity @s[tag=mg.zdbl] run scoreboard players set @s mg.gcd 6
execute if items entity @s weapon.mainhand *[custom_data~{pap:1b}] run tag @s add mg.gpap
tag @s add mg.gsh
scoreboard players set $gdn mg.st 8
scoreboard players set $grs mg.st 150
scoreboard players set $gstop mg.st 0
execute anchored eyes rotated ~0 ~0 positioned ^ ^ ^0.6 run function mg:gun/ray
tag @s remove mg.gsh
tag @s remove mg.gpap
tag @e[tag=mg.ghd] remove mg.ghd
playsound minecraft:entity.firework_rocket.large_blast player @a ~ ~ ~ 0.9 1.0
execute anchored eyes positioned ^-0.25 ^-0.15 ^0.8 run particle minecraft:small_flame ~ ~ ~ 0.02 0.02 0.02 0 3
execute if score @s mg.g8 matches 0 run function mg:gun/reload_8
