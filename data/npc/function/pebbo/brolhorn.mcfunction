execute positioned 10102 188 1309 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10102 188 1309 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brolhorn the Stonefist","color":"blue"},{"text":"> No funny business in the throne room. No goofing off in there or else you're gonna get in big trouble.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
