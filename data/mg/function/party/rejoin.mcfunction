# Remet @s sur le plateau (début, retour de mini-jeu, reconnexion, fin de survol) : spectateur derrière la caméra, son pion sur sa case
tag @s remove mg.out
tag @s remove mg.mpview
tag @s add mg.play
gamemode spectator @s
rotate @s -135 40
team join mg_party @s
function mg:party/place
tag @s add mg.mprj
execute as @e[type=minecraft:armor_stand,tag=mg.mppawn] if score @s mg.mpo = $pp mg.st at @s run tp @a[tag=mg.mprj,limit=1] ~5 ~7 ~5 facing entity @s eyes
tag @s remove mg.mprj
