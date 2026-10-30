execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lorra","color":"aqua"},{"text":"> How's this for advice from an old woman? Adventures can get","color":"white"},{"text":" increasingly difficult over time","color":"aqua"},{"text":", so sometimes it's good to pause and ","color":"white"},{"text":"do some other things on the side","color":"aqua"},{"text":" to strengthen you for your main goals.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
