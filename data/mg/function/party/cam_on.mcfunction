tag @s remove mg.mpfree
execute unless entity @s[tag=mg.mpview] run function mg:party/rejoin
tellraw @s [{"text":"🎥 Caméra suivie : tourne autour du joueur actif avec la souris.","color":"aqua"}]
