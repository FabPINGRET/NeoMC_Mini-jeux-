# La Forge du Titan — tick
# Petits cubes de magma nés d'une division : comptés et nettoyés comme les autres mobs de l'arène
execute as @e[type=minecraft:magma_cube,tag=!mg.mob,x=-40,y=55,z=10260,dx=80,dy=40,dz=80] run tag @s add mg.mob
# Niveau de lave : un palier toutes les 5 vagues (vagues 6, 11 et 16)
execute if score $wv mg.st matches 6.. if score $lvl mg.st matches 0 run function mg:mobarena/forge/raise1
execute if score $wv mg.st matches 11.. if score $lvl mg.st matches 1 run function mg:mobarena/forge/raise2
execute if score $wv mg.st matches 16.. if score $lvl mg.st matches 2 run function mg:mobarena/forge/raise3
execute as @e[type=minecraft:marker,tag=mg.meteor] at @s run function mg:mobarena/forge/meteor_tick
execute if entity @e[tag=mg.boss] run function mg:mobarena/forge/boss_tick
