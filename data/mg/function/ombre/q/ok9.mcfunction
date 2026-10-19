# Étape 9 validée (tessa)
scoreboard players add @s mg.olg 200
tellraw @s {"text":"  +200 💰","color":"gold"}
function mg:ombre/xp {n:300}
scoreboard players set @s mg.olsh 1
title @s times 10 50 15
title @s title {"text":"✦ ÉCLAT DE LUNE 1 / 8","color":"light_purple","bold":true}
execute at @s run playsound minecraft:block.amethyst_block.resonate player @s ~ ~ ~ 1 0.8
function mg:ombre/q/adv
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1
