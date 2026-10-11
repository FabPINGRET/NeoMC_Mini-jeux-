# @s : boîte d'un joueur armé ; propriétaire parti ou plus armé : supprimée
scoreboard players operation $gcid mg.st = @s mg.gcid
execute as @a[tag=mg.gcw] if score @s mg.gcid = $gcid mg.st run tag @s add mg.gcme
execute unless entity @a[tag=mg.gcme] run return run kill @s
execute if entity @a[tag=mg.gchas,tag=mg.gcme] run return run function mg:gun/cl_dup
execute if data entity @s attack on attacker if entity @s[tag=mg.gcme] run function mg:gun/cl_left
execute if data entity @s interaction on target if entity @s[tag=mg.gcme] run function mg:gun/cl_right
data remove entity @s attack
data remove entity @s interaction
execute at @a[tag=mg.gcme,limit=1] anchored eyes positioned ^ ^ ^ run tp @s ~ ~-1.3 ~
tag @a[tag=mg.gcme] add mg.gchas
tag @a remove mg.gcme
