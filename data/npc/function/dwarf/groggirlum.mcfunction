execute positioned -300 58 -163 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -300 58 -163 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Groggirlum","color":"dark_aqua"},{"text":"> Please don't complain to me about the state of things, I just work here.","color":"white"}]
execute positioned -300 58 -163 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Groggirlum","color":"dark_aqua"},{"text":"> I don't know what's going on, I just work here.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
