# Arbalétrier nain (pillager, région s)
tag @e[tag=mg.ollast] remove mg.ollast
summon minecraft:pillager ~ ~ ~ {Tags:["mg.ol","mg.olm","mg.oln","mg.ollast","mg.olk_arbaletrier"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,CustomName:{"text":"Arbalétrier nain","color":"gray"},CustomNameVisible:0b,Health:110f,equipment:{mainhand:{id:"minecraft:crossbow",count:1},head:{id:"minecraft:iron_helmet",count:1}},drop_chances:{mainhand:0f,head:0f},attributes:[{id:"minecraft:max_health",base:110},{id:"minecraft:attack_damage",base:13},{id:"minecraft:movement_speed",base:0.31},{id:"minecraft:follow_range",base:40},{id:"minecraft:scale",base:0.8},{id:"minecraft:step_height",base:1.1}]}
scoreboard players operation @e[tag=mg.oln] mg.olses = $olses mg.st
tag @e[tag=mg.oln] remove mg.oln
