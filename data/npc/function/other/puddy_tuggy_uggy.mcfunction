execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.nautilus.hurt_land neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Puddy Tuggy-Uggy","color":"aqua"},{"text":"> Oh, sorry my collar is all spitty and wet, I've been sucking on my shirt. Don't give me that look, I didn't know anyone was around. Who are you?","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
