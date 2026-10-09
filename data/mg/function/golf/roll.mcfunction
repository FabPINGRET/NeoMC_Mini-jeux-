# Au sol en fin de tick : frottement selon la surface, point sec mémorisé, arrêt sous le seuil
tag @s add mg.gfg
function mg:golf/surf
scoreboard players operation @s mg.gfu *= $gff mg.st
scoreboard players operation @s mg.gfu /= #gf1000 mg.st
scoreboard players operation @s mg.gfw *= $gff mg.st
scoreboard players operation @s mg.gfw /= #gf1000 mg.st
execute unless block ~ ~-0.05 ~ #minecraft:leaves unless block ~ ~-0.05 ~ #minecraft:logs run function mg:golf/dry
function mg:golf/speed
execute if score $gfsp mg.st matches ..24 if score @s mg.gfv matches -60..60 run function mg:golf/stop
