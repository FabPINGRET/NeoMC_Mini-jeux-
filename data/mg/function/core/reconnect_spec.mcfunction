# Reconnexion pendant une partie : spectateur dans le jeu en cours (@s = joueur)
# Il n'est pas participant (pas de mg.play) ; mg.out le ramènera au lobby à la fin de la partie.
tag @s remove mg.play
tag @s remove mg.win
tag @s remove mg.rsp
tag @s add mg.out
team leave @s
effect clear @s
function mg:core/attr_reset
clear @s
scoreboard players set @s mg.deaths 0
gamemode spectator @s

execute store result storage mg:c x int 1 run scoreboard players get $px mg.st
execute store result storage mg:c y int 1 run scoreboard players get $py mg.st
execute store result storage mg:c z int 1 run scoreboard players get $pz mg.st
function mg:core/tp_perch with storage mg:c

tellraw @s [{"text":"Une partie est en cours : tu la regardes en spectateur, tu joueras à la prochaine !","color":"gray"}]
