bossbar set boss:knotfire value 150
bossbar set boss:knotfire color green
bossbar set boss:knotfire players

tag @e[tag=knotfire_statue,distance=0..] remove active
function boss:mini/knotfire/arena/reset_statues

kill @n[tag=knotfire_boss,distance=0..]

#STOP TICK
setblock -10715 55 103 air
fill -10712 55 70 -10715 54 68 air replace minecraft:redstone_block

fill -10690 73 82 -10704 72 96 air
tag @e[tag=knotfire_statue,distance=0..] remove active
tag @e[tag=knotfire_statue,distance=0..] remove crashed

fill -10714 72 72 -10680 73 106 suspicious_sand replace minecraft:brown_glazed_terracotta
fill -10714 72 72 -10680 73 106 suspicious_sand replace minecraft:cyan_glazed_terracotta
fill -10714 61 72 -10680 64 106 air replace redstone_block

setblock -10715 54 98 air
execute as @n[tag=knotfire_boss_stand,distance=0..] at @s run tp @s -10697 72 89 -90 0

fill -10714 72 72 -10680 73 106 minecraft:cut_sandstone replace minecraft:suspicious_sand
execute positioned -10697 72 89 run kill @e[tag=walking_statue,distance=..30]
