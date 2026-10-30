fill ~ ~1 ~ ~ ~1 ~ cyan_wool replace minecraft:black_wool
fill ~ ~1 ~ ~ ~1 ~ black_wool replace minecraft:purple_wool
fill ~ ~1 ~ ~ ~1 ~ purple_wool replace minecraft:blue_wool
fill ~ ~1 ~ ~ ~1 ~ blue_wool replace minecraft:lime_wool
fill ~ ~1 ~ ~ ~1 ~ lime_wool replace minecraft:yellow_wool
fill ~ ~1 ~ ~ ~1 ~ yellow_wool replace minecraft:orange_wool
fill ~ ~1 ~ ~ ~1 ~ orange_wool replace minecraft:red_wool
fill ~ ~1 ~ ~ ~1 ~ red_wool replace minecraft:white_wool
fill ~ ~1 ~ ~ ~1 ~ white_wool replace minecraft:cyan_wool

execute if block ~ ~1 ~ minecraft:red_wool run data modify entity @n[type=minecraft:item_frame,distance=0..] Item set from block 9985 35 229 Items[0]
execute if block ~ ~1 ~ minecraft:orange_wool run data modify entity @n[type=minecraft:item_frame,distance=0..] Item set from block 9985 35 229 Items[1]
execute if block ~ ~1 ~ minecraft:yellow_wool run data modify entity @n[type=minecraft:item_frame,distance=0..] Item set from block 9985 35 229 Items[2]
execute if block ~ ~1 ~ minecraft:lime_wool run data modify entity @n[type=minecraft:item_frame,distance=0..] Item set from block 9985 35 229 Items[3]
execute if block ~ ~1 ~ minecraft:blue_wool run data modify entity @n[type=minecraft:item_frame,distance=0..] Item set from block 9985 35 229 Items[4]
execute if block ~ ~1 ~ minecraft:purple_wool run data modify entity @n[type=minecraft:item_frame,distance=0..] Item set from block 9985 35 229 Items[5]
execute if block ~ ~1 ~ minecraft:black_wool run data modify entity @n[type=minecraft:item_frame,distance=0..] Item set from block 9985 35 229 Items[6]
execute if block ~ ~1 ~ minecraft:white_wool run data modify entity @n[type=minecraft:item_frame,distance=0..] Item set from block 9985 35 229 Items[7]

execute if block ~ ~1 ~ minecraft:red_wool run fill 9985 33 ~ 9991 33 ~ minecraft:red_stained_glass
execute if block ~ ~1 ~ minecraft:orange_wool run fill 9985 33 ~ 9991 33 ~ minecraft:orange_stained_glass
execute if block ~ ~1 ~ minecraft:yellow_wool run fill 9985 33 ~ 9991 33 ~ minecraft:yellow_stained_glass
execute if block ~ ~1 ~ minecraft:lime_wool run fill 9985 33 ~ 9991 33 ~ minecraft:lime_stained_glass
execute if block ~ ~1 ~ minecraft:blue_wool run fill 9985 33 ~ 9991 33 ~ minecraft:blue_stained_glass
execute if block ~ ~1 ~ minecraft:purple_wool run fill 9985 33 ~ 9991 33 ~ minecraft:purple_stained_glass
execute if block ~ ~1 ~ minecraft:black_wool run fill 9985 33 ~ 9991 33 ~ minecraft:black_stained_glass
execute if block ~ ~1 ~ minecraft:white_wool run fill 9985 33 ~ 9991 33 ~ minecraft:white_stained_glass
