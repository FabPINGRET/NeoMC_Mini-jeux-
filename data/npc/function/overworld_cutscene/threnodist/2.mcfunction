execute positioned -11144 58 430 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.vex.death neutral @a[tag=mg.flw] ~ ~ ~ 3 0.1

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Folded Threnodist","color":"dark_purple"},{"text":"> ...","color":"white"}]

spawnpoint @a[tag=mg.flw] -11144 58 448 180 0
scoreboard players set $flsp mg.st 35

execute positioned -11144 23 430 run function summon:folded_threnodist
setblock -11131 38 416 minecraft:redstone_block

schedule function floaty:sched/npc/overworld_cutscene/threnodist/3 1s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
