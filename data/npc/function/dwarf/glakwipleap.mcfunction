execute positioned -355 58 -112 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -355 58 -112 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Glakwipleap","color":"dark_aqua"},{"text":"> There's no way I'm eating bread baked by a potential bone monster. Even shopping is dangerous these days.","color":"white"}]
execute positioned -355 58 -112 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Glakwipleap","color":"dark_aqua"},{"text":"> ♫ Gonna go to the market! Gonna buy some bread! And I know when I see it, it'll be looking back at my head! ♪","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
