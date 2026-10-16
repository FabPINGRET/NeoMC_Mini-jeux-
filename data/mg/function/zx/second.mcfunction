# Chaque seconde : les zombies dans l'enclos d'une fenêtre arrachent une planche ; zombie coincé = renvoyé à une apparition
execute if score $zph mg.st matches 1 as @e[type=minecraft:marker,tag=mg.zwin,scores={mg.zws=1..}] at @s if entity @e[tag=mg.zz,distance=..3.6] run function mg:zx/win_hit
execute if score $zph mg.st matches 1 as @e[tag=mg.zz] at @s run function mg:zx/stuck
execute as @e[type=minecraft:wolf,tag=mg.zz] at @s run particle minecraft:flame ~ ~0.4 ~ 0.25 0.2 0.25 0.01 2
scoreboard players add $zdg mg.st 1
execute if score $zdg mg.st matches 4.. run scoreboard players set $zdg mg.st 0
execute if score $zdg mg.st matches 0 as @e[type=minecraft:wolf,tag=mg.zz] at @s unless entity @a[tag=mg.play,tag=!mg.zdead,distance=..4] run function mg:zx/dog_aggro
