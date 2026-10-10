# Achat : 🟣 Perle de l'Ender (40 💰)
execute unless score @s mg.pco matches 40.. run return run tellraw @s [{"text":"💰 Pas assez de pièces pour ","color":"red"},{"text":"🟣 Perle de l'Ender","color":"dark_aqua"},{"text":" (40).","color":"red"}]
scoreboard players remove @s mg.pco 40
give @s minecraft:ender_pearl
tellraw @s [{"text":"✔ Acheté : ","color":"green"},{"text":"🟣 Perle de l'Ender","color":"dark_aqua"},{"text":" — reste ","color":"gray"},{"score":{"name":"@s","objective":"mg.pco"},"color":"yellow"},{"text":" 💰","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes master @s ~ ~ ~ 0.8 1.2
