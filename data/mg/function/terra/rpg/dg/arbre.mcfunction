# Cœur de l'Arbre-Mère : chaque seconde pendant le combat
execute positioned 55.5 102 -177.5 run bossbar set mg:trdg0 players @a[tag=mg.tvw,distance=..40]
execute store result bossbar mg:trdg0 value run data get entity @e[tag=mg.trdg_arbre,limit=1] Health
