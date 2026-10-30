particle dust{color:[1.000,0.467,0.000],scale:1} ^ ^ ^ 0.2 0.2 0.2 0 1

execute if block ^ ^ ^ air as @a[distance=..1.5,tag=mg.flw] run damage @s 16 minecraft:falling_anvil

execute if block ^ ^ ^ air positioned ^ ^ ^0.1 run function boss:mini/zalvorn/pumpkin_ray
