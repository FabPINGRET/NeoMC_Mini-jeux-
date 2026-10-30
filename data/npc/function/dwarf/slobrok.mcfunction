execute positioned -263 41 -64 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -263 41 -64 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Slobrok","color":"dark_aqua"},{"text":"> Welcome to the Grudgrumlin Grill! Please find a seat at any available table. The owner, ","color":"white"},{"text":"Grudgrumlin","color":"dark_aqua"},{"text":", is in the kitchen.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
