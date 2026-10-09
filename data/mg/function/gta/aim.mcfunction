# @s tient une arme : viseur au centre, rouge si une cible est dans la ligne de mire (48 blocs) ; sniper accroupi : lunette
execute if items entity @s weapon.mainhand *[custom_data~{gun:5}] if predicate mg:sneak run return run function mg:gta/scope
scoreboard players set $ga mg.st 0
scoreboard players set $gar mg.st 48
tag @s add mg.gaim
execute anchored eyes positioned ^ ^ ^1 run function mg:gta/aim_ray
tag @s remove mg.gaim
title @s times 0 5 2
execute if score $ga mg.st matches 0 run title @s title {"text":"","font":"mg:gta","color":"white","shadow_color":0}
execute if score $ga mg.st matches 1 run title @s title {"text":"","font":"mg:gta","color":"white","shadow_color":0}
