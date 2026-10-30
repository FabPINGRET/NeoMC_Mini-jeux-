execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"\n<"},{"text":"Narrator","color":"#D47453"},{"text":"> Due to signs of weak leadership, the Court of the Grengleshoft approached the king, formally questioning his ability to rule at such a toddlery age.","color":"white"},{"text":"\n\nHow should Spoom-Ee respond to the Court?","color":"dark_aqua"},{"text":"\nA)","color":"gold","bold":true},{"text":" Explode them\n","color":"white"},{"text":"B)","color":"gold","bold":true},{"text":" Abdicate the throne","color":"white"}]

execute at @n[tag=narrator,distance=0..] run playsound minecraft:entity.armadillo.death neutral @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] ~ ~ ~ 2 0.5
scoreboard players set firelight_script Value 4
