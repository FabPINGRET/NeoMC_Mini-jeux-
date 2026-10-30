execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.bee.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"H. Beetle","color":"green"},{"text":"> These woods are a wonderful home, I love exploring them during the day when it's safe. Some of my favorite places are the in the lower forest, where the conditions are perfect for mushrooms to grow! You can get down there pretty easily over a waterfall by the colony's south entrance, where we get our water from.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
