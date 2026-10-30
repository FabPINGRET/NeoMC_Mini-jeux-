execute positioned -297 58 -59 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -297 58 -59 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Plunktheeth","color":"dark_aqua"},{"text":"> I have a bad feeling about this guy, what if he shows his true colors as a bone monster and hurts someone?","color":"white"}]
execute positioned -297 58 -59 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Plunktheeth","color":"dark_aqua"},{"text":"> I'm one of Wumwug Bim's secret admirers too, so out of jealousy I'm gonna say Tugwi is innocent!","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
