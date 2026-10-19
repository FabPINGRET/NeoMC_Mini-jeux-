# Brennic, seigneur des brigands : apparition (ici)
summon minecraft:vindicator ~ ~ ~ {Tags:["mg.ol","mg.olm","mg.olboss","mg.ollast","mg.olbn"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,CustomName:{"text":"Brennic","color":"red","bold":true},CustomNameVisible:1b,Health:320f,equipment:{mainhand:{id:"minecraft:iron_axe",count:1},head:{id:"minecraft:golden_helmet",count:1},chest:{id:"minecraft:golden_chestplate",count:1}},drop_chances:{mainhand:0f,offhand:0f,head:0f,chest:0f,legs:0f,feet:0f},attributes:[{id:"minecraft:max_health",base:320},{id:"minecraft:attack_damage",base:9},{id:"minecraft:scale",base:1.3},{id:"minecraft:follow_range",base:48},{id:"minecraft:movement_speed",base:0.3},{id:"minecraft:knockback_resistance",base:0.8},{id:"minecraft:step_height",base:1.5}]}
tag @e[tag=mg.olbn] add mg.olb_brennic
tag @e[tag=mg.olbn] add mg.olboss
tag @e[tag=mg.olbn] add mg.olm
scoreboard players operation @e[tag=mg.olbn] mg.olses = $olses mg.st
tag @e[tag=mg.olbn] remove mg.olbn
