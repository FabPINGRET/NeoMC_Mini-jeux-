# square, diamond, triangle, heart, circle

playsound minecraft:block.note_block.banjo master @a[tag=mg.flw] -11088 95 -187 1 1
execute positioned -11088 95 -187 run tellraw @a[distance=..10,tag=mg.flw] {"text":"◆","color":"#44BBFF"}

execute unless score wm_roof Value matches 1 run scoreboard players set wm_roof Value 0
execute if score wm_roof Value matches 1 run scoreboard players set wm_roof Value 2
