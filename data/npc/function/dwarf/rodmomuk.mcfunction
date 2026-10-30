execute positioned -289 58 -69 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -289 58 -69 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Rodmomuk","color":"dark_aqua"},{"text":"> Court is in session! No that's ok, that means you can go talk to anyone in here whenever you want. Stones, I hate my job.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
