execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"\n<"},{"text":"Spoom-Ee IV","color":"#D47453"},{"text":"> Becometh exploded!","color":"white"},{"text":" ⇒","color":"light_purple"}]

particle minecraft:explosion_emitter 9899 59 -129
playsound minecraft:entity.generic.explode neutral @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] 9899 59 -129 2 0.7

function game:firelight/exit/pim_the_lesser

execute at @n[tag=spoom-ee4,distance=0..] run playsound minecraft:entity.armadillo.death neutral @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] ~ ~ ~ 2 0.7

schedule function floaty:sched/game/firelight/script/bbaa_1 5s replace
