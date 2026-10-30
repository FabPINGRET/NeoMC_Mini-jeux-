execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Moldy Romel","color":"aqua"},{"text":"> I've heard tell of a giant golden banana somewhere on that isle. The ","color":"white"},{"text":"Banana of Temptation","color":"yellow"},{"text":" as it's called in the rumors. It probably doesn't exist, but if it did, man I'd touch it immediately.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
