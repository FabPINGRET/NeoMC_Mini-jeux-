# Mine abandonnée : chaque seconde pendant le combat
execute positioned -224.5 65 -54.5 run bossbar set mg:trdg2 players @a[tag=mg.tvw,distance=..40]
execute store result bossbar mg:trdg2 value run data get entity @e[tag=mg.trdg_mine,limit=1] Health
