# @s : distributeur de la planque secrète, 300 à 600 $ gratuits (toutes les 20 s)
execute store result score $gcv mg.st run random value 300..600
function mg:gta/cash_gain
title @s actionbar [{"text":"💵 +","color":"green","bold":true},{"score":{"name":"$gcv","objective":"mg.st"},"color":"green","bold":true},{"text":" $ ","color":"green","bold":true},{"text":"retirés au distributeur secret","color":"gray"}]
playsound minecraft:block.chain.place player @s ~ ~ ~ 1 0.6
playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 1 1.2
particle minecraft:happy_villager ~ ~1.2 ~ 0.4 0.4 0.4 0 12
