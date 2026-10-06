# Trigger mg.pl (@s = joueur) : 1 = aller sur son plot, 2 = retour au spawn
execute if score @s mg.pl matches 1 run function mg:plot/enter
execute if score @s mg.pl matches 2 run function mg:plot/leave
scoreboard players reset @s mg.pl
