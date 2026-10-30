execute as @e[tag=simpletoid,tag=running,distance=0..] unless score @s bool matches 5 run function game:simpletoid/race_pose

execute as @e[tag=simpletoid,tag=running,distance=0..] at @s run playsound minecraft:block.gravel.step block @a[tag=mg.flw] ~ ~ ~ 0.4 1
execute as @e[tag=simpletoid,tag=running,distance=0..] at @s run particle minecraft:block{block_state:"dirt_path"} ~ ~ ~ 0.1 0 0.1 0 1

execute positioned 9957 39 -62 as @e[tag=simpletoid,x=9957,y=39,z=-62,dx=3,dy=1,dz=0] run scoreboard players set @s bool 2
execute positioned 9949 39 -62 as @e[tag=simpletoid,tag=1,x=9949,y=39,z=-62,dx=3,dy=1,dz=0] at @s run tp @s 9949 ~ ~
execute positioned 9949 39 -62 as @e[tag=simpletoid,tag=2,x=9949,y=39,z=-62,dx=3,dy=1,dz=0] at @s run tp @s 9950 ~ ~
execute positioned 9949 39 -62 as @e[tag=simpletoid,tag=3,x=9949,y=39,z=-62,dx=3,dy=1,dz=0] at @s run tp @s 9951 ~ ~
execute positioned 9949 39 -62 as @e[tag=simpletoid,x=9949,y=39,z=-62,dx=3,dy=1,dz=0] run scoreboard players set @s bool 3
execute positioned 9949 39 -52 as @e[tag=simpletoid,x=9949,y=39,z=-52,dx=3,dy=1,dz=0] run scoreboard players set @s bool 4
execute as @e[tag=simpletoid,distance=0..] at @s if score @s bool matches 4 positioned ^ ^ ^-0.4 if block ~ 39 ~ minecraft:white_concrete_powder run scoreboard players set @s bool 5

execute as @e[tag=simpletoid,distance=0..] at @s if score @s bool matches 3 run tp @s ~ ~ ~ 0 0
execute as @e[tag=simpletoid,distance=0..] at @s if score @s bool matches 3 unless entity @e[tag=simpletoid,tag=winner,distance=0..] run function game:simpletoid/rig
execute as @e[tag=simpletoid,distance=0..] at @s if score @s bool matches 5 run tp @s ~ ~ ~ 180 0
execute as @e[tag=simpletoid,distance=0..] at @s if score @s bool matches 5 run tag @s remove running

execute as @n[tag=simpletoid,tag=1,distance=0..] at @s if score @s bool matches 5 unless score simpletoid_winner Value matches 1 run data modify entity @s Pose set value {}
execute as @n[tag=simpletoid,tag=2,distance=0..] at @s if score @s bool matches 5 unless score simpletoid_winner Value matches 2 run data modify entity @s Pose set value {}
execute as @n[tag=simpletoid,tag=3,distance=0..] at @s if score @s bool matches 5 unless score simpletoid_winner Value matches 3 run data modify entity @s Pose set value {}


execute as @n[tag=simpletoid,tag=1,distance=0..] at @s if score @s bool matches 5 if score simpletoid_winner Value matches 0 run data modify entity @s Pose set value {RightArm:[180,0,-30],LeftArm:[180,0,30]}
execute as @n[tag=simpletoid,tag=1,distance=0..] at @s if score @s bool matches 5 if score simpletoid_winner Value matches 0 run scoreboard players set simpletoid_winner Value 1
execute as @n[tag=simpletoid,tag=2,distance=0..] at @s if score @s bool matches 5 if score simpletoid_winner Value matches 0 run data modify entity @s Pose set value {RightArm:[180,0,-30],LeftArm:[180,0,30]}
execute as @n[tag=simpletoid,tag=2,distance=0..] at @s if score @s bool matches 5 if score simpletoid_winner Value matches 0 run scoreboard players set simpletoid_winner Value 2
execute as @n[tag=simpletoid,tag=3,distance=0..] at @s if score @s bool matches 5 if score simpletoid_winner Value matches 0 run data modify entity @s Pose set value {RightArm:[180,0,-30],LeftArm:[180,0,30]}
execute as @n[tag=simpletoid,tag=3,distance=0..] at @s if score @s bool matches 5 if score simpletoid_winner Value matches 0 run scoreboard players set simpletoid_winner Value 3

