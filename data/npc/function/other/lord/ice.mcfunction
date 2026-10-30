execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:block.trial_spawner.detect_player neutral @a[tag=mg.flw] ~ ~ ~ 1 1.5
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:block.trial_spawner.spawn_item_begin neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute if score Inventory SoaringTrident matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Ice","color":"aqua"},{"text":"> Thank you for saving me! Do you wanna be my best friend? Oh, ok, yeah I can understand that any bestie inauguration will have to come after the ","color":"white"},{"text":"Lord of Water ","color":"blue"},{"text":"is found.","color":"white"}]

execute if score Inventory SoaringTrident matches 1 if score Inventory Smokewings matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Ice","color":"aqua"},{"text":"> Even though the","color":"white"},{"text":" Lord of Smoke ","color":"yellow"},{"text":"is pretty stinky, we still desperately need him.","color":"white"}]

execute if score Inventory Smokewings matches 1 if score lord_of_valor Story matches 0..1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Ice","color":"aqua"},{"text":"> Your world has the ","color":"white"},{"text":"Bell","color":"gold"},{"text":", yeah? In the same way, our world has the ","color":"white"},{"text":"Lords","color":"red"},{"text":". Us missing a seventh would be like if your","color":"white"},{"text":" Bell ","color":"gold"},{"text":"was missing the little dangly part that made it ring. See? It's bad news.","color":"white"}]

execute if score lord_of_valor Story matches 2 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Ice","color":"aqua"},{"text":"> Who is this? I'm interested to hear why you chose this person.","color":"white"}]

execute if score lord_of_valor Story matches 3 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Ice","color":"aqua"},{"text":"> At this point in your adventure, I'm sure you can do anything and everything you wish. Banishing ","color":"white"},{"text":"Morbex ","color":"dark_aqua"},{"text":"will be the last step...","color":"white"}]

execute if score lord_of_valor Story matches 4 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Ice","color":"aqua"},{"text":"> I calculate that the odds of you beating the","color":"white"},{"text":" World Virus","color":"dark_aqua"},{"text":" are... heheh ok let's actually forget about numbers today! I believe in you, buddy! Just make sure you have good life insurance.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
