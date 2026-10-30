execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.panda.cant_breed neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Zatinazita","color":"gold"},{"text":"> The huge skeletons littered across the desert remind us of where we come from. The ","color":"white"},{"text":"Great Dragons ","color":"gold"},{"text":"who used to rule this ancient land are lost to the past. Time swallows even the mightiest of creatures, it's a humbling thought.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
