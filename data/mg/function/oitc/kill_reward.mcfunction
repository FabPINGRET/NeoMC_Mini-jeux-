# Kill (@s = le tueur) : +1 flèche (1 fois sur 5 : une flèche enchantée), +1 kill
scoreboard players reset @s mg.pk
scoreboard players add @s mg.ok 1
execute store result score $osr mg.st run random value 1..5
execute unless score $osr mg.st matches 1 run give @s minecraft:arrow[custom_name=[{"text":"Flèche","color":"yellow","italic":false}]] 1
title @s actionbar [{"text":"☠ KILL ! ","color":"red","bold":true},{"score":{"name":"@s","objective":"mg.ok"},"color":"gold"},{"text":" / ","color":"gray"},{"score":{"name":"$og","objective":"mg.st"},"color":"gray"},{"text":"  ","color":"gray"},{"text":"+1 flèche","color":"yellow"}]
execute at @s run playsound minecraft:entity.arrow.hit_player master @s ~ ~ ~ 1 1.2
execute if score $osr mg.st matches 1 run function mg:oitc/special_give
