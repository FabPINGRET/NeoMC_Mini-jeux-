# @s : zone touchable cliquée (clic droit). Un caméléon a les yeux dans sa propre zone : son clic droit arrive ici, pas sur l'objet
execute on target if entity @s[tag=mg.cmh,tag=!mg.cmout] at @s run function mg:cham/use
data remove entity @s interaction
