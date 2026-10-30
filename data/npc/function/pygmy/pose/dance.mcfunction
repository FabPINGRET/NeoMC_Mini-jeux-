execute store result entity @n[tag=pygmy,tag=dancer,tag=leader,distance=0..] Pose.LeftLeg[0] float 1 run random value -70..70
execute store result entity @n[tag=pygmy,tag=dancer,tag=leader,distance=0..] Pose.LeftLeg[1] float 1 run random value -20..200
execute store result entity @n[tag=pygmy,tag=dancer,tag=leader,distance=0..] Pose.LeftLeg[2] float 1 run random value -50..20

execute store result entity @n[tag=pygmy,tag=dancer,tag=leader,distance=0..] Pose.RightLeg[0] float 1 run random value -70..70
execute store result entity @n[tag=pygmy,tag=dancer,tag=leader,distance=0..] Pose.RightLeg[1] float 1 run random value 160..380
execute store result entity @n[tag=pygmy,tag=dancer,tag=leader,distance=0..] Pose.RightLeg[2] float 1 run random value -20..50

execute store result entity @n[tag=pygmy,tag=dancer,tag=leader,distance=0..] Pose.LeftArm[0] float 1 run random value 200..380
execute store result entity @n[tag=pygmy,tag=dancer,tag=leader,distance=0..] Pose.LeftArm[1] float 1 run random value 250..380

execute store result entity @n[tag=pygmy,tag=dancer,tag=leader,distance=0..] Pose.RightArm[0] float 1 run random value 200..380
execute store result entity @n[tag=pygmy,tag=dancer,tag=leader,distance=0..] Pose.RightArm[1] float 1 run random value -20..110

data merge entity @n[tag=pygmy,tag=dancer,tag=leader,distance=0..] {Pose:{Head:[1f,1f,1f]}}

execute store result entity @n[tag=pygmy,tag=dancer,tag=leader,distance=0..] Pose.Head[1] float 1 run random value -60..60
execute store result entity @n[tag=pygmy,tag=dancer,tag=leader,distance=0..] Pose.Head[2] float 1 run random value -30..30


execute as @e[tag=pygmy,tag=dancer,tag=!leader,distance=0..] run data modify entity @s Pose set from entity @n[tag=pygmy,tag=dancer,tag=leader,distance=0..] Pose
