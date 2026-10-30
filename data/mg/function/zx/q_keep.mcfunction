# @s (objet au sol : arme du jeu) jeté par un joueur de la partie : gardé par le balayage des objets (survie/tick)
execute store success score $zk mg.st on origin if entity @s[tag=mg.play]
execute if score $zk mg.st matches 1 run tag @s add mg.keep
