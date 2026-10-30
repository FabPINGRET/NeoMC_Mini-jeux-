execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"\n<"},{"text":"Spoom-Ee IV","color":"#D47453"},{"text":"> Excuse me, what does \"stock market\" mean?","color":"white"}]
execute positioned 9873 57 -137 run tellraw @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] [{"text":"<"},{"text":"Master of Faces","color":"blue"},{"text":"> Oh, little boy are you lost? I uh, haha, well, it’s hard to explain. Businesses can raise capital by selling equity shares to investors on a public exchange, like the NASDAQ. You should probably go find your parents.","color":"white"},{"text":" ⇒","color":"light_purple"}]

execute at @n[tag=spoom-ee4,distance=0..] run playsound minecraft:entity.armadillo.death neutral @a[x=9873,y=57,z=-137,dx=28,dy=15,dz=11,tag=mg.flw] ~ ~ ~ 2 0.7

schedule function floaty:sched/game/firelight/script/abab_1 13s replace
