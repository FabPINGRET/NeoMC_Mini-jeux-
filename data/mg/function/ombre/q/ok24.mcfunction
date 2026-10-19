# Étape 24 validée (odo)
execute unless score @s mg.olm4 matches 4.. run return run tellraw @s [{"text":"Il te faut 4 × fiole de venin (tu en as ","color":"red"},{"score":{"name":"@s","objective":"mg.olm4"},"color":"yellow"},{"text":").","color":"red"}]
scoreboard players remove @s mg.olm4 4
function mg:ombre/xp {n:250}
function mg:ombre/q/adv
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1
