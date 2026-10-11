# Événements surprises (chaque tick, $setup 1)
scoreboard players add $evtk mg.st 1
execute if score $evtk mg.st matches 20.. run function mg:lobby/ev/second
execute if score $evon mg.st matches 1 run function mg:lobby/ev/e1_tick
execute if score $evon mg.st matches 3 as @e[type=minecraft:interaction,tag=mg.evti] if data entity @s interaction run function mg:lobby/ev/e3_click
