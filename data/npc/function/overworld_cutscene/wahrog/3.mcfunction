execute positioned -11146 68 332 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.frog.death neutral @a[tag=mg.flw] ~ ~ ~ 3 0.7

tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Wahrog the Prophet","color":"#44BBFF"},{"text":"> My crackle-pocked brain is doomed. You will donate yours to me now.","color":"white"},{"text":" ⇒","color":"light_purple"}]

spawnpoint @a[tag=mg.flw] -11146 68 347 180 0
scoreboard players set $flsp mg.st 38
execute positioned -11146 18 332 run function summon:wahrog

setblock -11163 27 350 minecraft:redstone_block
setblock -11157 28 350 minecraft:redstone_block

schedule function floaty:sched/npc/overworld_cutscene/wahrog/4 6s

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
