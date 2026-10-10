# Achat : ⚡ Potion de vitesse (1 min 30) (25 💰)
execute unless score @s mg.pco matches 25.. run return run tellraw @s [{"text":"💰 Pas assez de pièces pour ","color":"red"},{"text":"⚡ Potion de vitesse (1 min 30)","color":"aqua"},{"text":" (25).","color":"red"}]
scoreboard players remove @s mg.pco 25
give @s minecraft:potion[potion_contents={potion:"minecraft:swiftness"},custom_name=[{"text":"Potion de vitesse","color":"aqua","italic":false}]]
tellraw @s [{"text":"✔ Acheté : ","color":"green"},{"text":"⚡ Potion de vitesse (1 min 30)","color":"aqua"},{"text":" — reste ","color":"gray"},{"score":{"name":"@s","objective":"mg.pco"},"color":"yellow"},{"text":" 💰","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes master @s ~ ~ ~ 0.8 1.2
