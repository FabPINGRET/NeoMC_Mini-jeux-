execute as @n[tag=boss_sh_loc,distance=0..] if entity @s[tag=south] run return 2000
execute as @n[tag=boss_sh_loc,distance=0..] if entity @s[tag=north] run return -2000
execute as @n[tag=boss_sh_loc,distance=0..] if entity @s[tag=east] run return run random value -1000..1000
execute as @n[tag=boss_sh_loc,distance=0..] if entity @s[tag=west] run return run random value -1000..1000
