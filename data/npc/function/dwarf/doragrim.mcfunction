execute positioned -157 58 -80 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -157 58 -80 if score Inventory Bonestride matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Doragrim","color":"dark_aqua"},{"text":"> Good luck getting into the city, that gatekeeper is a real piece of work. If you can't find any other ways in, try asking around. There are always ways to smuggle people into places.","color":"white"}]
execute positioned -157 58 -80 if score Inventory Bonestride matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Doragrim","color":"dark_aqua"},{"text":"> There used to be a bunch of orphans living around here, but they started some sort of digging operation around the same time the","color":"white"},{"text":" scourges","color":"light_purple"},{"text":" showed up. I wonder what became of them.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
