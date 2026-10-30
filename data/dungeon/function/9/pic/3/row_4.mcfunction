# GENERAL
execute if block ~ ~1 ~ coal_block run setblock ~ ~1 ~ red_wool
execute if block ~ ~1 ~ smooth_quartz run setblock ~ ~1 ~ coal_block
execute if block ~ ~1 ~ red_wool run setblock ~ ~1 ~ smooth_quartz

# ROW SPECIFIC
clone ~ ~1 ~ ~ ~1 ~ ~ 54 -216 replace

# WIN CHECK
execute if blocks -11093 35 -216 -11087 41 -216 -11093 51 -216 all run setblock -11094 36 -216 minecraft:redstone_block
