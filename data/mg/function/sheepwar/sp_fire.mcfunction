# Mouton spécial « Mouton de feu » (@s = le mouton qui vient d'être lancé)
tag @s add mg.k
tag @s add mg.k_fire
data modify entity @s Color set value 1b
data modify entity @s CustomName set value {text:"Mouton de feu",color:"gold"}
data modify entity @s CustomNameVisible set value 1b
title @a[tag=mg.play] actionbar [{"text":"♨ Mouton de feu en approche","color":"gold"}]
