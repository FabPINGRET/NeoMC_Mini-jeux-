execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"\n<"},{"text":"Guathman","color":"red"},{"text":"> Young master, I'm going to stop you right there. Just go home. You need to learn to take care of your hygiene.","color":"white"},{"text":" ⇒","color":"light_purple"}]

execute at @n[tag=guathman,distance=0..] run playsound minecraft:entity.armadillo.death neutral @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] ~ ~ ~ 2 0.5

schedule function floaty:sched/game/firelight/script/baba_1 10s replace
