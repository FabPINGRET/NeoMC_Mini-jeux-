execute positioned -337 57 -244 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -337 57 -244 if block -340 49 -253 minecraft:redstone_block if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Bogothook","color":"dark_aqua"},{"text":"> The entrance keeps closing itself and we in the Dwarf Legion can't find any other way in! There must be a","color":"white"},{"text":" bone monster in the city somewhere making sure it stays closed","color":"dark_aqua"},{"text":" to us.","color":"white"}]
execute positioned -337 57 -244 if block -340 49 -253 minecraft:air if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Bogothook","color":"dark_aqua"},{"text":"> The seal on the entrance broke! Are you... gonna jump inside? I'm afraid of what might be waiting down there...","color":"white"}]
execute positioned -337 57 -244 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Bogothook","color":"dark_aqua"},{"text":"> Hero, something in the air just changed for the better. Did you defeat the ","color":"white"},{"text":"bone contagion","color":"gray"},{"text":"? Wow! President Snuguki will want to hear about this, I'm sure!","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
