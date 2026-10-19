# Brigand (vindicator, région w)
tag @e[tag=mg.ollast] remove mg.ollast
summon minecraft:vindicator ~ ~ ~ {Tags:["mg.ol","mg.olm","mg.oln","mg.ollast","mg.olk_bandit"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,CustomName:{"text":"Brigand","color":"red"},CustomNameVisible:0b,Health:22f,equipment:{mainhand:{id:"minecraft:iron_axe",count:1},head:{id:"minecraft:leather_helmet",count:1,components:{"minecraft:dyed_color":6704179}},chest:{id:"minecraft:leather_chestplate",count:1,components:{"minecraft:dyed_color":6704179}}},drop_chances:{mainhand:0f,head:0f,chest:0f},attributes:[{id:"minecraft:max_health",base:22},{id:"minecraft:attack_damage",base:4},{id:"minecraft:movement_speed",base:0.33},{id:"minecraft:follow_range",base:40},{id:"minecraft:scale",base:1.0},{id:"minecraft:step_height",base:1.1}]}
scoreboard players operation @e[tag=mg.oln] mg.olses = $olses mg.st
tag @e[tag=mg.oln] remove mg.oln
