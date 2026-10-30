# yellow, purple, green, red, blue

execute unless score wm_kitchen Value matches 1 run setblock -11094 77 -185 minecraft:redstone_block
execute if score wm_kitchen Value matches 1 run playsound minecraft:block.note_block.bit master @a[tag=mg.flw] ~ ~2 ~ 1 1
execute if score wm_kitchen Value matches 1 run fill -11074 79 -189 -11074 80 -189 minecraft:purple_wool

execute if score wm_kitchen Value matches 1 run scoreboard players set wm_kitchen Value 2
