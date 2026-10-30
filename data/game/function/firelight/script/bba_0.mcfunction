execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"\n<"},{"text":"Narrator","color":"#D47453"},{"text":"> Spoom-Ee began learning about royal nouns and kingly participles. He wanted to test a new sentence on his steward, Pim the Lesser.","color":"white"},{"text":"\n\nWhat should he say?","color":"dark_aqua"},{"text":"\nA)","color":"gold","bold":true},{"text":" \"Becometh exploded\"\n","color":"white"},{"text":"B)","color":"gold","bold":true},{"text":" \"Inhaleth my crown jewels, clotpole\"","color":"white"}]

execute as @n[tag=spoom-ee4,distance=0..] at @s run tp @s ~ ~ ~ 50 0

execute at @n[tag=narrator,distance=0..] run playsound minecraft:entity.armadillo.death neutral @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] ~ ~ ~ 2 0.5
schedule function floaty:sched/game/firelight/script/bba_1 1t replace
