function boss:mini/memory_contagion/hide_stand_head
tp @n[tag=mem_nexus_stand,distance=0..] -9960 84 370

setblock -9946 85 357 minecraft:redstone_block
setblock -9944 85 357 air
setblock -9957 84 357 minecraft:redstone_block
function boss:mini/memory_contagion/hide_contagion
setblock -9963 84 371 redstone_block

schedule function floaty:sched/boss/mini/memory_contagion/summon_monsters 1.5s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 

function music:miniboss
