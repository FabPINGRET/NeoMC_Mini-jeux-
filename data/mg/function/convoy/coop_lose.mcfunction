# Coop : convoi détruit ou trop lent
kill @e[tag=mg.cvm]
scoreboard players set $state mg.st 3
scoreboard players set $timer mg.st 60
title @a[tag=!mg.surv] title {"text":"CONVOI PERDU...","color":"dark_red","bold":true}
tellraw @a [{"text":"☠ Le convoi s'est arrêté à ","color":"gray"},{"score":{"name":"$cvp","objective":"mg.st"},"color":"red","bold":true},{"text":" blocs sur 120.","color":"gray"}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.wither.death master @s ~ ~ ~ 0.5 0.8
