# Retour au spawn depuis son plot (@s = joueur) : aventure, inventaire du lobby
execute unless entity @s[tag=mg.inplot] run return run tellraw @s [{"text":"Tu n'es pas sur ton plot.","color":"gray"}]
function mg:plot/walls_fix
tag @s remove mg.inplot
function mg:core/reset_player
