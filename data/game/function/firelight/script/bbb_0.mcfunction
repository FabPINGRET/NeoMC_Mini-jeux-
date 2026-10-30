execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"\n<"},{"text":"Narrator","color":"#D47453"},{"text":"> Spoom-Ee began learning about the wide world of mythical numbers greater than 10.","color":"white"},{"text":"\n\nHow should he use this knowledge?","color":"dark_aqua"},{"text":"\nA)","color":"gold","bold":true},{"text":" Try to guess the ages of the kingdom’s elders\n","color":"white"},{"text":"B)","color":"gold","bold":true},{"text":" Try to count to wuhungred","color":"white"}]

execute at @n[tag=narrator,distance=0..] run playsound minecraft:entity.armadillo.death neutral @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] ~ ~ ~ 2 0.5
schedule function floaty:sched/game/firelight/script/bbb_1 1t replace
