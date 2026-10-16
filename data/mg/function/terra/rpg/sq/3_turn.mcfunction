# @s rend « La mine maudite »
scoreboard players operation $b mg.st = @s mg.trsa
scoreboard players operation $b mg.st /= #p2 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run return run tellraw @s {"text":"Accepte d'abord la quête.","color":"gray"}
scoreboard players operation $b mg.st = @s mg.trdg
scoreboard players operation $b mg.st /= #p2 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run return run tellraw @s {"text":"L'alpha de la mine rôde toujours…","color":"red"}
scoreboard players operation @s mg.trsa -= #p2 mg.st
scoreboard players operation $b mg.st = @s mg.trsq
scoreboard players operation $b mg.st /= #p2 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run scoreboard players operation @s mg.trsq += #p2 mg.st
scoreboard players add @s mg.tvc 300
function mg:terra/rpg/xp {n:500}
title @s times 5 40 10
title @s title {"text":"✔ La mine maudite","color":"yellow","bold":true}
title @s subtitle {"text":"500 XP, 300 ₵, 1 point de caractéristique","color":"gray"}
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1.1
scoreboard players add @s mg.trsp 1
