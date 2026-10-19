# Rampant des profondeurs (cave_spider, région s)
tag @e[tag=mg.ollast] remove mg.ollast
summon minecraft:cave_spider ~ ~ ~ {Tags:["mg.ol","mg.olm","mg.oln","mg.ollast","mg.olk_rampant","mg.olprov"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,CustomName:{"text":"Rampant des profondeurs","color":"dark_gray"},CustomNameVisible:0b,Health:100f,attributes:[{id:"minecraft:max_health",base:100},{id:"minecraft:attack_damage",base:14},{id:"minecraft:movement_speed",base:0.33},{id:"minecraft:follow_range",base:40},{id:"minecraft:scale",base:1.9},{id:"minecraft:step_height",base:1.1}]}
scoreboard players operation @e[tag=mg.oln] mg.olses = $olses mg.st
tag @e[tag=mg.oln] remove mg.oln
