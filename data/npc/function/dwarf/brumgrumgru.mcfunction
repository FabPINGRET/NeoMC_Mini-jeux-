execute positioned -325 60 -135 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -325 60 -135 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brumgrumgru","color":"dark_aqua"},{"text":"> Not all of our number are here at the Bureau, ","color":"white"},{"text":"two of us","color":"dark_aqua"},{"text":" are currently doing field work. They're trying to get accurate measurements of one of the towers ","color":"white"},{"text":"on top of the courthouse","color":"dark_aqua"},{"text":".","color":"white"}]
execute positioned -325 60 -135 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brumgrumgru","color":"dark_aqua"},{"text":"> Promise me you'll let me weigh you hero! I must get your measurements!","color":"white"}]

setblock -9768 80 422 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
