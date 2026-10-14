# @s (dinosaure, à sa position) : son modèle le suit (position et cap)
scoreboard players operation $tvi mg.st = @s mg.tvid
scoreboard players set $tvf mg.st 0
execute rotated ~ 0 as @e[type=minecraft:block_display,tag=mg.tvp,distance=..14] if score @s mg.tvid = $tvi mg.st run function mg:terra/pf
# téléporté (repoussé hors de la colonie…) : modèle cherché partout
execute if score $tvf mg.st matches 0 rotated ~ 0 as @e[type=minecraft:block_display,tag=mg.tvp] if score @s mg.tvid = $tvi mg.st run function mg:terra/pf
