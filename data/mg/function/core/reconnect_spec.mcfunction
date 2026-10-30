# Reconnexion pendant une partie : spectateur dans le jeu en cours (@s = joueur)
# Il n'est pas participant (pas de mg.play) ; mg.out le ramènera au lobby à la fin de la partie.
tag @s remove mg.play
# rôles de jeu périmés : cacheur (Prop Hunt, Caméléon), mort en attente (Quake, Convoi), porteur de drapeau (CTF), activités du spawn
tag @s remove mg.phh
tag @s remove mg.cmh
tag @s remove mg.qdd
tag @s remove mg.cvw
tag @s remove mg.cfcr
tag @s remove mg.cfcb
tag @s remove mg.pkr
execute if entity @s[tag=mg.ely] run function mg:elytra/stop_quiet
execute if entity @s[tag=mg.elyf] run function mg:elytra/free_stop
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
