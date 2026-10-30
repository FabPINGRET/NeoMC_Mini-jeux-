execute positioned -310 65 -158 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -310 65 -158 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Dwotgrum","color":"dark_aqua"},{"text":"> I'm riffling through these bone monster sightings to see which are legitimate and which are just paranoia!","color":"white"}]
execute positioned -310 65 -158 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Dwotgrum","color":"dark_aqua"},{"text":"> The Food and Drug and Rock Administration just warned against eating asbestos. Bunch of cowards is what I'd call em.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
