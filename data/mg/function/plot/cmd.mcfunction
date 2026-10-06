# Trigger mg.pl (@s = joueur) : 1 = aller sur son plot, 2 = retour au spawn, 3 = liste des plots, 101..115 = visiter le plot n°1..15 en spectateur
execute if score @s mg.pl matches 1 run function mg:plot/enter
execute if score @s mg.pl matches 2 run function mg:plot/leave
execute if score @s mg.pl matches 3 run function mg:plot/list
execute if score @s mg.pl matches 101..115 run function mg:plot/visit
scoreboard players reset @s mg.pl
