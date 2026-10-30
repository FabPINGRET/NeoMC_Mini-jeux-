execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.frog.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7

#PRE MEMORY RESTORATION
execute if score memory_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Nubwump","color":"#44BBFF"},{"text":"> This memory loss, it feels so eerie. It's not natural whatever it is. Either the gods are punishing us, or something sinister is afoot on our isle.","color":"white"}]

#POST MEMORY RESTORATION, PRE DUNGEON
execute if score memory_contagion bool matches 1 if score Inventory SoaringTrident matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Nubwump","color":"#44BBFF"},{"text":"> It feels good to remember again, but bad to remember the","color":"white"},{"text":" Lord of Water","color":"blue"},{"text":" is gone. I'm sure Frogcrates knows where he is.","color":"white"}]

#POST DUNGEON
execute if score Inventory SoaringTrident matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Nubwump","color":"#44BBFF"},{"text":"> I love going on little swims! It reminds me of my tadpole days. Those were simpler times...","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
