particle item_slime ^ ^ ^ 0.1 0.1 0.1 0 1
particle dust{scale:1,color:[1.000,0.600,0.000]} ^ ^ ^ 0.2 0.2 0.2 0 1

execute if block ^ ^ ^ air positioned ~ ~-1 ~ as @a[distance=..2,tag=mg.flw] run damage @s 18 minecraft:magic by @n[tag=boss_sh_loc,distance=0..]

execute if block ^ ^ ^ air positioned ^ ^ ^0.1 run function boss:6/shellbeam/ray
