execute positioned -211 58 -93 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -211 58 -93 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Gogikud","color":"dark_aqua"},{"text":"> It's hard to tell the exact age of one of these trees without cutting it down, but if I had to guess I'd say this one was like a hundred or something, who cares.","color":"white"}]

setblock -9762 76 424 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
