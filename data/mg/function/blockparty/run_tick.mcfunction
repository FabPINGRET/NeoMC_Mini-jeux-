# Compte à rebours de la manche
function mg:blockparty/music_tick
scoreboard players remove $bt mg.st 1
scoreboard players operation $sec mg.st = $bt mg.st
scoreboard players add $sec mg.st 19
scoreboard players operation $sec mg.st /= $c20 mg.st
title @a[tag=mg.play] actionbar [{"text":"Manche ","color":"gray"},{"score":{"name":"$rd","objective":"mg.st"},"color":"light_purple","bold":true},{"text":" — ","color":"gray"},{"score":{"name":"$sec","objective":"mg.st"},"color":"yellow","bold":true},{"text":" s","color":"gray"}]
execute if score $bt mg.st matches 60 as @a at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1
execute if score $bt mg.st matches 40 as @a at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.3
execute if score $bt mg.st matches 20 as @a at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.6
execute if score $bt mg.st matches ..0 run function mg:blockparty/strip_now
