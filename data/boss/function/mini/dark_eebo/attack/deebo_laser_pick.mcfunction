execute as @n[tag=deebo_stand,distance=0..] at @s run playsound minecraft:item.lodestone_compass.lock hostile @a[tag=mg.flw] ~ ~ ~ 1 1.5

summon area_effect_cloud -11538 175 -183 {Tags:["deebo_laser_temp","1","exclude"]}
summon area_effect_cloud -11538 175 -183 {Tags:["deebo_laser_temp","2","exclude"]}
summon area_effect_cloud -11538 175 -183 {Tags:["deebo_laser_temp","3","exclude"]}
summon area_effect_cloud -11538 175 -183 {Tags:["deebo_laser_temp","4","exclude"]}
summon area_effect_cloud -11538 175 -183 {Tags:["deebo_laser_temp","5","exclude"]}
summon area_effect_cloud -11538 175 -183 {Tags:["deebo_laser_temp","6","exclude"]}
summon area_effect_cloud -11538 175 -183 {Tags:["deebo_laser_temp","7","exclude"]}
summon area_effect_cloud -11538 175 -183 {Tags:["deebo_laser_temp","8","exclude"]}
summon area_effect_cloud -11538 175 -183 {Tags:["deebo_laser_temp","9","exclude"]}


tag @e[type=minecraft:area_effect_cloud,tag=deebo_laser_temp,limit=1,sort=random,distance=0..] remove exclude
kill @e[type=minecraft:area_effect_cloud,tag=deebo_laser_temp,tag=exclude,distance=0..]

execute if entity @e[tag=deebo_laser_temp,tag=1,distance=0..] as @n[tag=deebo_stand,distance=0..] at @s positioned ~ ~0.7 ~ positioned ^ ^ ^0.35 facing ^ ^-1 ^ run function boss:mini/dark_eebo/attack/deebo_laser
execute if entity @e[tag=deebo_laser_temp,tag=2,distance=0..] as @n[tag=deebo_stand,distance=0..] at @s positioned ~ ~0.7 ~ positioned ^ ^ ^0.35 facing ^ ^-1 ^0.3 run function boss:mini/dark_eebo/attack/deebo_laser
execute if entity @e[tag=deebo_laser_temp,tag=3,distance=0..] as @n[tag=deebo_stand,distance=0..] at @s positioned ~ ~0.7 ~ positioned ^ ^ ^0.35 facing ^ ^-1 ^0.6 run function boss:mini/dark_eebo/attack/deebo_laser

execute if entity @e[tag=deebo_laser_temp,tag=4,distance=0..] as @n[tag=deebo_stand,distance=0..] at @s positioned ~ ~0.7 ~ positioned ^ ^ ^0.35 facing ^-0.5 ^-1 ^ run function boss:mini/dark_eebo/attack/deebo_laser
execute if entity @e[tag=deebo_laser_temp,tag=5,distance=0..] as @n[tag=deebo_stand,distance=0..] at @s positioned ~ ~0.7 ~ positioned ^ ^ ^0.35 facing ^-0.5 ^-1 ^0.3 run function boss:mini/dark_eebo/attack/deebo_laser
execute if entity @e[tag=deebo_laser_temp,tag=6,distance=0..] as @n[tag=deebo_stand,distance=0..] at @s positioned ~ ~0.7 ~ positioned ^ ^ ^0.35 facing ^-0.5 ^-1 ^0.6 run function boss:mini/dark_eebo/attack/deebo_laser

execute if entity @e[tag=deebo_laser_temp,tag=7,distance=0..] as @n[tag=deebo_stand,distance=0..] at @s positioned ~ ~0.7 ~ positioned ^ ^ ^0.35 facing ^0.5 ^-1 ^ run function boss:mini/dark_eebo/attack/deebo_laser
execute if entity @e[tag=deebo_laser_temp,tag=8,distance=0..] as @n[tag=deebo_stand,distance=0..] at @s positioned ~ ~0.7 ~ positioned ^ ^ ^0.35 facing ^0.5 ^-1 ^0.3 run function boss:mini/dark_eebo/attack/deebo_laser
execute if entity @e[tag=deebo_laser_temp,tag=9,distance=0..] as @n[tag=deebo_stand,distance=0..] at @s positioned ~ ~0.7 ~ positioned ^ ^ ^0.35 facing ^0.5 ^-1 ^0.6 run function boss:mini/dark_eebo/attack/deebo_laser

kill @e[type=minecraft:area_effect_cloud,tag=deebo_laser_temp,distance=0..]
