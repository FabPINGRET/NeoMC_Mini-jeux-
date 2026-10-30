# yellow, purple, green, red, blue

execute unless score wm_kitchen Value matches 2 run setblock -11094 77 -185 minecraft:redstone_block
execute if score wm_kitchen Value matches 2 run playsound minecraft:block.note_block.bit master @a[tag=mg.flw] ~ ~2 ~ 1 1.2
execute if score wm_kitchen Value matches 2 run fill -11082 79 -189 -11082 80 -189 minecraft:lime_wool

execute if score wm_kitchen Value matches 2 run scoreboard players set wm_kitchen Value 3
