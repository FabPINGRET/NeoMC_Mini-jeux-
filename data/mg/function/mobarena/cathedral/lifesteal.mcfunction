# Récompense de l'advancement cathedral_hit (@s = joueur frappé par le Comte) : life-steal
advancement revoke @s only mg:cathedral_hit
execute as @e[tag=mg.boss,limit=1] run effect give @s minecraft:instant_health 1 3 true
execute at @e[tag=mg.boss,limit=1] run particle minecraft:heart ~ ~2.5 ~ 0.5 0.6 0.5 0 6
execute at @s run particle minecraft:damage_indicator ~ ~1 ~ 0.3 0.4 0.3 0.1 6
