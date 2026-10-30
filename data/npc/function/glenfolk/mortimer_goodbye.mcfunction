execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.ghast.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mortimer Sorrowloo","color":"aqua"},{"text":">","color":"white"},{"text":" I will return to the sewer for now...","color":"white","italic":true}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
