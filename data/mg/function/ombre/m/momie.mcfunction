# Momie (husk, région e)
tag @e[tag=mg.ollast] remove mg.ollast
summon minecraft:husk ~ ~ ~ {Tags:["mg.ol","mg.olm","mg.oln","mg.ollast","mg.olk_momie","mg.olund"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,CustomName:{"text":"Momie","color":"gold"},CustomNameVisible:0b,Health:80f,CanBreakDoors:0b,attributes:[{id:"minecraft:max_health",base:80},{id:"minecraft:attack_damage",base:12},{id:"minecraft:movement_speed",base:0.26},{id:"minecraft:follow_range",base:40},{id:"minecraft:scale",base:1.1},{id:"minecraft:step_height",base:1.1}]}
scoreboard players operation @e[tag=mg.oln] mg.olses = $olses mg.st
tag @e[tag=mg.oln] remove mg.oln
