# Compte à rebours de réapparition (@s = joueur éliminé)
scoreboard players remove @s mg.pt 1
execute if score @s mg.pt matches 41..60 run title @s actionbar [{"text":"☠ Réapparition dans 3...","color":"gray"}]
execute if score @s mg.pt matches 21..40 run title @s actionbar [{"text":"☠ Réapparition dans 2...","color":"gray"}]
execute if score @s mg.pt matches 1..20 run title @s actionbar [{"text":"☠ Réapparition dans 1...","color":"gold"}]
execute if score @s mg.pt matches ..0 run function mg:quake/respawn
