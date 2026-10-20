# Coup de couteau (@s = victime ; l'attaquant porte mg.tmsh) : 1 dégât, frag si les PV sont épuisés
scoreboard players set $tmd mg.st 1
function mg:tdm/hit
execute if score @s mg.tmhp matches ..0 run function mg:tdm/frag
