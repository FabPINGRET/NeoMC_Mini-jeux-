$function mg:ombre/cl/hit {d:$(d)}
effect give @s minecraft:slowness 2 2 true
execute unless entity @s[tag=mg.olbig] facing entity @a[tag=mg.olcast,limit=1] feet rotated ~180 -20 positioned 0.0 0.0 0.0 summon minecraft:marker run function mg:ombre/vec {d:1.2}
execute unless entity @s[tag=mg.olbig] run function mg:ombre/push
