execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Kyrtha","color":"aqua"},{"text":"> I'm in charge of making sure everything is running smoothly around here and everyone is doing their part. I'm busy trying to figure out what to do about all the","color":"white"},{"text":" Dwarves ","color":"dark_aqua"},{"text":"who have moved here lately. They've been through a lot.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
