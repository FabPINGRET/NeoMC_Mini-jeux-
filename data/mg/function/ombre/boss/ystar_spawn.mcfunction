# Ysh'tar, la reine-araignée : apparition (ici)
summon minecraft:spider ~ ~ ~ {Tags:["mg.ol","mg.olm","mg.olboss","mg.ollast","mg.olbn"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,CustomName:{"text":"Ysh'tar","color":"dark_green","bold":true},CustomNameVisible:1b,Health:650f,attributes:[{id:"minecraft:max_health",base:650},{id:"minecraft:attack_damage",base:10},{id:"minecraft:scale",base:3.4},{id:"minecraft:follow_range",base:48},{id:"minecraft:movement_speed",base:0.32},{id:"minecraft:knockback_resistance",base:0.8},{id:"minecraft:step_height",base:1.5}]}
tag @e[tag=mg.olbn] add mg.olb_ystar
tag @e[tag=mg.olbn] add mg.olboss
tag @e[tag=mg.olbn] add mg.olm
scoreboard players operation @e[tag=mg.olbn] mg.olses = $olses mg.st
tag @e[tag=mg.olbn] remove mg.olbn
