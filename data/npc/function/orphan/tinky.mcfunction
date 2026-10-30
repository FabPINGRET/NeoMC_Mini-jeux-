execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Tinky","color":"aqua"},{"text":"> Oi'm trying teh dig through this 'ere wall to visit my fellow orphans! Oi 'ear them digging around down there. If only Oi 'ad a","color":"white"},{"text":" magic shovel","color":"gold"},{"text":", Oi've heard there's a way teh get one somewhere.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
