# @s a participé à la victoire sur Le Colosse de runes
title @s times 10 60 20
title @s title {"text":"VICTOIRE","color":"gold","bold":true}
title @s subtitle {"text":"Le Colosse de runes est tombé","color":"yellow"}
scoreboard players add @s mg.olg 1400
scoreboard players add @s mg.olm7 5
scoreboard players add @s mg.olm9 1
function mg:ombre/xp {n:2800}
tellraw @s {"text":"  +1400 💰, +5 minerai de runite, +1 poussière de lune","color":"gold"}
scoreboard players operation $b mg.st = @s mg.olbk
scoreboard players operation $b mg.st /= #p6 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/boss/colosse_first
execute if score @s mg.olch matches 43 run function mg:ombre/q/adv
