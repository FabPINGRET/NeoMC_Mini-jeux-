# @s met un point en 🎯 Précision
execute unless score @s mg.trsp matches 1.. run return run tellraw @s {"text":"Aucun point à répartir.","color":"gray"}
execute if score @s mg.trs4 matches 10.. run return run tellraw @s {"text":"🎯 Précision est déjà au maximum (10).","color":"gray"}
scoreboard players remove @s mg.trsp 1
scoreboard players add @s mg.trs4 1
function mg:terra/rpg/st/apply
tellraw @s [{"text":"🎯 Précision ","color":"aqua","bold":true},{"score":{"name":"@s","objective":"mg.trs4"},"color":"white"},{"text":" / 10  (+1 dégât de fusil tous les 2 points)","color":"gray"}]
execute at @s run playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 0.7 1.4
function mg:terra/rpg/sheet
