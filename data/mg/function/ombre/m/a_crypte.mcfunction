# Seigneur des cryptes (zombie, région w)
tag @e[tag=mg.ollast] remove mg.ollast
summon minecraft:zombie ~ ~ ~ {Tags:["mg.ol","mg.olm","mg.oln","mg.ollast","mg.olk_a_crypte","mg.olund","mg.olalpha"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,CustomName:{"text":"Seigneur des cryptes","color":"dark_red"},CustomNameVisible:0b,Health:320f,equipment:{mainhand:{id:"minecraft:iron_sword",count:1},head:{id:"minecraft:golden_helmet",count:1},chest:{id:"minecraft:chainmail_chestplate",count:1}},drop_chances:{mainhand:0f,head:0f,chest:0f},CanBreakDoors:0b,attributes:[{id:"minecraft:max_health",base:320},{id:"minecraft:attack_damage",base:8},{id:"minecraft:movement_speed",base:0.27},{id:"minecraft:follow_range",base:40},{id:"minecraft:scale",base:1.5},{id:"minecraft:step_height",base:1.1},{id:"minecraft:knockback_resistance",base:0.6}]}
scoreboard players operation @e[tag=mg.oln] mg.olses = $olses mg.st
tag @e[tag=mg.oln] remove mg.oln
