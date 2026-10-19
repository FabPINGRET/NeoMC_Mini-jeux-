# @s : élan = vecteur du marqueur mg.olv
data modify entity @s Motion set from entity @e[type=minecraft:marker,tag=mg.olv,limit=1] Pos
kill @e[type=minecraft:marker,tag=mg.olv]
