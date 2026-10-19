# Chevalier calciné (wither_skeleton, région se)
tag @e[tag=mg.ollast] remove mg.ollast
summon minecraft:wither_skeleton ~ ~ ~ {Tags:["mg.ol","mg.olm","mg.oln","mg.ollast","mg.olk_calcine","mg.olund"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,CustomName:{"text":"Chevalier calciné","color":"dark_red"},CustomNameVisible:0b,Health:120f,equipment:{mainhand:{id:"minecraft:stone_sword",count:1}},drop_chances:{mainhand:0f},attributes:[{id:"minecraft:max_health",base:120},{id:"minecraft:attack_damage",base:16},{id:"minecraft:movement_speed",base:0.3},{id:"minecraft:follow_range",base:40},{id:"minecraft:scale",base:1.0},{id:"minecraft:step_height",base:1.1}]}
scoreboard players operation @e[tag=mg.oln] mg.olses = $olses mg.st
tag @e[tag=mg.oln] remove mg.oln
