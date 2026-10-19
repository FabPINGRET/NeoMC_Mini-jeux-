# @s rend « Les mines profondes »
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p13 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run return run tellraw @s {"text":"Accepte d'abord la quête.","color":"gray"}
scoreboard players operation $b mg.st = @s mg.oldg
scoreboard players operation $b mg.st /= #p6 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run return run tellraw @s {"text":"Le donjon n'est pas encore terminé.","color":"red"}
scoreboard players operation @s mg.olsa -= #p13 mg.st
scoreboard players operation @s mg.olsd += #p13 mg.st
scoreboard players add @s mg.olg 1000
function mg:ombre/xp {n:1700}
title @s times 5 40 10
title @s title {"text":"✔ Les mines profondes","color":"yellow","bold":true}
title @s subtitle {"text":"1700 XP, 1000 💰, 1 gemme (+1 point)","color":"gray"}
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1.1
scoreboard players add @s mg.olsp 1
