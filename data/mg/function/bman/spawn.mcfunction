# @s : numéro (mg.yid) et case de départ
scoreboard players add $yk mg.st 1
scoreboard players operation @s mg.yid = $yk mg.st
execute if score $ym mg.st matches 0 run return run function mg:bman/sp_solo
execute if entity @s[team=mg_red] run return run function mg:bman/sp_red
function mg:bman/sp_blue
