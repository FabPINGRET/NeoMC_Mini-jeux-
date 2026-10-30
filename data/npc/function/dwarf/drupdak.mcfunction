execute positioned -297 58 -56 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -297 58 -56 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Drupdak","color":"dark_aqua"},{"text":"> I think my fellow juror might be a bone monster, I bet he's going to confound the court as much as possible! I'm going to disagree with whichever verdict he's going to say.","color":"white"}]
execute positioned -297 58 -56 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Drupdak","color":"dark_aqua"},{"text":"> Jury duty is for the birds I tell you! For the birds!","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
