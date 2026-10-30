# GENERAL
execute if block ~ ~1 ~ coal_block run setblock ~ ~1 ~ red_wool
execute if block ~ ~1 ~ smooth_quartz run setblock ~ ~1 ~ coal_block
execute if block ~ ~1 ~ red_wool run setblock ~ ~1 ~ smooth_quartz

# ROW SPECIFIC
clone ~ ~1 ~ ~ ~1 ~ -11112 70 ~ replace

# WIN CHECK
execute if blocks -11112 70 -51 -11112 74 -47 -11112 61 -51 all run setblock -11112 62 -46 minecraft:redstone_block
