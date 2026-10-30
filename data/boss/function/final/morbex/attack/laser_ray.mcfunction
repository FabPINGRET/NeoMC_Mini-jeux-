particle trial_omen ~ ~ ~ 0.1 0.1 0.1 0.01 1

execute positioned ~ ~-1.8 ~ as @a[distance=..0.3,tag=mg.flw] run damage @s 28 minecraft:mob_attack by @n[tag=l_morbex_2,distance=0..]


execute positioned ^ ^ ^0.1 if block ^ ^ ^ #hb_passthrough run function boss:final/morbex/attack/laser_ray
