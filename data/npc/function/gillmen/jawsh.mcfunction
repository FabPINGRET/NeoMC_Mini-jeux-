execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.wolf.growl neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Jawsh","color":"yellow"},{"text":"> I'm sad we had to leave our ","color":"white"},{"text":"Lake","color":"blue"},{"text":", but I'll take these cramped glass bowls over deadly monsters any day. Plus, even if I wanted to go back to the ","color":"white"},{"text":"Lake","color":"blue"},{"text":", I couldn't. Not without ","color":"white"},{"text":"Blue","color":"blue"},{"text":" opening the gate for me.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
