# Étape 5 validée (tessa)
scoreboard players add @s mg.olg 40
tellraw @s {"text":"  +40 💰","color":"gold"}
function mg:ombre/xp {n:80}
function mg:ombre/q/adv
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1
