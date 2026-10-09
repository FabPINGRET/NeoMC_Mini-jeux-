# @s (voiture PNJ) volée par le joueur tagué mg.gthief : devient une vraie voiture pilotable, il monte au volant (une chance sur deux d'être vu : ★)
scoreboard players operation $gv mg.st = @s mg.gvid
execute as @e[tag=mg.gta,type=!minecraft:marker] if score @s mg.gvid = $gv mg.st run kill @s
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
scoreboard players operation $gv mg.st = $gvid mg.st
execute as @a[tag=mg.gthief,limit=1] run function mg:gta/car_mount
execute as @a[tag=mg.gthief] run title @s actionbar {"text":"🔑 Voiture volée !","color":"gold","bold":true}
execute as @a[tag=mg.gthief] run scoreboard players set @s mg.gal 40
execute store result score $gr mg.st run random value 0..1
execute if score $gr mg.st matches 0 as @a[tag=mg.gthief] run function mg:gta/wanted_up
playsound minecraft:block.iron_door.open neutral @a ~ ~ ~ 1 1.2
kill @s
