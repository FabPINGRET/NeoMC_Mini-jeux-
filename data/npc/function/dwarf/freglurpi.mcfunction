execute positioned -359 58 -148 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -359 58 -148 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Freglurpi","color":"dark_aqua"},{"text":"> We should really have more dwarves stationed in the lower city, I've heard reports of beasts appearing down there at night.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
