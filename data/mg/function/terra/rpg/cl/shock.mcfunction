# @s (cible) prise dans l'onde
execute if score $rk mg.st matches 1 run damage @s 8 minecraft:player_explosion by @a[tag=mg.trsrc,limit=1]
execute if score $rk mg.st matches 2.. run damage @s 12 minecraft:player_explosion by @a[tag=mg.trsrc,limit=1]
execute unless entity @s[tag=mg.tvbig] facing entity @a[tag=mg.trsrc,limit=1] feet rotated ~180 -25 positioned 0.0 0.0 0.0 summon minecraft:marker run function mg:terra/vec {d:1.4}
execute unless entity @s[tag=mg.tvbig] run function mg:terra/push
