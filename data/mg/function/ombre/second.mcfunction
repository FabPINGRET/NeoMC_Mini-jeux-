# Chaque seconde (dimension) : régions, lieux, quêtes, monstres, classes, boss, donjons
execute unless score $olsu mg.st matches 1.. run return 0
effect give @a[tag=mg.olw] minecraft:saturation infinite 0 true
scoreboard players enable @a[tag=mg.olw] mg.oltk
execute as @a[tag=mg.olw,tag=!mg.olcine] at @s run function mg:ombre/region
execute as @a[tag=mg.olw,tag=!mg.olcine] at @s run function mg:ombre/q/gotick
function mg:ombre/ws_tick
execute as @a[tag=mg.olw,tag=!mg.olintro,tag=!mg.olcine,scores={mg.olch=0}] run function mg:ombre/intro_go
execute if score $olq60 mg.st matches 0 run function mg:ombre/pois
execute if score $olq60 mg.st matches 40 run function mg:ombre/pois
execute if score $olq60 mg.st matches 20 as @a[tag=mg.olw,tag=!mg.olcine] at @s run function mg:ombre/hazard
execute if score $olq60 mg.st matches 40 as @a[tag=mg.olw,tag=!mg.olcine] at @s run function mg:ombre/hazard
execute if score $olq100 mg.st matches 0 as @a[tag=mg.olw] run function mg:ombre/achievements
function mg:ombre/m/second
function mg:ombre/cl/second
function mg:ombre/bosses
function mg:ombre/bclean
# entités d'une session précédente restées dans une zone non chargée : retirées
execute as @e[tag=mg.olm] unless score @s mg.olses = $olses mg.st run kill @s
