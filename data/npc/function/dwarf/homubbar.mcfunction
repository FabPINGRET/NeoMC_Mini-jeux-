execute positioned -321 58 -73 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -321 58 -73 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Homubbar","color":"dark_aqua"},{"text":"> Guarding these dwarves makes me feel like a big, mean bully. I... kinda like it. Is that bad?","color":"white"}]
execute positioned -321 58 -73 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Homubbar","color":"dark_aqua"},{"text":"> We let the dwarves in here free. Turns out they weren't actually bone monsters! I hope they forgive me.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
