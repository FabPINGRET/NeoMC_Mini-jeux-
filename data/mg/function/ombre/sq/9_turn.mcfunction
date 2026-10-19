# @s rend « Ambre du désert »
scoreboard players operation $b mg.st = @s mg.olsa
scoreboard players operation $b mg.st /= #p8 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run return run tellraw @s {"text":"Accepte d'abord la quête.","color":"gray"}
execute unless score @s mg.olm5 matches 6.. run return run tellraw @s {"text":"Il en faut 6.","color":"red"}
scoreboard players remove @s mg.olm5 6
scoreboard players operation @s mg.olsa -= #p8 mg.st
scoreboard players operation @s mg.olsd += #p8 mg.st
scoreboard players add @s mg.olg 500
function mg:ombre/xp {n:900}
title @s times 5 40 10
title @s title {"text":"✔ Ambre du désert","color":"yellow","bold":true}
title @s subtitle {"text":"900 XP, 500 💰, 1 gemme (+1 point)","color":"gray"}
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1.1
scoreboard players add @s mg.olsp 1
