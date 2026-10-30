execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Finn","color":"yellow"},{"text":"> The folks here are all being very nice to me. I hate to be pitied though, my people are resilient. Visit ","color":"white"},{"text":"Ishbowl ","color":"blue"},{"text":"sometime, and you'll see what I mean! Maybe someday, you can help restore some peace to","color":"white"},{"text":" Bubble Lake","color":"blue"},{"text":".","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
