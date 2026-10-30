execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Paol","color":"aqua"},{"text":"> The greatest diplomatic achievement of my life was brokering the deal between the Dwarves and Glenfolk that got Glenfolk Castle built. The greatest diplomatic failure of my life was accidentally calling the dwarf president \"dad\" one time. Yeah, that one keeps me up at night.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
