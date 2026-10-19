# @s rend « Cordes d'arc »
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p2 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run return run tellraw @s {"text":"Accepte d'abord la quête.","color":"gray"}
execute unless score @s mg.olm2 matches 8.. run return run tellraw @s {"text":"Il en faut 8.","color":"red"}
scoreboard players remove @s mg.olm2 8
scoreboard players operation @s mg.olsa -= #p2 mg.st
scoreboard players operation @s mg.olsd += #p2 mg.st
scoreboard players add @s mg.olg 250
function mg:ombre/xp {n:350}
title @s times 5 40 10
title @s title {"text":"✔ Cordes d'arc","color":"yellow","bold":true}
title @s subtitle {"text":"350 XP, 250 💰, 1 gemme (+1 point)","color":"gray"}
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1.1
scoreboard players add @s mg.olsp 1
