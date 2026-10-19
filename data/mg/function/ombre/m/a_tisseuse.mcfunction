# Tisseuse alpha (spider, région nw)
tag @e[tag=mg.ollast] remove mg.ollast
summon minecraft:spider ~ ~ ~ {Tags:["mg.ol","mg.olm","mg.oln","mg.ollast","mg.olk_a_tisseuse","mg.olprov","mg.olalpha"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,CustomName:{"text":"Tisseuse alpha","color":"dark_red"},CustomNameVisible:0b,Health:480f,attributes:[{id:"minecraft:max_health",base:480},{id:"minecraft:attack_damage",base:10},{id:"minecraft:movement_speed",base:0.33},{id:"minecraft:follow_range",base:40},{id:"minecraft:scale",base:2.2},{id:"minecraft:step_height",base:1.1},{id:"minecraft:knockback_resistance",base:0.6}]}
scoreboard players operation @e[tag=mg.oln] mg.olses = $olses mg.st
tag @e[tag=mg.oln] remove mg.oln
