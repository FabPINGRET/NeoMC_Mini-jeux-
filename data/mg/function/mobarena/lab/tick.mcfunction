# Le Laboratoire Alchimique — tick
execute as @e[tag=mg.cloud] at @s run function mg:mobarena/lab/cloud_tick
# Petits slimes issus des alambics brisés : supprimés
kill @e[distance=0..,type=minecraft:slime,tag=!mg.alembic]
# Sorcières : toutes les 4 s, un nuage de potion de zone sous le joueur le plus proche d'elles
scoreboard players operation $m1 mg.st = $bt mg.st
scoreboard players operation $m1 mg.st %= $k80 mg.st
execute if score $m1 mg.st matches 0 as @e[type=minecraft:witch,tag=mg.mob] at @p[tag=mg.play] run function mg:mobarena/lab/cloud_small
execute if entity @e[tag=mg.boss] run function mg:mobarena/lab/boss_tick
