tag @s remove mg.gads
attribute @s minecraft:movement_speed modifier remove mg:aim
title @s[tag=!mg.gtw] clear
execute if entity @s[tag=mg.gscope] run function mg:gta/unscope
