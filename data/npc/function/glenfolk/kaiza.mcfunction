execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Kaiza","color":"aqua"},{"text":"> Don't be a stranger hero, make yourself comfortable. Might as well enjoy the time you have while you can, there's enough stress and tension out there as is. If you haven't checked it out yet, I heard the old gravedigger and his wife found something cool in the Undercroft beneath the castle...","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
