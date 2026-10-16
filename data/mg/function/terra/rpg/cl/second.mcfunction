# Chaque seconde : tourelles, soins du scientifique (toutes les 5 s)
execute as @e[type=minecraft:marker,tag=mg.trtm] at @s run function mg:terra/rpg/cl/turret_one
execute if score $trq3 mg.st matches 0 as @a[tag=mg.tvw,scores={mg.trcl=3}] at @s run effect give @a[tag=mg.tvw,distance=..6] minecraft:regeneration 3 0 true
