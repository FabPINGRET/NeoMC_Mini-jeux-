playsound minecraft:entity.creaking.unfreeze hostile @a[tag=mg.flw] -10697 71 89 2 0.1

setblock -10715 54 98 air
execute as @n[tag=knotfire_boss_stand,distance=0..] at @s run tp @s -10697 54 89 -90 0
fill -10714 72 72 -10680 73 106 minecraft:suspicious_sand replace minecraft:cut_sandstone
setblock -10715 55 103 minecraft:redstone_block
setblock -10715 55 69 minecraft:redstone_block

bossbar set boss:knotfire color green
bossbar set boss:knotfire players @a[tag=mg.flw]

schedule function floaty:sched/boss/mini/knotfire/attack/repo_1 60t
setblock -10679 54 70 minecraft:redstone_block

function boss:mini/knotfire/arena/start_sus_sand_check

function music:miniboss

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
