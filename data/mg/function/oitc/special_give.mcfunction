# Offre une flèche enchantée aléatoire (@s = joueur)
execute store result score $osk mg.st run random value 1..3
execute if score $osk mg.st matches 1 run give @s minecraft:arrow[custom_name=[{"text":"✦ Flèche explosive","color":"red","italic":false}],lore=[{"text":"Explose au contact : tue tout autour","color":"gray","italic":false}],enchantment_glint_override=true,custom_data={mg_ar:1}] 1
execute if score $osk mg.st matches 2 run give @s minecraft:arrow[custom_name=[{"text":"✦ Flèche perforante","color":"aqua","italic":false}],lore=[{"text":"Traverse jusqu'à 4 joueurs","color":"gray","italic":false}],enchantment_glint_override=true,custom_data={mg_ar:2}] 1
execute if score $osk mg.st matches 3 run give @s minecraft:arrow[custom_name=[{"text":"✦ Flèche révélatrice","color":"light_purple","italic":false}],lore=[{"text":"Tous les adversaires brillent 6 s","color":"gray","italic":false}],enchantment_glint_override=true,custom_data={mg_ar:3}] 1
title @s actionbar [{"text":"✦ Flèche enchantée reçue ! ","color":"light_purple","bold":true},{"text":"(elle part avant tes flèches normales)","color":"gray"}]
execute at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 1.6
execute at @s run particle minecraft:enchant ~ ~1 ~ 0.4 0.6 0.4 0.5 30
