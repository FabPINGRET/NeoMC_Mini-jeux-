tp @n[tag=sphere_custodian,distance=0..] 10319 32 -103
tp @a[tag=mg.flw] -10441 84 429 0 0


#custodian face player
setblock -9769 240 422 minecraft:redstone_block

schedule function floaty:sched/npc/overworld_cutscene/custodian/3 5s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
