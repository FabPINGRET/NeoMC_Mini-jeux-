# Sheep War — murs invisibles (barrières) tout autour de l'arène, de y=45 à y=230, + plafond à y=231
# Les moutons perdus (boule porteuse) rebondissent sur le mur et retombent dans l'arène.
# Macro : $(x) = demi-largeur (x de -x à +x), $(z0)/$(z1) = bords en z
$fill -$(x) 45 $(z0) $(x) 230 $(z0) minecraft:barrier
$fill -$(x) 45 $(z1) $(x) 230 $(z1) minecraft:barrier
$fill -$(x) 45 $(z0) -$(x) 230 $(z1) minecraft:barrier
$fill $(x) 45 $(z0) $(x) 230 $(z1) minecraft:barrier
$fill -$(x) 231 $(z0) $(x) 231 $(z1) minecraft:barrier
