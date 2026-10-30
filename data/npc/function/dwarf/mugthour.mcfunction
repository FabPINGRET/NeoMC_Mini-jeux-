execute if score tective Story matches 7 if block -9768 75 422 redstone_lamp[lit=true] run scoreboard players set tective Story 8

execute positioned -359 57 -133 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute unless score tective Story matches 8 positioned -359 57 -133 if block -9762 76 422 air run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mugthour","color":"dark_aqua"},{"text":"> This tree is gray. It has colorless leaves. I am liking it.","color":"white"}]
execute unless score tective Story matches 8 positioned -359 57 -133 if block -9762 76 422 redstone_block run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mugthour","color":"dark_aqua"},{"text":"> Mind your business, snooper. You have not talked to my coworkers, one of them may be a monster instead.","color":"white"}]
execute if score tective Story matches 8 positioned -359 57 -133 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Bone Monster","color":"dark_aqua"},{"text":"> RAH!!! EVEN IF I DIE YOU WILL BE LIQUIFIED IN THE CRUCIBLE OF BONE!","color":"white"}]
execute if score tective Story matches 8 run fill -359 57 -133 -360 57 -132 air
execute if score tective Story matches 8 run setblock -363 52 -136 redstone_block
execute if score tective Story matches 8 positioned -359 57 -133 run function summon:bone_monster
execute if score tective Story matches 8 run particle minecraft:gust -359 58 -133 0.2 0.5 0.2 0 5 force


setblock -9762 76 422 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
