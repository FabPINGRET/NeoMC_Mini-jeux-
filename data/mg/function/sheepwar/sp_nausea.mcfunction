# Mouton spécial « Mouton nauséeux » (@s = le mouton qui vient d'être lancé)
tag @s add mg.k
tag @s add mg.k_nausea
data modify entity @s Color set value 5b
data modify entity @s CustomName set value {text:"Mouton nauséeux",color:"green"}
data modify entity @s CustomNameVisible set value 1b
title @a[tag=mg.play] actionbar [{"text":"☣ Mouton nauséeux en approche : nausée !","color":"green"}]
