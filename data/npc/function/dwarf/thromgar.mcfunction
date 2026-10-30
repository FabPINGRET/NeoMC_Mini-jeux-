execute positioned -274 41 -58 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute if score BetterEconomy bool matches 0 positioned -274 41 -58 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Thromgar","color":"dark_aqua"},{"text":"> We can't really afford to be giving food out right now to non-dwarves. We're basically 75% tummy and the rest is mostly skin and hair. Sorry, that's a weird Dwarf fact. Maybe if times get better we could let you try our famous Grud Platter.","color":"white"}]
execute if score BetterEconomy bool matches 1 positioned -274 41 -58 run tellraw @a[distance=..10,tag=!vendor_mutton_2,tag=mg.flw] [{"text":"<"},{"text":"Thromgar","color":"dark_aqua"},{"text":"> One Grud Platter to go! It's a bunch of mutton chops, all stacked up on top of each other!","color":"white"}]
execute if score BetterEconomy bool matches 1 positioned -274 41 -58 run tellraw @a[distance=..10,tag=vendor_mutton_2,tag=mg.flw] [{"text":"<"},{"text":"Thromgar","color":"dark_aqua"},{"text":"> Hey, I know you haven't finished the Grud Platter I already gave you today. If you're feeling up for another one, come back tomorrow.","color":"white"}]

execute if score BetterEconomy bool matches 1 positioned -274 41 -58 run give @a[distance=..10,tag=!vendor_mutton_2,tag=mg.flw] cooked_mutton 8
execute if score BetterEconomy bool matches 1 positioned -274 41 -58 run tag @a[distance=..10,tag=!vendor_mutton_2,tag=mg.flw] add vendor_mutton_2


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
