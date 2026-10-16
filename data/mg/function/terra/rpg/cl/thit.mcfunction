# prédateur touché par la tourelle (dégâts attribués au propriétaire)
scoreboard players operation $own mg.st = @e[tag=mg.trcur,limit=1] mg.tvo
tag @a remove mg.trtown
execute as @a[tag=mg.tvw] if score @s mg.tvpid = $own mg.st run tag @s add mg.trtown
execute if entity @e[tag=mg.trcur,tag=mg.trtx] run return run damage @s 8 minecraft:player_attack by @a[tag=mg.trtown,limit=1]
damage @s 5 minecraft:player_attack by @a[tag=mg.trtown,limit=1]
particle minecraft:crit ~ ~1 ~ 0.3 0.3 0.3 0.2 8
