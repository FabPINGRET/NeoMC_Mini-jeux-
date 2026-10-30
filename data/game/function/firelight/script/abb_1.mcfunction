item replace entity @n[tag=spoom-ee4,distance=0..] weapon.mainhand with minecraft:rabbit_hide
item replace entity @n[tag=guathman,distance=0..] weapon.mainhand with minecraft:air

execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"\n<"},{"text":"Narrator","color":"#D47453"},{"text":"> Spoom-Ee accepted the rag in bashful hands.","color":"white"},{"text":"\n\nWhat should Spoom-Ee do?","color":"dark_aqua"},{"text":"\nA)","color":"gold","bold":true},{"text":" Wipe\n","color":"white"},{"text":"B)","color":"gold","bold":true},{"text":" Ask the gatekeeper how to be a good king","color":"white"}]

execute at @n[tag=narrator,distance=0..] run playsound minecraft:entity.armadillo.death neutral @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] ~ ~ ~ 2 0.5
scoreboard players set firelight_script Value 11
