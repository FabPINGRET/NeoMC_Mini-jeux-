execute positioned -302 65 -158 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -302 65 -158 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Tulgrig","color":"dark_aqua"},{"text":"> There were some strange characters that came in a little bit ago to try and give the dwarf president some mysterious gift. I wonder what it was.","color":"white"}]
execute positioned -302 65 -158 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Tulgrig","color":"dark_aqua"},{"text":"> President Snuguki is so good at his job, we increased the term length to 500 years for any president whose name ends in \"guki!\"","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
