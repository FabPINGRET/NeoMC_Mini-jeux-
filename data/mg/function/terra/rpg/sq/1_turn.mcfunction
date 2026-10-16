# @s rend « Remèdes du marais »
scoreboard players operation $b mg.st = @s mg.trsa
scoreboard players operation $b mg.st /= #p0 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run return run tellraw @s {"text":"Accepte d'abord la quête.","color":"gray"}
execute unless score @s mg.trvn matches 5.. run return run tellraw @s {"text":"Il en faut 5.","color":"red"}
scoreboard players remove @s mg.trvn 5
scoreboard players operation @s mg.trsa -= #p0 mg.st
scoreboard players operation $b mg.st = @s mg.trsq
scoreboard players operation $b mg.st /= #p0 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run scoreboard players operation @s mg.trsq += #p0 mg.st
scoreboard players add @s mg.tvc 150
function mg:terra/rpg/xp {n:300}
title @s times 5 40 10
title @s title {"text":"✔ Remèdes du marais","color":"yellow","bold":true}
title @s subtitle {"text":"300 XP, 150 ₵, 3 trousses de soins","color":"gray"}
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1.1
give @s minecraft:golden_apple[custom_name={"text":"✚ Trousse de soins","color":"red","italic":false,"bold":true}] 3
