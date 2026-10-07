# @s atterrit dans l'eau en premier : il gagne la manche
execute unless score $dcph mg.st matches 1 run return 0
scoreboard players add @s mg.dpw 1
scoreboard players set $dcph mg.st 2
scoreboard players set $dct mg.st 0
execute at @s run particle minecraft:splash ~ ~ ~ 0.5 0.5 0.5 0.2 80
title @a[tag=!mg.surv] title [{"selector":"@s","color":"gold","bold":true}]
title @a[tag=!mg.surv] subtitle [{"text":"remporte la manche !","color":"yellow"}]
tellraw @a[tag=!mg.surv] [{"text":"⬇ ","color":"aqua"},{"selector":"@s","color":"gold","bold":true},{"text":" gagne la manche (","color":"gray"},{"score":{"name":"@s","objective":"mg.dpw"},"color":"yellow"},{"text":"/3)","color":"gray"}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 1.2
execute if score @s mg.dpw matches 3.. run function mg:core/win_player
