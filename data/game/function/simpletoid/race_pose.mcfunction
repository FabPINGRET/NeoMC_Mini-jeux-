data modify entity @s Pose set value {RightArm:[1,0,0],LeftArm:[1,0,0],LeftLeg:[1,0,0],RightLeg:[1,0,0]}
execute store result entity @s Pose.LeftLeg[0] float 1 run random value -90..90
execute store result entity @s Pose.RightLeg[0] float 1 run random value -90..90
execute store result entity @s Pose.LeftArm[0] float 1 run random value -120..120
execute store result entity @s Pose.RightArm[0] float 1 run random value -120..120
