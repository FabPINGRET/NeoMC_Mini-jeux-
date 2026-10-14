# @s a tué un herbivore : braconnage, -25 ₵
scoreboard players set @s mg.tvkb 0
scoreboard players set @s mg.tvkg 0
scoreboard players remove @s mg.tvc 25
execute if score @s mg.tvc matches ..-1 run scoreboard players set @s mg.tvc 0
scoreboard players set @s mg.tval 50
title @s actionbar [{"text":"-25 ₵ ","color":"red","bold":true},{"text":"braconnage : les herbivores sont protégés","color":"gray"}]
