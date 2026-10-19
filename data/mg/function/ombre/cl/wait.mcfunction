$scoreboard players operation $s mg.st = @s mg.olc$(s)
scoreboard players add $s mg.st 19
scoreboard players operation $s mg.st /= #20 mg.st
scoreboard players set @s mg.olal 20
title @s actionbar [{"text":"⏳ Compétence prête dans ","color":"gray"},{"score":{"name":"$s","objective":"mg.st"},"color":"yellow","bold":true},{"text":" s","color":"gray"}]
playsound minecraft:block.dispenser.fail player @s ~ ~ ~ 0.4 1.6
