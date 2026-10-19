# @s a participé à la victoire sur Brennic, seigneur des brigands
title @s times 10 60 20
title @s title {"text":"VICTOIRE","color":"gold","bold":true}
title @s subtitle {"text":"Brennic, seigneur des brigands est tombé","color":"yellow"}
scoreboard players add @s mg.olg 200
scoreboard players add @s mg.olm1 5
scoreboard players add @s mg.olm9 1
function mg:ombre/xp {n:400}
tellraw @s {"text":"  +200 💰, +5 peau de bête, +1 poussière de lune","color":"gold"}
scoreboard players operation $b mg.st = @s mg.olbk
scoreboard players operation $b mg.st /= #p0 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/boss/brennic_first
execute if score @s mg.olch matches 8 run function mg:ombre/q/adv
