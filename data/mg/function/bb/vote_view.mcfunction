# Téléporte tous les participants au point de vue de la construction $bbk
execute as @e[type=minecraft:marker,tag=mg.bpm] if score @s mg.bi = $bbk mg.st at @s run tp @a[tag=mg.play] ~ ~12 ~-30 facing ~ ~8 ~
