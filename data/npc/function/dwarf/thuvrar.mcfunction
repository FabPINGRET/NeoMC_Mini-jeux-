execute positioned -254 34 -169 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -254 34 -169 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Thuvrar","color":"dark_aqua"},{"text":"> If you remember, last time you were here, there was a giant stone hand emerging from the ground in the south city which belonged to an entity called the Empyrean. It was made of minerals, so we ate it!","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
