# Royaume Koopa : fin
function mg:kart/t2/fl_remove
data modify storage mg:kart built2 set value 1b
execute unless data storage mg:kart built3 run schedule function mg:kart/t3/build 3s
tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Circuit Royaume Koopa construit.","color":"green"}]
