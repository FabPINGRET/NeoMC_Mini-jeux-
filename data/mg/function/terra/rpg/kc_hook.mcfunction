# @s a abattu un carnotaure : quête du vulcanologue (sur le volcan)
scoreboard players operation $b mg.st = @s mg.trsa
scoreboard players operation $b mg.st /= #p3 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 if score @s mg.trrg matches 4 run scoreboard players add @s mg.trq4 1
execute if score $b mg.st matches 1 if score @s mg.trrg matches 4 run tellraw @s [{"text":"🌋 Gardiens de cendre : ","color":"gold"},{"score":{"name":"@s","objective":"mg.trq4"},"color":"yellow"},{"text":" / 3","color":"yellow"}]
