# @s (dinosaure) pris dans l'onde : dégâts, ralenti, repoussé (sauf les géants)
damage @s 3 minecraft:sonic_boom by @a[tag=mg.tvsrc,limit=1]
effect give @s minecraft:slowness 4 2 true
execute if entity @s[tag=mg.tvbig] run return 0
execute if entity @s[tag=mg.tvcarno] facing entity @a[tag=mg.tvsrc,limit=1] feet rotated ~180 -20 positioned 0.0 0.0 0.0 summon minecraft:marker run function mg:terra/vec {d:0.9}
execute unless entity @s[tag=mg.tvcarno] facing entity @a[tag=mg.tvsrc,limit=1] feet rotated ~180 -25 positioned 0.0 0.0 0.0 summon minecraft:marker run function mg:terra/vec {d:1.8}
function mg:terra/push
