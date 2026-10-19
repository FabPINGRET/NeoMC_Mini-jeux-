# @s rend « Le temple englouti »
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p7 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run return run tellraw @s {"text":"Accepte d'abord la quête.","color":"gray"}
scoreboard players operation $b mg.st = @s mg.oldg
scoreboard players operation $b mg.st /= #p3 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run return run tellraw @s {"text":"Le donjon n'est pas encore terminé.","color":"red"}
scoreboard players operation @s mg.olsa -= #p7 mg.st
scoreboard players operation @s mg.olsd += #p7 mg.st
scoreboard players add @s mg.olg 600
function mg:ombre/xp {n:1000}
title @s times 5 40 10
title @s title {"text":"✔ Le temple englouti","color":"yellow","bold":true}
title @s subtitle {"text":"1000 XP, 600 💰, 1 gemme (+1 point)","color":"gray"}
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1.1
scoreboard players add @s mg.olsp 1
