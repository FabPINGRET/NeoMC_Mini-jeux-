# Hrimgar, le géant du givre : apparition (ici)
summon minecraft:zombie ~ ~ ~ {Tags:["mg.ol","mg.olm","mg.olboss","mg.ollast","mg.olbn"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,CustomName:{"text":"Hrimgar","color":"aqua","bold":true},CustomNameVisible:1b,Health:1000f,equipment:{mainhand:{id:"minecraft:iron_axe",count:1},head:{id:"minecraft:leather_helmet",count:1,components:{"minecraft:dyed_color":14741759}},chest:{id:"minecraft:leather_chestplate",count:1,components:{"minecraft:dyed_color":14741759}},legs:{id:"minecraft:leather_leggings",count:1,components:{"minecraft:dyed_color":14741759}}},drop_chances:{mainhand:0f,offhand:0f,head:0f,chest:0f,legs:0f,feet:0f},CanBreakDoors:0b,attributes:[{id:"minecraft:max_health",base:1000},{id:"minecraft:attack_damage",base:16},{id:"minecraft:scale",base:3.0},{id:"minecraft:follow_range",base:48},{id:"minecraft:movement_speed",base:0.28},{id:"minecraft:knockback_resistance",base:0.8},{id:"minecraft:step_height",base:1.5}]}
tag @e[tag=mg.olbn] add mg.olb_hrimgar
tag @e[tag=mg.olbn] add mg.olboss
tag @e[tag=mg.olbn] add mg.olm
scoreboard players operation @e[tag=mg.olbn] mg.olses = $olses mg.st
tag @e[tag=mg.olbn] remove mg.olbn
