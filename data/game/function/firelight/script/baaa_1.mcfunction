execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"\n<"},{"text":"Spoom-Ee III","color":"#D47453"},{"text":"> You came and found me! You're gonna be a great king, I love you.","color":"white"},{"text":" ⇒","color":"light_purple"}]

data modify entity @n[tag=spoom-ee3,distance=0..] Pose set value {Head:[-30,0,0],RightArm:[-130,0,0],LeftArm:[-130,0,0]}

execute positioned 9897 60 -132 run tp @n[tag=spoom-ee4,distance=0..] ~0.5 ~0.5 ~0.5

execute at @n[tag=spoom-ee3,distance=0..] run playsound minecraft:entity.armadillo.death neutral @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] ~ ~ ~ 2 0.5

schedule function floaty:sched/game/firelight/script/baaa_2 6s replace
