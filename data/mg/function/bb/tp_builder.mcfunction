# @s = constructeur : téléportation au centre de sa parcelle
scoreboard players operation $bbme mg.st = @s mg.bi
tag @s add mg.bme
execute as @e[type=minecraft:marker,tag=mg.bpm] if score @s mg.bi = $bbme mg.st at @s run tp @a[tag=mg.bme,limit=1] ~ ~1 ~ 0 15
tag @s remove mg.bme
