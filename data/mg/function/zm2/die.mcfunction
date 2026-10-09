# @s est tombé : spectateur jusqu'à la fin de la manche, perd ses boissons
scoreboard players set @s mg.deaths 0
tag @s add mg.zdead
gamemode spectator @s
tp @s 0 84 35800
execute if entity @s[tag=mg.zjug] run attribute @s minecraft:max_health base set 20
tag @s remove mg.zjug
tag @s remove mg.zsc
tellraw @a[tag=mg.play] [{"text":"☠ ","color":"red"},{"selector":"@s","color":"red"},{"text":" est tombé ! Il reviendra à la fin de la manche.","color":"gray"}]
