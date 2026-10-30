execute if score tective Story matches 1 if block -9765 79 425 redstone_lamp[lit=true] run scoreboard players set tective Story 2

execute positioned -248 41 -52 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute unless score tective Story matches 2 positioned -248 41 -52 if block -9762 80 422 air run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Royroy","color":"dark_aqua"},{"text":"> I am becoming warmed. I am becoming cleaned. Ah, yes. Comfort.","color":"white"}]
execute unless score tective Story matches 2 positioned -248 41 -52 if block -9762 80 422 redstone_block run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Royroy","color":"dark_aqua"},{"text":"> You accuse me? You have not even talked to everyone here yet. Fool.","color":"white"}]
execute if score tective Story matches 2 positioned -248 41 -52 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Bone Monster","color":"dark_aqua"},{"text":"> RAH!!!","color":"white"}]
execute if score tective Story matches 2 run fill -248 42 -51 -248 41 -52 air
execute if score tective Story matches 2 run setblock -251 41 -54 minecraft:redstone_block
execute if score tective Story matches 2 positioned -248 41 -52 run function summon:bone_monster
execute if score tective Story matches 2 run particle minecraft:gust -248 42 -52 0.2 0.5 0.2 0 5 force


setblock -9762 80 422 minecraft:redstone_block



#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
