execute positioned -242 49 -182 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -242 49 -182 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Budgred","color":"dark_aqua"},{"text":"> I'm tired of living in fear. I'm tired of wondering when a friend is going to transform into a bone monster and hurt me or someone I love.","color":"white"}]
execute positioned -242 49 -182 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Budgred","color":"dark_aqua"},{"text":"> You should visit the Grand Courthouse if you haven't yet, me and a couple of buddies built it in an afternoon. Oh, you've been there?","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