#STRAIGHTAWAY 1
execute as @e[tag=simpletoid,distance=0..] at @s if score @s bool matches 1 if score @s Value matches 1 run tp @s ~ ~ ~-0.1
execute as @e[tag=simpletoid,distance=0..] at @s if score @s bool matches 1 if score @s Value matches 2 run tp @s ~ ~ ~-0.12
execute as @e[tag=simpletoid,distance=0..] at @s if score @s bool matches 1 if score @s Value matches 3 run tp @s ~ ~ ~-0.14
execute as @e[tag=simpletoid,distance=0..] at @s if score @s bool matches 1 if score @s Value matches 4 run tp @s ~ ~ ~-0.16
execute as @e[tag=simpletoid,distance=0..] at @s if score @s bool matches 1 if score @s Value matches 5 run tp @s ~ ~ ~-0.2

#CURVE 1
execute as @e[tag=simpletoid,tag=1,distance=0..] if score @s bool matches 2 if score @s Value matches 1 as @n[tag=simpletoid_pivot_a,tag=1,distance=0..] at @s run tp @s ~ ~ ~ ~-1.4 0
execute as @e[tag=simpletoid,tag=1,distance=0..] if score @s bool matches 2 if score @s Value matches 2 as @n[tag=simpletoid_pivot_a,tag=1,distance=0..] at @s run tp @s ~ ~ ~ ~-1.6 0
execute as @e[tag=simpletoid,tag=1,distance=0..] if score @s bool matches 2 if score @s Value matches 3 as @n[tag=simpletoid_pivot_a,tag=1,distance=0..] at @s run tp @s ~ ~ ~ ~-1.8 0
execute as @e[tag=simpletoid,tag=1,distance=0..] if score @s bool matches 2 if score @s Value matches 4 as @n[tag=simpletoid_pivot_a,tag=1,distance=0..] at @s run tp @s ~ ~ ~ ~-2 0
execute as @e[tag=simpletoid,tag=1,distance=0..] if score @s bool matches 2 if score @s Value matches 5 as @n[tag=simpletoid_pivot_a,tag=1,distance=0..] at @s run tp @s ~ ~ ~ ~-2.6 0

execute as @e[tag=simpletoid,tag=2,distance=0..] if score @s bool matches 2 if score @s Value matches 1 as @n[tag=simpletoid_pivot_a,tag=2,distance=0..] at @s run tp @s ~ ~ ~ ~-1.4 0
execute as @e[tag=simpletoid,tag=2,distance=0..] if score @s bool matches 2 if score @s Value matches 2 as @n[tag=simpletoid_pivot_a,tag=2,distance=0..] at @s run tp @s ~ ~ ~ ~-1.6 0
execute as @e[tag=simpletoid,tag=2,distance=0..] if score @s bool matches 2 if score @s Value matches 3 as @n[tag=simpletoid_pivot_a,tag=2,distance=0..] at @s run tp @s ~ ~ ~ ~-1.8 0
execute as @e[tag=simpletoid,tag=2,distance=0..] if score @s bool matches 2 if score @s Value matches 4 as @n[tag=simpletoid_pivot_a,tag=2,distance=0..] at @s run tp @s ~ ~ ~ ~-2 0
execute as @e[tag=simpletoid,tag=2,distance=0..] if score @s bool matches 2 if score @s Value matches 5 as @n[tag=simpletoid_pivot_a,tag=2,distance=0..] at @s run tp @s ~ ~ ~ ~-2.6 0

execute as @e[tag=simpletoid,tag=3,distance=0..] if score @s bool matches 2 if score @s Value matches 1 as @n[tag=simpletoid_pivot_a,tag=3,distance=0..] at @s run tp @s ~ ~ ~ ~-1.4 0
execute as @e[tag=simpletoid,tag=3,distance=0..] if score @s bool matches 2 if score @s Value matches 2 as @n[tag=simpletoid_pivot_a,tag=3,distance=0..] at @s run tp @s ~ ~ ~ ~-1.6 0
execute as @e[tag=simpletoid,tag=3,distance=0..] if score @s bool matches 2 if score @s Value matches 3 as @n[tag=simpletoid_pivot_a,tag=3,distance=0..] at @s run tp @s ~ ~ ~ ~-1.8 0
execute as @e[tag=simpletoid,tag=3,distance=0..] if score @s bool matches 2 if score @s Value matches 4 as @n[tag=simpletoid_pivot_a,tag=3,distance=0..] at @s run tp @s ~ ~ ~ ~-2 0
execute as @e[tag=simpletoid,tag=3,distance=0..] if score @s bool matches 2 if score @s Value matches 5 as @n[tag=simpletoid_pivot_a,tag=3,distance=0..] at @s run tp @s ~ ~ ~ ~-2.6 0

