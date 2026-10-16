# @s rend « Le ciel des Aiguilles »
scoreboard players operation $b mg.st = @s mg.trsa
scoreboard players operation $b mg.st /= #p1 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run return run tellraw @s {"text":"Accepte d'abord la quête.","color":"gray"}
execute unless score @s mg.trai matches 6.. run return run tellraw @s {"text":"Il en faut 6.","color":"red"}
scoreboard players remove @s mg.trai 6
scoreboard players operation @s mg.trsa -= #p1 mg.st
scoreboard players operation $b mg.st = @s mg.trsq
scoreboard players operation $b mg.st /= #p1 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run scoreboard players operation @s mg.trsq += #p1 mg.st
scoreboard players add @s mg.tvc 200
function mg:terra/rpg/xp {n:400}
title @s times 5 40 10
title @s title {"text":"✔ Le ciel des Aiguilles","color":"yellow","bold":true}
title @s subtitle {"text":"400 XP, 200 ₵","color":"gray"}
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1.1
