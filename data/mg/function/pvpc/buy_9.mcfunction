# Achat : ♥ Potion de régénération (45 s) (40 💰)
execute unless score @s mg.pco matches 40.. run return run tellraw @s [{"text":"💰 Pas assez de pièces pour ","color":"red"},{"text":"♥ Potion de régénération (45 s)","color":"light_purple"},{"text":" (40).","color":"red"}]
scoreboard players remove @s mg.pco 40
give @s minecraft:potion[potion_contents={potion:"minecraft:regeneration"},custom_name=[{"text":"Potion de régénération","color":"light_purple","italic":false}]]
tellraw @s [{"text":"✔ Acheté : ","color":"green"},{"text":"♥ Potion de régénération (45 s)","color":"light_purple"},{"text":" — reste ","color":"gray"},{"score":{"name":"@s","objective":"mg.pco"},"color":"yellow"},{"text":" 💰","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes master @s ~ ~ ~ 0.8 1.2
