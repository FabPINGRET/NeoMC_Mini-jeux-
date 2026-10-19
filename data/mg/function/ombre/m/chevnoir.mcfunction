# Chevalier noir (wither_skeleton, région sw)
tag @e[tag=mg.ollast] remove mg.ollast
summon minecraft:wither_skeleton ~ ~ ~ {Tags:["mg.ol","mg.olm","mg.oln","mg.ollast","mg.olk_chevnoir","mg.olund"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,CustomName:{"text":"Chevalier noir","color":"dark_purple"},CustomNameVisible:0b,Health:180f,equipment:{mainhand:{id:"minecraft:netherite_sword",count:1},chest:{id:"minecraft:netherite_chestplate",count:1}},drop_chances:{mainhand:0f,chest:0f},attributes:[{id:"minecraft:max_health",base:180},{id:"minecraft:attack_damage",base:22},{id:"minecraft:movement_speed",base:0.3},{id:"minecraft:follow_range",base:40},{id:"minecraft:scale",base:1.1},{id:"minecraft:step_height",base:1.1}]}
scoreboard players operation @e[tag=mg.oln] mg.olses = $olses mg.st
tag @e[tag=mg.oln] remove mg.oln
