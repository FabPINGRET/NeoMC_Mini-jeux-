# Wendigo des glaces (stray, région n)
tag @e[tag=mg.ollast] remove mg.ollast
summon minecraft:stray ~ ~ ~ {Tags:["mg.ol","mg.olm","mg.oln","mg.ollast","mg.olk_a_wendigo","mg.olund","mg.olalpha"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,CustomName:{"text":"Wendigo des glaces","color":"dark_red"},CustomNameVisible:0b,Health:640f,equipment:{mainhand:{id:"minecraft:iron_axe",count:1},head:{id:"minecraft:skeleton_skull",count:1}},drop_chances:{mainhand:0f,head:0f},attributes:[{id:"minecraft:max_health",base:640},{id:"minecraft:attack_damage",base:14},{id:"minecraft:movement_speed",base:0.3},{id:"minecraft:follow_range",base:40},{id:"minecraft:scale",base:1.7},{id:"minecraft:step_height",base:1.1},{id:"minecraft:knockback_resistance",base:0.6}]}
scoreboard players operation @e[tag=mg.oln] mg.olses = $olses mg.st
tag @e[tag=mg.oln] remove mg.oln
