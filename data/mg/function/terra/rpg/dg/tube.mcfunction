# Tube de lave : chaque seconde pendant le combat
execute positioned -23.5 90 186.5 run bossbar set mg:trdg3 players @a[tag=mg.tvw,distance=..40]
execute store result bossbar mg:trdg3 value run data get entity @e[tag=mg.trdg_tube,limit=1] Health
