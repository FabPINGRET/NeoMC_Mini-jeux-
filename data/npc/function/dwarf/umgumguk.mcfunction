execute positioned -207 59 -109 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -207 59 -109 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Umgumguk","color":"dark_aqua"},{"text":"> Like everything else in this city, our weapons are fashioned from stone.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
