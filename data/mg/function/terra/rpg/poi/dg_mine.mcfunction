# @s découvre « Mine abandonnée »
scoreboard players operation $b mg.st = @s mg.trpo
scoreboard players operation $b mg.st /= #p19 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return 0
scoreboard players operation @s mg.trpo += #p19 mg.st
title @s times 10 50 15
title @s title {"text":"Mine abandonnée","color":"yellow","bold":true}
title @s subtitle {"text":"✦ Lieu découvert","color":"gold"}
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.5 1.6
function mg:terra/rpg/xp {n:80}
