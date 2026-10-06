# Joueur touché (@s) : spectateur sur place pendant 3 s, puis réapparition ailleurs (voir dead_tick)
scoreboard players set @s mg.ks 0
tag @s add mg.qdd
tag @s add mg.prot
scoreboard players set @s mg.qp 999
scoreboard players set @s mg.pt 60
scoreboard players set @s mg.deaths 0
gamemode spectator @s
title @s title [{"text":"☠","color":"red"}]
