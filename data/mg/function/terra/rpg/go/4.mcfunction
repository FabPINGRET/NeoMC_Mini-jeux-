# @s voyage vers Belvédère
scoreboard players operation $b mg.st = @s mg.trtv
scoreboard players operation $b mg.st /= #p3 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run return run tellraw @s {"text":"🌀 Balise « Belvédère » pas encore activée : va la découvrir à pied.","color":"red"}
execute if entity @s[tag=mg.tvcar] run return run tellraw @s {"text":"📦 Impossible avec la caisse !","color":"red"}
execute in mg:terranova run tp @s -139.5 81 62.5
execute in mg:terranova run spawnpoint @s -139 81 62
execute at @s run playsound minecraft:entity.enderman.teleport player @a ~ ~ ~ 0.7 1.2
execute at @s run particle minecraft:reverse_portal ~ ~1 ~ 0.4 0.9 0.4 0.05 60
