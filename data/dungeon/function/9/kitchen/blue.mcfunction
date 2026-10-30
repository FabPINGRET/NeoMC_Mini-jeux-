# yellow, purple, green, red, blue

execute unless score wm_kitchen Value matches 4 run setblock -11094 77 -185 minecraft:redstone_block
execute if score wm_kitchen Value matches 4 run playsound minecraft:zelda.secret master @a[tag=mg.flw] -11082 80 -189 1 1 1
execute if score wm_kitchen Value matches 4 run fill -11078 79 -189 -11078 80 -189 minecraft:blue_wool

execute if score wm_kitchen Value matches 4 run scoreboard players set wm_kitchen Value 5
execute if score wm_kitchen Value matches 5 run fill -11074 79 -188 -11090 79 -188 light[level=15] replace minecraft:stone_button
