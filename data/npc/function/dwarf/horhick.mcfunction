execute positioned -311 65 -167 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -311 65 -167 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Horhick","color":"dark_aqua"},{"text":"> What do we do if President Snuguki has been replaced by a bone monster? I'm worried he takes his own security too lightly.","color":"white"}]
execute positioned -311 65 -167 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Horhick","color":"dark_aqua"},{"text":"> Let us know if there's anything we dwarves can do for you.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
