execute positioned -284 43 -131 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -284 43 -131 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Burguki","color":"dark_aqua"},{"text":"> It's-a-me! Despair :(","color":"white"}]
execute positioned -284 43 -131 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Burguki","color":"dark_aqua"},{"text":"> It's-a-me! Burguki! I'm in love with your body.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
