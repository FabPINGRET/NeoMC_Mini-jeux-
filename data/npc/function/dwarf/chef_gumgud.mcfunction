execute positioned -280 41 -61 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -280 41 -61 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Chef Gumgud","color":"dark_aqua"},{"text":"> Order up! By the way, I did not cough into the food twice this morning.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
