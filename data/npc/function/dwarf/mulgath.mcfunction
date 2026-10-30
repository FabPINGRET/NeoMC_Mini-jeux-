execute positioned -312 58 -163 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -312 58 -163 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mulgath","color":"dark_aqua"},{"text":"> Hero! President Snuguki was hoping you'd arrive. He's waiting in his office for you, just up those ladders!","color":"white"}]
execute positioned -312 58 -163 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mulgath","color":"dark_aqua"},{"text":"> President Snuguki would like to thank you, Hero! You can go talk to him anytime.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