execute as @e[tag=simpletoid,tag=4,distance=0..] if score @s bool matches 2 if score @s Value matches 1 as @n[tag=simpletoid_pivot_a,tag=4,distance=0..] at @s run tp @s ~ ~ ~ ~-1.4 0
execute as @e[tag=simpletoid,tag=4,distance=0..] if score @s bool matches 2 if score @s Value matches 2 as @n[tag=simpletoid_pivot_a,tag=4,distance=0..] at @s run tp @s ~ ~ ~ ~-1.6 0
execute as @e[tag=simpletoid,tag=4,distance=0..] if score @s bool matches 2 if score @s Value matches 3 as @n[tag=simpletoid_pivot_a,tag=4,distance=0..] at @s run tp @s ~ ~ ~ ~-1.8 0
execute as @e[tag=simpletoid,tag=4,distance=0..] if score @s bool matches 2 if score @s Value matches 4 as @n[tag=simpletoid_pivot_a,tag=4,distance=0..] at @s run tp @s ~ ~ ~ ~-2 0
execute as @e[tag=simpletoid,tag=4,distance=0..] if score @s bool matches 2 if score @s Value matches 5 as @n[tag=simpletoid_pivot_a,tag=4,distance=0..] at @s run tp @s ~ ~ ~ ~-2.6 0

execute as @e[tag=simpletoid,tag=1,distance=0..] if score @s bool matches 2 as @n[tag=simpletoid_pivot_a,tag=1,distance=0..] at @s positioned ^ ^ ^5 rotated ~-90 0 run tp @n[tag=simpletoid,tag=1,distance=0..] ~ 40 ~ ~ ~
execute as @e[tag=simpletoid,tag=2,distance=0..] if score @s bool matches 2 as @n[tag=simpletoid_pivot_a,tag=2,distance=0..] at @s positioned ^ ^ ^4 rotated ~-90 0 run tp @n[tag=simpletoid,tag=2,distance=0..] ~ 40 ~ ~ ~
execute as @e[tag=simpletoid,tag=3,distance=0..] if score @s bool matches 2 as @n[tag=simpletoid_pivot_a,tag=3,distance=0..] at @s positioned ^ ^ ^3 rotated ~-90 0 run tp @n[tag=simpletoid,tag=3,distance=0..] ~ 40 ~ ~ ~


#STRAIGHTAWAY 2
execute as @e[tag=simpletoid,distance=0..] at @s if score @s bool matches 3 if score @s Value matches 1 run tp @s ~ ~ ~0.1
execute as @e[tag=simpletoid,distance=0..] at @s if score @s bool matches 3 if score @s Value matches 2 run tp @s ~ ~ ~0.12
execute as @e[tag=simpletoid,distance=0..] at @s if score @s bool matches 3 if score @s Value matches 3 run tp @s ~ ~ ~0.14
execute as @e[tag=simpletoid,distance=0..] at @s if score @s bool matches 3 if score @s Value matches 4 run tp @s ~ ~ ~0.16
execute as @e[tag=simpletoid,distance=0..] at @s if score @s bool matches 3 if score @s Value matches 5 run tp @s ~ ~ ~0.2

#CURVE 2
execute as @e[tag=simpletoid,tag=1,distance=0..] if score @s bool matches 4 if score @s Value matches 1 as @n[tag=simpletoid_pivot_b,tag=1,distance=0..] at @s run tp @s ~ ~ ~ ~-1.4 0
execute as @e[tag=simpletoid,tag=1,distance=0..] if score @s bool matches 4 if score @s Value matches 2 as @n[tag=simpletoid_pivot_b,tag=1,distance=0..] at @s run tp @s ~ ~ ~ ~-1.6 0
execute as @e[tag=simpletoid,tag=1,distance=0..] if score @s bool matches 4 if score @s Value matches 3 as @n[tag=simpletoid_pivot_b,tag=1,distance=0..] at @s run tp @s ~ ~ ~ ~-1.8 0
execute as @e[tag=simpletoid,tag=1,distance=0..] if score @s bool matches 4 if score @s Value matches 4 as @n[tag=simpletoid_pivot_b,tag=1,distance=0..] at @s run tp @s ~ ~ ~ ~-2 0
execute as @e[tag=simpletoid,tag=1,distance=0..] if score @s bool matches 4 if score @s Value matches 5 as @n[tag=simpletoid_pivot_b,tag=1,distance=0..] at @s run tp @s ~ ~ ~ ~-2.6 0

execute as @e[tag=simpletoid,tag=2,distance=0..] if score @s bool matches 4 if score @s Value matches 1 as @n[tag=simpletoid_pivot_b,tag=2,distance=0..] at @s run tp @s ~ ~ ~ ~-1.4 0
execute as @e[tag=simpletoid,tag=2,distance=0..] if score @s bool matches 4 if score @s Value matches 2 as @n[tag=simpletoid_pivot_b,tag=2,distance=0..] at @s run tp @s ~ ~ ~ ~-1.6 0
execute as @e[tag=simpletoid,tag=2,distance=0..] if score @s bool matches 4 if score @s Value matches 3 as @n[tag=simpletoid_pivot_b,tag=2,distance=0..] at @s run tp @s ~ ~ ~ ~-1.8 0
execute as @e[tag=simpletoid,tag=2,distance=0..] if score @s bool matches 4 if score @s Value matches 4 as @n[tag=simpletoid_pivot_b,tag=2,distance=0..] at @s run tp @s ~ ~ ~ ~-2 0
execute as @e[tag=simpletoid,tag=2,distance=0..] if score @s bool matches 4 if score @s Value matches 5 as @n[tag=simpletoid_pivot_b,tag=2,distance=0..] at @s run tp @s ~ ~ ~ ~-2.6 0

