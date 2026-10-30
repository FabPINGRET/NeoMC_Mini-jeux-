execute as @n[tag=threnodist_stand,distance=0..] at @s run particle minecraft:portal ~ ~1.5 ~ 0 0 0 0.5 200
execute as @n[tag=threnodist_stand,distance=0..] at @s run playsound minecraft:entity.enderman.teleport hostile @a[tag=mg.flw] ~ ~ ~ 3 0.7
spreadplayers -11144 430 7 18 false @e[tag=thren_rand,distance=0..]
execute as @e[tag=thren_rand,distance=0..] at @s if block ~ 124 ~ glass run tag @s add viable
execute positioned -11144 58 430 run tag @e[tag=thren_rand,sort=furthest,limit=10,distance=0..] remove viable
execute as @e[tag=thren_rand,tag=viable,sort=random,limit=1,distance=0..] at @s run tp @n[tag=threnodist_stand,distance=0..] ~ 58 ~
tag @e[tag=thren_rand,distance=0..] remove viable
