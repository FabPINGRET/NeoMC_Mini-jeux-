# @s rend « Sangsues géantes »
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p6 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run return run tellraw @s {"text":"Accepte d'abord la quête.","color":"gray"}
execute unless score @s mg.olq7 matches 6.. run return run tellraw @s [{"text":"Progression : ","color":"red"},{"score":{"name":"@s","objective":"mg.olq7"},"color":"yellow"},{"text":" / 6","color":"yellow"}]
scoreboard players operation @s mg.olsa -= #p6 mg.st
scoreboard players operation @s mg.olsd += #p6 mg.st
scoreboard players add @s mg.olg 400
function mg:ombre/xp {n:700}
title @s times 5 40 10
title @s title {"text":"✔ Sangsues géantes","color":"yellow","bold":true}
title @s subtitle {"text":"700 XP, 400 💰","color":"gray"}
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1.1
