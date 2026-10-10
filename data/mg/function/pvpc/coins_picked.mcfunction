# @s a ramassé des pièces : 1 pépite = 1 pièce
execute store result score $n mg.st run clear @s minecraft:gold_nugget[custom_data~{pvpc_coin:1b}]
scoreboard players operation @s mg.pco += $n mg.st
playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1.4
title @s actionbar [{"text":"💰 +","color":"gold"},{"score":{"name":"$n","objective":"mg.st"},"color":"yellow","bold":true},{"text":" pièces","color":"gold"}]
