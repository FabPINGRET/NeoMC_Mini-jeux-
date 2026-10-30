#particle dust_color_transition{from_color:[0.000,0.000,0.000],scale:1,to_color:[1.000,1.000,0.000]} ~ ~ ~ 0.4 0.4 0.4 0 1
#particle dust_color_transition{from_color:[0.200,0.200,1.000],scale:1,to_color:[1.000,1.000,1.000]} ~ ~ ~ 0 0 0 0 1

particle dust{color:[1.000,1.000,0.000],scale:1} ~ ~ ~ 0 0 0 0 1 normal

#execute positioned ~ ~-1 ~ as @a[gamemode=!spectator,distance=..4] run damage @s 28 minecraft:dragon_breath by @n[tag=ta_boss_name]

execute positioned ^ ^ ^0.1 if block ^ ^ ^ air run function boss:10/attack/pred_tracer
execute positioned ^ ^ ^0.1 if block ^ ^ ^ light run function boss:10/attack/pred_tracer

#execute unless block ^ ^ ^0.2 air unless block ^ ^ ^0.2 light run particle explosion ~ ~ ~ 0.7 0.7 0.7 0 1
