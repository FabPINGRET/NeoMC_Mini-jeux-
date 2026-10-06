# Retour au spawn depuis son plot ou depuis une visite (@s = joueur) : aventure, inventaire du lobby
execute unless entity @s[tag=mg.inplot] unless entity @s[tag=mg.visit] run return run tellraw @s [{"text":"Tu n'es pas sur un plot.","color":"gray"}]
execute if entity @s[tag=mg.inplot] run function mg:plot/walls_fix
tag @s remove mg.inplot
tag @s remove mg.visit
function mg:core/reset_player
