# Une meute sur un point d'apparition entre 24 et 64 blocs d'un colon (aucun à moins de 22)
scoreboard players set $tvpk mg.st 5
tag @e[tag=mg.trok] remove mg.trok
execute as @e[type=minecraft:marker,tag=mg.tvsp] at @s if entity @a[tag=mg.tvout,gamemode=adventure,distance=24..64] unless entity @a[tag=mg.tvw,distance=..22] run tag @s add mg.trok
# un seul point tiré parmi les points possibles (une condition « if score » serait évaluée pour tous avant la première apparition)
execute as @e[tag=mg.trok,sort=random,limit=1] at @s run function mg:terra/pack_at
tag @e[tag=mg.trok] remove mg.trok
