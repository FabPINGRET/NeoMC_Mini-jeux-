# @s : choix dans le téléphone (mg.gmis)
scoreboard players operation $gmc mg.st = @s mg.gmis
scoreboard players reset @s mg.gmis
execute if score $gmc mg.st matches 9 run return run function mg:gta/mis_fail
execute if score @s mg.gmt matches 1.. run return run title @s actionbar {"text":"📱 Termine (ou abandonne) ta mission en cours d'abord","color":"red"}
execute if score $gmc mg.st matches 1 at @s run function mg:gta/mis1_start
execute if score $gmc mg.st matches 2 at @s run function mg:gta/mis2_start
execute if score $gmc mg.st matches 3 at @s run function mg:gta/mis3_start
