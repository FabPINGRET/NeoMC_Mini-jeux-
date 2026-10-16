# @s a vaincu l'alpha : Mine abandonnée
scoreboard players add @s mg.trgr 6
scoreboard players add @s mg.tvc 150
function mg:terra/rpg/xp {n:300}
tellraw @s {"text":"  +6 griffes, +150 ₵","color":"gold"}
title @s title {"text":"ALPHA VAINCU","color":"gold","bold":true}
scoreboard players operation $b mg.st = @s mg.trdg
scoreboard players operation $b mg.st /= #p2 mg.st
scoreboard players operation $b mg.st %= #2 mg.st
execute if score $b mg.st matches 0 run function mg:terra/rpg/dg/mine_first
