execute positioned -9960 99 370 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.zoglin.angry neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -9960 99 370 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Memory Nexus","color":"green"},{"text":"> Form a memory of it! It's the last one you're gonna make...","color":"white"}]

tag @a[tag=mg.flw] remove cutscene

schedule function floaty:sched/npc/overworld_cutscene/memory_contagion/6 7s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
