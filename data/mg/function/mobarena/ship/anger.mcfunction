# Rend les endermen hostiles envers le joueur le plus proche pendant 2 min (26.1+ : angry_at + anger_end_time, tick absolu)
execute store result score $eat mg.st run time query gametime
scoreboard players add $eat mg.st 2400
execute as @e[type=minecraft:enderman,tag=mg.agro] run data modify entity @s angry_at set from entity @p[tag=mg.play] UUID
execute as @e[type=minecraft:enderman,tag=mg.agro] store result entity @s anger_end_time long 1 run scoreboard players get $eat mg.st
