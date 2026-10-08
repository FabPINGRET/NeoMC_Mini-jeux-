# Fin de la construction (ou de l'effacement)
function mg:sky/fl_secs_off
execute if score $skbm mg.st matches 1 run data modify storage mg:sky built set value 1b
execute if score $skbm mg.st matches 1 run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Élytra : parcours d'anneaux et arène de survie construits.","color":"green"}]
execute if score $skbm mg.st matches 2 run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Élytra : décor effacé.","color":"gray"}]
scoreboard players set $skbm mg.st 0
