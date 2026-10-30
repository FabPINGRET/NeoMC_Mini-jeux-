execute if score zoid_hurt bool matches 0 run particle small_flame ~ ~ ~ 0.1 0.1 0.1 0 1
execute if score zoid_hurt bool matches 1 run particle soul_fire_flame ~ ~ ~ 0.1 0.1 0.1 0 1

particle mycelium

execute positioned ^ ^ ^ if entity @e[distance=..1,tag=abnormazoid] as @e[distance=..1,tag=abnormazoid] at @s run function utility:abnormazoid_flag
execute positioned ^ ^ ^ positioned ~ ~-1 ~ if entity @e[distance=..1,tag=abnormazoid] as @e[distance=..1,tag=abnormazoid] at @s run function utility:abnormazoid_flag
execute positioned ^ ^ ^ positioned ~ ~-2 ~ if entity @e[distance=..1,tag=abnormazoid] as @e[distance=..1,tag=abnormazoid] at @s run function utility:abnormazoid_flag


execute positioned ^ ^ ^ if entity @e[distance=..1,tag=enemy] if score zoid_hurt bool matches 1 as @e[distance=..1,tag=enemy] run damage @s 10 minecraft:magic by @p[tag=zoiding,tag=mg.flw]
execute positioned ^ ^ ^ positioned ~ ~-1 ~ if entity @e[distance=..1,tag=enemy] if score zoid_hurt bool matches 1 as @e[distance=..1,tag=enemy] run damage @s 10 minecraft:magic by @p[tag=zoiding,tag=mg.flw]
execute positioned ^ ^ ^ positioned ~ ~-2 ~ if entity @e[distance=..1,tag=enemy] if score zoid_hurt bool matches 1 as @e[distance=..1,tag=enemy] run damage @s 10 minecraft:magic by @p[tag=zoiding,tag=mg.flw]

scoreboard players add @s shortray 1
execute if block ^ ^ ^ air unless score @s shortray matches 80 positioned ^ ^ ^0.1 run function utility:zoidray
