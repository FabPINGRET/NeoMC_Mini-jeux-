execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.villager.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Gwyrm","color":"aqua"},{"text":"> The","color":"white"},{"text":" Dwarves","color":"dark_aqua"},{"text":" helped us build this castle, they're pretty chill little fellas most times. Personally, I want to know how in the world the ","color":"white"},{"text":"Gillmen","color":"yellow"},{"text":" built their new floating city.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
