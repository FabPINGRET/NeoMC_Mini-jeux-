scoreboard players add @s mg.trrx 1
scoreboard players add @s mg.tvc 400
function mg:terra/rpg/xp {n:1000}
tellraw @s {"text":"  +1 croc du Roi, +400 ₵","color":"dark_red"}
title @s title {"text":"LE ROI EST MORT","color":"gold","bold":true}
execute if score @s mg.trch matches 80 run function mg:terra/rpg/ch {n:85}
