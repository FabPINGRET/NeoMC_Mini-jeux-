# @s voyage vers Bastion des Braises
scoreboard players operation $b mg.st = @s mg.olws
scoreboard players operation $b mg.st /= #p6 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run return run tellraw @s {"text":"🌀 La pierre « Bastion des Braises » n'est pas encore éveillée : va la toucher.","color":"red"}
execute if entity @s[tag=mg.olboss_in] run return run tellraw @s {"text":"Impossible pendant un combat de boss.","color":"red"}
execute in mg:ombrelune run tp @s 145.5 67 114.5
execute in mg:ombrelune run spawnpoint @s 145 67 114
execute at @s run playsound minecraft:entity.enderman.teleport player @a ~ ~ ~ 0.7 1.2
execute at @s run particle minecraft:reverse_portal ~ ~1 ~ 0.4 0.9 0.4 0.05 60
