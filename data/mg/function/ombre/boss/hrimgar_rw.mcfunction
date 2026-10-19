# @s a participé à la victoire sur Hrimgar, le géant du givre
title @s times 10 60 20
title @s title {"text":"VICTOIRE","color":"gold","bold":true}
title @s subtitle {"text":"Hrimgar, le géant du givre est tombé","color":"yellow"}
scoreboard players add @s mg.olg 600
scoreboard players add @s mg.olm3 5
scoreboard players add @s mg.olm9 1
function mg:ombre/xp {n:1200}
tellraw @s {"text":"  +600 💰, +5 éclat de givre, +1 poussière de lune","color":"gold"}
scoreboard players operation $b mg.st = @s mg.olbk
scoreboard players operation $b mg.st /= #p2 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:ombre/boss/hrimgar_first
execute if score @s mg.olch matches 21 run function mg:ombre/q/adv
