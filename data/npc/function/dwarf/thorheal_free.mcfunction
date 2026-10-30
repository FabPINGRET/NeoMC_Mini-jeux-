execute positioned -276 39 -184 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -276 39 -184 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Thorheal","color":"dark_aqua"},{"text":"> Thanks to you, I'm free! I never want to go back to a cell again. Next time, I'll be more careful making \"haha look at me, I'm a bone monster!\" jokes.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
