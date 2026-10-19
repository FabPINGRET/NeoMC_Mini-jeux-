execute unless score @s mg.olg matches 60.. run return run function mg:ombre/sh/poor
scoreboard players remove @s mg.olg 60
give @s minecraft:potion[potion_contents={potion:"minecraft:strong_healing"},custom_name={"text":"✚ Potion de soin","color":"red","italic":false,"bold":true}] 3
scoreboard players set @s mg.olal 40
title @s actionbar [{"text":"✔ 3 potions de soin ","color":"green","bold":true},{"text":"(-60 💰)","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes player @s ~ ~ ~ 0.8 1.1
