tag @s add active
execute positioned ^7 ^ ^-3 run summon turtle ~ 88 ~ {NoGravity:1b,Silent:1b,Invulnerable:1b,PersistenceRequired:1b,NoAI:1b,Tags:["pretzel_turtle","new"],attributes:[{id:"minecraft:scale",base:4}]}

execute as @n[tag=pretzel_turtle,tag=new,distance=0..] at @s rotated as @n[tag=pretzel_turtle_spawn,tag=active,distance=0..] run tp @s ~ 88 ~ ~ 0
tag @e[tag=pretzel_turtle,distance=0..] remove new
tag @s remove active
