execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!darknyss,tag=mg.flw] [{"text":"<"},{"text":"Darknyss Pierre","color":"aqua"},{"text":"> Welcome to my clinic, darling. Need your legs changed? Some pesky tendons getting in your way? Just pop over to the bed and I'll make a few snips, nice and clean.","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=darknyss,tag=mg.flw] [{"text":"<"},{"text":"Darknyss Pierre","color":"aqua"},{"text":"> How do those legs feel, darling? I hope they feel excellent. If not, I can always reattach the things I unattached with another surgery. Anything that's unconnected can always be reconnected!","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
