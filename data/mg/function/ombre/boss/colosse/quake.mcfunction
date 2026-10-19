# Le Colosse de runes : quake
particle minecraft:explosion ~ ~0.5 ~ 4 0.3 4 0 16 force
particle minecraft:block{block_state:"minecraft:deepslate_tiles"} ~ ~0.3 ~ 6 0.2 6 0 200 force
playsound minecraft:entity.iron_golem.damage hostile @a ~ ~ ~ 2 0.4
playsound minecraft:entity.generic.explode hostile @a ~ ~ ~ 1.5 0.5
execute as @a[tag=mg.olw,gamemode=adventure,distance=..8] run damage @s 14 minecraft:mob_attack by @e[tag=mg.olb_colosse,limit=1]
effect give @a[tag=mg.olw,gamemode=adventure,distance=..8] minecraft:levitation 1 3 true
