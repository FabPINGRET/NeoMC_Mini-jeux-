# Chaque seconde : pics de glace, pluies de feu, piqué de Nyxar, piliers
scoreboard players remove @e[type=minecraft:marker,tag=mg.olspike] mg.olst 1
scoreboard players remove @e[type=minecraft:marker,tag=mg.olfall] mg.olst 1
scoreboard players remove @e[type=minecraft:marker,tag=mg.oldive] mg.olst 1
execute as @e[type=minecraft:marker,tag=mg.olspike] at @s run particle minecraft:snowflake ~ ~0.2 ~ 0.6 0.1 0.6 0 12
execute as @e[type=minecraft:marker,tag=mg.olfall] at @s run particle minecraft:flame ~ ~6 ~ 0.6 2 0.6 0.02 20 force
execute as @e[type=minecraft:marker,tag=mg.olspike,scores={mg.olst=..0}] at @s run function mg:ombre/boss/spike_hit
execute as @e[type=minecraft:marker,tag=mg.olfall,scores={mg.olst=..0}] at @s run function mg:ombre/boss/fall_hit
execute as @e[type=minecraft:marker,tag=mg.oldive,scores={mg.olst=..0}] at @s run function mg:ombre/boss/dive_hit
function mg:ombre/boss/pill_sec
