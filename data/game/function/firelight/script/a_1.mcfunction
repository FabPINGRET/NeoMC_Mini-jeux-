execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"\n<"},{"text":"Narrator","color":"#D47453"},{"text":"> All the Grenglesphere wept and grieved for their exploded king, which made Spoom-Ee feel rather glum.","color":"white"},{"text":"\n\nHow should Spoom-Ee respond to his feelings?","color":"dark_aqua"},{"text":"\nA)","color":"gold","bold":true},{"text":" Immediately retract the mourning decree\n","color":"white"},{"text":"B)","color":"gold","bold":true},{"text":" Escape the crying sounds","color":"white"}]

execute at @n[tag=narrator,distance=0..] run playsound minecraft:entity.armadillo.death neutral @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] ~ ~ ~ 2 0.5
scoreboard players set firelight_script Value 2
