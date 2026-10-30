execute as @a[sort=arbitrary,scores={sneak_last=1,push_mode=0},tag=mg.flw] at @s positioned ~ ~1 ~ positioned ^ ^ ^1 if entity @e[tag=furniture,distance=..0.6] run tag @e[tag=furniture,distance=..0.6] add push_check

execute as @e[tag=push_check,distance=0..] at @s unless block ~1 ~-1 ~ quartz_stairs if block ~1 ~ ~ air at @s positioned ~-1 ~ ~ if entity @a[distance=..0.8,scores={sneak_last=1,push_mode=0},tag=mg.flw] run tag @s add pushing_east

execute as @e[tag=push_check,distance=0..] at @s unless block ~-1 ~-1 ~ quartz_stairs if block ~-1 ~ ~ air at @s positioned ~1 ~ ~ if entity @a[distance=..0.8,scores={sneak_last=1,push_mode=0},tag=mg.flw] run tag @s add pushing_west

execute as @e[tag=push_check,distance=0..] at @s unless block ~ ~-1 ~1 quartz_stairs if block ~ ~ ~1 air at @s positioned ~ ~ ~-1 if entity @a[distance=..0.8,scores={sneak_last=1,push_mode=0},tag=mg.flw] run tag @s add pushing_south

execute as @e[tag=push_check,distance=0..] at @s unless block ~ ~-1 ~-1 quartz_stairs if block ~ ~ ~-1 air at @s positioned ~ ~ ~1 if entity @a[distance=..0.8,scores={sneak_last=1,push_mode=0},tag=mg.flw] run tag @s add pushing_north

execute as @e[tag=pushing_east,distance=0..] at @s as @p[gamemode=!spectator,tag=mg.flw] run attribute @s minecraft:sneaking_speed base set 1
execute as @e[tag=pushing_east,distance=0..] at @s as @p[gamemode=!spectator,tag=mg.flw] run scoreboard players set @s sneak_speed_timer 10
execute as @e[tag=pushing_west,distance=0..] at @s as @p[gamemode=!spectator,tag=mg.flw] run attribute @s minecraft:sneaking_speed base set 1
execute as @e[tag=pushing_west,distance=0..] at @s as @p[gamemode=!spectator,tag=mg.flw] run scoreboard players set @s sneak_speed_timer 10
execute as @e[tag=pushing_south,distance=0..] at @s as @p[gamemode=!spectator,tag=mg.flw] run attribute @s minecraft:sneaking_speed base set 1
execute as @e[tag=pushing_south,distance=0..] at @s as @p[gamemode=!spectator,tag=mg.flw] run scoreboard players set @s sneak_speed_timer 10
execute as @e[tag=pushing_north,distance=0..] at @s as @p[gamemode=!spectator,tag=mg.flw] run attribute @s minecraft:sneaking_speed base set 1
execute as @e[tag=pushing_north,distance=0..] at @s as @p[gamemode=!spectator,tag=mg.flw] run scoreboard players set @s sneak_speed_timer 10

execute at @e[tag=pushing_east,distance=0..] run playsound minecraft:block.grindstone.use block @a[tag=mg.flw] ~ ~ ~ 1 2
execute as @e[tag=pushing_east,distance=0..] at @s run clone ~ ~ ~ ~ ~2 ~ ~1 ~ ~ replace move
execute as @e[tag=pushing_east,distance=0..] at @s run tp @s ~1 ~ ~
tag @e[tag=pushing_east,distance=0..] remove pushing_west
tag @e[tag=pushing_east,distance=0..] remove pushing_south
tag @e[tag=pushing_east,distance=0..] remove pushing_north

execute at @e[tag=pushing_west,distance=0..] run playsound minecraft:block.grindstone.use block @a[tag=mg.flw] ~ ~ ~ 1 2
execute as @e[tag=pushing_west,distance=0..] at @s run clone ~ ~ ~ ~ ~2 ~ ~-1 ~ ~ replace move
execute as @e[tag=pushing_west,distance=0..] at @s run tp @s ~-1 ~ ~
tag @e[tag=pushing_west,distance=0..] remove pushing_south
tag @e[tag=pushing_west,distance=0..] remove pushing_north

execute at @e[tag=pushing_south,distance=0..] run playsound minecraft:block.grindstone.use block @a[tag=mg.flw] ~ ~ ~ 1 2
execute as @e[tag=pushing_south,distance=0..] at @s run clone ~ ~ ~ ~ ~2 ~ ~ ~ ~1 replace move
execute as @e[tag=pushing_south,distance=0..] at @s run tp @s ~ ~ ~1
tag @e[tag=pushing_south,distance=0..] remove pushing_north

execute at @e[tag=pushing_north,distance=0..] run playsound minecraft:block.grindstone.use block @a[tag=mg.flw] ~ ~ ~ 1 2
execute as @e[tag=pushing_north,distance=0..] at @s run clone ~ ~ ~ ~ ~2 ~ ~ ~ ~-1 replace move
execute as @e[tag=pushing_north,distance=0..] at @s run tp @s ~ ~ ~-1

tag @e[distance=0..] remove push_check
tag @e[distance=0..] remove pushing_east
tag @e[distance=0..] remove pushing_west
tag @e[distance=0..] remove pushing_south
tag @e[distance=0..] remove pushing_north
