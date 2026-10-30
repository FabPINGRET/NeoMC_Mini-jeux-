execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Captain Crazybones","color":"aqua"},{"text":"> Hero! To what do I owe the pleasure of welcoming you aboard my ship? We're just making the final arrangements to sail away from these accursed Isles once and for all. Far away people in far away lands will need things smuggled now and again too, eh?","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
