# Goule (zombie, région w)
tag @e[tag=mg.ollast] remove mg.ollast
summon minecraft:zombie ~ ~ ~ {Tags:["mg.ol","mg.olm","mg.oln","mg.ollast","mg.olk_goule","mg.olund"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,CustomName:{"text":"Goule","color":"dark_green"},CustomNameVisible:0b,Health:24f,CanBreakDoors:0b,attributes:[{id:"minecraft:max_health",base:24},{id:"minecraft:attack_damage",base:3},{id:"minecraft:movement_speed",base:0.25},{id:"minecraft:follow_range",base:40},{id:"minecraft:scale",base:1.0},{id:"minecraft:step_height",base:1.1}]}
scoreboard players operation @e[tag=mg.oln] mg.olses = $olses mg.st
tag @e[tag=mg.oln] remove mg.oln
