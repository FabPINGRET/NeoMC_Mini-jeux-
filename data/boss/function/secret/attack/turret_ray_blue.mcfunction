particle dust{color:[0.000,0.000,1.000],scale:2} ~ ~ ~ 0.1 0.3 0.1 0 1 normal

execute positioned ~ ~ ~ as @a[gamemode=!spectator,distance=..1,tag=mg.flw] run damage @s 26 minecraft:dragon_breath
execute positioned ~ ~-1 ~ as @a[gamemode=!spectator,distance=..1,tag=mg.flw] run damage @s 26 minecraft:dragon_breath


execute positioned ^ ^ ^0.1 if block ^ ^ ^ air run function boss:secret/attack/turret_ray_blue
