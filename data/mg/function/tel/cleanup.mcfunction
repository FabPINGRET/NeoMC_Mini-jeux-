# Fin de partie Téléphone
function mg:tel/fl_remove
tag @a remove mg.tdone
scoreboard players reset @a mg.ti
scoreboard players reset @a mg.tc
scoreboard players reset @a mg.tpt
clear @a minecraft:writable_book
data remove storage mg:tel ch
