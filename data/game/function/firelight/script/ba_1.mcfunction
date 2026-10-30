execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"\n<"},{"text":"Narrator","color":"#D47453"},{"text":"> Spoom-Ee decided to find his father's ghost and ask him how to be a good king. So he set off down the road to where he figured ghosts must go: the Caverns of Froun. At the entrance, he met a mysterious gatekeeper...","color":"white"},{"text":" ⇒","color":"light_purple"}]

execute at @n[tag=narrator,distance=0..] run playsound minecraft:entity.armadillo.death neutral @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] ~ ~ ~ 2 0.5

schedule function floaty:sched/game/firelight/script/ba_2 11s replace
