execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"<"},{"text":"Narrator","color":"#D47453"},{"text":"> Our story begins with the young king Spoom-Ee IV, who was just crowned king of the Grenglesphere at age 3 after his father, Spoom-Ee III, died in a world-explosion accident.\n\n","color":"white"},{"text":"What shall his first decree as king be?","color":"dark_aqua"},{"text":"\nA)","color":"gold","bold":true},{"text":" Decree that the kingdom enter a time of mourning\n","color":"white"},{"text":"B)","color":"gold","bold":true},{"text":" Decree that bathtime is outlawed","color":"white"}]

execute at @n[tag=narrator,distance=0..] run playsound minecraft:entity.armadillo.death neutral @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] ~ ~ ~ 2 0.5

scoreboard players set firelight_script Value 1
