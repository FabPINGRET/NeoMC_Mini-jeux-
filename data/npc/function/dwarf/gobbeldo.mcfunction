execute positioned -241 45 -80 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -241 45 -80 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Gobbeldo","color":"dark_aqua"},{"text":"> I'm pruney past the point of return. My fingertips are wrinkled beyond the faintest hope of repair.","color":"white"}]

setblock -9762 80 418 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
