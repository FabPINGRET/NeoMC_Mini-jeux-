# Cultiste de Malveth (vindicator, région sw)
tag @e[tag=mg.ollast] remove mg.ollast
summon minecraft:vindicator ~ ~ ~ {Tags:["mg.ol","mg.olm","mg.oln","mg.ollast","mg.olk_cultiste"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,CustomName:{"text":"Cultiste de Malveth","color":"dark_purple"},CustomNameVisible:0b,Health:160f,equipment:{mainhand:{id:"minecraft:netherite_axe",count:1},head:{id:"minecraft:leather_helmet",count:1,components:{"minecraft:dyed_color":3289650}},chest:{id:"minecraft:leather_chestplate",count:1,components:{"minecraft:dyed_color":3289650}}},drop_chances:{mainhand:0f,head:0f,chest:0f},attributes:[{id:"minecraft:max_health",base:160},{id:"minecraft:attack_damage",base:22},{id:"minecraft:movement_speed",base:0.33},{id:"minecraft:follow_range",base:40},{id:"minecraft:scale",base:1.0},{id:"minecraft:step_height",base:1.1}]}
scoreboard players operation @e[tag=mg.oln] mg.olses = $olses mg.st
tag @e[tag=mg.oln] remove mg.oln
