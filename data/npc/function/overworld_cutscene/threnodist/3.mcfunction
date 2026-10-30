setblock -11129 37 416 minecraft:redstone_block
setblock -11133 37 425 minecraft:redstone_block

schedule function floaty:sched/npc/overworld_cutscene/threnodist/4 2s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
