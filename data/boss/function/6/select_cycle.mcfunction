execute if score boss:sh_state Value matches 0 positioned -10486 41 -71 run function boss:6/cycle_normal
# PHASE 1 DAMAGED
execute if score boss:sh_state Value matches 1 run setblock -10473 42 -56 minecraft:redstone_block
# MID-FIGHT CUTSCENE
execute if score boss:sh_state Value matches 2 run setblock -10502 42 -98 minecraft:redstone_block
# PHASE 2 DAMAGED
execute if score boss:sh_state Value matches 3 run setblock -10502 42 -58 minecraft:redstone_block
# PURSUE SLIME MAN
execute if score boss:sh_state Value matches 4 run setblock -10502 42 -61 minecraft:redstone_block
execute if score boss:sh_state Value matches 5 run setblock -10502 42 -66 minecraft:redstone_block
