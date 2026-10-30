execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute if score mind_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5

execute if score mind_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Germ Eater","color":"dark_aqua"},{"text":"> Sometimes, the most loyal ","color":"white"},{"text":"Germ Eaters","color":"dark_aqua"},{"text":" get changed into ","color":"white"},{"text":"Mind Monsters","color":"dark_aqua"},{"text":"! A noble fate indeed, an honorable fate. I live to serve.","color":"white"}]
execute if score mind_contagion bool matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Comedy Eater","color":"#D47453"},{"text":"> Nice, I like your energy! Just from the walk-up alone, I’m getting... protagonist but emotionally unavailable. Did I get that right? Oh, you're not doing a character?","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
