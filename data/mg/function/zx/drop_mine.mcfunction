# @s (objet au sol) : jeté par le joueur dont l'UUID est dans mg:zm du ?
data modify storage mg:zm dt set from storage mg:zm du
execute store success score $zq mg.st run data modify storage mg:zm dt set from entity @s Thrower
execute if score $zq mg.st matches 0 run tag @s add mg.zdi
