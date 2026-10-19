# Elfe noir (illusioner, région nw)
tag @e[tag=mg.ollast] remove mg.ollast
summon minecraft:illusioner ~ ~ ~ {Tags:["mg.ol","mg.olm","mg.oln","mg.ollast","mg.olk_elfe"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,CustomName:{"text":"Elfe noir","color":"dark_purple"},CustomNameVisible:0b,Health:38f,equipment:{mainhand:{id:"minecraft:bow",count:1}},drop_chances:{mainhand:0f},attributes:[{id:"minecraft:max_health",base:38},{id:"minecraft:attack_damage",base:5},{id:"minecraft:movement_speed",base:0.33},{id:"minecraft:follow_range",base:40},{id:"minecraft:scale",base:1.0},{id:"minecraft:step_height",base:1.1}]}
scoreboard players operation @e[tag=mg.oln] mg.olses = $olses mg.st
tag @e[tag=mg.oln] remove mg.oln
