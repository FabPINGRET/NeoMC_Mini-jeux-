# @s a vaincu l'alpha : Cœur de l'Arbre-Mère
scoreboard players add @s mg.trvn 3
scoreboard players add @s mg.tvc 150
function mg:terra/rpg/xp {n:300}
tellraw @s {"text":"  +3 glandes à venin, +150 ₵","color":"gold"}
title @s title {"text":"ALPHA VAINCU","color":"gold","bold":true}
scoreboard players operation $b mg.st = @s mg.trdg
scoreboard players operation $b mg.st /= #p0 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:terra/rpg/dg/arbre_first
