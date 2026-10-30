execute positioned -11760 174 -196 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.squid.death neutral @a[tag=mg.flw] ~ ~ ~ 1 1
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Mind Nexus","color":"dark_aqua"},{"text":"> Prepare to be emptied.","color":"white"}]

schedule function floaty:sched/npc/overworld_cutscene/mind_contagion/6 3s

setblock -11751 147 -177 minecraft:redstone_block
setblock -11757 147 -177 redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
