# @s met un point en ✦ Esprit
execute unless score @s mg.olsp matches 1.. run return run tellraw @s {"text":"Aucun point à répartir.","color":"gray"}
scoreboard players remove @s mg.olsp 1
scoreboard players add @s mg.ols4 1
function mg:ombre/stats
tellraw @s [{"text":"✦ Esprit ","color":"aqua","bold":true},{"score":{"name":"@s","objective":"mg.ols4"},"color":"white"},{"text":"  (+8 mana, puissance des sorts et soins)","color":"gray"}]
execute at @s run playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 0.7 1.4
function mg:ombre/sheet
