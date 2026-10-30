execute positioned 10072 195 1262 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10072 195 1262 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Kraggtun the Onescar","color":"blue"},{"text":"> I lead the domestic division of the ","color":"white"},{"text":"Rubblewalkers","color":"blue"},{"text":". We're planning countermeasures in case anyone tries stealing any more of our sacred buildings.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
