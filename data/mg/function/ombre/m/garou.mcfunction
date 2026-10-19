# Loup-garou (wolf, région nw)
tag @e[tag=mg.ollast] remove mg.ollast
summon minecraft:wolf ~ ~ ~ {Tags:["mg.ol","mg.olm","mg.oln","mg.ollast","mg.olk_garou","mg.olprov"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,CustomName:{"text":"Loup-garou","color":"dark_gray"},CustomNameVisible:0b,Health:60f,variant:"minecraft:black",attributes:[{id:"minecraft:max_health",base:60},{id:"minecraft:attack_damage",base:8},{id:"minecraft:movement_speed",base:0.36},{id:"minecraft:follow_range",base:40},{id:"minecraft:scale",base:1.6},{id:"minecraft:step_height",base:1.1}]}
scoreboard players operation @e[tag=mg.oln] mg.olses = $olses mg.st
tag @e[tag=mg.oln] remove mg.oln
