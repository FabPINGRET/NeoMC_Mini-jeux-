execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.blaze.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"?","color":"yellow"},{"text":"> Come, Igor. The dwarf president was a fool to decline our gift. We will find another to safeguard it.","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Igor","color":"yellow"},{"text":"> ","color":"white"},{"text":"Yesssss master, of courssssse master.","italic":true,"color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
