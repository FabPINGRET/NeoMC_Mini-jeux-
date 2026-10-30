execute positioned -237 60 -118 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -237 60 -118 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Hobroid","color":"dark_aqua"},{"text":"> The invisible hand of the market looks skeletal and nightmarish these days. Not even Dwarf treasury bonds are safe.","color":"white"}]
execute positioned -237 60 -118 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Hobroid","color":"dark_aqua"},{"text":"> You've saved my wallet! And, um, my neighbors I guess. And family I suppose.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
