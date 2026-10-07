# Chrono et progression (@s)
scoreboard players operation $es mg.st = @s mg.et
scoreboard players operation $es mg.st /= #20 mg.st
scoreboard players operation $ecs mg.st = @s mg.et
scoreboard players operation $ecs mg.st %= #20 mg.st
scoreboard players operation $ecs mg.st *= #5 mg.st
execute if score $ecs mg.st matches ..9 run title @s actionbar [{"text":"⏱ ","color":"aqua"},{"score":{"name":"$es","objective":"mg.st"},"color":"white"},{"text":",","color":"white"},{"text":"0","color":"white"},{"score":{"name":"$ecs","objective":"mg.st"},"color":"white"},{"text":" s   ◎ ","color":"gray"},{"score":{"name":"@s","objective":"mg.ec"},"color":"aqua"},{"text":"/8","color":"gray"}]
execute if score $ecs mg.st matches 10.. run title @s actionbar [{"text":"⏱ ","color":"aqua"},{"score":{"name":"$es","objective":"mg.st"},"color":"white"},{"text":",","color":"white"},{"score":{"name":"$ecs","objective":"mg.st"},"color":"white"},{"text":" s   ◎ ","color":"gray"},{"score":{"name":"@s","objective":"mg.ec"},"color":"aqua"},{"text":"/8","color":"gray"}]
