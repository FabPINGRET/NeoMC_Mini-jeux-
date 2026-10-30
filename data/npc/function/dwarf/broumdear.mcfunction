execute positioned -259 43 -169 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -259 43 -169 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Broumdear","color":"dark_aqua"},{"text":"> Stay back! I don't want any bone monsters near my house!","color":"white"}]
execute positioned -259 43 -169 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Broumdear","color":"dark_aqua"},{"text":"> I burped in here just a little bit ago so sorry if it reeks.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
