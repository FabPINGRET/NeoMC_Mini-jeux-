# square, diamond, triangle, heart, circle

playsound minecraft:block.note_block.banjo master @a[tag=mg.flw] -10993 109 -169 1 1
execute positioned -10993 109 -169 run tellraw @a[distance=..10,tag=mg.flw] {"text":"▲","color":"#44BBFF"}

execute unless score wm_roof Value matches 2 run scoreboard players set wm_roof Value 0
execute if score wm_roof Value matches 2 run scoreboard players set wm_roof Value 3
