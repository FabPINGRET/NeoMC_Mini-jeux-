# Circuit : fin
function mg:kart/t1/fl_remove
data modify storage mg:kart built set value 1b
execute unless data storage mg:kart built2 run schedule function mg:kart/t2/build 3s
tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Circuit Champignon construit.","color":"green"}]
