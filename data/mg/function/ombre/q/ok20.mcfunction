# Étape 20 validée (bjorn)
scoreboard players add @s mg.olg 200
tellraw @s {"text":"  +200 💰","color":"gold"}
function mg:ombre/xp {n:300}
function mg:ombre/q/adv
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1
