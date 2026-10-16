# @s met un point en 💨 Agilité
execute unless score @s mg.trsp matches 1.. run return run tellraw @s {"text":"Aucun point à répartir.","color":"gray"}
execute if score @s mg.trs3 matches 10.. run return run tellraw @s {"text":"💨 Agilité est déjà au maximum (10).","color":"gray"}
scoreboard players remove @s mg.trsp 1
scoreboard players add @s mg.trs3 1
function mg:terra/rpg/st/apply
tellraw @s [{"text":"💨 Agilité ","color":"green","bold":true},{"score":{"name":"@s","objective":"mg.trs3"},"color":"white"},{"text":" / 10  (+2 % de vitesse par point)","color":"gray"}]
execute at @s run playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 0.7 1.4
function mg:terra/rpg/sheet
