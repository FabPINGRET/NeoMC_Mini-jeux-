# Monte une marche d'un bloc (en roulant) : perd 40 % de sa vitesse
scoreboard players operation @s mg.gfy /= #gf1000 mg.st
scoreboard players add @s mg.gfy 1
scoreboard players operation @s mg.gfy *= #gf1000 mg.st
execute store result entity @s Pos[1] double 0.001 run scoreboard players get @s mg.gfy
scoreboard players set $gfk mg.st 6
scoreboard players operation @s mg.gfu *= $gfk mg.st
scoreboard players operation @s mg.gfu /= #gf10 mg.st
scoreboard players operation @s mg.gfw *= $gfk mg.st
scoreboard players operation @s mg.gfw /= #gf10 mg.st
