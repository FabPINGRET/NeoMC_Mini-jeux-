execute if score tective Story matches 4 if block -9773 79 421 redstone_lamp[lit=true] run scoreboard players set tective Story 5

execute positioned -296 66 -57 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute unless score tective Story matches 5 positioned -296 66 -57 if block -9768 80 416 air run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brogueen","color":"dark_aqua"},{"text":"> This tower weighs so heavy. This tower measures so high.","color":"white"}]
execute unless score tective Story matches 5 positioned -296 66 -57 if block -9768 80 416 redstone_block run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brogueen","color":"dark_aqua"},{"text":"> Hey! Do not slander me. You have not even talked to all of my colleagues yet. Shame.","color":"white"}]
execute if score tective Story matches 5 positioned -296 66 -57 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Bone Monster","color":"dark_aqua"},{"text":"> RAH!!!","color":"white"}]
execute if score tective Story matches 5 run fill -295 67 -57 -296 66 -57 air
execute if score tective Story matches 5 run setblock -290 64 -58 redstone_block
execute if score tective Story matches 5 positioned -296 66 -57 run function summon:bone_monster
execute if score tective Story matches 5 run particle minecraft:gust -296 67 -57 0.2 0.5 0.2 0 5 force


setblock -9768 80 416 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
