# @s a abattu : dilophosaure
scoreboard players operation $kk mg.st = @s mg.tkdilo
scoreboard players set @s mg.tkdilo 0
scoreboard players operation @s mg.trvn += $kk mg.st
function mg:terra/rpg/xpk {n:20}
title @s actionbar [{"text":"+1 glande à venin ","color":"green"},{"text":"dilophosaure abattu","color":"gray"}]
scoreboard players set @s mg.tval 30
scoreboard players add @s mg.tvc 15
