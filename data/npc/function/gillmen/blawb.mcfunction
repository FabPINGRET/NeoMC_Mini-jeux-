execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Blawb","color":"yellow"},{"text":"> You can't breathe underwater? Are you just like allergic to it or something? Hey, listen, air is nice and all but I really think you should just be able to breathe water. Just figure it out, ok?","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
