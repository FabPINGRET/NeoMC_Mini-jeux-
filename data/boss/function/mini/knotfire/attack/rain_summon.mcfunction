tag @e[tag=knotfire_rand,tag=!used,sort=random,limit=1,distance=0..] add raining

execute as @n[tag=raining,distance=0..] at @s run summon armor_stand ~ 68 ~ {NoGravity:1b,Silent:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["knotfire_rain_loc"],attributes:[{id:"minecraft:scale",base:2}],Pose:{Head:[180f,0f,0f]},DisabledSlots:4144959,equipment:{head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{"properties":[{"name":"textures","value":"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYzQzZjEyYzgzNjlmOWMzODg4YTQ1YWFmNmQ3NzYxNTc4NDAyYjQyNDE5NThmN2Q0YWU0ZWNlYjU2YTg2N2QyYSJ9fX0="}]}}}}}

execute as @e[tag=knotfire_rain_loc,distance=0..] at @s run tp @s ~ 78 ~
execute as @n[tag=raining,distance=0..] at @s run playsound minecraft:block.sculk.charge hostile @a[tag=mg.flw] ~ 72 ~ 1 2

tag @n[tag=raining,distance=0..] add used
tag @e[tag=knotfire_rand,distance=0..] remove raining
