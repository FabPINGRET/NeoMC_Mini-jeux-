# @s = joueur qui franchit son prochain point de passage
scoreboard players add @s mg.cp 1
execute at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 1 1.6
execute if score @s mg.cp matches 1..9 run title @s actionbar [{"text":"⚑ Point de passage ","color":"aqua"},{"score":{"name":"@s","objective":"mg.cp"},"color":"yellow"},{"text":" / 10","color":"gray"}]
execute if score @s mg.cp matches 10.. run function mg:icerace/lap_done
function mg:icerace/progress
