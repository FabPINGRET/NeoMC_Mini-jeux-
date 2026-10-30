tp @n[tag=mind_nexus_base,distance=0..] 10071 36 -104
tp @a[tag=mg.flw] -11760 173 -184 180 0
schedule function floaty:sched/npc/overworld_cutscene/mind_contagion/4 3s
setblock -9773 268 428 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
