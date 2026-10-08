# Arrivée (@s) : temps, record du serveur (mode 1), victoire
scoreboard players operation $es mg.st = $skt mg.st
scoreboard players operation $es mg.st /= #20 mg.st
scoreboard players operation $ecs mg.st = $skt mg.st
scoreboard players operation $ecs mg.st %= #20 mg.st
scoreboard players operation $ecs mg.st *= #5 mg.st
tag @s add mg.skf
effect give @s minecraft:slow_falling 30 0 true
title @s title [{"text":"🏁 Arrivée !","color":"gold","bold":true}]
execute if score $ecs mg.st matches ..9 run tellraw @a[tag=!mg.surv] [{"text":"🏁 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" boucle la course en ","color":"gray"},{"score":{"name":"$es","objective":"mg.st"},"color":"gold"},{"text":",","color":"gold"},{"text":"0","color":"gold"},{"score":{"name":"$ecs","objective":"mg.st"},"color":"gold"},{"text":" s","color":"gold"}]
execute if score $ecs mg.st matches 10.. run tellraw @a[tag=!mg.surv] [{"text":"🏁 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" boucle la course en ","color":"gray"},{"score":{"name":"$es","objective":"mg.st"},"color":"gold"},{"text":",","color":"gold"},{"score":{"name":"$ecs","objective":"mg.st"},"color":"gold"},{"text":" s","color":"gold"}]
execute unless score $skrec mg.st matches 1.. run scoreboard players set $skrec mg.st 999999
execute if score $elm mg.st matches 1 if score $skt mg.st < $skrec mg.st run function mg:sky/record
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. run effect give @a[tag=mg.play] minecraft:slow_falling 15 0 true
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. run return run function mg:core/win_player
tellraw @s [{"text":"(Mode test solo : menu → Arrêter pour finir)","color":"dark_gray","italic":true}]
