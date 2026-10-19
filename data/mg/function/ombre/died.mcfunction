# @s est tombé (inventaire gardé) : -10 % d'or, réapparition à la dernière pierre d'appel
scoreboard players set @s mg.deaths 0
scoreboard players operation $l mg.st = @s mg.olg
scoreboard players operation $l mg.st /= #10 mg.st
scoreboard players operation @s mg.olg -= $l mg.st
scoreboard players operation @s mg.olmp = @s mg.olmm
function mg:ombre/mana_bar
title @s times 5 40 15
title @s title {"text":"☠ TU ES TOMBÉ","color":"dark_red","bold":true}
title @s subtitle [{"text":"Le temple a pris ","color":"gray"},{"score":{"name":"$l","objective":"mg.st"},"color":"gold"},{"text":" 💰 pour te ranimer","color":"gray"}]
