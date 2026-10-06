# @s = joueur : placé sur la ligne de son regard, 10 blocs derrière le pion actif ; seule la position est imposée, la rotation reste libre
execute at @e[type=minecraft:armor_stand,tag=mg.mpfocus,limit=1] rotated as @s positioned ~ ~1.4 ~ positioned ^ ^ ^-10 run tp @s ~ ~ ~
