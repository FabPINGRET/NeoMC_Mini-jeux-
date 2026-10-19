# Étape 46 validée (aldric_sw)
scoreboard players add @s mg.olg 200
tellraw @s {"text":"  +200 💰","color":"gold"}
function mg:ombre/xp {n:200}
function mg:ombre/q/adv
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1
