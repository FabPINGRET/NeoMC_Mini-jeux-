# @s (voiture PNJ) volée par le joueur accroupi le plus proche : devient une vraie voiture pilotable (une chance sur deux d'être vu : ★)
scoreboard players operation $gv mg.st = @s mg.gvid
execute as @e[type=minecraft:block_display,tag=mg.gtrd] if score @s mg.gvid = $gv mg.st run kill @s
execute if score @s mg.gtmod matches 1 run function mg:gta/car/spawn_1
execute if score @s mg.gtmod matches 2 run function mg:gta/car/spawn_2
execute if score @s mg.gtmod matches 3 run function mg:gta/car/spawn_3
execute if score @s mg.gtmod matches 4 run function mg:gta/car/spawn_4
execute if score @s mg.gtmod matches 5 run function mg:gta/car/spawn_5
execute if score @s mg.gtmod matches 6 run function mg:gta/car/spawn_6
execute if score @s mg.gtmod matches 7 run function mg:gta/car/spawn_7
execute if score @s mg.gtmod matches 8 run function mg:gta/car/spawn_8
execute if score @s mg.gtmod matches 9 run function mg:gta/car/spawn_9
execute if score @s mg.gtmod matches 10 run function mg:gta/car/spawn_10
execute as @p[tag=mg.gtw] run title @s actionbar {"text":"🔑 Voiture volée ! Monte dedans (clic droit).","color":"gold","bold":true}
execute as @p[tag=mg.gtw] run scoreboard players set @s mg.gal 40
execute store result score $gr mg.st run random value 0..1
execute if score $gr mg.st matches 0 as @p[tag=mg.gtw] run function mg:gta/wanted_up
playsound minecraft:block.iron_door.open neutral @a ~ ~ ~ 1 1.2
kill @s
