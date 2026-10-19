# @s rend « Fourrures d'ours »
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p4 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run return run tellraw @s {"text":"Accepte d'abord la quête.","color":"gray"}
execute unless score @s mg.olq5 matches 4.. run return run tellraw @s [{"text":"Progression : ","color":"red"},{"score":{"name":"@s","objective":"mg.olq5"},"color":"yellow"},{"text":" / 4","color":"yellow"}]
scoreboard players operation @s mg.olsa -= #p4 mg.st
scoreboard players operation @s mg.olsd += #p4 mg.st
scoreboard players add @s mg.olg 300
function mg:ombre/xp {n:500}
title @s times 5 40 10
title @s title {"text":"✔ Fourrures d'ours","color":"yellow","bold":true}
title @s subtitle {"text":"500 XP, 300 💰","color":"gray"}
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1.1
