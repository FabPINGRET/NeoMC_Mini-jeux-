# @s termine Tombeaux d'Azhar
scoreboard players add @s mg.olg 750
scoreboard players add @s mg.olm5 4
function mg:ombre/xp {n:1500}
execute store result score $r mg.st run random value 1..2
execute if score $r mg.st matches 1 run scoreboard players add @s mg.olsp 1
title @s times 10 50 15
title @s title {"text":"DONJON TERMINÉ","color":"gold","bold":true}
title @s subtitle {"text":"Tombeaux d'Azhar","color":"yellow"}
tellraw @s {"text":"  +750 💰, +4 matériaux (et peut-être une gemme)","color":"gold"}
scoreboard players operation $b mg.st = @s mg.oldg
scoreboard players operation $b mg.st /= #p4 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/dg/tomb/first
