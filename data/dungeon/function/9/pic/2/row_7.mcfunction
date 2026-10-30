# GENERAL
execute if block ~ ~1 ~ coal_block run setblock ~ ~1 ~ red_wool
execute if block ~ ~1 ~ smooth_quartz run setblock ~ ~1 ~ coal_block
execute if block ~ ~1 ~ red_wool run setblock ~ ~1 ~ smooth_quartz

# ROW SPECIFIC
clone ~ ~1 ~ ~ ~1 ~ ~ 96 -141 replace

# WIN CHECK
execute if blocks -11019 52 -141 -11013 58 -141 -11019 96 -141 all run setblock -11012 53 -141 minecraft:redstone_block
