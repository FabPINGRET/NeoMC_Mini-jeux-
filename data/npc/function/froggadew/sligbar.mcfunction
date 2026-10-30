execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.frog.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7

#PRE MEMORY RESTORATION
execute if score memory_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Trusted Sligbar","color":"#44BBFF"},{"text":"> Gods forgive us, we six high priests cannot remember which god we each serve! Nor can we recall which god rules which domain. None of us have more than a ","color":"white"},{"text":"couple memories","color":"aqua"},{"text":" related to our priestly duties. I pray there's","color":"white"},{"text":" enough information left in our minds ","color":"aqua"},{"text":"to be able to piece our memories back together.","color":"white"}]

#POST MEMORY RESTORATION, PRE DUNGEON
execute if score memory_contagion bool matches 1 if score Inventory SoaringTrident matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Trusted Sligbar","color":"#44BBFF"},{"text":"> My memories return to me like a fountain shooting up from the ground! Yes, the ","color":"white"},{"text":"Lord of Water","color":"blue"},{"text":", he was talking about going into hiding a day or two before our memories were taken. I wonder where he is now?","color":"white"}]

#POST DUNGEON
execute if score Inventory SoaringTrident matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Trusted Sligbar","color":"#44BBFF"},{"text":"> Our ","color":"white"},{"text":"Pools","color":"blue"},{"text":" are much better off now. Thank you.","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run kill @n[tag=quest_marker,distance=..3]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
