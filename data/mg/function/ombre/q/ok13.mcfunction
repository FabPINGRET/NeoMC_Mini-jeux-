# Étape 13 validée (elyndra)
scoreboard players add @s mg.olg 180
tellraw @s {"text":"  +180 💰","color":"gold"}
function mg:ombre/xp {n:300}
function mg:ombre/q/adv
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1
