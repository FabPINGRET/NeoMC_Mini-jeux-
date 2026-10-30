execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Joshuly","color":"aqua"},{"text":"> It might be a good idea to","color":"white"},{"text":" sleep in 'ere to set your spawn","color":"green"},{"text":". Down 'ere you're never too far from any part of the Floa'y Isles yew've already been to. Yew can use moi bed and chest, yew can!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
