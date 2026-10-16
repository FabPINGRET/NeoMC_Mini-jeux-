# @s rend « Les gardiens de cendre »
scoreboard players operation $b mg.st = @s mg.trsa
scoreboard players operation $b mg.st /= #p3 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run return run tellraw @s {"text":"Accepte d'abord la quête.","color":"gray"}
execute unless score @s mg.trq4 matches 3.. run return run tellraw @s [{"text":"Carnotaures abattus sur le volcan : ","color":"red"},{"score":{"name":"@s","objective":"mg.trq4"},"color":"yellow"},{"text":" / 3","color":"yellow"}]
scoreboard players operation @s mg.trsa -= #p3 mg.st
scoreboard players operation $b mg.st = @s mg.trsq
scoreboard players operation $b mg.st /= #p3 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run scoreboard players operation @s mg.trsq += #p3 mg.st
scoreboard players add @s mg.tvc 400
function mg:terra/rpg/xp {n:600}
title @s times 5 40 10
title @s title {"text":"✔ Les gardiens de cendre","color":"yellow","bold":true}
title @s subtitle {"text":"600 XP, 400 ₵, 1 gemme d'ambre","color":"gray"}
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1.1
scoreboard players add @s mg.trsp 1
