execute positioned -210 59 -100 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -210 59 -100 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Yumgrup","color":"dark_aqua"},{"text":"> The city's gatekeeper can be a bit overproud. The Dwarf Legion can defend this city just fine! Not to mention the fact we have a police now. Yeah, one police, why do you ask?","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
