# Tableau à droite dans le lobby (classement affiché, pas de vote en cours)
scoreboard players remove $hrt mg.st 1
execute unless score $hrt mg.st matches 1.. run function mg:hall/rotate
