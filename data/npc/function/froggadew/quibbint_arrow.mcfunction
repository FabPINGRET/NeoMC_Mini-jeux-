execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.frog.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.7
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=!vendor_arrow_9,tag=mg.flw] [{"text":"<"},{"text":"Quibbint","color":"#44BBFF"},{"text":"> My arrows are sourced from a secret source. If I told you, I'd have to kill you with a rock.","color":"white"}]
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=vendor_arrow_9,tag=mg.flw] [{"text":"<"},{"text":"Quibbint","color":"#44BBFF"},{"text":"> My secret source needs to send me more of those first.","color":"white"}]

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run give @a[distance=..10,tag=!vendor_arrow_9,tag=mg.flw] arrow 24
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tag @a[distance=..10,tag=!vendor_arrow_9,tag=mg.flw] add vendor_arrow_9


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
