execute as @a[sort=arbitrary,scores={sneak_last=1,push_mode=1},tag=mg.flw] at @s positioned ~ ~1 ~ positioned ^ ^ ^2 if entity @e[tag=lantern,distance=..0.6] run tag @e[tag=lantern,distance=..0.6] add push_check

execute as @e[tag=push_check,distance=0..] at @s if block ~1 ~-1 ~ yellow_stained_glass if block ~1 ~ ~ air at @s positioned ~2.2 ~ ~ if entity @a[distance=..0.8,scores={sneak_last=1,push_mode=1},tag=mg.flw] run tag @s add pushing_east

execute as @e[tag=push_check,distance=0..] at @s if block ~-1 ~-1 ~ yellow_stained_glass if block ~-1 ~ ~ air at @s positioned ~-2.2 ~ ~ if entity @a[distance=..0.8,scores={sneak_last=1,push_mode=1},tag=mg.flw] run tag @s add pushing_west

execute as @e[tag=push_check,distance=0..] at @s if block ~ ~-1 ~1 yellow_stained_glass if block ~ ~ ~1 air at @s positioned ~ ~ ~2.2 if entity @a[distance=..0.8,scores={sneak_last=1,push_mode=1},tag=mg.flw] run tag @s add pushing_south

execute as @e[tag=push_check,distance=0..] at @s if block ~ ~-1 ~-1 yellow_stained_glass if block ~ ~ ~-1 air at @s positioned ~ ~ ~-2.2 if entity @a[distance=..0.8,scores={sneak_last=1,push_mode=1},tag=mg.flw] run tag @s add pushing_north

execute as @e[tag=pushing_east,distance=0..] at @s as @p[gamemode=!spectator,tag=mg.flw] run attribute @s minecraft:sneaking_speed base set 1
execute as @e[tag=pushing_east,distance=0..] at @s as @p[gamemode=!spectator,tag=mg.flw] run scoreboard players set @s sneak_speed_timer 10
execute as @e[tag=pushing_west,distance=0..] at @s as @p[gamemode=!spectator,tag=mg.flw] run attribute @s minecraft:sneaking_speed base set 1
execute as @e[tag=pushing_west,distance=0..] at @s as @p[gamemode=!spectator,tag=mg.flw] run scoreboard players set @s sneak_speed_timer 10
execute as @e[tag=pushing_south,distance=0..] at @s as @p[gamemode=!spectator,tag=mg.flw] run attribute @s minecraft:sneaking_speed base set 1
execute as @e[tag=pushing_south,distance=0..] at @s as @p[gamemode=!spectator,tag=mg.flw] run scoreboard players set @s sneak_speed_timer 10
execute as @e[tag=pushing_north,distance=0..] at @s as @p[gamemode=!spectator,tag=mg.flw] run attribute @s minecraft:sneaking_speed base set 1
execute as @e[tag=pushing_north,distance=0..] at @s as @p[gamemode=!spectator,tag=mg.flw] run scoreboard players set @s sneak_speed_timer 10

execute at @e[tag=pushing_east,distance=0..] run playsound minecraft:block.grindstone.use block @a[tag=mg.flw] ~ ~ ~ 1 2
execute as @e[tag=pushing_east,distance=0..] at @s run clone ~ ~-17 ~ ~ ~14 ~ ~1 ~-17 ~ replace move
execute as @e[tag=pushing_east,distance=0..] at @s run tp @s ~1 ~ ~
execute as @e[tag=pushing_east,distance=0..] run fill -11515 131 330 -11532 131 308 minecraft:yellow_stained_glass replace air
execute as @e[tag=pushing_east,distance=0..] run fill -11532 115 330 -11516 130 309 light[level=12] replace air
execute as @e[tag=pushing_east,distance=0..] as @n[tag=lantern,tag=first,distance=0..] at @s if blocks ~ 115 ~ ~8 146 ~ -11528 115 299 all run setblock -11516 142 305 minecraft:redstone_block
tag @e[tag=pushing_east,distance=0..] remove pushing_west
tag @e[tag=pushing_east,distance=0..] remove pushing_south
tag @e[tag=pushing_east,distance=0..] remove pushing_north

execute at @e[tag=pushing_west,distance=0..] run playsound minecraft:block.grindstone.use block @a[tag=mg.flw] ~ ~ ~ 1 2
execute as @e[tag=pushing_west,distance=0..] at @s run clone ~ ~-17 ~ ~ ~14 ~ ~-1 ~-17 ~ replace move
execute as @e[tag=pushing_west,distance=0..] at @s run tp @s ~-1 ~ ~
execute as @e[tag=pushing_west,distance=0..] run fill -11515 131 330 -11532 131 308 minecraft:yellow_stained_glass replace air
execute as @e[tag=pushing_west,distance=0..] run fill -11532 115 330 -11516 130 309 light[level=12] replace air
execute as @e[tag=pushing_west,distance=0..] as @n[tag=lantern,tag=first,distance=0..] at @s if blocks ~ 115 ~ ~8 146 ~ -11528 115 299 all run setblock -11516 142 305 minecraft:redstone_block
tag @e[tag=pushing_west,distance=0..] remove pushing_south
tag @e[tag=pushing_west,distance=0..] remove pushing_north

execute at @e[tag=pushing_south,distance=0..] run playsound minecraft:block.grindstone.use block @a[tag=mg.flw] ~ ~ ~ 1 2
execute as @e[tag=pushing_south,distance=0..] at @s run clone ~ ~-17 ~ ~ ~14 ~ ~ ~-17 ~1 replace move
execute as @e[tag=pushing_south,distance=0..] at @s run tp @s ~ ~ ~1
execute as @e[tag=pushing_south,distance=0..] run fill -11515 131 330 -11532 131 308 minecraft:yellow_stained_glass replace air
execute as @e[tag=pushing_south,distance=0..] run fill -11532 115 330 -11516 130 309 light[level=12] replace air
execute as @e[tag=pushing_south,distance=0..] as @n[tag=lantern,tag=first,distance=0..] at @s if blocks ~ 115 ~ ~8 146 ~ -11528 115 299 all run setblock -11516 142 305 minecraft:redstone_block
tag @e[tag=pushing_south,distance=0..] remove pushing_north

execute at @e[tag=pushing_north,distance=0..] run playsound minecraft:block.grindstone.use block @a[tag=mg.flw] ~ ~ ~ 1 2
execute as @e[tag=pushing_north,distance=0..] at @s run clone ~ ~-17 ~ ~ ~14 ~ ~ ~-17 ~-1 replace move
execute as @e[tag=pushing_north,distance=0..] at @s run tp @s ~ ~ ~-1
execute as @e[tag=pushing_north,distance=0..] run fill -11515 131 330 -11532 131 308 minecraft:yellow_stained_glass replace air
execute as @e[tag=pushing_north,distance=0..] run fill -11532 115 330 -11516 130 309 light[level=12] replace air
execute as @e[tag=pushing_north,distance=0..] as @n[tag=lantern,tag=first,distance=0..] at @s if blocks ~ 115 ~ ~8 146 ~ -11528 115 299 all run setblock -11516 142 305 minecraft:redstone_block

tag @e[distance=0..] remove push_check
tag @e[distance=0..] remove pushing_east
tag @e[distance=0..] remove pushing_west
tag @e[distance=0..] remove pushing_south
tag @e[distance=0..] remove pushing_north
