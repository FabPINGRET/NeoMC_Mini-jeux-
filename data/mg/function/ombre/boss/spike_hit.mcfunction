particle minecraft:block{block_state:"minecraft:blue_ice"} ~ ~1 ~ 0.4 1 0.4 0 40 force
playsound minecraft:block.glass.break hostile @a ~ ~ ~ 1 0.6
execute as @a[tag=mg.olw,gamemode=adventure,distance=..2] run damage @s 10 minecraft:freeze
effect give @a[tag=mg.olw,gamemode=adventure,distance=..2] minecraft:levitation 1 5 true
kill @s
