execute if score wm_memory1 bool matches 1 run setblock -11103 46 -107 minecraft:redstone_block
execute if score wm_memory2 bool matches 1 run setblock -11103 46 -111 minecraft:redstone_block
execute if score wm_memory3 bool matches 1 run setblock -11103 42 -107 minecraft:redstone_block
execute if score wm_memory4 bool matches 1 run setblock -11103 42 -111 minecraft:redstone_block

execute if score wm_memory1 bool matches 1 if score wm_memory2 bool matches 1 if score wm_memory3 bool matches 1 if score wm_memory4 bool matches 1 run clone -11099 18 -115 -11097 35 -103 -11103 37 -115 replace
