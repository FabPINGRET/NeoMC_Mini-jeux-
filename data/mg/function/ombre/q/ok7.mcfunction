# Étape 7 validée (tessa)
scoreboard players add @s mg.olg 120
tellraw @s {"text":"  +120 💰","color":"gold"}
function mg:ombre/xp {n:200}
function mg:ombre/q/adv
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1
