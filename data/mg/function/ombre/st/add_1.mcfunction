# @s met un point en ❤ Vigueur
execute unless score @s mg.olsp matches 1.. run return run tellraw @s {"text":"Aucun point à répartir.","color":"gray"}
scoreboard players remove @s mg.olsp 1
scoreboard players add @s mg.ols1 1
function mg:ombre/stats
tellraw @s [{"text":"❤ Vigueur ","color":"red","bold":true},{"score":{"name":"@s","objective":"mg.ols1"},"color":"white"},{"text":"  (+2 PV par point)","color":"gray"}]
execute at @s run playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 0.7 1.4
function mg:ombre/sheet
