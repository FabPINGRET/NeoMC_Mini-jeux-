# @s (objet au sol : arme du jeu) : jeté par un joueur de la partie ? Il revient à son lanceur et se recharge
tag @s add mg.zdi
execute on origin if entity @s[tag=mg.play] run function mg:zx/q_back
tag @s remove mg.zdi
