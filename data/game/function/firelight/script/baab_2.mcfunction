execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"\n<"},{"text":"Spoom-Ee IV","color":"#D47453"},{"text":"> Go exploded, world!","color":"white"},{"text":" ⇒","color":"light_purple"}]

execute at @n[tag=spoom-ee4,distance=0..] run playsound minecraft:entity.armadillo.death neutral @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] ~ ~ ~ 2 0.7

particle minecraft:explosion_emitter 9898 61 -134
particle minecraft:explosion_emitter 9898 61 -129

playsound minecraft:entity.generic.explode neutral @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] 9898 60 -131.5 2 0.7

function game:firelight/exit/all

fill 9900 59 -137 9898 64 -126 air
fill 9898 65 -136 9900 65 -127 air
fill 9900 66 -135 9898 66 -128 air

schedule function floaty:sched/game/firelight/script/baab_3 5s replace
