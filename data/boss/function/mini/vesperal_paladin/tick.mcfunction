execute as @e[tag=vesperal_spike,tag=main,distance=0..] at @s if block ~ ~-1 ~ air run tp @s ~ ~ ~ ~5 ~

execute as @n[tag=vesperal_spike_pos,tag=1,distance=0..] at @s run tp @n[tag=vesperal_spike,tag=1,distance=0..] ~ ~ ~
execute as @n[tag=vesperal_spike_pos,tag=2,distance=0..] at @s run tp @n[tag=vesperal_spike,tag=2,distance=0..] ~ ~ ~
execute as @n[tag=vesperal_spike_pos,tag=3,distance=0..] at @s run tp @n[tag=vesperal_spike,tag=3,distance=0..] ~ ~ ~
execute as @n[tag=vesperal_spike_pos,tag=4,distance=0..] at @s run tp @n[tag=vesperal_spike,tag=4,distance=0..] ~ ~ ~
execute as @n[tag=vesperal_spike_pos,tag=5,distance=0..] at @s run tp @n[tag=vesperal_spike,tag=5,distance=0..] ~ ~ ~

execute as @e[tag=vesperal_spike_pos,tag=!grounded,distance=0..] at @s unless block ~ ~-0.1 ~ air run function boss:mini/vesperal_paladin/ground_spike
execute as @e[tag=vesperal_spike_pos,tag=grounded,distance=0..] at @s positioned ~ ~10 ~ unless entity @e[tag=mooneye,distance=..3] as @s at @s run function boss:mini/vesperal_paladin/break_spike

execute as @e[type=arrow,distance=0..] run data merge entity @s {pickup:1b}

execute if entity @p[nbt={Inventory:[{id:"minecraft:arrow",components:{"minecraft:intangible_projectile":{}}}]},tag=mg.flw] run tag @s add intangible_arrow
clear @a[tag=intangible_arrow,tag=mg.flw] arrow[intangible_projectile={}] 1
give @a[tag=intangible_arrow,tag=mg.flw] arrow 1
tag @a[tag=mg.flw] remove intangible_arrow
