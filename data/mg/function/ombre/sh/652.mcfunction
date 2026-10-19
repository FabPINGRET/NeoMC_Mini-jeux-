execute unless score @s mg.olg matches 60.. run return run function mg:ombre/sh/poor
scoreboard players remove @s mg.olg 60
give @s minecraft:honey_bottle[custom_data={olmana:1b},item_model="minecraft:potion",custom_name={"text":"✦ Potion de mana","color":"aqua","italic":false,"bold":true},lore=[{"text":"Boire : +60 mana","color":"gray","italic":false}]] 3
scoreboard players set @s mg.olal 40
title @s actionbar [{"text":"✔ 3 potions de mana ","color":"green","bold":true},{"text":"(-60 💰)","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes player @s ~ ~ ~ 0.8 1.1
