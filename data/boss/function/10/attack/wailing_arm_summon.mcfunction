execute as @n[tag=allsoul_loc,tag=low,distance=0..] at @s run tag @e[tag=boss_ta_rand,limit=15,sort=nearest,distance=0..] add arm_loc
execute as @n[tag=allsoul_loc,tag=low,distance=0..] at @s run tag @e[tag=boss_ta_rand,limit=5,sort=nearest,distance=0..] remove arm_loc


execute as @e[tag=boss_ta_rand,tag=arm_loc,sort=random,limit=1,distance=0..] run tag @s add arm_4_loc

tag @n[tag=arm_4_loc,distance=0..] remove arm_loc

execute as @e[tag=boss_ta_rand,tag=arm_loc,sort=random,limit=1,distance=0..] run tag @s add arm_7_loc

tag @n[tag=arm_7_loc,distance=0..] remove arm_loc

execute as @e[tag=boss_ta_rand,tag=arm_loc,sort=random,limit=1,distance=0..] run tag @s add arm_9_loc

tag @n[tag=arm_9_loc,distance=0..] remove arm_loc
tag @e[tag=boss_ta_rand,distance=0..] remove arm_loc


execute as @n[tag=arm_4_loc,distance=0..] at @s run function boss:10/arm/arm_4
execute as @n[tag=arm_7_loc,distance=0..] at @s run function boss:10/arm/arm_7
execute as @n[tag=arm_9_loc,distance=0..] at @s run function boss:10/arm/arm_9

tag @e[tag=boss_ta_rand,distance=0..] remove arm_4_loc
tag @e[tag=boss_ta_rand,distance=0..] remove arm_7_loc
tag @e[tag=boss_ta_rand,distance=0..] remove arm_9_loc

execute as @n[tag=allsoul_arm,tag=4,distance=0..] at @s run tp @s ~ 220 ~
execute as @n[tag=allsoul_arm,tag=7,distance=0..] at @s run tp @s ~ 223 ~
execute as @n[tag=allsoul_arm,tag=9,distance=0..] at @s run tp @s ~ 225 ~

execute as @e[tag=allsoul_arm,distance=0..] at @s run particle minecraft:sculk_soul ~ 217 ~ 0.4 0.1 0.4 0.1 100
execute as @e[tag=allsoul_arm,distance=0..] at @s run playsound minecraft:block.trial_spawner.spawn_mob hostile @a[tag=mg.flw] ~ ~ ~ 3 1
