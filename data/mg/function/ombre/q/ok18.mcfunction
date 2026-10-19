# Étape 18 validée (bjorn)
scoreboard players add @s mg.olg 60
tellraw @s {"text":"  +60 💰","color":"gold"}
function mg:ombre/xp {n:100}
function mg:ombre/q/adv
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1
