execute as @n[tag=fs_bot_writer,tag=1,distance=0..] at @s run fill ~ ~ ~ ~ ~1 ~ purple_concrete_powder
execute as @n[tag=fs_bot_writer,tag=1,distance=0..] at @s run setblock ~1 ~1 ~ minecraft:purple_wall_banner[facing=east]{patterns:[{color:"white",pattern:"minecraft:piglin"}]}
execute as @n[tag=fs_bot_writer,tag=1,distance=0..] at @s run tp @s ~ ~ ~-1
