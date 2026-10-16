# @s met un point en ⚔ Force
execute unless score @s mg.trsp matches 1.. run return run tellraw @s {"text":"Aucun point à répartir.","color":"gray"}
execute if score @s mg.trs2 matches 10.. run return run tellraw @s {"text":"⚔ Force est déjà au maximum (10).","color":"gray"}
scoreboard players remove @s mg.trsp 1
scoreboard players add @s mg.trs2 1
function mg:terra/rpg/st/apply
tellraw @s [{"text":"⚔ Force ","color":"gold","bold":true},{"score":{"name":"@s","objective":"mg.trs2"},"color":"white"},{"text":" / 10  (+0,5 dégât de mêlée par point)","color":"gray"}]
execute at @s run playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 0.7 1.4
function mg:terra/rpg/sheet
