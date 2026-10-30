execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.frog.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7

#PRE MEMORY RESTORATION
execute if score memory_contagion bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Trusted Beeb'm","color":"#44BBFF"},{"text":"> We need to get into Womwort's sanctum to see why he has afflicted us so. The problem is, none of us can remember how to get in! We can't even remember who Womwort's high priest is.","color":"white"}]

#POST MEMORY RESTORATION, PRE DUNGEON
execute if score memory_contagion bool matches 1 if score Inventory SoaringTrident matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Trusted Beeb'm","color":"#44BBFF"},{"text":"> So, that wasn't Womwort cursing us? It was a Contagion of the","color":"white"},{"text":" World Virus","color":"dark_aqua"},{"text":"? Sacrilege!","color":"white"}]

#POST DUNGEON
execute if score Inventory SoaringTrident matches 1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Trusted Beeb'm","color":"#44BBFF"},{"text":"> Noddrin be praised for your success! After all, you have to keep a firm grip on that trident, eh? Say a prayer of thanks to Noddrin whenever you remember to.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
