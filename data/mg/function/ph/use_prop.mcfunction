# @s = interaction cliquée (clic droit) : si c'est un cacheur → corne
execute on target if entity @s[tag=mg.phh] run tag @s add mg.phuse
data remove entity @s interaction
