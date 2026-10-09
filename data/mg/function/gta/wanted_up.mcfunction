# @s : une étoile de plus (5 max), 20 s avant de redescendre
execute if score @s mg.gwl matches ..4 run scoreboard players add @s mg.gwl 1
scoreboard players set @s mg.gwt 400
team leave @s
execute at @s run playsound minecraft:block.note_block.pling player @s ~ ~ ~ 0.8 0.6
execute at @s run playsound minecraft:block.note_block.bell player @s ~ ~ ~ 0.6 1.8
