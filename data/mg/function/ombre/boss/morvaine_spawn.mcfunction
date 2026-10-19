# Morvaine, la mère-sorcière : apparition (ici)
summon minecraft:witch ~ ~ ~ {Tags:["mg.ol","mg.olm","mg.olboss","mg.ollast","mg.olbn"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,CustomName:{"text":"Morvaine","color":"dark_purple","bold":true},CustomNameVisible:1b,Health:1024f,active_effects:[{id:"minecraft:resistance",amplifier:0,duration:-1,show_particles:0b}],attributes:[{id:"minecraft:max_health",base:1024},{id:"minecraft:attack_damage",base:10},{id:"minecraft:scale",base:1.4},{id:"minecraft:follow_range",base:48},{id:"minecraft:movement_speed",base:0.3},{id:"minecraft:knockback_resistance",base:0.8},{id:"minecraft:step_height",base:1.5}]}
tag @e[tag=mg.olbn] add mg.olb_morvaine
tag @e[tag=mg.olbn] add mg.olboss
tag @e[tag=mg.olbn] add mg.olm
scoreboard players operation @e[tag=mg.olbn] mg.olses = $olses mg.st
tag @e[tag=mg.olbn] remove mg.olbn
