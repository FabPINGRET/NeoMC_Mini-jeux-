execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.ghast.scream neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1
execute if score mortimer bool matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mortimer Sorrowloo","color":"aqua"},{"text":">","color":"white"},{"text":" Ohhh woe is me! I do not know where I was buried and I cannot find my grave... I know I was buried by rushing water, so here is a good a place as any to look...","color":"white","italic":true}]

execute if score mortimer bool matches 1 if block 86 59 42 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mortimer Sorrowloo","color":"aqua"},{"text":">","color":"white"},{"text":" You... found my grave? I was buried by a waterfall? Oh... that is less cozy than these comfy little pipes. A waterfall, really? Disappointing. Let me give you something I found flushed down here for your troubles...","color":"white","italic":true}]
execute if score mortimer bool matches 1 if block 86 59 42 purple_shulker_box at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mortimer Sorrowloo","color":"aqua"},{"text":">","color":"white"},{"text":" Here I will remain, receiving whatever foul libation people decide to offer me in their flushing... Who in their right mind would want to be buried by a waterfall anyway...","color":"white","italic":true}]
execute if score mortimer bool matches 1 run setblock 85 55 44 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
