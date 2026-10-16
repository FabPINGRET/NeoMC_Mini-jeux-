# @s découvre « Fort des Renégats »
scoreboard players operation $b mg.st = @s mg.trpo
scoreboard players operation $b mg.st /= #p11 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return 0
scoreboard players operation @s mg.trpo += #p11 mg.st
title @s times 10 50 15
title @s title {"text":"Fort des Renégats","color":"yellow","bold":true}
title @s subtitle {"text":"✦ Lieu découvert","color":"gold"}
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.5 1.6
function mg:terra/rpg/xp {n:100}
