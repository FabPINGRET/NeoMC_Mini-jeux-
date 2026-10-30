execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"\n<"},{"text":"Spoom-Ee IV","color":"#D47453"},{"text":"> Gatekeeper, how do I become a good king?","color":"white"}]

execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"<"},{"text":"Guathman","color":"red"},{"text":"> Young master, I wasn't expecting a question like that. I suppose I would start by remembering to wipe.","color":"white"},{"text":" ⇒","color":"light_purple"}]

execute at @n[tag=spoom-ee4,distance=0..] run playsound minecraft:entity.armadillo.death neutral @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] ~ ~ ~ 2 0.7

schedule function floaty:sched/game/firelight/script/babb_1 10s replace
