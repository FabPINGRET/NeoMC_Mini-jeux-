execute positioned 174 59 -2 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned 174 59 -2 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mudroy","color":"dark_aqua"},{"text":"> The","color":"white"},{"text":" bone contagion","color":"gray"},{"text":" has done horrible things to Dwarf City. Bone monsters disguised as Dwarves hide in broad daylight.","color":"white"}]
execute positioned 174 59 -2 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Mudroy","color":"dark_aqua"},{"text":"> The","color":"white"},{"text":" bone contagion","color":"gray"},{"text":" did horrible things to Dwarf City, but it sounds like those dark days are over thanks to you!.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
