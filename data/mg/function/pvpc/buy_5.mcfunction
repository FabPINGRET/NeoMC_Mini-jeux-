# Achat : 🐺 Chien de garde (60 💰)
execute unless score @s mg.pco matches 60.. run return run tellraw @s [{"text":"💰 Pas assez de pièces pour ","color":"red"},{"text":"🐺 Chien de garde","color":"white"},{"text":" (60).","color":"red"}]
scoreboard players remove @s mg.pco 60
function mg:pvpc/dog
tellraw @s [{"text":"✔ Acheté : ","color":"green"},{"text":"🐺 Chien de garde","color":"white"},{"text":" — reste ","color":"gray"},{"score":{"name":"@s","objective":"mg.pco"},"color":"yellow"},{"text":" 💰","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes master @s ~ ~ ~ 0.8 1.2
