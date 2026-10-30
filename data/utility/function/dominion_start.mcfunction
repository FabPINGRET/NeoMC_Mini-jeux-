scoreboard players set @s shortray 0
execute as @s at @s run playsound minecraft:item.lodestone_compass.lock player @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute as @s at @s run playsound minecraft:block.note_block.chime player @a[tag=mg.flw] ~ ~ ~ 0.2 0.6
execute as @s at @s run playsound minecraft:block.bubble_column.whirlpool_inside player @a[tag=mg.flw] ~ ~ ~ 0.5 0.1
execute as @s at @s anchored eyes positioned ~ ~1.3 ~ run function utility:dominion_ray
