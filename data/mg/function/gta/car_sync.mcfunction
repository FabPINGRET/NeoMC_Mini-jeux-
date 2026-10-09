# @s : cheval d'une voiture. La carrosserie suit ; lancée (> 0,2 bloc/tick), elle renverse ce qu'elle percute
scoreboard players operation $gv mg.st = @s mg.gvid
execute store result score $gx mg.st run data get entity @s Pos[0] 100
execute store result score $gz mg.st run data get entity @s Pos[2] 100
scoreboard players operation $gdx mg.st = $gx mg.st
scoreboard players operation $gdx mg.st -= @s mg.gpx
scoreboard players operation $gdz mg.st = $gz mg.st
scoreboard players operation $gdz mg.st -= @s mg.gpz
scoreboard players operation @s mg.gpx = $gx mg.st
scoreboard players operation @s mg.gpz = $gz mg.st
scoreboard players operation $gdx mg.st *= $gdx mg.st
scoreboard players operation $gdz mg.st *= $gdz mg.st
scoreboard players operation $gdx mg.st += $gdz mg.st
execute unless score $gdx mg.st matches 100..100000 as @e[type=minecraft:block_display,tag=mg.gcard] if score @s mg.gvid = $gv mg.st run function mg:gta/vd_follow
execute if score $gdx mg.st matches 100..899 positioned ^ ^ ^0.3 as @e[type=minecraft:block_display,tag=mg.gcard] if score @s mg.gvid = $gv mg.st run function mg:gta/vd_follow
execute if score $gdx mg.st matches 900..1599 positioned ^ ^ ^0.6 as @e[type=minecraft:block_display,tag=mg.gcard] if score @s mg.gvid = $gv mg.st run function mg:gta/vd_follow
execute if score $gdx mg.st matches 1600..100000 positioned ^ ^ ^0.9 as @e[type=minecraft:block_display,tag=mg.gcard] if score @s mg.gvid = $gv mg.st run function mg:gta/vd_follow
execute if score $gdx mg.st matches 400..100000 on passengers run function mg:gta/car_ram
execute if score $gdx mg.st matches 400..100000 run particle minecraft:smoke ^ ^0.3 ^-1.8 0.1 0.05 0.1 0.01 1
execute if score $gdx mg.st matches 100..100000 if score $gq mg.st matches 0 run playsound minecraft:entity.minecart.riding neutral @a ~ ~ ~ 0.35 1.3
execute if score $gdx mg.st matches 100..100000 if score $gq mg.st matches 10 run playsound minecraft:entity.minecart.riding neutral @a ~ ~ ~ 0.35 1.3
