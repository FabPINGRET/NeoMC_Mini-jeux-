execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"\n<"},{"text":"Narrator","color":"#D47453"},{"text":"> Spoom-Ee purchased a subscription to King Weekly with the taxes of 10,000 serfs. It said all good kings must study Regal Grammar and Advanced Counting.\n\n","color":"white"},{"text":"Which should Spoom-Ee study first?","color":"dark_aqua"},{"text":"\nA)","color":"gold","bold":true},{"text":" Regal Grammar\n","color":"white"},{"text":"B)","color":"gold","bold":true},{"text":" Advanced Counting","color":"white"}]

item replace entity @n[tag=spoom-ee4,distance=0..] weapon.mainhand with book

execute at @n[tag=narrator,distance=0..] run playsound minecraft:entity.armadillo.death neutral @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] ~ ~ ~ 2 0.5
schedule function floaty:sched/game/firelight/script/bb_1 1t replace
