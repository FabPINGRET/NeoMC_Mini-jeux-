# @s met un point en 💨 Agilité
execute unless score @s mg.olsp matches 1.. run return run tellraw @s {"text":"Aucun point à répartir.","color":"gray"}
scoreboard players remove @s mg.olsp 1
scoreboard players add @s mg.ols3 1
function mg:ombre/stats
tellraw @s [{"text":"💨 Agilité ","color":"green","bold":true},{"score":{"name":"@s","objective":"mg.ols3"},"color":"white"},{"text":"  (+1,5 % de vitesse, compétences du rôdeur)","color":"gray"}]
execute at @s run playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 0.7 1.4
function mg:ombre/sheet
