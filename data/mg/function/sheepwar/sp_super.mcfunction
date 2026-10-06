# Mouton spécial « super explosif » (@s = le mouton qui vient d'être lancé)
tag @s add mg.k
tag @s add mg.k_super
data modify entity @s Color set value 4b
data modify entity @s CustomName set value {text:"SUPER explosif",color:"yellow"}
data modify entity @s CustomNameVisible set value 1b
title @a[tag=mg.play] actionbar [{"text":"⚡ Mouton SUPER explosif en approche : il explose dès qu'il se pose !","color":"yellow"}]
