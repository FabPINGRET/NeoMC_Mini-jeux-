execute positioned -237 60 -102 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -237 60 -102 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Gibromli","color":"dark_aqua"},{"text":"> I'm buying embalming fluid futures like a madman over here! Yeah it's morbid, but I've got a family to feed.","color":"white"}]
execute positioned -237 60 -102 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Gibromli","color":"dark_aqua"},{"text":"> Oh man, you ruined me. Nobody thinks their life is in danger since you saved the city, and now my embalming fluid futures are worthless! Good thing I hedged my bets by buying trophy options, I bet Dwarves are gonna be buying you millions of trophies!","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
