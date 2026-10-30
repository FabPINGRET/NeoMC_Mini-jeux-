particle dust_color_transition{from_color:[0.098,0.604,0.820],to_color:[0.110,0.808,0.859],scale:1} ~ ~ ~ 0 0 0 0 1

execute positioned ~ ~ ~ as @a[gamemode=!spectator,distance=..2,tag=mg.flw] run damage @s 16 minecraft:dragon_breath by @n[tag=deebo_name,distance=0..]

execute positioned ^ ^ ^0.1 if block ^ ^ ^ air run function boss:mini/dark_eebo/attack/deebo_laser
execute positioned ^ ^ ^0.1 if block ^ ^ ^ light run function boss:mini/dark_eebo/attack/deebo_laser
execute positioned ^ ^ ^0.1 if block ^ ^ ^ #minecraft:wool_carpets run function boss:mini/dark_eebo/attack/deebo_laser

execute unless block ^ ^ ^0.1 air unless block ^ ^ ^0.1 light unless block ^ ^ ^0.1 #minecraft:wool_carpets run particle dust_color_transition{from_color:[0.098,0.604,0.820],to_color:[0.110,0.808,0.859],scale:2} ~ ~ ~ 0 0 0 0 5
