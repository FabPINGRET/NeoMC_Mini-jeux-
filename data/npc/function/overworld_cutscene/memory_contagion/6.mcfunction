function boss:mini/memory_contagion/hide_stand
bossbar set boss:memory_contagion players @a[tag=mg.flw]
execute positioned -9960 69 370 run function summon:memory_nexus

schedule function floaty:sched/npc/overworld_cutscene/memory_contagion/7 1.5s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
