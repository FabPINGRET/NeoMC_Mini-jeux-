# @s quitte les équipes du foot (tags ; équipe quittée seulement si c'est mg_ftr / mg_ftb : jamais celle d'un jeu)
tag @s remove mg.ftr
tag @s remove mg.ftb
execute if entity @s[team=mg_ftr] run team leave @s
execute if entity @s[team=mg_ftb] run team leave @s
