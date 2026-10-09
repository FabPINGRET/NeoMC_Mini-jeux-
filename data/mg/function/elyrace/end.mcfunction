# Fin de la course : gagne le premier arrivé encore en ligne (plus petite place mg.xf) ; les autres sont classés dans le chat
execute unless entity @a[tag=mg.play,scores={mg.xf=1..}] run return run function mg:core/draw
scoreboard players set #mn mg.st 9999
execute as @a[tag=mg.play,scores={mg.xf=1..}] run scoreboard players operation #mn mg.st < @s mg.xf
tag @a remove mg.xw1
execute as @a[tag=mg.play,scores={mg.xf=1..}] if score @s mg.xf = #mn mg.st run tag @s add mg.xw1
execute as @a[tag=mg.xw1,limit=1] run function mg:core/win_player
tag @a remove mg.xw1
