# Forteresse Bob-omb : fin
function mg:kart/t3/fl_remove
data modify storage mg:kart built3 set value 1b
tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Arène Forteresse Bob-omb construite.","color":"green"}]
