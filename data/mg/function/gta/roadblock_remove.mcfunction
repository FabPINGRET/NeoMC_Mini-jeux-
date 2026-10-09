# @s (marqueur de barrage) : le barrage est levé
execute as @e[type=minecraft:horse,tag=mg.grbc,distance=..6] run function mg:gta/veh_remove
kill @s
