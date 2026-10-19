# Chaque seconde : mana, pluies de flèches, marques, aura du clerc
execute as @a[tag=mg.olw] run function mg:ombre/mana_tick
execute as @e[type=minecraft:marker,tag=mg.olrain] at @s run function mg:ombre/cl/rain
scoreboard players remove @e[tag=mg.olm,scores={mg.olmk=1..}] mg.olmk 1
execute as @e[tag=mg.olm,scores={mg.olmk=..0}] run function mg:ombre/cl/unmark
execute if score $olq100 mg.st matches 0 as @a[tag=mg.olw,scores={mg.olcl=4}] at @s run effect give @a[tag=mg.olw,distance=..6] minecraft:regeneration 3 0 true
