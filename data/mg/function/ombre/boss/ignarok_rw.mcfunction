# @s a participé à la victoire sur Ignarok, dragon de feu
title @s times 10 60 20
title @s title {"text":"VICTOIRE","color":"gold","bold":true}
title @s subtitle {"text":"Ignarok, dragon de feu est tombé","color":"yellow"}
scoreboard players add @s mg.olg 1200
scoreboard players add @s mg.olm6 5
scoreboard players add @s mg.olm9 1
function mg:ombre/xp {n:2400}
tellraw @s {"text":"  +1200 💰, +5 écaille de drake, +1 poussière de lune","color":"gold"}
scoreboard players operation $b mg.st = @s mg.olbk
scoreboard players operation $b mg.st /= #p5 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/boss/ignarok_first
execute if score @s mg.olch matches 38 run function mg:ombre/q/adv
