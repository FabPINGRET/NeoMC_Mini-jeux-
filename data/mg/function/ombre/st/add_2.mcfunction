# @s met un point en ⚔ Force
execute unless score @s mg.olsp matches 1.. run return run tellraw @s {"text":"Aucun point à répartir.","color":"gray"}
scoreboard players remove @s mg.olsp 1
scoreboard players add @s mg.ols2 1
function mg:ombre/stats
tellraw @s [{"text":"⚔ Force ","color":"gold","bold":true},{"score":{"name":"@s","objective":"mg.ols2"},"color":"white"},{"text":"  (+0,5 dégât de mêlée, compétences du chevalier)","color":"gray"}]
execute at @s run playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 0.7 1.4
function mg:ombre/sheet
