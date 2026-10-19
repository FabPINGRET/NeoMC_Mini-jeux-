# Étape 36 validée (durgan)
execute unless score @s mg.olm6 matches 6.. run return run tellraw @s [{"text":"Il te faut 6 × écaille de drake (tu en as ","color":"red"},{"score":{"name":"@s","objective":"mg.olm6"},"color":"yellow"},{"text":").","color":"red"}]
scoreboard players remove @s mg.olm6 6
function mg:ombre/xp {n:300}
scoreboard players set @s mg.olfire 1
tellraw @s {"text":"🔥 Talisman ignifuge : la chaleur de Pyrecendre ne t'atteint plus.","color":"gold"}
function mg:ombre/q/adv
execute at @s run playsound minecraft:ui.toast.challenge_complete player @s ~ ~ ~ 0.6 1
