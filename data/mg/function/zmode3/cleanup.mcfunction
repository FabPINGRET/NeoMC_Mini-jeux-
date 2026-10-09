scoreboard players set $zpts mg.st 0
function mg:zm3/kill_all
execute as @a[tag=mg.zjug] run attribute @s minecraft:max_health base set 20
tag @a remove mg.zjug
tag @a remove mg.zsc
tag @a remove mg.zdead
tag @a remove mg.inf
tag @a remove mg.gtg
execute as @a run function mg:gun/reset
team leave @a[team=mg_green]
effect clear @a[tag=mg.play] minecraft:speed
effect clear @a[tag=mg.play] minecraft:strength
scoreboard players reset * mg.zpt
forceload remove -17 36061 39 36117
schedule clear mg:zmode3/prepare_b
