# Quakecraft — marqueur de grenade (@s = marker, exécuté à sa position)
execute if entity @e[type=minecraft:snowball,tag=mg.grs,distance=..5] run tp @s @e[type=minecraft:snowball,tag=mg.grs,distance=..5,sort=nearest,limit=1]
# Impact : mèche courte (0,5 s)
execute unless entity @e[type=minecraft:snowball,tag=mg.grs,distance=..5] if score @s mg.t matches 11.. run scoreboard players set @s mg.t 10
particle minecraft:smoke ~ ~ ~ 0 0 0 0.01 2
particle minecraft:flame ~ ~ ~ 0 0 0 0.01 1
execute if score @s mg.t matches 10 run playsound minecraft:block.note_block.pling master @a ~ ~ ~ 1 0.5
scoreboard players remove @s mg.t 1
execute if score @s mg.t matches ..0 run function mg:quake/gren_boom
