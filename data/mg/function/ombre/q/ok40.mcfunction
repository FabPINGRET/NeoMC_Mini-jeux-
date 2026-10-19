# Étape 40 validée (thrain)
scoreboard players add @s mg.olg 150
tellraw @s {"text":"  +150 💰","color":"gold"}
function mg:ombre/xp {n:150}
function mg:ombre/q/adv
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1
