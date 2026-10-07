# Royaume Koopa : fin
function mg:kart/t2/fl_remove
data modify storage mg:kart built2 set value 1b
tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Circuit Royaume Koopa construit.","color":"green"}]
