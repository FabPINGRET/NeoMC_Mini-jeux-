execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.dolphin.hurt neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Blue","color":"blue"},{"text":"> I'm glad it's you who found my back entrance, and not a foul monster. I wouldn't be able to live with myself if something bad were to happen to my ","color":"white"},{"text":"daughter","color":"blue"},{"text":". She's in the basement, talk to her if you need to go to ","color":"white"},{"text":"Bubble Lake","color":"blue"},{"text":".","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
