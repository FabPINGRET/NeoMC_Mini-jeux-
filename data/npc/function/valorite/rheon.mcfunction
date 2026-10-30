execute positioned 10034 56 -167 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.9

execute positioned 10034 56 -169 if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute positioned 10034 56 -169 if score mind_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5

execute positioned 10034 56 -169 if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Germ Eater","color":"dark_aqua"},{"text":"> Little Rheon, embrace the great ","color":"white"},{"text":"Virus","color":"dark_aqua"},{"text":"! I need you to experience the searing warmth of his ","color":"white"},{"text":"Mind Contagion's","color":"dark_aqua"},{"text":" tentacles branching across your cortices. Live to serve as I live to serve.","color":"white"}]

execute positioned 10034 56 -169 if score mind_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Comedy Eater","color":"#D47453"},{"text":"> What separates an improv artist from a regular comedian is the same thing that separates sprinters from distance runners. High-intensity interval training.","color":"white"}]

execute positioned 10034 56 -167 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Rheon","color":"#D47453"},{"text":"> Dad, you're scaring me!","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
