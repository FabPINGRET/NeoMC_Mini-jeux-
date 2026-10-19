# @s découvre « Village des pilotis »
scoreboard players operation $b mg.st = @s mg.olpo
scoreboard players operation $b mg.st /= #p13 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return 0
scoreboard players operation @s mg.olpo += #p13 mg.st
title @s times 10 50 15
title @s title {"text":"Village des pilotis","color":"yellow","bold":true}
title @s subtitle {"text":"✦ Lieu découvert","color":"gold"}
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.5 1.6
function mg:ombre/xp {n:100}
