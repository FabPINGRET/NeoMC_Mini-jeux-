# @s : élan = vecteur du marqueur mg.tvv
data modify entity @s Motion set from entity @e[type=minecraft:marker,tag=mg.tvv,limit=1] Pos
kill @e[type=minecraft:marker,tag=mg.tvv]
