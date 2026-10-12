# Chaque seconde : les zombies collés à une fenêtre arrachent une planche
execute if score $zph mg.st matches 1 as @e[type=minecraft:marker,tag=mg.zwin,scores={mg.zws=1..}] at @s if entity @e[tag=mg.zz,distance=..2.3] run function mg:zx/win_hit
