# @s rend « Le puits des âmes »
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p15 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run return run tellraw @s {"text":"Accepte d'abord la quête.","color":"gray"}
scoreboard players operation $b mg.st = @s mg.oldg
scoreboard players operation $b mg.st /= #p7 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run return run tellraw @s {"text":"Le donjon n'est pas encore terminé.","color":"red"}
scoreboard players operation @s mg.olsa -= #p15 mg.st
scoreboard players operation @s mg.olsd += #p15 mg.st
scoreboard players add @s mg.olg 1200
function mg:ombre/xp {n:2000}
title @s times 5 40 10
title @s title {"text":"✔ Le puits des âmes","color":"yellow","bold":true}
title @s subtitle {"text":"2000 XP, 1200 💰, 1 gemme (+1 point)","color":"gray"}
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1.1
scoreboard players add @s mg.olsp 1
