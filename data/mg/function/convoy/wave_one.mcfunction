# Un monstre (husk / pillard / vindicateur), position variable
execute if score $cvk mg.st matches ..0 run return 0
scoreboard players remove $cvk mg.st 1
execute store result score $cvz mg.st run random value 0..5
execute if score $cvz mg.st matches 0..2 run summon minecraft:husk ~ ~ ~-4 {Tags:["mg.cvm","mg.mob"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty"}
execute if score $cvz mg.st matches 3..4 run summon minecraft:pillager ~1 ~ ~4 {Tags:["mg.cvm","mg.mob"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",drop_chances:{mainhand:0f}}
execute if score $cvz mg.st matches 5 run summon minecraft:vindicator ~2 ~ ~ {Tags:["mg.cvm","mg.mob"],PersistenceRequired:1b,DeathLootTable:"minecraft:empty",drop_chances:{mainhand:0f}}
execute positioned ~1 ~ ~ run function mg:convoy/wave_one
