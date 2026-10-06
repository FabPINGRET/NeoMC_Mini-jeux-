# Mouton spécial « mitraillette » (@s = le mouton qui vient d'être lancé) : insensible à ses propres explosions
tag @s add mg.k
tag @s add mg.k_mitra
data modify entity @s Invulnerable set value 1b
data modify entity @s Color set value 8b
data modify entity @s CustomName set value {text:"Mitraillette",color:"gray",bold:true}
data modify entity @s CustomNameVisible set value 1b
title @a[tag=mg.play] actionbar [{"text":"▮ Mouton MITRAILLETTE en approche : 3 explosions d'affilée !","color":"gray"}]
