# @s touché par une balle de la police
execute if score $gcd2 mg.st matches 2 run damage @s 2 minecraft:mob_attack by @e[tag=mg.gcsh,limit=1]
execute if score $gcd2 mg.st matches 3 run damage @s 3 minecraft:mob_attack by @e[tag=mg.gcsh,limit=1]
particle minecraft:damage_indicator ~ ~1.2 ~ 0.2 0.3 0.2 0 2
