execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"\n<"},{"text":"Guathman","color":"red"},{"text":"> Young master, to enter the Caverns you must answer me one question. Have you remembered to wipe?","color":"white"}]

execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"\n<"},{"text":"Narrator","color":"#D47453"},{"text":"> ","color":"white"},{"text":"How should Spoom-Ee answer?","color":"dark_aqua"},{"text":"\nA)","color":"gold","bold":true},{"text":" Lie\n","color":"white"},{"text":"B)","color":"gold","bold":true},{"text":" Tell the truth","color":"white"}]

execute at @n[tag=guathman,distance=0..] run playsound minecraft:entity.armadillo.death neutral @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] ~ ~ ~ 2 0.5
scoreboard players set firelight_script Value 6
