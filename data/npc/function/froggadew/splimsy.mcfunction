execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.frog.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7

#PRE MEMORY RESTORATION
execute if score memory_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Splimsy","color":"#44BBFF"},{"text":"> Why can't I remember anything? I think the high priests are meeting in the ","color":"white"},{"text":"Temple Cavern","color":"aqua"},{"text":" to figure it out.","color":"white"}]

#POST MEMORY RESTORATION, PRE DUNGEON
execute if score memory_contagion bool matches 1 if score Inventory SoaringTrident matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Splimsy","color":"#44BBFF"},{"text":"> My memories being back don't help me much, now I'm just worried about the ","color":"white"},{"text":"Lord of Water","color":"blue"},{"text":"!","color":"white"}]

#POST DUNGEON
execute if score Inventory SoaringTrident matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Splimsy","color":"#44BBFF"},{"text":"> I'm proud to call the ","color":"white"},{"text":"Alabaster Pools ","color":"blue"},{"text":"home! And proud to call you my best pal, haha! Right?","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
