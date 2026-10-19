execute if entity @s[tag=mg.olund] run function mg:ombre/cl/hit2
$execute unless entity @s[tag=mg.olund] run function mg:ombre/cl/hit {d:$(d)}
particle minecraft:flash{color:[1.0,1.0,0.7,1.0]} ~ ~1 ~ 0 0 0 0 1 force
scoreboard players set $olr mg.st 999
