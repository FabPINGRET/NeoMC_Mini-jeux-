# @s : se lève. Le siège occupé est retiré (le joueur en descend) ; aucun autre véhicule n'est touché
execute on vehicle if entity @s[type=minecraft:item_display,tag=mg.seat] run kill @s
tag @s remove mg.sit
