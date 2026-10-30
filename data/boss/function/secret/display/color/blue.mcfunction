execute as @e[tag=sc_boss_model_body,tag=wool,distance=0..] run data modify entity @s block_state.Name set value "minecraft:blue_wool"

execute as @e[tag=sc_boss_model_head,tag=up,distance=0..] run data modify entity @s block_state.Name set value "minecraft:air"
execute as @e[tag=sc_boss_model_head,tag=down,distance=0..] run data modify entity @s block_state.Name set value "minecraft:crying_obsidian"
