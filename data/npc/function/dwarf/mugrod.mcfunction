execute positioned -359 58 -95 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -359 58 -95 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mugrod","color":"dark_aqua"},{"text":"> I accidentally left my shopping list at home. If I forget to buy eggs again the wife is gonna flay me alive.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value
