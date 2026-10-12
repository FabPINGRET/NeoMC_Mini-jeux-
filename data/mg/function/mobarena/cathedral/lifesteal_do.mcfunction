# Le Comte (mort-vivant) se soigne : instant_damage soigne les morts-vivants (instant_health les blesse)
execute as @e[tag=mg.comte,tag=mg.boss,limit=1,sort=nearest] run effect give @s minecraft:instant_damage 1 3 true
execute at @e[tag=mg.comte,tag=mg.boss,limit=1,sort=nearest] run particle minecraft:heart ~ ~2.5 ~ 0.5 0.6 0.5 0 6
execute at @s run particle minecraft:damage_indicator ~ ~1 ~ 0.3 0.4 0.3 0.1 6
