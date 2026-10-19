# Chaque tick : recharges des compétences, pièges, météores
scoreboard players remove @a[tag=mg.olw,scores={mg.olc0=1..}] mg.olc0 1
scoreboard players remove @a[tag=mg.olw,scores={mg.olc1=1..}] mg.olc1 1
scoreboard players remove @a[tag=mg.olw,scores={mg.olc2=1..}] mg.olc2 1
scoreboard players remove @a[tag=mg.olw,scores={mg.olc3=1..}] mg.olc3 1
scoreboard players remove @a[tag=mg.olw,scores={mg.olc4=1..}] mg.olc4 1
execute as @e[type=minecraft:marker,tag=mg.oltrap] at @s if entity @e[tag=mg.olm,distance=..1.4] run function mg:ombre/cl/trap_fire
execute as @e[type=minecraft:marker,tag=mg.olmeteor] at @s run function mg:ombre/cl/meteor
function mg:ombre/dmg_tick