execute as @e[tag=simpletoid,tag=3,distance=0..] if score @s bool matches 4 if score @s Value matches 1 as @n[tag=simpletoid_pivot_b,tag=3,distance=0..] at @s run tp @s ~ ~ ~ ~-1.4 0
execute as @e[tag=simpletoid,tag=3,distance=0..] if score @s bool matches 4 if score @s Value matches 2 as @n[tag=simpletoid_pivot_b,tag=3,distance=0..] at @s run tp @s ~ ~ ~ ~-1.6 0
execute as @e[tag=simpletoid,tag=3,distance=0..] if score @s bool matches 4 if score @s Value matches 3 as @n[tag=simpletoid_pivot_b,tag=3,distance=0..] at @s run tp @s ~ ~ ~ ~-1.8 0
execute as @e[tag=simpletoid,tag=3,distance=0..] if score @s bool matches 4 if score @s Value matches 4 as @n[tag=simpletoid_pivot_b,tag=3,distance=0..] at @s run tp @s ~ ~ ~ ~-2 0
execute as @e[tag=simpletoid,tag=3,distance=0..] if score @s bool matches 4 if score @s Value matches 5 as @n[tag=simpletoid_pivot_b,tag=3,distance=0..] at @s run tp @s ~ ~ ~ ~-2.6 0

execute as @e[tag=simpletoid,tag=4,distance=0..] if score @s bool matches 4 if score @s Value matches 1 as @n[tag=simpletoid_pivot_b,tag=4,distance=0..] at @s run tp @s ~ ~ ~ ~-1.4 0
execute as @e[tag=simpletoid,tag=4,distance=0..] if score @s bool matches 4 if score @s Value matches 2 as @n[tag=simpletoid_pivot_b,tag=4,distance=0..] at @s run tp @s ~ ~ ~ ~-1.6 0
execute as @e[tag=simpletoid,tag=4,distance=0..] if score @s bool matches 4 if score @s Value matches 3 as @n[tag=simpletoid_pivot_b,tag=4,distance=0..] at @s run tp @s ~ ~ ~ ~-1.8 0
execute as @e[tag=simpletoid,tag=4,distance=0..] if score @s bool matches 4 if score @s Value matches 4 as @n[tag=simpletoid_pivot_b,tag=4,distance=0..] at @s run tp @s ~ ~ ~ ~-2 0
execute as @e[tag=simpletoid,tag=4,distance=0..] if score @s bool matches 4 if score @s Value matches 5 as @n[tag=simpletoid_pivot_b,tag=4,distance=0..] at @s run tp @s ~ ~ ~ ~-2.6 0

execute as @e[tag=simpletoid,tag=1,distance=0..] if score @s bool matches 4 as @n[tag=simpletoid_pivot_b,tag=1,distance=0..] at @s positioned ^ ^ ^5 rotated ~-90 0 run tp @n[tag=simpletoid,tag=1,distance=0..] ~ 40 ~ ~ ~
execute as @e[tag=simpletoid,tag=2,distance=0..] if score @s bool matches 4 as @n[tag=simpletoid_pivot_b,tag=2,distance=0..] at @s positioned ^ ^ ^4 rotated ~-90 0 run tp @n[tag=simpletoid,tag=2,distance=0..] ~ 40 ~ ~ ~
execute as @e[tag=simpletoid,tag=3,distance=0..] if score @s bool matches 4 as @n[tag=simpletoid_pivot_b,tag=3,distance=0..] at @s positioned ^ ^ ^3 rotated ~-90 0 run tp @n[tag=simpletoid,tag=3,distance=0..] ~ 40 ~ ~ ~

#RESPEED

scoreboard players remove simpletoid_respeed Value 1
execute if score simpletoid_respeed Value matches ..0 run function game:simpletoid/respeed
execute if score simpletoid_respeed Value matches ..0 run scoreboard players set simpletoid_respeed Value 20

execute as @n[tag=simpletoid,tag=1,distance=0..] if score @s bool matches 5 as @n[tag=simpletoid,tag=2,distance=0..] if score @s bool matches 5 as @n[tag=simpletoid,tag=3,distance=0..] if score @s bool matches 5 run function game:simpletoid/end
