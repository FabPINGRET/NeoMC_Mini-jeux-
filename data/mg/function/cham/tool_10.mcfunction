# Lance-peinture : rayon de 40 blocs (cadence 0,6 s)
execute if score @s mg.cmgc matches 1.. run return 0
scoreboard players set @s mg.cmgc 12
tag @s add mg.cmhunt
scoreboard players set $cmr mg.st 160
execute at @s run playsound minecraft:entity.slime.squish player @a ~ ~ ~ 1 1.6
execute anchored eyes positioned ^ ^ ^0.3 run function mg:cham/shot_ray
tag @s remove mg.cmhunt
