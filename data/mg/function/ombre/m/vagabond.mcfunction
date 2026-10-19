# Vagabond gelé (stray, région n)
tag @e[tag=mg.ollast] remove mg.ollast
summon minecraft:stray ~ ~ ~ {Tags:["mg.ol","mg.olm","mg.oln","mg.ollast","mg.olk_vagabond","mg.olund"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,CustomName:{"text":"Vagabond gelé","color":"aqua"},CustomNameVisible:0b,Health:40f,equipment:{mainhand:{id:"minecraft:bow",count:1}},drop_chances:{mainhand:0f},attributes:[{id:"minecraft:max_health",base:40},{id:"minecraft:attack_damage",base:6},{id:"minecraft:movement_speed",base:0.27},{id:"minecraft:follow_range",base:40},{id:"minecraft:scale",base:1.0},{id:"minecraft:step_height",base:1.1}]}
scoreboard players operation @e[tag=mg.oln] mg.olses = $olses mg.st
tag @e[tag=mg.oln] remove mg.oln
