execute store result entity @n[tag=mime_stand,distance=0..] Pose.LeftLeg[0] float 1 run random value -50..50
execute store result entity @n[tag=mime_stand,distance=0..] Pose.LeftLeg[1] float 1 run random value 0..180
execute store result entity @n[tag=mime_stand,distance=0..] Pose.LeftLeg[2] float 1 run random value -30..0

execute store result entity @n[tag=mime_stand,distance=0..] Pose.RightLeg[0] float 1 run random value -50..50
execute store result entity @n[tag=mime_stand,distance=0..] Pose.RightLeg[1] float 1 run random value 180..360
execute store result entity @n[tag=mime_stand,distance=0..] Pose.RightLeg[2] float 1 run random value 0..30

execute store result entity @n[tag=mime_stand,distance=0..] Pose.LeftArm[0] float 1 run random value 220..360
execute store result entity @n[tag=mime_stand,distance=0..] Pose.LeftArm[1] float 1 run random value 270..360

execute store result entity @n[tag=mime_stand,distance=0..] Pose.RightArm[0] float 1 run random value 220..360
execute store result entity @n[tag=mime_stand,distance=0..] Pose.RightArm[1] float 1 run random value 0..90

#data merge entity @n[tag=mime_stand] {Pose:{Head:[-40f,0f,0f]}}
#execute store result entity @n[tag=mime_stand] Pose.Head[2] float 1 run random value -10..10
