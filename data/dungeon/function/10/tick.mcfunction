# FLY CHECK
execute as @a[tag=mg.flw] store result score @s flying run data get entity @s FallFlying 1

execute as @a[tag=mg.flw] run attribute @s minecraft:gravity base reset
execute as @a[scores={twister_timer=1..},tag=mg.flw] run attribute @s minecraft:gravity base set -0.3

execute as @a[scores={twister_timer=0},tag=mg.flw] at @s positioned ~ ~ ~ if entity @n[tag=ta_tornado,distance=..1.25] if score @s flying matches 1 run scoreboard players set @s twister_timer 8
execute as @a[scores={twister_timer=0},tag=mg.flw] at @s positioned ~ ~-1 ~ if entity @n[tag=ta_tornado,distance=..1.25] if score @s flying matches 1 run scoreboard players set @s twister_timer 8
execute as @a[scores={twister_timer=0},tag=mg.flw] at @s positioned ~ ~-2 ~ if entity @n[tag=ta_tornado,distance=..1.25] if score @s flying matches 1 run scoreboard players set @s twister_timer 8


#execute as @e[tag=ta_tornado] at @s run particle minecraft:smoke ~ ~1 ~ 0.1 0.6 0.1 0 1
#execute as @e[tag=ta_tornado] at @s run particle minecraft:campfire_cosy_smoke ~ ~1 ~ 0.2 0.5 0.2 0 1
execute as @e[tag=ta_tornado,distance=0..] at @s run particle minecraft:small_gust ~ ~1 ~ 0.2 0.6 0.2 0 1

execute as @e[tag=ta_tornado_display,distance=0..] at @s run tp @s ~ ~ ~ ~25 ~

execute as @a[scores={twister_timer=1..},tag=mg.flw] run scoreboard players remove @s twister_timer 1

execute as @e[tag=ta_soul_display,distance=0..] at @s facing entity @p[gamemode=!spectator,tag=mg.flw] eyes run tp @s ~ ~ ~ ~ ~

execute as @e[tag=ta_soul_display,distance=0..] at @s run particle minecraft:white_smoke ~ ~1.8 ~ 0.2 0.1 0.2 0 1

execute as @a[gamemode=!spectator,sort=arbitrary,tag=mg.flw] run function dungeon:10/push/push_check
execute as @a[gamemode=!spectator,sort=arbitrary,tag=mg.flw] run function dungeon:10/push/pull_check
