execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7
execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Professor Whir","color":"#D47453"},{"text":"> Professors Hum and Whiz were normal, intelligent, rational people, but both left to join the ","color":"white"},{"text":"Germ Eaters","color":"dark_aqua"},{"text":"! I don't know what changed...","color":"white"}]
execute if score mind_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Professor Whir","color":"#D47453"},{"text":"> Professors Hum and Whiz were normal, intelligent, rational people, but both left to join the Comedy Eaters! Guess I was wrong about them.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
