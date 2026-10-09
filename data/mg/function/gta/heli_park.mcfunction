# @s : hélico ou avion sans pilote, il reste sur place
tag @s add mg.gpark
attribute @s minecraft:flying_speed modifier add mg:park -1 add_multiplied_total
data merge entity @s {Motion:[0d,0d,0d]}
