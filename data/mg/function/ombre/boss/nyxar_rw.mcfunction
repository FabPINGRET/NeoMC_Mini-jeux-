# @s a participé à la victoire sur Nyxar, dragon de la Lune Noire
title @s times 10 60 20
title @s title {"text":"VICTOIRE","color":"gold","bold":true}
title @s subtitle {"text":"Nyxar, dragon de la Lune Noire est tombé","color":"yellow"}
scoreboard players add @s mg.olg 1600
scoreboard players add @s mg.olm8 5
scoreboard players add @s mg.olm9 1
function mg:ombre/xp {n:3200}
tellraw @s {"text":"  +1600 💰, +5 essence d'ombre, +1 poussière de lune","color":"gold"}
scoreboard players operation $b mg.st = @s mg.olbk
scoreboard players operation $b mg.st /= #p8 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/boss/nyxar_first
execute if score @s mg.olch matches 50 run function mg:ombre/q/adv
