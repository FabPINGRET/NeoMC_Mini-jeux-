execute positioned -232 46 -75 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -232 46 -75 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mukrogobu","color":"dark_aqua"},{"text":"> I'm so clean I squeak.","color":"white"},{"text":" *squeak!*","color":"gray","italic":true}]
execute positioned -232 46 -75 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mukrogobu","color":"dark_aqua"},{"text":"> It's crazy that Royroy was a bone monster the whole time. He coulda drowned me if he wanted!","color":"white"}]

setblock -9762 80 416 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
