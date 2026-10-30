execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.silverfish.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 2
execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.puffer_fish.blow_up neutral @a[tag=mg.flw] ~ ~ ~ 1 0.1

execute if score Inventory DominionRod matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Spores","color":"light_purple"},{"text":"> Thank you for saving my life, hero. Tell ","color":"white"},{"text":"Slime Man","color":"green"},{"text":"thank you from me if you see him again. He's got a good heart. The ","color":"white"},{"text":"Lord of Stone","color":"gray"},{"text":" will need your help next.","color":"white"}]

execute if score Inventory DominionRod matches 1 if score Inventory IcelightScepter matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Spores","color":"light_purple"},{"text":"> The ","color":"white"},{"text":"Lord of Ice","color":"aqua"},{"text":" was always incredibly honorable. It's disturbing what has happened to Windbite in the Lord's absence.","color":"white"}]

execute if score Inventory IcelightScepter matches 1 if score Inventory SoaringTrident matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Spores","color":"light_purple"},{"text":"> I believe there is a Contagion of the ","color":"white"},{"text":"Virus ","color":"dark_aqua"},{"text":"at play in the Alabaster Pools. You have more experience than anyone destroying Contagions.","color":"white"}]

execute if score Inventory SoaringTrident matches 1 if score Inventory Smokewings matches 0 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Spores","color":"light_purple"},{"text":"> Can you find a way to survive on the Isle of Smoke? You'll need to. The ","color":"white"},{"text":"Lord of Smoke","color":"yellow"},{"text":" is the last piece of the puzzle.","color":"white"}]

execute if score Inventory Smokewings matches 1 if score lord_of_valor Story matches 0..1 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Spores","color":"light_purple"},{"text":"> Who might make a good choice for a seventh Lord? Well, each of us were chosen from a position of leadership over our respective peoples. My instinct would be to find a leader, but my instincts can be out of tune.","color":"white"}]

execute if score lord_of_valor Story matches 2 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Spores","color":"light_purple"},{"text":"> I'm pleased you chose a Glooblin, hero. They are a gross people, but kind.","color":"white"}]

execute if score lord_of_valor Story matches 3 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Spores","color":"light_purple"},{"text":"> The","color":"white"},{"text":" Lord of Valor","color":"yellow"},{"text":"... That does have a nice ring to it. I'm proud he is from the ","color":"white"},{"text":"Moldsap Woods","color":"light_purple"},{"text":".","color":"white"}]

execute if score lord_of_valor Story matches 4 at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lord of Spores","color":"light_purple"},{"text":"> The","color":"white"},{"text":" Lord of Valor","color":"yellow"},{"text":" looks cool. Cooler than the Lord of Smoke ever did. Plus, this new guy isn't an evil traitor.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
