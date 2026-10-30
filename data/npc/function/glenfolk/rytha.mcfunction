execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Rytha","color":"aqua"},{"text":"> The","color":"white"},{"text":" Nightrobes","color":"light_purple"},{"text":" have been acting nervous lately, it's not a good sign. I'd bet they know something about the ","color":"white"},{"text":"scourges ","color":"light_purple"},{"text":"that we don't.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
