execute positioned 172 59 -33 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute if score BetterEconomy bool matches 0 positioned 172 59 -33 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Throtmut","color":"dark_aqua"},{"text":"> Things are so expensive right now. I wish I had some mutton to give you, but I don't, I apologize. Supply just isn't there.","color":"white"}]
execute if score BetterEconomy bool matches 1 positioned 172 59 -33 run tellraw @a[distance=..10,tag=!vendor_mutton_0,tag=mg.flw] [{"text":"<"},{"text":"Throtmut","color":"dark_aqua"},{"text":"> I have mutton for you today! Rubbed with the best Dwarven herbs and spices! I hope you love it, friend.","color":"white"}]
execute if score BetterEconomy bool matches 1 positioned 172 59 -33 run tellraw @a[distance=..10,tag=vendor_mutton_0,tag=mg.flw] [{"text":"<"},{"text":"Throtmut","color":"dark_aqua"},{"text":"> I'm marinating more mutton for tomorrow!","color":"white"}]

execute if score BetterEconomy bool matches 1 positioned 172 59 -33 run give @a[distance=..10,tag=!vendor_mutton_0,tag=mg.flw] cooked_mutton 8
execute if score BetterEconomy bool matches 1 positioned 172 59 -33 run tag @a[distance=..10,tag=!vendor_mutton_0,tag=mg.flw] add vendor_mutton_0


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
