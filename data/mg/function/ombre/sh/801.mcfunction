# @s : améliorer son arme (palier suivant)
execute if score @s mg.olwt matches 8.. run return run tellraw @s {"text":"⚒ « Au-delà, seule la magie de l'Aube peut forger mieux. »","color":"yellow"}
execute if score @s mg.olcl matches 0 run return run tellraw @s {"text":"⚒ « Choisis d'abord ta voie à la guilde. »","color":"red"}
execute if score @s mg.olwt matches 1 run return run function mg:ombre/sh/fw2
execute if score @s mg.olwt matches 2 run return run function mg:ombre/sh/fw3
execute if score @s mg.olwt matches 3 run return run function mg:ombre/sh/fw4
execute if score @s mg.olwt matches 4 run return run function mg:ombre/sh/fw5
execute if score @s mg.olwt matches 5 run return run function mg:ombre/sh/fw6
execute if score @s mg.olwt matches 6 run return run function mg:ombre/sh/fw7
execute if score @s mg.olwt matches 7 run return run function mg:ombre/sh/fw8
