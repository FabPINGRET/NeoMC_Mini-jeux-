execute positioned -292 58 -55 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -292 58 -55 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Wumwug Bim","color":"dark_aqua"},{"text":"> Your honor, there's no way this guy doesn't have so many bones, I don't trust him at all. I've never accused anyone of being a bone monster before but this guy is! Literally count his bones your honor, count the insane number of bones he has.","color":"white"}]
execute positioned -292 58 -55 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Wumwug Bim","color":"dark_aqua"},{"text":"> Tugwi, you rascal, I think it's you leaving me all those sweet treats and kind notes! Haha I'm gonna get to the bottom of this, I've got a really sweet, kind, thoughtful admirer out there and I'm accusing you of being him! Aw you're blushing, I know it's you Tugwi!","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
