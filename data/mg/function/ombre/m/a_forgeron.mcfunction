# Forgeron calciné (wither_skeleton, région se)
tag @e[tag=mg.ollast] remove mg.ollast
summon minecraft:wither_skeleton ~ ~ ~ {Tags:["mg.ol","mg.olm","mg.oln","mg.ollast","mg.olk_a_forgeron","mg.olund","mg.olalpha"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CanPickUpLoot:0b,CustomName:{"text":"Forgeron calciné","color":"dark_red"},CustomNameVisible:0b,Health:1024f,equipment:{mainhand:{id:"minecraft:netherite_axe",count:1}},drop_chances:{mainhand:0f},active_effects:[{id:"minecraft:resistance",amplifier:0,duration:-1,show_particles:0b}],attributes:[{id:"minecraft:max_health",base:1024},{id:"minecraft:attack_damage",base:20},{id:"minecraft:movement_speed",base:0.3},{id:"minecraft:follow_range",base:40},{id:"minecraft:scale",base:1.5},{id:"minecraft:step_height",base:1.1},{id:"minecraft:knockback_resistance",base:0.6}]}
scoreboard players operation @e[tag=mg.oln] mg.olses = $olses mg.st
tag @e[tag=mg.oln] remove mg.oln
