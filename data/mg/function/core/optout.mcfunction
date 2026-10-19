# @s refuse la partie lancée par un admin (seulement pendant le compte à rebours) : renvoyé là où il était
execute unless score $state mg.st matches 1 run return run tellraw @s {"text":"Trop tard : la partie a commencé.","color":"gray"}
execute unless entity @s[tag=mg.play] run return 0
tag @s remove mg.play
execute in minecraft:overworld run function mg:core/reset_player
execute if entity @s[tag=mg.pulls] in minecraft:overworld run function mg:survie/enter
execute if entity @s[tag=mg.pullg] in minecraft:overworld run function mg:gta/enter
execute if entity @s[tag=mg.pullt] in minecraft:overworld run function mg:terra/enter
execute if entity @s[tag=mg.pullo] in minecraft:overworld run function mg:ombre/enter
tag @s remove mg.pulls
tag @s remove mg.pullg
tag @s remove mg.pullt
tag @s remove mg.pullo
execute if entity @s[tag=!mg.optq] run tellraw @s {"text":"✖ Tu ne participes pas à cette partie.","color":"gray"}
tag @s remove mg.optq
