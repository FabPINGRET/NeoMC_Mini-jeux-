#particle dust_color_transition{from_color:[0.659,0.898,1.000],scale:2,to_color:[0.039,1.000,0.969]} ~ ~ ~ 0.4 0.4 0.4 0 1
#particle dust_color_transition{from_color:[0.200,0.200,1.000],scale:1,to_color:[1.000,1.000,1.000]} ~ ~ ~ 0 0 0 0 1

particle soul_fire_flame ~ ~ ~ 0.2 0.2 0.2 0.1 1
particle soul_fire_flame ~ ~ ~ 0.2 0.2 0.2 0 1


execute positioned ~ ~-1 ~ as @a[gamemode=!spectator,distance=..2,tag=mg.flw] run damage @s 28 minecraft:dragon_breath 

#particle snowflake ~ ~ ~ 0.2 0 0.2 0 1

execute positioned ^ ^ ^0.2 if block ^ ^ ^ #hb_passthrough run function boss:final/virus/attack/eyelaser_ray

#execute unless block ^ ^ ^0.2 #hb_passthrough run particle explosion ~ ~ ~ 0.7 0.7 0.7 0 1
