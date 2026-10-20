# Pic du Nid : chaque seconde pendant le combat
execute positioned 228.5 114 24.5 run bossbar set mg:trdg1 players @a[tag=mg.tvw,distance=..40]
execute store result bossbar mg:trdg1 value run data get entity @e[tag=mg.trdg_pic,limit=1] Health
