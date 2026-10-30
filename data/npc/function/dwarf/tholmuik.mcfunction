execute positioned -236 60 -110 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -236 60 -110 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Tholmuik","color":"dark_aqua"},{"text":"> Stock broker? I hardly know her! Haha, just kiddin' around. Dwarf City is under so much attack.","color":"white"}]
execute positioned -236 60 -110 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Tholmuik","color":"dark_aqua"},{"text":"> Stock broker? I hardly know her! Haha, just bein' me.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
