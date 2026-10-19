# Gardien runique (iron_golem, région s)
tag @e[tag=mg.ollast] remove mg.ollast
summon minecraft:iron_golem ~ ~ ~ {Tags:["mg.ol","mg.olm","mg.oln","mg.ollast","mg.olk_gardien","mg.olprov"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,CustomName:{"text":"Gardien runique","color":"blue"},CustomNameVisible:0b,Health:200f,PlayerCreated:0b,attributes:[{id:"minecraft:max_health",base:200},{id:"minecraft:attack_damage",base:20},{id:"minecraft:movement_speed",base:0.27},{id:"minecraft:follow_range",base:40},{id:"minecraft:scale",base:1.0},{id:"minecraft:step_height",base:1.1}]}
scoreboard players operation @e[tag=mg.oln] mg.olses = $olses mg.st
tag @e[tag=mg.oln] remove mg.oln
