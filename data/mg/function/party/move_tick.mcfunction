# Déplacement case par case (une case toutes les 10 ticks)
scoreboard players remove $mpw mg.st 1
execute if score $mpw mg.st matches 1.. run return 0
scoreboard players set $mpw mg.st 10
execute as @a[tag=mg.mpcur] run function mg:party/step
execute unless entity @a[tag=mg.mpcur] run function mg:party/next_turn
