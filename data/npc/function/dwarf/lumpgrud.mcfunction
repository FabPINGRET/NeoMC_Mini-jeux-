execute positioned -323 58 -91 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -323 58 -91 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lumpgrud","color":"dark_aqua"},{"text":"> The","color":"white"},{"text":" Magma Kingdom","color":"red"},{"text":" is just down this road. It's closed off now, for their protection and our own.","color":"white"}]
execute positioned -323 58 -91 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lumpgrud","color":"dark_aqua"},{"text":"> The","color":"white"},{"text":" Magma Kingdom ","color":"red"},{"text":"is just down this road. It's so interesting to see how a ","color":"white"},{"text":"fire golem","color":"red"},{"text":" culture has arisen, given that they're all inanimate objects.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
