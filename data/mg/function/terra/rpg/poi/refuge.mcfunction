# @s découvre « Refuge du Cendre »
scoreboard players operation $b mg.st = @s mg.trpo
scoreboard players operation $b mg.st /= #p14 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 1 run return 0
scoreboard players operation @s mg.trpo += #p14 mg.st
title @s times 10 50 15
title @s title {"text":"Refuge du Cendre","color":"yellow","bold":true}
title @s subtitle {"text":"✦ Lieu découvert","color":"gold"}
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.5 1.6
function mg:terra/rpg/xp {n:60}
scoreboard players operation $b mg.st = @s mg.trtv
scoreboard players operation $b mg.st /= #p4 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run scoreboard players operation @s mg.trtv += #p4 mg.st
execute in mg:terranova run spawnpoint @s -23 69 122
tellraw @s [{"text":"🌀 Balise de voyage activée : ","color":"light_purple"},{"text":"Refuge du Cendre","color":"yellow"},{"text":" (réapparition ici, voyage depuis n'importe quelle balise)","color":"gray"}]
