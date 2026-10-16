# @s découvre « Colonie Terra Nova »
scoreboard players operation $b mg.st = @s mg.trpo
scoreboard players operation $b mg.st /= #p0 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return 0
scoreboard players operation @s mg.trpo += #p0 mg.st
scoreboard players operation $b mg.st = @s mg.trtv
scoreboard players operation $b mg.st /= #p0 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run scoreboard players operation @s mg.trtv += #p0 mg.st
execute in mg:terranova run spawnpoint @s 0 65 4
tellraw @s [{"text":"🌀 Balise de voyage activée : ","color":"light_purple"},{"text":"Colonie","color":"yellow"},{"text":" (réapparition ici, voyage depuis n'importe quelle balise)","color":"gray"}]
