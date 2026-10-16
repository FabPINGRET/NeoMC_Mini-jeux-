# Un groupe de sixer sur un point de la région w (joueur entre 24 et 72 blocs, aucun à moins de 20)
tag @e[tag=mg.trok] remove mg.trok
execute as @e[type=minecraft:marker,tag=mg.trsp_w,tag=mg.trsp_sixer] at @s if entity @a[tag=mg.tvw,distance=24..72] unless entity @a[tag=mg.tvw,distance=..20] run tag @s add mg.trok
execute as @e[tag=mg.trok,sort=random,limit=1] at @s run function mg:terra/rpg/sp/w_sixer_at
tag @e[tag=mg.trok] remove mg.trok
