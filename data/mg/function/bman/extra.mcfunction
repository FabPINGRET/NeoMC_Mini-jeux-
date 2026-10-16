# @s : plus de place dans l'arène → spectateur
tag @s remove mg.play
tag @s add mg.out
gamemode spectator @s
tp @s 0 76 40700
tellraw @s {"text":"💣 Arène pleine (8 joueurs, 4 par équipe) : tu regardes cette partie.","color":"gray"}
