# Mouton spécial « Mouton glacé » (@s = le mouton qui vient d'être lancé)
tag @s add mg.k
tag @s add mg.k_freeze
data modify entity @s Color set value 3b
data modify entity @s CustomName set value {text:"Mouton glacé",color:"aqua"}
data modify entity @s CustomNameVisible set value 1b
title @a[tag=mg.play] actionbar [{"text":"❄ Mouton glacé en approche : blocage sur place !","color":"aqua"}]
