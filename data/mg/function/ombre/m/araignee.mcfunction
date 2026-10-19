# Araignée sylvestre (spider, région nw)
tag @e[tag=mg.ollast] remove mg.ollast
summon minecraft:spider ~ ~ ~ {Tags:["mg.ol","mg.olm","mg.oln","mg.ollast","mg.olk_araignee","mg.olprov"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,CustomName:{"text":"Araignée sylvestre","color":"dark_green"},CustomNameVisible:0b,Health:34f,attributes:[{id:"minecraft:max_health",base:34},{id:"minecraft:attack_damage",base:5},{id:"minecraft:movement_speed",base:0.32},{id:"minecraft:follow_range",base:40},{id:"minecraft:scale",base:1.25},{id:"minecraft:step_height",base:1.1}]}
scoreboard players operation @e[tag=mg.oln] mg.olses = $olses mg.st
tag @e[tag=mg.oln] remove mg.oln
