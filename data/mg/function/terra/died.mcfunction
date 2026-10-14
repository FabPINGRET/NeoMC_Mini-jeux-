# @s est mort à Terra Nova (inventaire gardé) : -10 % de crédits, caisse lâchée
scoreboard players set @s mg.deaths 0
scoreboard players set #10 mg.st 10
execute if entity @s[tag=mg.tvcar] run function mg:terra/crate_drop
scoreboard players operation $tvl mg.st = @s mg.tvc
scoreboard players operation $tvl mg.st /= #10 mg.st
scoreboard players operation @s mg.tvc -= $tvl mg.st
scoreboard players set @s mg.tvhm 0
scoreboard players set @s mg.tvh 0
tag @s remove mg.tvoh
title @s times 5 40 15
title @s title {"text":"☠ DÉVORÉ","color":"dark_red","bold":true}
title @s subtitle [{"text":"Frais d'infirmerie : -","color":"gray"},{"score":{"name":"$tvl","objective":"mg.st"},"color":"red"},{"text":" ₵","color":"red"}]
