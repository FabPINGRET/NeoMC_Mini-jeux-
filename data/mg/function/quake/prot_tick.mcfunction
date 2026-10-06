# Invincibilité (@s = joueur protégé)
scoreboard players remove @s mg.qp 1
execute if score @s mg.qp matches ..0 run tag @s remove mg.prot
execute at @s run particle minecraft:end_rod ~ ~1 ~ 0.3 0.6 0.3 0 1
