# @s vient de mourir : réapparition à l'hôpital (WASTED) ou au commissariat (BUSTED, tag mg.gbust)
execute if entity @s[tag=mg.gbust] in mg:gta run tp @s 36.5 66 32377.5 0 0
execute unless entity @s[tag=mg.gbust] in mg:gta run tp @s -59.5 66 32377.5 0 0
tag @s remove mg.gbust
