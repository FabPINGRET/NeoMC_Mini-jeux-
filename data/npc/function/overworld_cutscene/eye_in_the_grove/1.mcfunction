setblock -32 58 -189 air

tp @a[tag=mg.flw] -10060 116 322 0 0

setblock -9761 244 422 minecraft:redstone_block
schedule function floaty:sched/npc/overworld_cutscene/eye_in_the_grove/2 3s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
