# En étoile : les karts touchés partent en tête-à-queue
tag @s add mg.kme
execute at @s as @a[tag=mg.play,tag=!mg.kme,distance=..1.8] run function mg:kart/hit
tag @s remove mg.kme
