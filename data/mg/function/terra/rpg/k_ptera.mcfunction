# @s a abattu : ptéranodon
scoreboard players operation $kk mg.st = @s mg.tkptera
scoreboard players set @s mg.tkptera 0
scoreboard players operation @s mg.trai += $kk mg.st
function mg:terra/rpg/xpk {n:25}
title @s actionbar [{"text":"+1 aile ","color":"aqua"},{"text":"ptéranodon abattu","color":"gray"}]
scoreboard players set @s mg.tval 30
scoreboard players add @s mg.tvc 15
