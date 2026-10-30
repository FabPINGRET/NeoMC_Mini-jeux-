
tp @n[tag=f_thren,distance=0..] 285 79 1457
#start stand face player
setblock -9761 236 418 minecraft:redstone_block

tp @a[tag=mg.flw] -11144 58 448 180 0

schedule function floaty:sched/npc/overworld_cutscene/threnodist/2 3s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
