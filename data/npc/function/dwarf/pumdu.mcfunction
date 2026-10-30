execute positioned -353 58 -139 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -353 58 -139 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Pumdu","color":"dark_aqua"},{"text":"> It's dangerous being in the Dwarf Legion. They arm us for our own safety, but... what if one of my mates here is actually a bone monster? He could stab us all in our sleep!","color":"white"}]
execute positioned -353 58 -139 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Pumdu","color":"dark_aqua"},{"text":"> You're an inspiration to us all, Hero. Turns out none of my friends were bone monsters after all! Just some random guys I didn't know too well.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
