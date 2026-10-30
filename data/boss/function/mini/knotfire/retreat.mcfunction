execute at @n[tag=knotfire_boss,distance=0..] run playsound minecraft:entity.creaking.unfreeze hostile @a[tag=mg.flw] ~ ~ ~ 1 0.1

tp @n[tag=knotfire_boss,distance=0..] -10697 41 89

fill -10704 72 96 -10690 73 82 air

tp @n[tag=knotfire_statue,tag=crashed,distance=0..] @n[tag=knotfire_run_dest,distance=0..]

execute as @e[tag=knotfire_statue,distance=0..] run function boss:mini/knotfire/pose/blank
execute as @e[tag=knotfire_statue,distance=0..] at @s facing -10697 72 89 run tp @s ~ ~ ~ ~ ~

tag @e[tag=knotfire_statue,distance=0..] remove crashed
kill @e[tag=knotfire_run_dest,distance=0..]

setblock -10682 67 81 minecraft:redstone_block
setblock -10680 67 89 minecraft:redstone_block
setblock -10682 67 97 minecraft:redstone_block
setblock -10689 67 104 minecraft:redstone_block
setblock -10697 67 106 minecraft:redstone_block
setblock -10705 67 104 minecraft:redstone_block
setblock -10712 67 97 minecraft:redstone_block
setblock -10714 67 89 minecraft:redstone_block
setblock -10712 67 81 minecraft:redstone_block
setblock -10705 67 74 minecraft:redstone_block
setblock -10697 67 72 minecraft:redstone_block
setblock -10689 67 74 minecraft:redstone_block

execute positioned -10697 72 89 run kill @e[tag=walking_statue,distance=..30]
