execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.drowned.ambient_water neutral @a[tag=mg.flw] ~ ~ ~ 1 2

execute if score Inventory Smokewings matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Water","color":"blue"},{"text":"> I'm very impressed that you were able to find me. I'm hopeful the ","color":"white"},{"text":"Virus ","color":"dark_aqua"},{"text":"is running out of weapons to use against us, but I doubt that is the case. The ","color":"white"},{"text":"Lord of Smoke","color":"yellow"},{"text":" will be even harder to rescue.","color":"white"}]

execute if score Inventory Smokewings matches 1 if score lord_of_valor Story matches 0..1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Water","color":"blue"},{"text":"> I'm furious with the ","color":"white"},{"text":"Lord of Smoke","color":"yellow"},{"text":". Imagine what suffering could have been avoided if he had stood up to the","color":"white"},{"text":" World Virus","color":"dark_aqua"},{"text":" instead of kneeling like a coward. If he had died then, at least he would have died a hero. Above all else, the next seventh Lord must have a pure heart...","color":"white"}]

execute if score lord_of_valor Story matches 2 positioned 10022 97 -95 if entity @a[gamemode=!spectator,distance=10..,tag=mg.flw] positioned 10027 94 -101 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Water","color":"blue"},{"text":"> Gather everyone here, and hurry.","color":"white"}]

execute if score lord_of_valor Story matches 3 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Water","color":"blue"},{"text":"> You can reach ","color":"white"},{"text":"Morbex's machine","color":"dark_aqua"},{"text":" from the ","color":"white"},{"text":"Alabaster Pools","color":"blue"},{"text":". Try launching yourself from the top of the ","color":"white"},{"text":"tallest watertree","color":"blue"},{"text":"!","color":"white"}]

execute if score lord_of_valor Story matches 4 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Water","color":"blue"},{"text":"> The","color":"white"},{"text":" Dark Isles","color":"dark_purple"},{"text":" might be stronger than ever now. It will take some time to rebuild, and the new cultists are a pain in the rear, but we always make it through hardship having grown.","color":"white"}]


execute if score lord_of_valor Story matches 2 positioned 10022 97 -95 if entity @a[gamemode=!spectator,distance=..10,tag=mg.flw] unless entity @a[gamemode=!spectator,distance=10..,tag=mg.flw] positioned 10027 94 -101 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run function npc:overworld_cutscene/lord_of_valor/0

execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run kill @n[tag=quest_marker,distance=..3]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
