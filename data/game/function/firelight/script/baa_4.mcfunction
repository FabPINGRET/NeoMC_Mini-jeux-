execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"\n<"},{"text":"Narrator","color":"#D47453"},{"text":"> Finally, he came upon the Bazaar of Souls, where the dead go shopping. There, he saw the ghost of his father shopping for masks!","color":"white"},{"text":"\n\nWhat should Spoom-Ee say to his father's ghost?","color":"dark_aqua"},{"text":"\nA)","color":"gold","bold":true},{"text":" \"Dad! It's you!\"\n","color":"white"},{"text":"B)","color":"gold","bold":true},{"text":" \"Why do you look half-exploded?\"","color":"white"}]

execute at @n[tag=narrator,distance=0..] run playsound minecraft:entity.armadillo.death neutral @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] ~ ~ ~ 2 0.5
scoreboard players set firelight_script Value 12
