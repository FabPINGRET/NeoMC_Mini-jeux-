# @s touche la pierre « Bastion des Braises »
execute in mg:ombrelune run spawnpoint @s 145 67 114
scoreboard players operation $b mg.st = @s mg.olws
scoreboard players operation $b mg.st /= #p6 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return 0
scoreboard players operation @s mg.olws += #p6 mg.st
tellraw @s [{"text":"🌀 Pierre d'appel éveillée : ","color":"light_purple"},{"text":"Bastion des Braises","color":"yellow","bold":true},{"text":" (voyage et réapparition)","color":"gray"}]
execute at @s run playsound minecraft:block.respawn_anchor.charge player @s ~ ~ ~ 1 1.2
