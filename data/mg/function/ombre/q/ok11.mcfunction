# Étape 11 validée (elyndra)
scoreboard players add @s mg.olg 80
tellraw @s {"text":"  +80 💰","color":"gold"}
function mg:ombre/xp {n:150}
function mg:ombre/q/adv
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1
