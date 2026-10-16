scoreboard players add @s mg.tvc 120
function mg:terra/rpg/xp {n:300}
tellraw @s {"text":"  +120 ₵ (prime sur Varek)","color":"green"}
execute if score @s mg.trch matches 62 run function mg:terra/rpg/ch {n:64}
title @s title {"text":"VAREK EST TOMBÉ","color":"gold","bold":true}
