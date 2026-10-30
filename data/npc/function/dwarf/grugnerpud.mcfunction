execute positioned -195 59 -115 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -195 59 -115 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Grugnerpud","color":"dark_aqua"},{"text":"> Dwarf City is closed to outsiders by order of President Snuguki until the Grand Court can sort out who's a scary bone monster and who's not. You're not getting in here, sorry pal. Those bone monsters coming from the contagion can disguise themselves as anyone! Don't you know?","color":"white"}]
execute positioned -195 59 -115 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Grugnerpud","color":"dark_aqua"},{"text":"> I appreciate the \"you defeating the looming threat of destruction\" stuff and all, but, well, what's a gatekeeper supposed to do all day now? Did you ever stop to think about people's job security when you were messing up that Kraken?","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value
