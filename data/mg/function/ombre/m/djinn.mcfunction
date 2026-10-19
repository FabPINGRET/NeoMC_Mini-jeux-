# Djinn des vents (breeze, région e)
tag @e[tag=mg.ollast] remove mg.ollast
summon minecraft:breeze ~ ~ ~ {Tags:["mg.ol","mg.olm","mg.oln","mg.ollast","mg.olk_djinn"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,CustomName:{"text":"Djinn des vents","color":"aqua"},CustomNameVisible:0b,Health:70f,attributes:[{id:"minecraft:max_health",base:70},{id:"minecraft:attack_damage",base:10},{id:"minecraft:movement_speed",base:0.3},{id:"minecraft:follow_range",base:40},{id:"minecraft:scale",base:1.2},{id:"minecraft:step_height",base:1.1}]}
scoreboard players operation @e[tag=mg.oln] mg.olses = $olses mg.st
tag @e[tag=mg.oln] remove mg.oln
