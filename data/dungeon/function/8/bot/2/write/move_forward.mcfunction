execute as @n[tag=fs_bot_writer,tag=2,distance=0..] at @s run fill ~ ~ ~ ~ ~1 ~ red_concrete_powder
execute as @n[tag=fs_bot_writer,tag=2,distance=0..] at @s run setblock ~1 ~1 ~ minecraft:red_wall_banner[facing=east]{patterns:[{color:"white",pattern:"minecraft:stripe_center"},{color:"white",pattern:"minecraft:square_top_left"},{color:"white",pattern:"minecraft:square_top_right"},{color:"red",pattern:"minecraft:curly_border"}]}
execute as @n[tag=fs_bot_writer,tag=2,distance=0..] at @s run tp @s ~ ~ ~-1
