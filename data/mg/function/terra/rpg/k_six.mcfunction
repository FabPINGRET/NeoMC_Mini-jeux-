# @s a abattu : renégat
scoreboard players operation $kk mg.st = @s mg.tksix
scoreboard players set @s mg.tksix 0
function mg:terra/rpg/xpk {n:20}
scoreboard players add @s mg.tvc 20
title @s actionbar [{"text":"+20 ₵ ","color":"green"},{"text":"renégat neutralisé","color":"gray"}]
scoreboard players set @s mg.tval 30
