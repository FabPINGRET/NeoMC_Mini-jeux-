# @s = constructeur : reste dans sa parcelle (±13 blocs, y 56 à 105)
scoreboard players operation $bbme mg.st = @s mg.bi
tag @s add mg.bme
execute as @e[type=minecraft:marker,tag=mg.bpm] if score @s mg.bi = $bbme mg.st at @s positioned ~-13 ~-8 ~-13 unless entity @a[tag=mg.bme,dx=25,dy=48,dz=25] run function mg:bb/confine_tp
tag @s remove mg.bme
