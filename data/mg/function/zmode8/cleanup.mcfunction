scoreboard players set $zpts mg.st 0
function mg:zx/reset
function mg:zm8/kill_all
execute as @a[tag=mg.zjug] run attribute @s minecraft:max_health base set 20
tag @a remove mg.zjug
tag @a remove mg.zsc
tag @a remove mg.zdead
tag @a remove mg.inf
tag @a remove mg.gtg
tag @a remove mg.zqr
tag @a remove mg.zqrw
tag @a remove mg.zdbl
tag @a remove mg.zst
tag @a remove mg.zmu
execute as @a run function mg:gun/reset
team leave @a[team=mg_green]
effect clear @a[tag=mg.play] minecraft:speed
effect clear @a[tag=mg.play] minecraft:strength
scoreboard players reset * mg.zpt
forceload remove -27 42068 27 42132
schedule clear mg:zmode8/prepare_b
