# @s est recherché : renforts toutes les 2 s tant qu'il y a moins de policiers que voulu dans les 40 blocs {1: 4, 2: 8, 3: 12, 4: 16, 5: 22}
execute store result score $gc mg.st if entity @e[tag=mg.gcop,distance=..40]
execute if score @s mg.gwl matches 1 run scoreboard players set $gw mg.st 4
execute if score @s mg.gwl matches 2 run scoreboard players set $gw mg.st 8
execute if score @s mg.gwl matches 3 run scoreboard players set $gw mg.st 12
execute if score @s mg.gwl matches 4 run scoreboard players set $gw mg.st 16
execute if score @s mg.gwl matches 5 run scoreboard players set $gw mg.st 22
execute if score $gc mg.st >= $gw mg.st run return 0
execute as @e[type=minecraft:marker,tag=mg.gix,distance=14..45,sort=random,limit=1] at @s run function mg:gta/cop_spawn
execute if score @s mg.gwl matches 2.. as @e[type=minecraft:marker,tag=mg.gix,distance=14..45,sort=random,limit=1] at @s run function mg:gta/cop_spawn
execute if score @s mg.gwl matches 5 as @e[type=minecraft:marker,tag=mg.gix,distance=14..45,sort=random,limit=1] at @s run function mg:gta/cop_spawn
execute if score @s mg.gwl matches 3.. as @e[type=minecraft:marker,tag=mg.gix,distance=14..45,sort=random,limit=1] at @s run function mg:gta/swat_spawn
execute if score @s mg.gwl matches 4.. as @e[type=minecraft:marker,tag=mg.gix,distance=14..45,sort=random,limit=1] at @s run function mg:gta/swat_spawn
execute if score @s mg.gwl matches 5 as @e[type=minecraft:marker,tag=mg.gix,distance=14..45,sort=random,limit=1] at @s run function mg:gta/swat_spawn
