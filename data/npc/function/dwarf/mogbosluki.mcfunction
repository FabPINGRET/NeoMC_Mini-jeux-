execute positioned -321 58 -130 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -321 58 -130 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mogbosluki","color":"dark_aqua"},{"text":"> We have the most essential jobs in the Dwarf Government. If we don't figure out how much everything weighs and how long and tall and wide everything is, who will?","color":"white"}]

setblock -9768 80 424 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
