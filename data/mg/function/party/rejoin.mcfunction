# Remet @s sur le plateau comme joueur (début, retour de mini-jeu, reconnexion, fin de survol)
tag @s remove mg.out
tag @s remove mg.mpview
tag @s add mg.play
team join mg_party @s
gamemode adventure @s
team join mg_party @s
function mg:party/freeze
function mg:party/place
