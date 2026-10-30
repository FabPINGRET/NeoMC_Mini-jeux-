#---FIND DIRECTION---
execute as @p[tag=sc_snake_captain_1,tag=mg.flw] at @s run summon armor_stand ~ ~ ~-2 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["sc_ride_dir_1","north"],DisabledSlots:4144959}
execute as @p[tag=sc_snake_captain_1,tag=mg.flw] at @s run summon armor_stand ~ ~ ~2 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["sc_ride_dir_1","south"],DisabledSlots:4144959}
execute as @p[tag=sc_snake_captain_1,tag=mg.flw] at @s run summon armor_stand ~-2 ~ ~ {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["sc_ride_dir_1","west"],DisabledSlots:4144959}
execute as @p[tag=sc_snake_captain_1,tag=mg.flw] at @s run summon armor_stand ~2 ~ ~ {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["sc_ride_dir_1","east"],DisabledSlots:4144959}

execute as @p[tag=sc_snake_captain_1,tag=mg.flw] at @s run summon armor_stand ^ ^ ^2 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["sc_ride_point_1"],DisabledSlots:4144959}

execute as @e[tag=sc_ride_point_1,distance=0..] at @s run tag @e[tag=sc_ride_dir_1,limit=1,sort=nearest,distance=0..] add sc_ride_conf_1

#---CHECK FREE---
execute if entity @e[tag=sc_ride_conf_1,tag=north,distance=0..] as @e[tag=sc_snake_ride_1,tag=1,distance=0..] at @s if block ~ ~ ~-1 air run scoreboard players set sc_ride_free_1 Countdown 1
execute if entity @e[tag=sc_ride_conf_1,tag=south,distance=0..] as @e[tag=sc_snake_ride_1,tag=1,distance=0..] at @s if block ~ ~ ~1 air run scoreboard players set sc_ride_free_1 Countdown 1
execute if entity @e[tag=sc_ride_conf_1,tag=west,distance=0..] as @e[tag=sc_snake_ride_1,tag=1,distance=0..] at @s if block ~-1 ~ ~ air run scoreboard players set sc_ride_free_1 Countdown 1
execute if entity @e[tag=sc_ride_conf_1,tag=east,distance=0..] as @e[tag=sc_snake_ride_1,tag=1,distance=0..] at @s if block ~1 ~ ~ air run scoreboard players set sc_ride_free_1 Countdown 1

#---MOVE---
execute if score sc_ride_free_1 Countdown matches 1 as @e[tag=sc_snake_ride_1,tag=7,distance=0..] at @s unless entity @e[tag=sc_snake_ride_1,tag=6,distance=..0.5] run fill ~ ~ ~ ~ ~ ~ air replace purple_wool strict

execute if score sc_ride_free_1 Countdown matches 1 at @e[tag=sc_snake_ride_1,tag=6,distance=0..] run tp @e[tag=sc_snake_ride_1,tag=7,distance=0..] ~ ~ ~
execute if score sc_ride_free_1 Countdown matches 1 at @e[tag=sc_snake_ride_1,tag=5,distance=0..] run tp @e[tag=sc_snake_ride_1,tag=6,distance=0..] ~ ~ ~
execute if score sc_ride_free_1 Countdown matches 1 at @e[tag=sc_snake_ride_1,tag=4,distance=0..] run tp @e[tag=sc_snake_ride_1,tag=5,distance=0..] ~ ~ ~
execute if score sc_ride_free_1 Countdown matches 1 at @e[tag=sc_snake_ride_1,tag=3,distance=0..] run tp @e[tag=sc_snake_ride_1,tag=4,distance=0..] ~ ~ ~
execute if score sc_ride_free_1 Countdown matches 1 at @e[tag=sc_snake_ride_1,tag=2,distance=0..] run tp @e[tag=sc_snake_ride_1,tag=3,distance=0..] ~ ~ ~
execute if score sc_ride_free_1 Countdown matches 1 at @e[tag=sc_snake_ride_1,tag=1,distance=0..] run tp @e[tag=sc_snake_ride_1,tag=2,distance=0..] ~ ~ ~

execute if score sc_ride_free_1 Countdown matches 1 if entity @e[tag=sc_ride_conf_1,tag=north,distance=0..] as @e[tag=sc_snake_ride_1,tag=1,distance=0..] at @s run tp @s ~ ~ ~-1
execute if score sc_ride_free_1 Countdown matches 1 if entity @e[tag=sc_ride_conf_1,tag=south,distance=0..] as @e[tag=sc_snake_ride_1,tag=1,distance=0..] at @s run tp @s ~ ~ ~1
execute if score sc_ride_free_1 Countdown matches 1 if entity @e[tag=sc_ride_conf_1,tag=west,distance=0..] as @e[tag=sc_snake_ride_1,tag=1,distance=0..] at @s run tp @s ~-1 ~ ~
execute if score sc_ride_free_1 Countdown matches 1 if entity @e[tag=sc_ride_conf_1,tag=east,distance=0..] as @e[tag=sc_snake_ride_1,tag=1,distance=0..] at @s run tp @s ~1 ~ ~

execute if score sc_ride_free_1 Countdown matches 1 as @e[tag=sc_snake_ride_1,tag=1,distance=0..] at @s run fill ~ ~ ~ ~ ~ ~ purple_wool replace air strict

kill @e[tag=sc_ride_dir_1,distance=0..]
kill @e[tag=sc_ride_point_1,distance=0..]
scoreboard players set sc_ride_free_1 Countdown 0

#---ADVANCE---
execute as @e[tag=sc_snake_ride_1,tag=1,distance=0..] at @s if entity @p[tag=sc_snake_captain_1,distance=..10,tag=mg.flw] run schedule function floaty:sched/dungeon/extra/snake/1_advance 7t replace
execute as @e[tag=sc_snake_ride_1,tag=1,distance=0..] at @s unless entity @p[tag=sc_snake_captain_1,distance=..10,tag=mg.flw] run function dungeon:extra/snake/1_end
