execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"\n<"},{"text":"Narrator","color":"#D47453"},{"text":"> ","color":"white"},{"text":"What should Spoom-Ee say to his distressed steward, Pim the Lesser?","color":"dark_aqua"},{"text":"\nA)","color":"gold","bold":true},{"text":" \"Don’t worry, you’re not going to get exploded\"\n","color":"white"},{"text":"B)","color":"gold","bold":true},{"text":" \"I think I’m going to explode you now\"","color":"white"}]
execute as @n[tag=spoom-ee4,distance=0..] at @s run tp @s ~ ~ ~ 130 0

execute at @n[tag=narrator,distance=0..] run playsound minecraft:entity.armadillo.death neutral @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] ~ ~ ~ 2 0.5
scoreboard players set firelight_script Value 8
