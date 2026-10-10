# Achat : 🍎 Pomme d'or (30 💰)
execute unless score @s mg.pco matches 30.. run return run tellraw @s [{"text":"💰 Pas assez de pièces pour ","color":"red"},{"text":"🍎 Pomme d'or","color":"gold"},{"text":" (30).","color":"red"}]
scoreboard players remove @s mg.pco 30
give @s minecraft:golden_apple
tellraw @s [{"text":"✔ Acheté : ","color":"green"},{"text":"🍎 Pomme d'or","color":"gold"},{"text":" — reste ","color":"gray"},{"score":{"name":"@s","objective":"mg.pco"},"color":"yellow"},{"text":" 💰","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes master @s ~ ~ ~ 0.8 1.2
