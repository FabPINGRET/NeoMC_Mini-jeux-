execute positioned -281 58 -53 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -281 58 -53 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Orgus","color":"dark_aqua"},{"text":"> I'm so","color":"white"},{"text":" dddd","obfuscated":true},{"text":"ing overwhelmed.","color":"white"}]
execute positioned -281 58 -53 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Orgus","color":"dark_aqua"},{"text":"> Oh man, you have no idea how relieved I am you cleared up that mess for us. It's back to normal arrests for me! Normal arrests completely unrelated to horrifying, suspicion-sowing monsters.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
