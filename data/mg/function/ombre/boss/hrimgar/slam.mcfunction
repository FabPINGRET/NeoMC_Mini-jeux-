# Hrimgar, le géant du givre : slam
particle minecraft:explosion ~ ~0.5 ~ 3 0.2 3 0 12
particle minecraft:block{block_state:"minecraft:packed_ice"} ~ ~0.3 ~ 4 0.2 4 0 120
playsound minecraft:entity.generic.explode hostile @a ~ ~ ~ 1.5 0.5
scoreboard players set @s mg.olat 10
execute as @a[tag=mg.olw,gamemode=adventure,distance=..6] run damage @s 12 minecraft:mob_attack by @e[tag=mg.olb_hrimgar,limit=1]
effect give @a[tag=mg.olw,gamemode=adventure,distance=..6] minecraft:levitation 1 2 true
