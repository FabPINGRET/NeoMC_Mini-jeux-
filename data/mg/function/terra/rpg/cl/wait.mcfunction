scoreboard players operation $s mg.st = @s mg.trcd
scoreboard players add $s mg.st 19
scoreboard players set #20 mg.st 20
scoreboard players operation $s mg.st /= #20 mg.st
scoreboard players set @s mg.tval 20
title @s actionbar [{"text":"⏳ Capacité prête dans ","color":"gray"},{"score":{"name":"$s","objective":"mg.st"},"color":"yellow","bold":true},{"text":" s","color":"gray"}]
playsound minecraft:block.dispenser.fail player @s ~ ~ ~ 0.4 1.6
