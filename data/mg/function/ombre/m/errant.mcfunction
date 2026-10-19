# Ombre errante (enderman, région sw)
tag @e[tag=mg.ollast] remove mg.ollast
summon minecraft:enderman ~ ~ ~ {Tags:["mg.ol","mg.olm","mg.oln","mg.ollast","mg.olk_errant","mg.olprov"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,CustomName:{"text":"Ombre errante","color":"dark_purple"},CustomNameVisible:0b,Health:160f,attributes:[{id:"minecraft:max_health",base:160},{id:"minecraft:attack_damage",base:20},{id:"minecraft:movement_speed",base:0.32},{id:"minecraft:follow_range",base:40},{id:"minecraft:scale",base:1.0},{id:"minecraft:step_height",base:1.1}]}
scoreboard players operation @e[tag=mg.oln] mg.olses = $olses mg.st
tag @e[tag=mg.oln] remove mg.oln
