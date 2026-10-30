execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute if score mind_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5

execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Germ Eater","color":"dark_aqua"},{"text":"> We would've compelled the ","color":"white"},{"text":"Orcs","color":"green"},{"text":" to build this obelisk for us, but we can't speak their ","color":"white"},{"text":"language","color":"green"},{"text":"! Stupid brutes.","color":"white"}]
execute if score mind_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Comedy Eater","color":"#D47453"},{"text":"> We've tried performing a few shows for the ","color":"white"},{"text":"Orcs","color":"green"},{"text":", but they just don't get it. ","color":"white"},{"text":"*sigh*","color":"gray","italic":true},{"text":" Improv comedy is the most persecuted art form.","color":"white","italic":false}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
