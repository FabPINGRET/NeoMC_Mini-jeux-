execute positioned -11760 174 -196 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 1
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Mind Nexus","color":"dark_aqua"},{"text":"> If I cannot empty your mind by persuasion, I will empty it through a hole in your skull. I can rebuild you into a perfect ","color":"white"},{"text":"Germ Eater","color":"dark_aqua"},{"text":" either way.","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/mind_contagion/5 10s

spawnpoint @a[tag=mg.flw] -11760 173 -184 180 0
scoreboard players set $flsp mg.st 32

execute positioned -11760 124 -196 run function summon:mind_nexus

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
