execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Jaivra","color":"aqua"},{"text":"> The crest of us Glenfolk is a phoenix rising in the darkness. It's a fitting symbol in my estimation. This castle has given our people a sense of rebirth, and the","color":"white"},{"text":" Bell","color":"gold"},{"text":" keeps us strong, ready to face whatever future.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
