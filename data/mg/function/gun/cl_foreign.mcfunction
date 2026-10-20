# @s = attaquant (pas le propriétaire de la boîte) ; la victime est @a[tag=mg.gcme], propriétaire de la boîte frappée
# attaquant armé (mg.gcw) : le ciblage a pris la boîte adverse au lieu de la sienne, son clic gauche est un tir
execute if entity @s[tag=mg.gcw] run return run function mg:gun/cl_left
execute if entity @s[tag=mg.dl] run return run function mg:duel/box_knife
execute if entity @s[tag=mg.play] if score $game mg.st matches 246 run return run function mg:tdm/box_knife
