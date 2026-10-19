# @s touche la pierre « Havreclair »
execute in mg:ombrelune run spawnpoint @s 7 65 6
scoreboard players operation $b mg.st = @s mg.olws
scoreboard players operation $b mg.st /= #p0 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return 0
scoreboard players operation @s mg.olws += #p0 mg.st
tellraw @s [{"text":"🌀 Pierre d'appel éveillée : ","color":"light_purple"},{"text":"Havreclair","color":"yellow","bold":true},{"text":" (voyage et réapparition)","color":"gray"}]
execute at @s run playsound minecraft:block.respawn_anchor.charge player @s ~ ~ ~ 1 1.2
