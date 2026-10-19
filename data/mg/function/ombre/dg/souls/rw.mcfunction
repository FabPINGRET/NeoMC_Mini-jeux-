# @s termine Puits des âmes
scoreboard players add @s mg.olg 1200
scoreboard players add @s mg.olm8 4
function mg:ombre/xp {n:2400}
execute store result score $r mg.st run random value 1..2
execute if score $r mg.st matches 1 run scoreboard players add @s mg.olsp 1
title @s times 10 50 15
title @s title {"text":"DONJON TERMINÉ","color":"gold","bold":true}
title @s subtitle {"text":"Puits des âmes","color":"yellow"}
tellraw @s {"text":"  +1200 💰, +4 matériaux (et peut-être une gemme)","color":"gold"}
scoreboard players operation $b mg.st = @s mg.oldg
scoreboard players operation $b mg.st /= #p7 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/dg/souls/first
