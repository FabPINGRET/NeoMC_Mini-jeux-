# Chaque seconde : les zombies dans l'enclos d'une fenêtre arrachent une planche ; zombie coincé = renvoyé à une apparition
execute if score $zph mg.st matches 1 as @e[type=minecraft:marker,tag=mg.zwin,scores={mg.zws=1..}] at @s if entity @e[tag=mg.zz,distance=..3.6] run function mg:zx/win_hit
execute if score $zph mg.st matches 1 as @e[tag=mg.zz] at @s run function mg:zx/stuck
