execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.frog.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7

#PRE MEMORY RESTORATION
execute if score memory_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Blibberglee","color":"#44BBFF"},{"text":"> Bend over, pilgrim! Let Pucheeki soothe you! I wrote on my hand that I'm supposed to say that to people who come in here but I don't remember why...","color":"white"}]

#POST MEMORY RESTORATION, PRE DUNGEON
execute if score memory_contagion bool matches 1 if score Inventory SoaringTrident matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Blibberglee","color":"#44BBFF"},{"text":"> Bend over, pilgrim! Let Pucheeki soothe you! It's an honor serving Pucheeki, he performs ointment and cream miracles all the time.","color":"white"}]

#POST DUNGEON
execute if score Inventory SoaringTrident matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Blibberglee","color":"#44BBFF"},{"text":"> Bend over, pilgrim! Let Pucheeki soothe you! It's an honor serving Pucheeki, he performs ointment and cream miracles all the time.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
