execute positioned -314 45 -127 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -314 45 -127 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Groordrec","color":"dark_aqua"},{"text":"> Lots of monsters show up down here in the lower parts of the city at night. No, not the shape-shifting bone kind, just standard rock monsters. Careful you don't get ground to dust.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
