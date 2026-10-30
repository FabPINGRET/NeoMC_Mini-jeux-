execute positioned -318 58 -119 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -318 58 -119 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Krugbar","color":"dark_aqua"},{"text":"> The ","color":"white"},{"text":"bone contagion","color":"gray"},{"text":" crisis is weighing heavily on us all. The measure of disunity that has fallen upon Dwarf City is great. Weight jokes are the only thing getting me through this.","color":"white"}]
execute positioned -318 58 -119 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Krugbar","color":"dark_aqua"},{"text":"> How much do the Floaty Isles weigh, I wonder?","color":"white"}]

setblock -9768 80 426 minecraft:redstone_block

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
