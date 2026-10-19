# Brute calcinée (piglin_brute, région se)
tag @e[tag=mg.ollast] remove mg.ollast
summon minecraft:piglin_brute ~ ~ ~ {Tags:["mg.ol","mg.olm","mg.oln","mg.ollast","mg.olk_brute"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,CustomName:{"text":"Brute calcinée","color":"dark_red"},CustomNameVisible:0b,Health:130f,equipment:{mainhand:{id:"minecraft:golden_axe",count:1}},drop_chances:{mainhand:0f},IsImmuneToZombification:1b,attributes:[{id:"minecraft:max_health",base:130},{id:"minecraft:attack_damage",base:17},{id:"minecraft:movement_speed",base:0.35},{id:"minecraft:follow_range",base:40},{id:"minecraft:scale",base:1.05},{id:"minecraft:step_height",base:1.1}]}
scoreboard players operation @e[tag=mg.oln] mg.olses = $olses mg.st
tag @e[tag=mg.oln] remove mg.oln
