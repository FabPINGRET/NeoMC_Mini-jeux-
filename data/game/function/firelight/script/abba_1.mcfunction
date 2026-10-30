execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"\n<"},{"text":"Narrator","color":"#D47453"},{"text":"> Spoom-Ee went home, disgraced by the gatekeeper. He never learned to be a good king.","color":"white"},{"text":"\n\nThe End","color":"dark_aqua","bold":true}]

execute at @n[tag=narrator,distance=0..] run playsound minecraft:entity.armadillo.death neutral @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] ~ ~ ~ 2 0.5

schedule function floaty:sched/game/firelight/end/4 7s
