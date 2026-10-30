execute positioned -293 58 -49 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -293 58 -49 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Gumgumgud","color":"dark_aqua"},{"text":"> I swear on penalty of perjury I witnessed Tugwi brushing his teeth your honor, which, if you didn't know, teeth is bones your honor.","color":"white"}]
execute positioned -293 58 -49 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Gumgumgud","color":"dark_aqua"},{"text":"> I swear on penalty of perjury I witnessed Tugwi secretly deliver a gift basket and a note to Wumwug Bim's apartment your honor.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
