execute as @e[tag=frostbyte_head_screen,distance=0..] run data modify entity @s block_state.Name set value "minecraft:diamond_block"
execute as @e[tag=frostbyte_draw_ice,distance=0..] run data modify entity @s block_state.Name set value "minecraft:ice"
execute as @e[tag=frostbyte_draw_horns,distance=0..] run data modify entity @s block_state.Name set value "minecraft:light_blue_glazed_terracotta"
