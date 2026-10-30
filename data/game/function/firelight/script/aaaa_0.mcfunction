execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"\n<"},{"text":"Spoom-Ee IV","color":"#D47453"},{"text":"> Don't worry, you're not going to get exploded.","color":"white"}]
execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"<"},{"text":"Pim the Lesser","color":"#D47453"},{"text":"> Ohh...","color":"white"},{"text":" ⇒","color":"light_purple"}]

data modify entity @n[tag=pim_the_lesser,distance=0..] Pose set value {Head:[30,0,0],RightArm:[-110,-10,0],LeftArm:[-110,10,0]}

execute at @n[tag=spoom-ee4,distance=0..] run playsound minecraft:entity.armadillo.death neutral @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] ~ ~ ~ 2 0.7

schedule function floaty:sched/game/firelight/script/aaaa_1 6s replace
