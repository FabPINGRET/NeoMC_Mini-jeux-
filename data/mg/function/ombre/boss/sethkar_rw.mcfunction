# @s a participé à la victoire sur Sethkar, le pharaon-liche
title @s times 10 60 20
title @s title {"text":"VICTOIRE","color":"gold","bold":true}
title @s subtitle {"text":"Sethkar, le pharaon-liche est tombé","color":"yellow"}
scoreboard players add @s mg.olg 1000
scoreboard players add @s mg.olm5 5
scoreboard players add @s mg.olm9 1
function mg:ombre/xp {n:2000}
tellraw @s {"text":"  +1000 💰, +5 ambre solaire, +1 poussière de lune","color":"gold"}
scoreboard players operation $b mg.st = @s mg.olbk
scoreboard players operation $b mg.st /= #p4 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/boss/sethkar_first
execute if score @s mg.olch matches 33 run function mg:ombre/q/adv
