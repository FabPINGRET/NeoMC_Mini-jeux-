# @s a tué un joueur
scoreboard players add @s mg.gta 100
title @s actionbar [{"text":"+100 $ ","color":"green","bold":true},{"text":"joueur éliminé","color":"gray"}]
execute at @s run playsound minecraft:block.note_block.bit player @s ~ ~ ~ 0.7 1.6
scoreboard players set @s mg.gal 40
scoreboard players remove @s mg.gkp 1
execute if score @s mg.gkp matches 1.. run function mg:gta/kill_player
