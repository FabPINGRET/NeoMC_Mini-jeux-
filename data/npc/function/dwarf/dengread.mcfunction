execute positioned -245 60 -110 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -245 60 -110 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Dengread","color":"dark_aqua"},{"text":"> What the stones... SNUD is going crazy right now. Time to sell all my SNUD!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
