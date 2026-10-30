#particle dust_color_transition{from_color:[0.000,0.000,0.000],scale:1,to_color:[1.000,1.000,0.000]} ~ ~ ~ 0.4 0.4 0.4 0 1
#particle dust_color_transition{from_color:[0.200,0.200,1.000],scale:1,to_color:[1.000,1.000,1.000]} ~ ~ ~ 0 0 0 0 1

particle sculk_soul ~ ~ ~ 0.2 0.2 0.2 0 1
particle dust_color_transition{from_color:[0.000,0.000,0.000],scale:1,to_color:[1.000,1.000,0.000]} ~ ~ ~ 0 0 0 0 1

execute positioned ~ ~-1 ~ as @a[gamemode=!spectator,distance=..4,tag=mg.flw] run damage @s 28 minecraft:dragon_breath by @n[tag=ta_boss_name,distance=0..]

execute positioned ^ ^ ^0.2 if block ^ ^ ^ air run function boss:10/attack/scorn_beam
execute positioned ^ ^ ^0.2 if block ^ ^ ^ light run function boss:10/attack/scorn_beam

#execute unless block ^ ^ ^0.2 air unless block ^ ^ ^0.2 light run particle explosion ~ ~ ~ 0.7 0.7 0.7 0 1
