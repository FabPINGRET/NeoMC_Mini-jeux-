# @s a fait un ou plusieurs kills : +10 pièces chacun, série, petit soin
scoreboard players operation $k mg.st = @s mg.pkc
scoreboard players reset @s mg.pkc
scoreboard players operation @s mg.pks += $k mg.st
scoreboard players operation $g mg.st = $k mg.st
scoreboard players set #10 mg.st 10
scoreboard players operation $g mg.st *= #10 mg.st
scoreboard players operation @s mg.pco += $g mg.st
effect give @s minecraft:regeneration 3 1 true
playsound minecraft:entity.player.levelup master @s ~ ~ ~ 0.7 1.6
title @s actionbar [{"text":"⚔ Kill ! ","color":"red","bold":true},{"text":"+","color":"gold"},{"score":{"name":"$g","objective":"mg.st"},"color":"yellow"},{"text":" 💰","color":"gold"}]
execute if score @s mg.pks matches 3 run function mg:pvpc/streak {n:3,b:15,t:"est en série"}
execute if score @s mg.pks matches 5 run function mg:pvpc/streak {n:5,b:30,t:"est déchaîné"}
execute if score @s mg.pks matches 10 run function mg:pvpc/streak {n:10,b:80,t:"est IMBATTABLE"}
