execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"\n<"},{"text":"Spoom-Ee III","color":"#D47453"},{"text":"> Don't you remember? We were visiting a distant world and you exploded it! That's how I died.","color":"white"}]
execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"<"},{"text":"Spoom-Ee IV","color":"#D47453"},{"text":"> Oh, yeah! Just like this...","color":"white"},{"text":" ⇒","color":"light_purple"}]


execute at @n[tag=spoom-ee3,distance=0..] run playsound minecraft:entity.armadillo.death neutral @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] ~ ~ ~ 2 0.5

schedule function floaty:sched/game/firelight/script/baab_2 8s replace
