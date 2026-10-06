# Récompense de l'advancement cathedral_hit (@s = joueur blessé) : life-steal du Comte s'il est au corps à corps
advancement revoke @s only mg:cathedral_hit
execute if entity @e[tag=mg.boss,distance=..5] run function mg:mobarena/cathedral/lifesteal_do
