# @s (dinosaure, à sa position) : son modèle le suit. Os du modèle 3D posés sur leurs articulations (image mg.tvak),
# modèle en blocs simplement déplacé. Chaque tick à moins de 32 blocs d’un joueur, toutes les 3 ticks jusqu’à 64, 2 fois par seconde au loin.
scoreboard players operation $tvi mg.st = @s mg.tvid
execute if entity @s[tag=mg.tvrp] if entity @a[tag=mg.tvw,distance=..48] run function mg:terra/an_state
scoreboard players operation $tvak mg.st = @s mg.tvak
execute as @e[type=#mg:tv_part,tag=mg.tvp,distance=..16] if score @s mg.tvid = $tvi mg.st run tag @s add mg.tvc
# téléporté (repoussé hors de la colonie…) : modèle cherché partout
execute unless entity @e[type=#mg:tv_part,tag=mg.tvc,distance=..16,limit=1] as @e[type=#mg:tv_part,tag=mg.tvp] if score @s mg.tvid = $tvi mg.st run tp @s ~ ~ ~
execute unless entity @e[type=#mg:tv_part,tag=mg.tvc,distance=..16,limit=1] as @e[type=#mg:tv_part,tag=mg.tvp,distance=..16] if score @s mg.tvid = $tvi mg.st run tag @s add mg.tvc
tag @e[type=#mg:tv_part,tag=mg.tvc,distance=..16] add mg.tvok
execute if entity @s[tag=mg.tvrp] rotated ~ 0 run function mg:terra/an_sp
execute as @e[type=#mg:tv_part,tag=mg.tvc,distance=..16] unless score @s mg.tvab matches 1.. run tp @s ~ ~ ~ ~ 0
tag @e[type=#mg:tv_part,tag=mg.tvc,distance=..16] remove mg.tvc
