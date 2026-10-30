execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Darrenth","color":"aqua"},{"text":"> Shields are incredibly useful; you should try to find one if you can. My gut tells me you could probably get one somewhere nearby, ","color":"white"},{"text":"before you ever need to go to Dwarf City","color":"aqua"},{"text":", if you look hard enough.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
