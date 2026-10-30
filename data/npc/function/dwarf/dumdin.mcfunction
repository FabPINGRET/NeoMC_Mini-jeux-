execute positioned -271 37 -128 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -271 37 -128 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Dumdin","color":"dark_aqua"},{"text":"> Are you a bone monster in disguise? Back off! I've heard they can disguise themselves to look like anything they want! You won't fool me.","color":"white"}]
execute positioned -271 37 -128 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Dumdin","color":"dark_aqua"},{"text":"> I'm saving up for an apartment in the residential district, it's gloomy here sometimes let me tell ya.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
