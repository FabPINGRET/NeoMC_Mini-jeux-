# square, diamond, triangle, heart, circle

playsound minecraft:block.note_block.banjo master @a[tag=mg.flw] -11032 109 -109 1 1
execute positioned -11032 109 -109 run tellraw @a[distance=..10,tag=mg.flw] {"text":"●","color":"#44BBFF"}

execute unless score wm_roof Value matches 4 run scoreboard players set wm_roof Value 0
execute if score wm_roof Value matches 4 run scoreboard players set wm_roof Value 5
execute if score wm_roof Value matches 5 run setblock -11040 107 -107 minecraft:redstone_block
