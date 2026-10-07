# Circuit : fin
function mg:kart/fl_remove
data modify storage mg:kart built set value 1b
tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Circuit Champignon construit.","color":"green"}]
