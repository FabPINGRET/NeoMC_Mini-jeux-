# square, diamond, triangle, heart, circle

playsound minecraft:block.note_block.banjo master @a[tag=mg.flw] -11051 109 -37 1 1
execute positioned -11051 109 -37 run tellraw @a[distance=..10,tag=mg.flw] {"text":"■","color":"#44BBFF"}

scoreboard players set wm_roof Value 1
