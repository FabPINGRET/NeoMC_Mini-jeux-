# Toiles posées par les monstres : retirées après 3 s
scoreboard players remove @e[type=minecraft:marker,tag=mg.olweb] mg.olst 1
execute as @e[type=minecraft:marker,tag=mg.olweb,scores={mg.olst=..0}] at @s run function mg:ombre/m/web_end
