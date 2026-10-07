# En étoile : les karts touchés partent en tête-à-queue
execute as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s as @e[type=minecraft:block_display,tag=mg.kart,tag=!mg.kk,distance=..1.8] run function mg:kart/owner_hit
