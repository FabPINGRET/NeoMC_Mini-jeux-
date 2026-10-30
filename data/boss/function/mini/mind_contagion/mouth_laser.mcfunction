particle dust{color:[0.000,0.145,0.149],scale:1} ~ ~ ~ 0.1 0.1 0.1 0 1

execute positioned ~ ~ ~ as @a[gamemode=!spectator,distance=..2,tag=mg.flw] run damage @s 16 minecraft:dragon_breath

execute positioned ^ ^ ^0.3 if block ^ ^ ^ air run function boss:mini/mind_contagion/mouth_laser
execute positioned ^ ^ ^0.3 if block ^ ^ ^ light run function boss:mini/mind_contagion/mouth_laser
execute positioned ^ ^ ^0.3 if block ^ ^ ^ #minecraft:wool_carpets run function boss:mini/mind_contagion/mouth_laser

#execute unless block ^ ^ ^0.1 air unless block ^ ^ ^0.1 light run particle explosion ~ ~ ~ 0 0 0 0 5
