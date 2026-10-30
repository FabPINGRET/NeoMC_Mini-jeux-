execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.step neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.creaking.unfreeze neutral @a[tag=mg.flw] ~ ~ ~ 1 1

execute if score Inventory Honeyboost matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Forest","color":"green"},{"text":"> Thank you for rescuing me, hero. That defiler had no business touching the Serpent King's bones. Please, rescue the","color":"white"},{"text":" Lord of Spores","color":"light_purple"},{"text":" next! We were always good friends.","color":"white"}]

execute if score Inventory Honeyboost matches 1 if score Inventory DominionRod matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Forest","color":"green"},{"text":"> I've never actually visited the ","color":"white"},{"text":"Isle of Silence","color":"gray"},{"text":". You'll have to let me know how it is, I've just never had a reason to go there.","color":"white"}]

execute if score Inventory DominionRod matches 1 if score Inventory IcelightScepter matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Forest","color":"green"},{"text":"> Rescuing the ","color":"white"},{"text":"Lord of Ice","color":"aqua"},{"text":" is the best next move. We would help you, but we've got enough on our plates trying to stall ","color":"white"},{"text":"Morbex's","color":"dark_aqua"},{"text":" plans. Plus, as hard as it is to admit, I don't think we're as strong as the Dreadwardens.","color":"white"}]

execute if score Inventory IcelightScepter matches 1 if score Inventory SoaringTrident matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Forest","color":"green"},{"text":"> It's time you investigated the Froggadews. We haven't heard word of anything unsavory happening to the","color":"white"},{"text":" Lord of Water","color":"blue"},{"text":", but he's also nowhere to be found. It's easy to guess he's in trouble.","color":"white"}]

execute if score Inventory SoaringTrident matches 1 if score Inventory Smokewings matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Forest","color":"green"},{"text":"> The","color":"white"},{"text":" Lord of Smoke","color":"yellow"},{"text":" represents the best of us. He always knew what to do.","color":"white"}]

execute if score Inventory Smokewings matches 1 if score lord_of_valor Story matches 0..1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Forest","color":"green"},{"text":"> The","color":"white"},{"text":" Lord of Smoke","color":"yellow"},{"text":" betrayed us after all. I had already discerned that the ","color":"white"},{"text":"Virus","color":"dark_aqua"},{"text":" knew too much about our weaknesses...","color":"white"}]

execute if score lord_of_valor Story matches 2 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Forest","color":"green"},{"text":"> Is that who I think it is? Haha, good choice!","color":"white"}]

execute if score lord_of_valor Story matches 3 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Forest","color":"green"},{"text":"> You can reach ","color":"white"},{"text":"Morbex's machine","color":"dark_aqua"},{"text":" if you try! There's an entrance in the west side, facing away from the Pools.","color":"white"}]

execute if score lord_of_valor Story matches 4 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Forest","color":"green"},{"text":"> Your fearlessness is inspiring, hero. Then again, I'd be fearless too if I were as freakishly strong as you are.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
