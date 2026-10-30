execute as @n[tag=boss_sh_loc,distance=0..] if entity @s[tag=east] run return 500
execute as @n[tag=boss_sh_loc,distance=0..] if entity @s[tag=west] run return -500
execute as @n[tag=boss_sh_loc,distance=0..] if entity @s[tag=north] run return 0
execute as @n[tag=boss_sh_loc,distance=0..] if entity @s[tag=south] run return 0
