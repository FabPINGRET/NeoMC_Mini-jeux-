execute as @n[tag=fs_bot_writer,tag=3,distance=0..] at @s run fill ~ ~ ~ ~ ~1 ~ lime_concrete_powder
execute as @n[tag=fs_bot_writer,tag=3,distance=0..] at @s run setblock ~1 ~1 ~ minecraft:lime_wall_banner[facing=east]{patterns:[{color:"white",pattern:"minecraft:rhombus"},{color:"white",pattern:"minecraft:stripe_left"},{color:"lime",pattern:"minecraft:square_bottom_left"},{color:"white",pattern:"minecraft:stripe_left"},{color:"lime",pattern:"minecraft:square_top_left"},{color:"lime",pattern:"minecraft:border"}]}
execute as @n[tag=fs_bot_writer,tag=3,distance=0..] at @s run tp @s ~ ~ ~-1
