execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"\n<"},{"text":"Narrator","color":"#D47453"},{"text":"> Spoom-Ee stepped down off his throne, disgraced. Prunt the Older Cousin would do a better job anyway.","color":"white"},{"text":"\n\nWhat should Spoom-Ee do now that he's no longer king?","color":"dark_aqua"},{"text":"\nA)","color":"gold","bold":true},{"text":" Go looking for his dad's ghost\n","color":"white"},{"text":"B)","color":"gold","bold":true},{"text":" Explode the whole world","color":"white"}]
function game:firelight/scene/abdicate
function game:firelight/scene_dress

execute at @n[tag=narrator,distance=0..] run playsound minecraft:entity.armadillo.death neutral @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] ~ ~ ~ 2 0.5

scoreboard players set firelight_script Value 9
