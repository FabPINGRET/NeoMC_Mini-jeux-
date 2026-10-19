# @s rend « Chevaliers noirs »
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p14 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run return run tellraw @s {"text":"Accepte d'abord la quête.","color":"gray"}
execute unless score @s mg.olq15 matches 6.. run return run tellraw @s [{"text":"Progression : ","color":"red"},{"score":{"name":"@s","objective":"mg.olq15"},"color":"yellow"},{"text":" / 6","color":"yellow"}]
scoreboard players operation @s mg.olsa -= #p14 mg.st
scoreboard players operation @s mg.olsd += #p14 mg.st
scoreboard players add @s mg.olg 900
function mg:ombre/xp {n:1600}
title @s times 5 40 10
title @s title {"text":"✔ Chevaliers noirs","color":"yellow","bold":true}
title @s subtitle {"text":"1600 XP, 900 💰","color":"gray"}
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1.1
