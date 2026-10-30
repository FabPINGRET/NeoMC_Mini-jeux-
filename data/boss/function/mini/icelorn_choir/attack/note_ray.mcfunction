execute if score icelorn_overdrive bool matches 0 run particle note ~ ~ ~ 0.73 0 0 1 0
execute if score icelorn_overdrive bool matches 1 run particle note ~ ~ ~ 0.2 0 0 1 0

execute if block ^ ^ ^ air positioned ~ ~-1 ~ as @a[distance=..1.5,tag=mg.flw] run damage @s 16 minecraft:falling_anvil
execute if block ^ ^ ^ pale_moss_carpet positioned ~ ~-1 ~ as @a[distance=..1.5,tag=mg.flw] run damage @s 16 minecraft:falling_anvil

execute if block ^ ^ ^ air positioned ^ ^ ^0.5 run function boss:mini/icelorn_choir/attack/note_ray
execute if block ^ ^ ^ pale_moss_carpet positioned ^ ^ ^0.5 run function boss:mini/icelorn_choir/attack/note_ray
