execute as @n[tag=fs_bot_writer,tag=3,distance=0..] at @s run fill ~ ~ ~ ~ ~1 ~ blue_concrete_powder
execute as @n[tag=fs_bot_writer,tag=3,distance=0..] at @s run setblock ~1 ~1 ~ minecraft:blue_wall_banner[facing=east]{patterns:[{color:"white",pattern:"minecraft:circle"},{color:"blue",pattern:"minecraft:flower"}]}
execute as @n[tag=fs_bot_writer,tag=3,distance=0..] at @s run tp @s ~ ~ ~-1
