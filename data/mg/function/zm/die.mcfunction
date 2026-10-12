# @s est tombé : spectateur jusqu'à la fin de la manche, perd ses boissons
scoreboard players set @s mg.deaths 0
tag @s add mg.zdead
gamemode spectator @s
tp @s 0 84 23200
execute if entity @s[tag=mg.zjug] run attribute @s minecraft:max_health base set 20
tag @s remove mg.zjug
tag @s remove mg.zsc
tag @s remove mg.zdbl
tag @s remove mg.zst
tag @s remove mg.zmu
execute if entity @s[tag=mg.zqr] run scoreboard players set @s mg.zrt 100
execute if entity @s[tag=mg.zqr] run tag @s add mg.zqrw
execute if entity @s[tag=mg.zqr] run return run tag @s remove mg.zqr
tellraw @a[tag=mg.play] [{"text":"☠ ","color":"red"},{"selector":"@s","color":"red"},{"text":" est tombé ! Il reviendra à la fin de la manche.","color":"gray"}]
