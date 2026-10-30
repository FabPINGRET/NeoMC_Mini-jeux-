execute positioned -299 66 -54 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute unless block -296 66 -57 air positioned -299 66 -54 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Hogub Gubson","color":"dark_aqua"},{"text":"> It's a challenging thing, weighing a tower, but it must be done! If we have time to measure it, we'll try to do that too!","color":"white"}]
execute if block -296 66 -57 air positioned -299 66 -54 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Hogub Gubson","color":"dark_aqua"},{"text":"> I'm in shock, you saved me! My partner was a bone monster the whole time and I didn't weigh his loyalties correctly at all!","color":"white"}]

setblock -9768 80 418 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
