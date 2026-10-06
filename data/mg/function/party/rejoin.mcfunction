# Remet @s sur le plateau (début, retour de mini-jeu, reconnexion, fin de survol) : spectateur derrière la caméra, son pion sur sa case
tag @s remove mg.out
tag @s remove mg.mpview
tag @s add mg.play
gamemode spectator @s
team join mg_party @s
function mg:party/place
