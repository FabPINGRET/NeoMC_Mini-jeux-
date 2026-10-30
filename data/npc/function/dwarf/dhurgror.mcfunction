execute positioned -272 49 -180 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -272 49 -180 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Dhurgror","color":"dark_aqua"},{"text":"> We dwarves are incredible architects, masons, miners, and builders. Except me, I'm a seamstress!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
