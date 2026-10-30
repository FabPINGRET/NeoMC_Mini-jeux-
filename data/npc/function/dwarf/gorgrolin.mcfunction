execute positioned -235 41 -139 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute if block -235 38 -140 air positioned -235 41 -139 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Gorgrolin","color":"dark_aqua"},{"text":"> GAH WHAT! By the stones, what were you doing in my banana closet? How did you get in there? Please, don't scare me like that, I thought for a moment you were a creature or a fiend of some sort.","color":"white"}]
execute if block -235 38 -140 stone positioned -235 41 -139 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Gorgrolin","color":"dark_aqua"},{"text":"> Please, don't scare me again, I thought for a moment you were a creature or a fiend of some sort.","color":"white"}]

setblock -235 38 -140 stone

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
