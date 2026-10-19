# @s rend « Runite pour la forge »
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p12 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run return run tellraw @s {"text":"Accepte d'abord la quête.","color":"gray"}
execute unless score @s mg.olm7 matches 8.. run return run tellraw @s {"text":"Il en faut 8.","color":"red"}
scoreboard players remove @s mg.olm7 8
scoreboard players operation @s mg.olsa -= #p12 mg.st
scoreboard players operation @s mg.olsd += #p12 mg.st
scoreboard players add @s mg.olg 800
function mg:ombre/xp {n:1300}
title @s times 5 40 10
title @s title {"text":"✔ Runite pour la forge","color":"yellow","bold":true}
title @s subtitle {"text":"1300 XP, 800 💰, 1 gemme (+1 point)","color":"gray"}
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1.1
scoreboard players add @s mg.olsp 1
