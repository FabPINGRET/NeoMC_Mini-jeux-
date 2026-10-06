# Ramène au point de vue ceux qui se sont trop éloignés
tag @a[tag=mg.play] add mg.bfar
execute as @e[type=minecraft:marker,tag=mg.bpm] if score @s mg.bi = $bbk mg.st at @s run tag @a[tag=mg.bfar,distance=..55] remove mg.bfar
execute as @e[type=minecraft:marker,tag=mg.bpm] if score @s mg.bi = $bbk mg.st at @s run tp @a[tag=mg.bfar] ~ ~12 ~-30 facing ~ ~8 ~
tag @a remove mg.bfar
