# Tout le monde est tombé
kill @e[tag=mg.zz]
scoreboard players set $state mg.st 3
scoreboard players set $timer mg.st 80
title @a[tag=!mg.surv] title {"text":"GAME OVER","color":"dark_red","bold":true}
title @a[tag=!mg.surv] subtitle [{"text":"Tombés à la manche ","color":"gray"},{"score":{"name":"$zr","objective":"mg.st"},"color":"red","bold":true}]
tellraw @a [{"text":"☠ Les zombies ont envahi le bunker à la manche ","color":"gray"},{"score":{"name":"$zr","objective":"mg.st"},"color":"red","bold":true}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.wither.death master @s ~ ~ ~ 0.5 0.8
