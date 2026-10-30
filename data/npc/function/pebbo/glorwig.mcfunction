execute positioned 10121 180 1276 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute if score BetterEconomy bool matches 1 positioned 10111 180 1283 run tellraw @a[distance=..10,tag=!vendor_cooked_beef_0,tag=mg.flw] [{"text":"<"},{"text":"Glorwig Plinket","color":"yellow"},{"text":"> I carved up a bovine beetle and smoked it for 14 hours after slathering it in butter, brown sugar, pepper, and hot honey. You gotta try this stuff.","color":"white"}]
execute if score BetterEconomy bool matches 1 positioned 10111 180 1283 run tellraw @a[distance=..10,tag=vendor_cooked_beef_0,tag=mg.flw] [{"text":"<"},{"text":"Glorwig Plinket","color":"yellow"},{"text":"> I will absolutely give you more meat if you give me time to smoke it.","color":"white"}]
execute if score BetterEconomy bool matches 0 positioned 10111 180 1283 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Glorwig Plinket","color":"yellow"},{"text":"> I'm sort of shocked that you haven't fixed the economy by now at this point in your adventures.","color":"white"}]

execute if score BetterEconomy bool matches 1 positioned 10111 180 1283 run give @a[distance=..10,tag=!vendor_cooked_beef_0,tag=mg.flw] cooked_beef 16
execute if score BetterEconomy bool matches 1 positioned 10111 180 1283 run tag @a[distance=..10,tag=!vendor_cooked_beef_0,tag=mg.flw] add vendor_cooked_beef_0


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
