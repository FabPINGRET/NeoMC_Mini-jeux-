# Étape 0 validée (liora)
scoreboard players add @s mg.olg 30
tellraw @s {"text":"  +30 💰","color":"gold"}
function mg:ombre/xp {n:60}
function mg:ombre/q/adv
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1
