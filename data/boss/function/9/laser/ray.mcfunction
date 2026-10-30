#particle dust_color_transition{from_color:[0.659,0.898,1.000],scale:2,to_color:[0.039,1.000,0.969]} ~ ~ ~ 0.4 0.4 0.4 0 1
#particle dust_color_transition{from_color:[0.200,0.200,1.000],scale:1,to_color:[1.000,1.000,1.000]} ~ ~ ~ 0 0 0 0 1

particle splash ~ ~ ~ 0.2 0.2 0.2 0 1
particle bubble_pop ~ ~ ~ 0.1 0.1 0.1 0 2


execute positioned ~ ~-1 ~ as @a[gamemode=!spectator,distance=..4,tag=mg.flw] run damage @s 22 minecraft:dragon_breath by @n[tag=wm_boss_name,distance=0..]

#particle snowflake ~ ~ ~ 0.2 0 0.2 0 1

execute positioned ^ ^ ^0.2 if block ^ ^ ^ air run function boss:9/laser/ray
execute positioned ^ ^ ^0.2 if block ^ ^ ^ light run function boss:9/laser/ray

execute unless block ^ ^ ^0.2 air unless block ^ ^ ^0.2 light run particle explosion ~ ~ ~ 0.7 0.7 0.7 0 1
