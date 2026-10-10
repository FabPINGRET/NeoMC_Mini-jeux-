# Achat : ➶ Flèches ×16 (10 💰)
execute unless score @s mg.pco matches 10.. run return run tellraw @s [{"text":"💰 Pas assez de pièces pour ","color":"red"},{"text":"➶ Flèches ×16","color":"gray"},{"text":" (10).","color":"red"}]
scoreboard players remove @s mg.pco 10
give @s minecraft:arrow 16
tellraw @s [{"text":"✔ Acheté : ","color":"green"},{"text":"➶ Flèches ×16","color":"gray"},{"text":" — reste ","color":"gray"},{"score":{"name":"@s","objective":"mg.pco"},"color":"yellow"},{"text":" 💰","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes master @s ~ ~ ~ 0.8 1.2
