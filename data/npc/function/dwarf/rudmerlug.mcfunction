execute positioned -258 52 -205 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -258 52 -205 if score mainstory Story <= 3 Value run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Rudmerlug","color":"dark_aqua"},{"text":"> In the past, the major threats to the Dwarves always came from beneath, what with us delving too deep and blah blah blah, all that classic Dwarf stuff. We still have no idea where these","color":"white"},{"text":" scourges","color":"light_purple"},{"text":" came from.","color":"white"}]
execute positioned -258 52 -205 if score mainstory Story > 3 Value run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Rudmerlug","color":"dark_aqua"},{"text":"> In the past, the major threats to the Dwarves always came from beneath, what with us delving too deep and blah blah blah, all that classic Dwarf stuff. Now, we're being threatened by an evil entity from another dimension. Feels weird that it's not actually our own fault this time.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
