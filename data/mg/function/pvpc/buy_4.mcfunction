# Achat : ☠ Potion de dégâts (jetable) (35 💰)
execute unless score @s mg.pco matches 35.. run return run tellraw @s [{"text":"💰 Pas assez de pièces pour ","color":"red"},{"text":"☠ Potion de dégâts (jetable)","color":"dark_purple"},{"text":" (35).","color":"red"}]
scoreboard players remove @s mg.pco 35
give @s minecraft:splash_potion[potion_contents={potion:"minecraft:strong_harming"},custom_name=[{"text":"Potion de dégâts","color":"dark_purple","italic":false}]]
tellraw @s [{"text":"✔ Acheté : ","color":"green"},{"text":"☠ Potion de dégâts (jetable)","color":"dark_purple"},{"text":" — reste ","color":"gray"},{"score":{"name":"@s","objective":"mg.pco"},"color":"yellow"},{"text":" 💰","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes master @s ~ ~ ~ 0.8 1.2
