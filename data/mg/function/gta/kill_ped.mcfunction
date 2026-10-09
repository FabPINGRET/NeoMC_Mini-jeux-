# @s a tué un passant : +5 $, une étoile de plus
scoreboard players add @s mg.gta 5
title @s actionbar [{"text":"+5 $ ","color":"yellow","bold":true},{"text":"passant","color":"gray"}]
execute at @s run playsound minecraft:block.note_block.bit player @s ~ ~ ~ 0.7 1.6
scoreboard players set @s mg.gal 40
scoreboard players remove @s mg.gkv 1
function mg:gta/wanted_up
execute if score @s mg.gkv matches 1.. run function mg:gta/kill_ped
