# Atterrissage dans l'eau (@s = joueur) : seul le premier de la manche marque
execute unless score $dph mg.st matches 1 run return 0
scoreboard players add @s mg.dp 1
scoreboard players set $dph mg.st 2
scoreboard players set $dtm mg.st 100
title @a title [{"selector":"@s","color":"gold","bold":true}]
title @a subtitle [{"text":"remporte la manche !","color":"yellow"}]
tellraw @a [{"text":"[Dropper] ","color":"aqua","bold":true},{"selector":"@s","color":"gold"},{"text":" atterrit dans l'eau et gagne la manche ! (","color":"gray"},{"score":{"name":"@s","objective":"mg.dp"},"color":"gold"},{"text":" / 2)","color":"gray"}]
execute at @s run particle minecraft:splash ~ ~ ~ 0.5 0.5 0.5 0.2 80
execute as @a at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 1.2
execute if score @s mg.dp matches 2.. run function mg:core/win_player
