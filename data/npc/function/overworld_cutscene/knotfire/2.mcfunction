tp @n[tag=knotfire_stand,distance=0..] -7 30 1600
tp @a[tag=mg.flw] -10682 72 89 90 0


#start facing player & particles
setblock -9773 240 416 minecraft:redstone_block

schedule function floaty:sched/npc/overworld_cutscene/knotfire/3 5s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
