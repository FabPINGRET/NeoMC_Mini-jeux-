# Dinosaure : Dilophosaure (zombie_villager invisible + modèle articulé, lié par mg.tvid)
tag @e[tag=mg.tvlast] remove mg.tvlast
scoreboard players add $tvid mg.st 1
summon minecraft:zombie_villager ~ ~ ~ {Tags:["mg.tv","mg.tvd","mg.tvtg","mg.tvn","mg.tvlast","mg.tvs_dilo","mg.tvhos","mg.tvdilo"],PersistenceRequired:1b,Silent:1b,DeathLootTable:"minecraft:empty",Health:26f,CustomName:{"text":"Dilophosaure","color":"dark_green"},CustomNameVisible:0b,CanPickUpLoot:0b,CanBreakDoors:0b,VillagerData:{profession:"minecraft:none",level:1,type:"minecraft:swamp"},active_effects:[{id:"minecraft:invisibility",duration:-1,amplifier:0,show_particles:0b}],attributes:[{id:"minecraft:max_health",base:26},{id:"minecraft:movement_speed",base:0.3},{id:"minecraft:follow_range",base:40},{id:"minecraft:attack_damage",base:4},{id:"minecraft:scale",base:1.05},{id:"minecraft:step_height",base:1.1}]}
execute if score $rp mg.st matches 1 run function mg:terra/dino/dilo_rp
execute unless score $rp mg.st matches 1 run function mg:terra/dino/dilo_bd
scoreboard players operation @e[tag=mg.tvn] mg.tvid = $tvid mg.st
scoreboard players operation @e[tag=mg.tvn] mg.tvses = $tvses mg.st
scoreboard players set #3 mg.st 3
scoreboard players operation @e[tag=mg.tvn,tag=mg.tvd] mg.tvph = $tvid mg.st
scoreboard players operation @e[tag=mg.tvn,tag=mg.tvd] mg.tvph %= #3 mg.st
tag @e[tag=mg.tvn] remove mg.tvn
execute as @e[tag=mg.tvlast,limit=1] at @s run function mg:terra/dsync
