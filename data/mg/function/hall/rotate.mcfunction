# Tableau à droite (lobby) : classement général 10 s, puis un jeu 6 s
execute if score $rph mg.st matches 1 run return run function mg:hall/rot_game
scoreboard players set $rph mg.st 1
scoreboard players set $hrt mg.st 200
scoreboard objectives setdisplay sidebar mg.wins
