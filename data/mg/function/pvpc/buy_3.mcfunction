# Achat : ❤ Potion de soin (jetable) (20 💰)
execute unless score @s mg.pco matches 20.. run return run tellraw @s [{"text":"💰 Pas assez de pièces pour ","color":"red"},{"text":"❤ Potion de soin (jetable)","color":"red"},{"text":" (20).","color":"red"}]
scoreboard players remove @s mg.pco 20
give @s minecraft:splash_potion[potion_contents={potion:"minecraft:strong_healing"},custom_name=[{"text":"Potion de soin","color":"red","italic":false}]]
tellraw @s [{"text":"✔ Acheté : ","color":"green"},{"text":"❤ Potion de soin (jetable)","color":"red"},{"text":" — reste ","color":"gray"},{"score":{"name":"@s","objective":"mg.pco"},"color":"yellow"},{"text":" 💰","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes master @s ~ ~ ~ 0.8 1.2
