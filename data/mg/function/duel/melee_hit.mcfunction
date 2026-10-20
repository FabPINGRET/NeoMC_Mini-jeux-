# Coup de couteau (@s = victime ; l'attaquant porte mg.dlsh) : 1 dégât, manche perdue si les PV sont épuisés
scoreboard players set $dld mg.st 1
function mg:duel/hit
execute if score @s mg.dlhp matches ..0 run function mg:duel/round
