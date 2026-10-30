execute positioned -352 59 -121 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -352 59 -121 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Grofelda","color":"dark_aqua"},{"text":"> Have some of my cake! I bake new ones every day, so don't be shy!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
