# @s rend « Élémentaires de feu »
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p10 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run return run tellraw @s {"text":"Accepte d'abord la quête.","color":"gray"}
execute unless score @s mg.olq11 matches 6.. run return run tellraw @s [{"text":"Progression : ","color":"red"},{"score":{"name":"@s","objective":"mg.olq11"},"color":"yellow"},{"text":" / 6","color":"yellow"}]
scoreboard players operation @s mg.olsa -= #p10 mg.st
scoreboard players operation @s mg.olsd += #p10 mg.st
scoreboard players add @s mg.olg 600
function mg:ombre/xp {n:1100}
title @s times 5 40 10
title @s title {"text":"✔ Élémentaires de feu","color":"yellow","bold":true}
title @s subtitle {"text":"1100 XP, 600 💰","color":"gray"}
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1.1
