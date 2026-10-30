execute positioned -281 57 -143 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -281 57 -143 if score mainstory Story <= 3 Value run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Dumguk","color":"dark_aqua"},{"text":"> This plaza was built as a nice public meeting place, but nobody hangs around here much anymore. Not since some bone monsters built that eerie structure back there. Our masons have tried, but they can't remove it.","color":"white"}]
execute positioned -281 57 -143 if score mainstory Story > 3 Value run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Dumguk","color":"dark_aqua"},{"text":"> It was a portal this whole time... I'm worried to see what else pours through. I doubt many dwarves will want to hang around here now.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory Story >= 0 Value 
