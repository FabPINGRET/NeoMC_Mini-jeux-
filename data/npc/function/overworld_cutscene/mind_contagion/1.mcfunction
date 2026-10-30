execute positioned 10071 40 -104 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 1
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Mind Nexus","color":"dark_aqua"},{"text":"> You will be the perfect ","color":"white"},{"text":"Germ Eater","color":"dark_aqua"},{"text":"! Let me infect your mind with a new selfhood.","color":"white"},{"text":" ⇒","color":"light_purple"}]

schedule function floaty:sched/npc/overworld_cutscene/mind_contagion/2 8s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
