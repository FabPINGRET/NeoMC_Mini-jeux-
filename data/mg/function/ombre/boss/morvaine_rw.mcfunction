# @s a participé à la victoire sur Morvaine, la mère-sorcière
title @s times 10 60 20
title @s title {"text":"VICTOIRE","color":"gold","bold":true}
title @s subtitle {"text":"Morvaine, la mère-sorcière est tombé","color":"yellow"}
scoreboard players add @s mg.olg 800
scoreboard players add @s mg.olm4 5
scoreboard players add @s mg.olm9 1
function mg:ombre/xp {n:1600}
tellraw @s {"text":"  +800 💰, +5 fiole de venin, +1 poussière de lune","color":"gold"}
scoreboard players operation $b mg.st = @s mg.olbk
scoreboard players operation $b mg.st /= #p3 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/boss/morvaine_first
execute if score @s mg.olch matches 27 run function mg:ombre/q/adv
