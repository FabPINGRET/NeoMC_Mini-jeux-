# yellow, purple, green, red, blue

execute unless score wm_kitchen Value matches 3 run setblock -11094 77 -185 minecraft:redstone_block
execute if score wm_kitchen Value matches 3 run playsound minecraft:block.note_block.bit master @a[tag=mg.flw] ~ ~2 ~ 1 1.4
execute if score wm_kitchen Value matches 3 run fill -11090 79 -189 -11090 80 -189 minecraft:red_wool

execute if score wm_kitchen Value matches 3 run scoreboard players set wm_kitchen Value 4
