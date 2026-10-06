# Barre de vie du boss (chaque tick) : suit la santé du boss, disparaît à sa mort
execute unless entity @e[tag=mg.boss] run return run bossbar set mg:boss visible false
bossbar set mg:boss players @a
execute store result bossbar mg:boss value run data get entity @e[tag=mg.boss,limit=1] Health 1
bossbar set mg:boss visible true
