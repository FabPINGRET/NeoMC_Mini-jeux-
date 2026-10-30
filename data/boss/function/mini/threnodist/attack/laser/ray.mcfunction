particle dust{color:[0.000,0.000,0.000],scale:2} ~ ~ ~ 0.1 0.1 0.1 0 0 normal
particle reverse_portal ~ ~ ~ 0 0 0 0.1 1 normal

execute positioned ~ 58 ~ as @a[gamemode=!spectator,distance=..1,tag=mg.flw] run damage @s 18 minecraft:dragon_breath
execute positioned ~ 59 ~ as @a[gamemode=!spectator,distance=..1,tag=mg.flw] run damage @s 18 minecraft:dragon_breath


execute positioned ^ ^ ^0.1 if block ^ ^ ^ air run function boss:mini/threnodist/attack/laser/ray
