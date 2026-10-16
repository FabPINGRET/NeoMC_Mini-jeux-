# @s met un point en ❤ Vigueur
execute unless score @s mg.trsp matches 1.. run return run tellraw @s {"text":"Aucun point à répartir.","color":"gray"}
execute if score @s mg.trs1 matches 10.. run return run tellraw @s {"text":"❤ Vigueur est déjà au maximum (10).","color":"gray"}
scoreboard players remove @s mg.trsp 1
scoreboard players add @s mg.trs1 1
function mg:terra/rpg/st/apply
tellraw @s [{"text":"❤ Vigueur ","color":"red","bold":true},{"score":{"name":"@s","objective":"mg.trs1"},"color":"white"},{"text":" / 10  (+2 PV par point)","color":"gray"}]
execute at @s run playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 0.7 1.4
function mg:terra/rpg/sheet
