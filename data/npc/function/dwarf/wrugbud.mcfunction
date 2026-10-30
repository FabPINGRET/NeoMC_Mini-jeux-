execute positioned -294 58 -185 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -294 58 -185 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Wrugbud","color":"dark_aqua"},{"text":"> Drawing up plans for a professional Dwarfball field is hard work! I had to start from scratch after I forgot to include exits in my last version.","color":"white"}]

setblock -9762 76 420 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
