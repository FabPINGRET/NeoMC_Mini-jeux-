# Étape 10 validée (liora)
scoreboard players add @s mg.olg 100
tellraw @s {"text":"  +100 💰","color":"gold"}
function mg:ombre/xp {n:200}
function mg:ombre/q/adv
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1
