# Pillard du désert (vindicator, région e)
tag @e[tag=mg.ollast] remove mg.ollast
summon minecraft:vindicator ~ ~ ~ {Tags:["mg.ol","mg.olm","mg.oln","mg.ollast","mg.olk_pillard"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,CustomName:{"text":"Pillard du désert","color":"gold"},CustomNameVisible:0b,Health:84f,equipment:{mainhand:{id:"minecraft:golden_axe",count:1},head:{id:"minecraft:golden_helmet",count:1},chest:{id:"minecraft:golden_chestplate",count:1}},drop_chances:{mainhand:0f,head:0f,chest:0f},attributes:[{id:"minecraft:max_health",base:84},{id:"minecraft:attack_damage",base:13},{id:"minecraft:movement_speed",base:0.33},{id:"minecraft:follow_range",base:40},{id:"minecraft:scale",base:1.0},{id:"minecraft:step_height",base:1.1}]}
scoreboard players operation @e[tag=mg.oln] mg.olses = $olses mg.st
tag @e[tag=mg.oln] remove mg.oln
