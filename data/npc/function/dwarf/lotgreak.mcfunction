execute positioned -268 57 -190 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -268 57 -190 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Lotgreak","color":"dark_aqua"},{"text":"> Most Dwarves live in this district, it's relatively comfortable. City life suits us; both digging through rock and building things with it cause our little brains to flood with more Dwarf dopamine than we know how to process! There's no ecstacy known to Dwarfkind greater than breaking a rock and putting it on top of another one somewhere else. Ooaaohhohh...","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
