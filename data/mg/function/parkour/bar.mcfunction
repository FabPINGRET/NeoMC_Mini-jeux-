# Barre d'action du coureur (@s)
scoreboard players operation $t mg.st = @s mg.ppt
execute if score $t mg.st matches ..-1 run scoreboard players set $t mg.st 0
scoreboard players operation $s mg.st = $t mg.st
scoreboard players operation $s mg.st /= $pk20 mg.st
scoreboard players operation $d mg.st = $t mg.st
scoreboard players operation $d mg.st %= $pk20 mg.st
scoreboard players operation $d mg.st /= $pk2 mg.st
title @s actionbar [{"text":"⏱ ","color":"green"},{"score":{"name":"$s","objective":"mg.st"},"color":"white","bold":true},{"text":".","color":"white"},{"score":{"name":"$d","objective":"mg.st"},"color":"white"},{"text":" s   ","color":"gray"},{"text":"Checkpoint ","color":"gray"},{"score":{"name":"@s","objective":"mg.ppc"},"color":"aqua"},{"text":"/3   ","color":"gray"},{"text":"Chutes ","color":"gray"},{"score":{"name":"@s","objective":"mg.ppf"},"color":"red"}]
