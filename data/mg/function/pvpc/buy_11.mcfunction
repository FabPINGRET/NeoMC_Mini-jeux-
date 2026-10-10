# Achat : 🗿 Totem d'immortalité (200 💰)
execute unless score @s mg.pco matches 200.. run return run tellraw @s [{"text":"💰 Pas assez de pièces pour ","color":"red"},{"text":"🗿 Totem d'immortalité","color":"yellow"},{"text":" (200).","color":"red"}]
scoreboard players remove @s mg.pco 200
give @s minecraft:totem_of_undying
tellraw @s [{"text":"✔ Acheté : ","color":"green"},{"text":"🗿 Totem d'immortalité","color":"yellow"},{"text":" — reste ","color":"gray"},{"score":{"name":"@s","objective":"mg.pco"},"color":"yellow"},{"text":" 💰","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes master @s ~ ~ ~ 0.8 1.2
