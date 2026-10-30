execute positioned 10071 40 -104 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 1
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Mind Nexus","color":"dark_aqua"},{"text":"> If you resist, no part of you will remain.","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/mind_contagion/3 6s


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
