execute positioned 172 59 -6 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 172 59 -6 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Kummuck","color":"dark_aqua"},{"text":"> I'm glad we escaped Dwarf City when we did, it sounds like they don't even let anyone come in anymore.","color":"white"}]
execute positioned 172 59 -6 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Kummuck","color":"dark_aqua"},{"text":"> I'm still glad we escaped Dwarf City when we did, but it's a relief to know it's safe to return whenever I want.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
