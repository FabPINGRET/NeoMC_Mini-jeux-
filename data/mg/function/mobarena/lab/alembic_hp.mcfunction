# PV des alambics (isolé)
execute as @e[tag=mg.alembic] run attribute @s minecraft:max_health base set 40
execute as @e[tag=mg.alembic] run data modify entity @s Health set value 40f
