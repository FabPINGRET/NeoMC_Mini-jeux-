# Un œuf vient d'être lancé (@s = l'œuf, à sa position) : on le marque ; le tireur = joueur le plus proche
tag @s add mg.eg
execute as @p[tag=mg.play,distance=..3] run function mg:splegg/shoot
