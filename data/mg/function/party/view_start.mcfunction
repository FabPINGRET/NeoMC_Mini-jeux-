# Vue du ciel sur la carte pendant 6 s (@s) : refusée pendant son propre tour
execute if entity @s[tag=mg.mpcur] run return run tellraw @s [{"text":"C'est ton tour : la carte attendra !","color":"red"}]
tag @s add mg.mpview
scoreboard players set @s mg.mpv 120
gamemode spectator @s
tp @s 0.5 200 15000.5 0 90
title @s actionbar [{"text":"🗺 La carte du plateau : retour dans 6 s","color":"gold"}]
