# Rend les endermen hostiles envers le joueur le plus proche (isolé ; clés NBT selon la version)
execute as @e[type=minecraft:enderman,tag=mg.agro] run data modify entity @s AngryAt set from entity @p[tag=mg.play] UUID
execute as @e[type=minecraft:enderman,tag=mg.agro] run data modify entity @s angry_at set from entity @p[tag=mg.play] UUID
