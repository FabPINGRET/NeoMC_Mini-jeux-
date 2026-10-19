# @s a participé à la victoire sur Ysh'tar, la reine-araignée
title @s times 10 60 20
title @s title {"text":"VICTOIRE","color":"gold","bold":true}
title @s subtitle {"text":"Ysh'tar, la reine-araignée est tombé","color":"yellow"}
scoreboard players add @s mg.olg 400
scoreboard players add @s mg.olm2 5
scoreboard players add @s mg.olm9 1
function mg:ombre/xp {n:800}
tellraw @s {"text":"  +400 💰, +5 soie d'araignée, +1 poussière de lune","color":"gold"}
scoreboard players operation $b mg.st = @s mg.olbk
scoreboard players operation $b mg.st /= #p1 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/boss/ystar_first
execute if score @s mg.olch matches 14 run function mg:ombre/q/adv
