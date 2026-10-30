# GENERAL
execute if block ~ ~1 ~ coal_block run setblock ~ ~1 ~ red_wool
execute if block ~ ~1 ~ smooth_quartz run setblock ~ ~1 ~ coal_block
execute if block ~ ~1 ~ red_wool run setblock ~ ~1 ~ smooth_quartz

# ROW SPECIFIC
clone ~ ~1 ~ ~ ~1 ~ -11044 167 ~ replace

# WIN CHECK
execute if blocks -11044 54 -176 -11044 60 -170 -11044 166 -176 all run setblock -11044 55 -169 minecraft:redstone_block
