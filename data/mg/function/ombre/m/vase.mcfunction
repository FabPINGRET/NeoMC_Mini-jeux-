# Vase putride (slime, région ne)
tag @e[tag=mg.ollast] remove mg.ollast
summon minecraft:slime ~ ~ ~ {Tags:["mg.ol","mg.olm","mg.oln","mg.ollast","mg.olk_vase"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,CustomName:{"text":"Vase putride","color":"green"},CustomNameVisible:0b,Health:40f,Size:2,attributes:[{id:"minecraft:max_health",base:40},{id:"minecraft:attack_damage",base:7},{id:"minecraft:movement_speed",base:0.4},{id:"minecraft:follow_range",base:40},{id:"minecraft:scale",base:1.0},{id:"minecraft:step_height",base:1.1}]}
scoreboard players operation @e[tag=mg.oln] mg.olses = $olses mg.st
tag @e[tag=mg.oln] remove mg.oln
