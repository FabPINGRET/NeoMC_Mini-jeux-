# yellow, purple, green, red, blue

execute unless score wm_kitchen Value matches 0 run setblock -11094 77 -185 minecraft:redstone_block
execute if score wm_kitchen Value matches 0 run playsound minecraft:block.note_block.bit master @a[tag=mg.flw] ~ ~2 ~ 1 0.8
execute if score wm_kitchen Value matches 0 run fill -11086 79 -189 -11086 80 -189 minecraft:yellow_wool

execute if score wm_kitchen Value matches 0 run scoreboard players set wm_kitchen Value 1
