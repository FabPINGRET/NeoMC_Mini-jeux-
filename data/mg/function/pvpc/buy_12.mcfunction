# Achat : 🗡 Épée en diamant (120 💰)
execute unless score @s mg.pco matches 120.. run return run tellraw @s [{"text":"💰 Pas assez de pièces pour ","color":"red"},{"text":"🗡 Épée en diamant","color":"aqua"},{"text":" (120).","color":"red"}]
scoreboard players remove @s mg.pco 120
give @s minecraft:diamond_sword[unbreakable={}]
tellraw @s [{"text":"✔ Acheté : ","color":"green"},{"text":"🗡 Épée en diamant","color":"aqua"},{"text":" — reste ","color":"gray"},{"score":{"name":"@s","objective":"mg.pco"},"color":"yellow"},{"text":" 💰","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes master @s ~ ~ ~ 0.8 1.2
