# Achat : 💪 Potion de force (1 min 30) (50 💰)
execute unless score @s mg.pco matches 50.. run return run tellraw @s [{"text":"💰 Pas assez de pièces pour ","color":"red"},{"text":"💪 Potion de force (1 min 30)","color":"dark_red"},{"text":" (50).","color":"red"}]
scoreboard players remove @s mg.pco 50
give @s minecraft:potion[potion_contents={potion:"minecraft:strength"},custom_name=[{"text":"Potion de force","color":"dark_red","italic":false}]]
tellraw @s [{"text":"✔ Acheté : ","color":"green"},{"text":"💪 Potion de force (1 min 30)","color":"dark_red"},{"text":" — reste ","color":"gray"},{"score":{"name":"@s","objective":"mg.pco"},"color":"yellow"},{"text":" 💰","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes master @s ~ ~ ~ 0.8 1.2
