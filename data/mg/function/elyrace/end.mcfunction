# Fin de la course : gagne le meilleur temps parmi les arrivés encore en ligne (clé mg.xft : temps bonus d'or déduit, puis place d'arrivée)
execute unless entity @a[tag=mg.play,scores={mg.xf=1..}] run return run function mg:core/draw
scoreboard players set #mn mg.st 2147483647
execute as @a[tag=mg.play,scores={mg.xf=1..}] run scoreboard players operation #mn mg.st < @s mg.xft
tag @a remove mg.xw1
execute as @a[tag=mg.play,scores={mg.xf=1..}] if score @s mg.xft = #mn mg.st run tag @s add mg.xw1
execute as @a[tag=mg.xw1,limit=1] run function mg:core/win_player
tag @a remove mg.xw1
