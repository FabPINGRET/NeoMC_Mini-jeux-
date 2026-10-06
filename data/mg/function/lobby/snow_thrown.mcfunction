# Boule de neige lancée au lobby (@s = lanceur, position = lanceur) : on la marque pour détecter ses impacts
scoreboard players reset @s mg.us
tag @e[type=minecraft:snowball,tag=!mg.sn,distance=..8] add mg.sn
