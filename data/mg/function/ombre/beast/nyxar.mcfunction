# Créature : Nyxar, dragon de la Lune Noire (ravager invisible + modèle articulé, lié par mg.olid)
tag @e[tag=mg.ollast] remove mg.ollast
scoreboard players add $olid mg.st 1
summon minecraft:ravager ~ ~ ~ {Tags:["mg.ol","mg.olbd","mg.oln","mg.ollast","mg.olbs_nyxar","mg.olm","mg.olboss","mg.olnyxar","mg.olbig"],PersistenceRequired:1b,Silent:1b,DeathLootTable:"minecraft:empty",Health:1024f,CustomName:{"text":"Nyxar, dragon de la Lune Noire","color":"dark_purple"},CustomNameVisible:0b,CanJoinRaid:0b,PatrolLeader:0b,active_effects:[{id:"minecraft:invisibility",duration:-1,amplifier:0,show_particles:0b}],attributes:[{id:"minecraft:max_health",base:1024},{id:"minecraft:movement_speed",base:0.32},{id:"minecraft:follow_range",base:64},{id:"minecraft:attack_damage",base:24},{id:"minecraft:scale",base:2.2},{id:"minecraft:step_height",base:1.6},{id:"minecraft:knockback_resistance",base:1.0},{id:"minecraft:attack_knockback",base:1.4},{id:"minecraft:armor",base:14}]}
effect give @e[tag=mg.ollast] minecraft:resistance infinite 2 true
execute if score $rp mg.st matches 1 run function mg:ombre/beast/nyxar_rp
execute unless score $rp mg.st matches 1 run function mg:ombre/beast/nyxar_bd
scoreboard players operation @e[tag=mg.oln] mg.olid = $olid mg.st
scoreboard players operation @e[tag=mg.oln] mg.olses = $olses mg.st
tag @e[tag=mg.oln] remove mg.oln
execute as @e[tag=mg.ollast,limit=1] at @s run function mg:ombre/bsync
