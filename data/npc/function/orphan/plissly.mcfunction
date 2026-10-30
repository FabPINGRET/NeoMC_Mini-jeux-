execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.8
execute unless block -199 46 -1201 minecraft:redstone_block at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Plissly","color":"aqua"},{"text":"> Oi keep 'avin oddly vivid dreams of a curious sculpture, so Oi tried to build one from memory. In me dream it feels loik a real object, from ","color":"white"},{"text":"somewhere out there in the world","color":"green"},{"text":", but me facsimile here ain't exactly roight. If Oi could get the ","color":"white"},{"text":"positionin' of the floatin' bits ","color":"gold"},{"text":"exactly how they are in me dream, Oi think Oi'd be a","color":"white"},{"text":" very, very 'appy Orphan","color":"red"},{"text":".","color":"white"}]

execute if block -199 46 -1201 minecraft:redstone_block at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Plissly","color":"aqua"},{"text":"> Oi, that's it! That's the sculpture just how it appeared in me dream! That makes me ","color":"white"},{"text":"very, very 'appy","color":"red"},{"text":". 'Ave yew been spying on me dreams, hero?","color":"white"}]

execute if block -199 46 -1201 minecraft:redstone_block at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1.25 ~ run particle minecraft:heart ~ ~ ~ 0.3 0.3 0.3 0 10 force
execute if block -199 46 -1201 minecraft:redstone_block run setblock -190 57 -1184 minecraft:redstone_block


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
