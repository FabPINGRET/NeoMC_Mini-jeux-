execute positioned ~ 72.1 ~ run particle small_gust ~ ~ ~ 0.3 0 0.3 0 1
execute positioned ~ 72.1 ~ run particle block{block_state:"sandstone"} ~ ~ ~ 0.2 0 0.2 0 1
execute positioned ~ 74 ~ run particle egg_crack ~ ~ ~ 0.2 1.5 0.2 0 1

execute positioned ~ 72 ~ as @a[distance=..1.4,tag=mg.flw] run damage @s 24 minecraft:dragon_breath by @n[tag=knotfire_boss,distance=0..]

execute positioned ^ ^ ^0.1 if block ^ ^ ^ air unless entity @e[tag=knotfire_run_dest,distance=..1] run function boss:mini/knotfire/attack/run_ray

execute positioned ^ ^ ^0.1 unless block ^ ^ ^ air positioned ^ ^ ^-0.5 run function boss:mini/knotfire/crash
execute positioned ^ ^ ^0.1 if entity @e[tag=knotfire_run_dest,distance=..1] run function boss:mini/knotfire/attack/run_end
