# Achat : ✨ Pomme d'or enchantée (250 💰)
execute unless score @s mg.pco matches 250.. run return run tellraw @s [{"text":"💰 Pas assez de pièces pour ","color":"red"},{"text":"✨ Pomme d'or enchantée","color":"light_purple"},{"text":" (250).","color":"red"}]
scoreboard players remove @s mg.pco 250
give @s minecraft:enchanted_golden_apple
tellraw @s [{"text":"✔ Acheté : ","color":"green"},{"text":"✨ Pomme d'or enchantée","color":"light_purple"},{"text":" — reste ","color":"gray"},{"score":{"name":"@s","objective":"mg.pco"},"color":"yellow"},{"text":" 💰","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes master @s ~ ~ ~ 0.8 1.2
