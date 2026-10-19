# Troggoïde (zombie, région s)
tag @e[tag=mg.ollast] remove mg.ollast
summon minecraft:zombie ~ ~ ~ {Tags:["mg.ol","mg.olm","mg.oln","mg.ollast","mg.olk_troggo"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,CustomName:{"text":"Troggoïde","color":"dark_gray"},CustomNameVisible:0b,Health:140f,equipment:{chest:{id:"minecraft:leather_chestplate",count:1,components:{"minecraft:dyed_color":5592405}},legs:{id:"minecraft:leather_leggings",count:1,components:{"minecraft:dyed_color":5592405}}},drop_chances:{chest:0f,legs:0f},CanBreakDoors:0b,attributes:[{id:"minecraft:max_health",base:140},{id:"minecraft:attack_damage",base:16},{id:"minecraft:movement_speed",base:0.27},{id:"minecraft:follow_range",base:40},{id:"minecraft:scale",base:1.25},{id:"minecraft:step_height",base:1.1}]}
scoreboard players operation @e[tag=mg.oln] mg.olses = $olses mg.st
tag @e[tag=mg.oln] remove mg.oln
