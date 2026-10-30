execute as @e[tag=pretzel_emerald_spawn,sort=random,limit=6,distance=0..] at @s run summon villager ~ ~-3 ~ {NoGravity:1b,Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["pretzel_emerald_villager"],VillagerData:{profession:"minecraft:nitwit",type:"minecraft:plains"}}
execute as @e[tag=pretzel_emerald_villager,distance=0..] at @s facing -10340 89 446 run tp @s ~ ~ ~ ~ 0

execute as @e[tag=pretzel_emerald_villager,distance=0..] at @s run function boss:mini/pretzel/utility/emerald_angle

setblock -10355 61 446 redstone_block

scoreboard players set pretzel_emerald_clock Value 0
