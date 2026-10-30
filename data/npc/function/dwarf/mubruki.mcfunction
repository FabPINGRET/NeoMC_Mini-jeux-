execute positioned 172 59 -12 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 172 59 -12 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mubruki","color":"dark_aqua"},{"text":"> Everything is so wooden here, it feels like it could all burn down at any moment.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
