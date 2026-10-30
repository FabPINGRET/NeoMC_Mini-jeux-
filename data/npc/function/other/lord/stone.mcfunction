execute positioned 10029 95 -95 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 0.8

execute if score Inventory IcelightScepter matches 0 positioned 10029 95 -95 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Stone","color":"gray"},{"text":"> Thanks for freeing me, I trust that you'll keep the secret of the Petrified Kingdom quiet. The ","color":"white"},{"text":"Lord of Ice","color":"aqua"},{"text":" is the next Lord you should rescue, I think.","color":"white"}]

execute if score Inventory IcelightScepter matches 1 if score Inventory SoaringTrident matches 0 positioned 10029 95 -95 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Stone","color":"gray"},{"text":"> How would one get to the Alabaster Pools? For a regular person, I don't know. That's where you must go next, though.","color":"white"}]

execute if score Inventory SoaringTrident matches 1 if score Inventory Smokewings matches 0 positioned 10029 95 -95 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Stone","color":"gray"},{"text":"> Good luck dealing with whatever monster was able to subdue the ","color":"white"},{"text":"Lord of Smoke","color":"yellow"},{"text":". I can't imagine how he could ever have been captured.","color":"white"}]

execute if score Inventory Smokewings matches 1 if score lord_of_valor Story matches 0..1 positioned 10029 95 -95 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Stone","color":"gray"},{"text":"> You actually destroyed the ","color":"white"},{"text":"Lord of Smoke","color":"yellow"},{"text":"? I don't understand how you're so strong, you'd be an even match for the seven, er, six of us put together I'd wager.","color":"white"}]

execute if score lord_of_valor Story matches 2 positioned 10029 95 -95 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Stone","color":"gray"},{"text":"> Are you sure this fellow should be the seventh Lord?","color":"white"}]

execute if score lord_of_valor Story matches 3 positioned 10029 95 -95 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Stone","color":"gray"},{"text":"> It is ","color":"white"},{"text":"Morbex's","color":"dark_aqua"},{"text":" final hour. If you need help reaching his machine, try deploying those","color":"white"},{"text":" wings","color":"yellow"},{"text":" you have ","color":"white"},{"text":"right after breaching the surface of the water","color":"blue"},{"text":"...","color":"white"}]

execute if score lord_of_valor Story matches 4 positioned 10029 95 -95 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Stone","color":"gray"},{"text":"> Once the enemy is defeated and the","color":"white"},{"text":" Floaty Isles","color":"gold"},{"text":" are safe, I hope the ","color":"white"},{"text":"Cobblemancers","color":"green"},{"text":" will come home. As the head of their order, I'd like to see them again.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
