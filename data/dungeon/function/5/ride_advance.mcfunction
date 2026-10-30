#---FIND DIRECTION---
execute as @p[tag=skt_snake_captain,tag=mg.flw] at @s run summon armor_stand ~ ~ ~-2 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["skt_ride_dir","north"],DisabledSlots:4144959}
execute as @p[tag=skt_snake_captain,tag=mg.flw] at @s run summon armor_stand ~ ~ ~2 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["skt_ride_dir","south"],DisabledSlots:4144959}
execute as @p[tag=skt_snake_captain,tag=mg.flw] at @s run summon armor_stand ~-2 ~ ~ {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["skt_ride_dir","west"],DisabledSlots:4144959}
execute as @p[tag=skt_snake_captain,tag=mg.flw] at @s run summon armor_stand ~2 ~ ~ {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["skt_ride_dir","east"],DisabledSlots:4144959}

execute as @p[tag=skt_snake_captain,tag=mg.flw] at @s run summon armor_stand ^ ^ ^2 {NoGravity:1b,Silent:1b,Invulnerable:1b,Small:1b,Invisible:1b,PersistenceRequired:1b,Tags:["skt_ride_point"],DisabledSlots:4144959}

execute as @e[tag=skt_ride_point,distance=0..] at @s run tag @e[tag=skt_ride_dir,limit=1,sort=nearest,distance=0..] add skt_ride_conf

#---CHECK FREE---
execute if entity @e[tag=skt_ride_conf,tag=north,distance=0..] as @e[tag=skt_snake_ride,tag=1,distance=0..] at @s if block ~ ~ ~-1 air run scoreboard players set skt_ride_free Countdown 1
execute if entity @e[tag=skt_ride_conf,tag=south,distance=0..] as @e[tag=skt_snake_ride,tag=1,distance=0..] at @s if block ~ ~ ~1 air run scoreboard players set skt_ride_free Countdown 1
execute if entity @e[tag=skt_ride_conf,tag=west,distance=0..] as @e[tag=skt_snake_ride,tag=1,distance=0..] at @s if block ~-1 ~ ~ air run scoreboard players set skt_ride_free Countdown 1
execute if entity @e[tag=skt_ride_conf,tag=east,distance=0..] as @e[tag=skt_snake_ride,tag=1,distance=0..] at @s if block ~1 ~ ~ air run scoreboard players set skt_ride_free Countdown 1

#---MOVE---
execute if score skt_ride_free Countdown matches 1 as @e[tag=skt_snake_ride,tag=7,distance=0..] at @s unless entity @e[tag=skt_snake_ride,tag=6,distance=..0.5] run fill ~ ~ ~ ~ ~ ~ air replace moss_block

execute if score skt_ride_free Countdown matches 1 at @e[tag=skt_snake_ride,tag=6,distance=0..] run tp @e[tag=skt_snake_ride,tag=7,distance=0..] ~ ~ ~
execute if score skt_ride_free Countdown matches 1 at @e[tag=skt_snake_ride,tag=5,distance=0..] run tp @e[tag=skt_snake_ride,tag=6,distance=0..] ~ ~ ~
execute if score skt_ride_free Countdown matches 1 at @e[tag=skt_snake_ride,tag=4,distance=0..] run tp @e[tag=skt_snake_ride,tag=5,distance=0..] ~ ~ ~
execute if score skt_ride_free Countdown matches 1 at @e[tag=skt_snake_ride,tag=3,distance=0..] run tp @e[tag=skt_snake_ride,tag=4,distance=0..] ~ ~ ~
execute if score skt_ride_free Countdown matches 1 at @e[tag=skt_snake_ride,tag=2,distance=0..] run tp @e[tag=skt_snake_ride,tag=3,distance=0..] ~ ~ ~
execute if score skt_ride_free Countdown matches 1 at @e[tag=skt_snake_ride,tag=1,distance=0..] run tp @e[tag=skt_snake_ride,tag=2,distance=0..] ~ ~ ~

execute if score skt_ride_free Countdown matches 1 if entity @e[tag=skt_ride_conf,tag=north,distance=0..] as @e[tag=skt_snake_ride,tag=1,distance=0..] at @s run tp @s ~ ~ ~-1
execute if score skt_ride_free Countdown matches 1 if entity @e[tag=skt_ride_conf,tag=south,distance=0..] as @e[tag=skt_snake_ride,tag=1,distance=0..] at @s run tp @s ~ ~ ~1
execute if score skt_ride_free Countdown matches 1 if entity @e[tag=skt_ride_conf,tag=west,distance=0..] as @e[tag=skt_snake_ride,tag=1,distance=0..] at @s run tp @s ~-1 ~ ~
execute if score skt_ride_free Countdown matches 1 if entity @e[tag=skt_ride_conf,tag=east,distance=0..] as @e[tag=skt_snake_ride,tag=1,distance=0..] at @s run tp @s ~1 ~ ~

execute if score skt_ride_free Countdown matches 1 as @e[tag=skt_snake_ride,tag=1,distance=0..] at @s run fill ~ ~ ~ ~ ~ ~ moss_block replace air

kill @e[tag=skt_ride_dir,distance=0..]
kill @e[tag=skt_ride_point,distance=0..]
scoreboard players set skt_ride_free Countdown 0

#---ADVANCE---
execute as @e[tag=skt_snake_ride,tag=1,distance=0..] at @s if entity @p[tag=skt_snake_captain,distance=..10,tag=mg.flw] run schedule function floaty:sched/dungeon/5/ride_advance 7t replace
execute as @e[tag=skt_snake_ride,tag=1,distance=0..] at @s unless entity @p[tag=skt_snake_captain,distance=..10,tag=mg.flw] run function dungeon:5/ride_end
