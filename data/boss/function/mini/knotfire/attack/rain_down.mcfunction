execute as @e[tag=knotfire_rain_loc,distance=0..] at @s run particle minecraft:dust_pillar{block_state:"lime_concrete_powder"} ~ 72 ~ 0 0 0 1 100

execute as @e[tag=knotfire_rain_loc,distance=0..] at @s run playsound minecraft:item.spear.lunge_1 hostile @a[tag=mg.flw] ~ 72 ~ 0.3 1.2

execute as @e[tag=knotfire_rain_loc,distance=0..] at @s positioned ~ 72 ~ as @a[distance=..1,tag=mg.flw] run damage @s 12 minecraft:dragon_breath by @n[tag=knotfire_boss,distance=0..] 

execute as @n[tag=knotfire_statue,tag=active,distance=0..] run function boss:mini/knotfire/pose/throw_down
