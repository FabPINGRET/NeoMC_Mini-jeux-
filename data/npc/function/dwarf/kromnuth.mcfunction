execute positioned -274 58 -223 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -274 58 -223 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Kromnuth","color":"dark_aqua"},{"text":"> The diplomats are all in today. They're in every day really, we don't let them leave anymore. They can't be trusted to not secretly be communicating with bone monsters!","color":"white"}]
execute positioned -274 58 -223 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Kromnuth","color":"dark_aqua"},{"text":"> All the diplomats are in today, go on up!","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
