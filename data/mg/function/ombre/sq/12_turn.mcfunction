# @s rend « La forge écarlate »
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p11 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run return run tellraw @s {"text":"Accepte d'abord la quête.","color":"gray"}
scoreboard players operation $b mg.st = @s mg.oldg
scoreboard players operation $b mg.st /= #p5 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run return run tellraw @s {"text":"Le donjon n'est pas encore terminé.","color":"red"}
scoreboard players operation @s mg.olsa -= #p11 mg.st
scoreboard players operation @s mg.olsd += #p11 mg.st
scoreboard players add @s mg.olg 800
function mg:ombre/xp {n:1400}
title @s times 5 40 10
title @s title {"text":"✔ La forge écarlate","color":"yellow","bold":true}
title @s subtitle {"text":"1400 XP, 800 💰, 1 gemme (+1 point)","color":"gray"}
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1.1
scoreboard players add @s mg.olsp 1
