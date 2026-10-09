# @s a tué un policier : +25 $, une étoile de plus
scoreboard players add @s mg.gta 25
title @s actionbar [{"text":"+25 $ ","color":"aqua","bold":true},{"text":"policier abattu","color":"gray"}]
execute at @s run playsound minecraft:block.note_block.bit player @s ~ ~ ~ 0.7 1.6
scoreboard players set @s mg.gal 40
scoreboard players reset @s mg.gks
scoreboard players reset @s mg.gkw
function mg:gta/wanted_up
