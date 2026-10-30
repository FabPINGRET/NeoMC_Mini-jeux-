execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"\n<"},{"text":"Spoom-Ee IV","color":"#D47453"},{"text":"> I... have not.","color":"white"}]

execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"<"},{"text":"Guathman","color":"red"},{"text":"> Regretfully, I suspected as much little master. Take this rag; no one unclean is allowed in the Caverns of Froun.","color":"white"},{"text":" ⇒","color":"light_purple"}]

item replace entity @n[tag=guathman,distance=0..] weapon.mainhand with minecraft:rabbit_hide

execute at @n[tag=spoom-ee4,distance=0..] run playsound minecraft:entity.armadillo.death neutral @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] ~ ~ ~ 2 0.7

schedule function floaty:sched/game/firelight/script/bab_1 10s replace
