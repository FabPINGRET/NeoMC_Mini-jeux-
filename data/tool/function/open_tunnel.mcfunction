execute as @n[tag=beacon_base,distance=0..] at @s run setblock ~ ~ ~ minecraft:iron_block
setblock ~ ~2 ~ air
fill ~ ~1 ~ ~ ~2 ~ air
playsound minecraft:block.rooted_dirt.break master @a[tag=mg.flw] ~ ~ ~ 1 0.1
playsound minecraft:block.packed_mud.break master @a[tag=mg.flw] ~ ~ ~ 1 1
playsound minecraft:item.shovel.flatten master @a[tag=mg.flw] ~ ~ ~ 2 0.7
playsound minecraft:ambient.cave master @a[tag=mg.flw] ~ ~ ~ 1 1
particle block{block_state:"minecraft:dirt"} ~ ~-2 ~ 0.5 1.5 0.5 0 150 force
setblock ~ ~ ~ polished_blackstone_pressure_plate
