# Créature : Drake des braises (hoglin invisible + modèle articulé, lié par mg.olid)
tag @e[tag=mg.ollast] remove mg.ollast
scoreboard players add $olid mg.st 1
summon minecraft:hoglin ~ ~ ~ {Tags:["mg.ol","mg.olbd","mg.oln","mg.ollast","mg.olbs_drake","mg.olm","mg.oldrake"],PersistenceRequired:1b,Silent:1b,DeathLootTable:"minecraft:empty",Health:150f,CustomName:{"text":"Drake des braises","color":"gold"},CustomNameVisible:0b,IsImmuneToZombification:1b,CannotBeHunted:1b,active_effects:[{id:"minecraft:invisibility",duration:-1,amplifier:0,show_particles:0b}],attributes:[{id:"minecraft:max_health",base:150},{id:"minecraft:movement_speed",base:0.32},{id:"minecraft:follow_range",base:40},{id:"minecraft:attack_damage",base:15},{id:"minecraft:scale",base:1.0},{id:"minecraft:step_height",base:1.1},{id:"minecraft:knockback_resistance",base:0.6}]}
execute if score $rp mg.st matches 1 run function mg:ombre/beast/drake_rp
execute unless score $rp mg.st matches 1 run function mg:ombre/beast/drake_bd
scoreboard players operation @e[tag=mg.oln] mg.olid = $olid mg.st
scoreboard players operation @e[tag=mg.oln] mg.olses = $olses mg.st
tag @e[tag=mg.oln] remove mg.oln
execute as @e[tag=mg.ollast,limit=1] at @s run function mg:ombre/bsync
