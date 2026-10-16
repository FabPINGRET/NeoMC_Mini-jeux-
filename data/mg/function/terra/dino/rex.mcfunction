# Dinosaure : Roi Tyran (ravager invisible + modèle articulé, lié par mg.tvid)
tag @e[tag=mg.tvlast] remove mg.tvlast
scoreboard players add $tvid mg.st 1
summon minecraft:ravager ~ ~ ~ {Tags:["mg.tv","mg.tvd","mg.tvtg","mg.tvn","mg.tvlast","mg.tvs_rex","mg.tvhos","mg.tvboss","mg.tvrex","mg.tvbig"],PersistenceRequired:1b,Silent:1b,DeathLootTable:"minecraft:empty",Health:900f,CustomName:{"text":"Roi Tyran","color":"dark_red"},CustomNameVisible:0b,CanJoinRaid:0b,PatrolLeader:0b,active_effects:[{id:"minecraft:invisibility",duration:-1,amplifier:0,show_particles:0b}],attributes:[{id:"minecraft:max_health",base:900},{id:"minecraft:movement_speed",base:0.31},{id:"minecraft:follow_range",base:64},{id:"minecraft:attack_damage",base:20},{id:"minecraft:scale",base:1.9},{id:"minecraft:step_height",base:1.6},{id:"minecraft:knockback_resistance",base:1.0},{id:"minecraft:attack_knockback",base:1.2}]}
execute if score $rp mg.st matches 1 run function mg:terra/dino/rex_rp
execute unless score $rp mg.st matches 1 run function mg:terra/dino/rex_bd
scoreboard players operation @e[tag=mg.tvn] mg.tvid = $tvid mg.st
scoreboard players operation @e[tag=mg.tvn] mg.tvses = $tvses mg.st
scoreboard players set #3 mg.st 3
scoreboard players operation @e[tag=mg.tvn,tag=mg.tvd] mg.tvph = $tvid mg.st
scoreboard players operation @e[tag=mg.tvn,tag=mg.tvd] mg.tvph %= #3 mg.st
tag @e[tag=mg.tvn] remove mg.tvn
execute as @e[tag=mg.tvlast,limit=1] at @s run function mg:terra/dsync
