# @s : réouverture de la fenêtre du casino
execute if entity @s[tag=mg.gcas_slot] run function mg:gta/cas_ui_slot
execute if entity @s[tag=mg.gcas_roulette] run function mg:gta/cas_ui_roulette
execute if entity @s[tag=mg.gcas_dice] run function mg:gta/cas_ui_dice
tag @s remove mg.gcas_slot
tag @s remove mg.gcas_roulette
tag @s remove mg.gcas_dice
