# Plongeon : la reine disparaît sous l'eau et ressurgit près d'un colon
scoreboard players set $trs2 mg.st 13
execute at @s run particle minecraft:splash ~ ~1 ~ 2 1 2 0 120 force
execute at @s run playsound minecraft:entity.generic.splash hostile @a ~ ~ ~ 2 0.5
execute store result score $r mg.st run random value 0..7
execute if score $r mg.st matches 0 run tp @s 24.5 62 -195.5
execute if score $r mg.st matches 1 run tp @s 20.5 62 -185.5
execute if score $r mg.st matches 2 run tp @s 10.5 62 -181.5
execute if score $r mg.st matches 3 run tp @s 0.5 62 -185.5
execute if score $r mg.st matches 4 run tp @s -3.5 62 -195.5
execute if score $r mg.st matches 5 run tp @s 0.5 62 -205.5
execute if score $r mg.st matches 6 run tp @s 10.5 62 -209.5
execute if score $r mg.st matches 7 run tp @s 20.5 62 -205.5
execute at @s run particle minecraft:bubble_column_up ~ ~ ~ 1.5 1 1.5 0.2 160 force
execute at @s run playsound minecraft:entity.ravager.roar hostile @a ~ ~ ~ 2 0.6
scoreboard players set @s mg.tvat 12
tag @s add mg.tvroar
execute at @s as @a[tag=mg.tvw,gamemode=adventure,distance=..4] run damage @s 10 minecraft:mob_attack by @e[tag=mg.tvspino,limit=1]
