# Lancement d'une partie : un participant présent sur son plot quitte le créatif (@s = joueur, garde mg.play)
tag @s remove mg.inplot
tag @s remove mg.visit
function mg:core/reset_player
tag @s add mg.play
