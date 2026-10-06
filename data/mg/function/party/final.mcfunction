# Fin de la Mini Party : vainqueur = le plus d'étoiles, puis (à égalité) le plus de pièces ; classement trié
scoreboard players set $mph mg.st 9
execute unless entity @a[tag=mg.mpp] run return run function mg:core/draw

# 1. Meilleur nombre d'étoiles, puis meilleures pièces parmi ceux qui l'ont
scoreboard players set $bs mg.st -1
execute as @a[tag=mg.mpp] if score @s mg.mpk > $bs mg.st run scoreboard players operation $bs mg.st = @s mg.mpk
scoreboard players set $bc mg.st -1
execute as @a[tag=mg.mpp] if score @s mg.mpk = $bs mg.st if score @s mg.mpm > $bc mg.st run scoreboard players operation $bc mg.st = @s mg.mpm
tag @a remove mg.mpwin
execute as @a[tag=mg.mpp] if score @s mg.mpk = $bs mg.st if score @s mg.mpm = $bc mg.st run tag @s add mg.mpwin

# 2. Classement complet, du premier au dernier
tellraw @a [{"text":"\n★ RÉSULTATS DE LA MINI PARTY ★","color":"gold","bold":true}]
tag @a remove mg.mprk
scoreboard players set $rk mg.st 0
function mg:party/rank_next

# 3. Victoire
execute as @a[tag=mg.mpwin] run function mg:party/win
tag @a remove mg.mprk
