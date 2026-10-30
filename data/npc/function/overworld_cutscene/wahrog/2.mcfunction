fill -9863 109 553 -9863 110 553 air
setblock -9863 113 552 air
tp @n[tag=wahrog_inmind,distance=0..] -9864 115 554

tp @a[tag=mg.flw] -11146 68 347 180 0

schedule function floaty:sched/npc/overworld_cutscene/wahrog/3 3s

#particles
setblock -9773 240 430 minecraft:redstone_block
#stand face player
setblock -9761 236 416 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
