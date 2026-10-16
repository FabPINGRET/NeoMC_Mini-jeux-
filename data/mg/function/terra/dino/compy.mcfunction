# Dinosaure : Compsognathus (silverfish invisible + modèle articulé, lié par mg.tvid)
tag @e[tag=mg.tvlast] remove mg.tvlast
scoreboard players add $tvid mg.st 1
summon minecraft:silverfish ~ ~ ~ {Tags:["mg.tv","mg.tvd","mg.tvtg","mg.tvn","mg.tvlast","mg.tvs_compy","mg.tvhos","mg.tvcompy"],PersistenceRequired:1b,Silent:1b,DeathLootTable:"minecraft:empty",Health:5f,CustomName:{"text":"Compsognathus","color":"yellow"},CustomNameVisible:0b,active_effects:[{id:"minecraft:invisibility",duration:-1,amplifier:0,show_particles:0b}],attributes:[{id:"minecraft:max_health",base:5},{id:"minecraft:movement_speed",base:0.34},{id:"minecraft:follow_range",base:32},{id:"minecraft:attack_damage",base:1.5},{id:"minecraft:scale",base:1.0}]}
execute if score $rp mg.st matches 1 run function mg:terra/dino/compy_rp
execute unless score $rp mg.st matches 1 run function mg:terra/dino/compy_bd
scoreboard players operation @e[tag=mg.tvn] mg.tvid = $tvid mg.st
scoreboard players operation @e[tag=mg.tvn] mg.tvses = $tvses mg.st
scoreboard players set #3 mg.st 3
scoreboard players operation @e[tag=mg.tvn,tag=mg.tvd] mg.tvph = $tvid mg.st
scoreboard players operation @e[tag=mg.tvn,tag=mg.tvd] mg.tvph %= #3 mg.st
tag @e[tag=mg.tvn] remove mg.tvn
execute as @e[tag=mg.tvlast,limit=1] at @s run function mg:terra/dsync
