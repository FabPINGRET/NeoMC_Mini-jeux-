# @s découvre « Grotte de givre »
scoreboard players operation $b mg.st = @s mg.olpo
scoreboard players operation $b mg.st /= #p12 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return 0
scoreboard players operation @s mg.olpo += #p12 mg.st
title @s times 10 50 15
title @s title {"text":"Grotte de givre","color":"yellow","bold":true}
title @s subtitle {"text":"✦ Lieu découvert","color":"gold"}
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.5 1.6
function mg:ombre/xp {n:50}
