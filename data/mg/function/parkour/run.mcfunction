# Coureur (@s = joueur, exécuté à sa position)
# Chrono : démarre quand on quitte le plot de départ
execute if score @s mg.ppt matches -1 unless entity @e[type=minecraft:marker,tag=mg.pks,distance=..2.3] run scoreboard players set @s mg.ppt 0
execute if score @s mg.ppt matches 0.. run scoreboard players add @s mg.ppt 1
# Checkpoints (dans l'ordre)
execute if score @s mg.ppc matches 0 if entity @e[type=minecraft:marker,tag=mg.pkc,scores={mg.t=1},distance=..2.3] run function mg:parkour/cp_1
execute if score @s mg.ppc matches 1 if entity @e[type=minecraft:marker,tag=mg.pkc,scores={mg.t=2},distance=..2.3] run function mg:parkour/cp_2
execute if score @s mg.ppc matches 2 if entity @e[type=minecraft:marker,tag=mg.pkc,scores={mg.t=3},distance=..2.3] run function mg:parkour/cp_3
# Arrivée
execute if score @s mg.ppc matches 3 if entity @e[type=minecraft:marker,tag=mg.pkf,distance=..2.3] run return run function mg:parkour/finish
# Chute
function mg:parkour/fall_check
# Barre d'action
function mg:parkour/bar
