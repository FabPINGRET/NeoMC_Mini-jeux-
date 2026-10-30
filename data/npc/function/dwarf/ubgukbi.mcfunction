execute positioned -347 59 -96 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute if score BetterEconomy bool matches 0 positioned -347 59 -96 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Ubgukbi","color":"dark_aqua"},{"text":"> I wish I had mutton to give, but I don't. Times are tough. Try closing your eyes and imagine as hard as you can that you're eating some tender mutton. It's better than nothing!","color":"white"}]
execute if score BetterEconomy bool matches 1 positioned -347 59 -96 run tellraw @a[distance=..10,tag=!vendor_mutton_1,tag=mg.flw] [{"text":"<"},{"text":"Ubgukbi","color":"dark_aqua"},{"text":"> We dwarves are famous for our mutton! The trick is to make sure you cook it. Here's some, try it!","color":"white"}]
execute if score BetterEconomy bool matches 1 positioned -347 59 -96 run tellraw @a[distance=..10,tag=vendor_mutton_1,tag=mg.flw] [{"text":"<"},{"text":"Ubgukbi","color":"dark_aqua"},{"text":"> No more meat for today, I gotta do my secret technique for preparing more. The technique is cooking it! Don't tell anyone, ok?","color":"white"}]

execute if score BetterEconomy bool matches 1 positioned -347 59 -96 run give @a[distance=..10,tag=!vendor_mutton_1,tag=mg.flw] cooked_mutton 8
execute if score BetterEconomy bool matches 1 positioned -347 59 -96 run tag @a[distance=..10,tag=!vendor_mutton_1,tag=mg.flw] add vendor_mutton_1


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
