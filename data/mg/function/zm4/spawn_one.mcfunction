# Un zombie (macro : $(hp) vie, $(sp) vitesse)
$summon minecraft:zombie ~ ~ ~ {Tags:["mg.zz","mg.gtg","mg.mob"],PersistenceRequired:1b,CanPickUpLoot:0b,IsBaby:0b,CanBreakDoors:0b,DeathLootTable:"minecraft:empty",Health:$(hp)f,attributes:[{id:"minecraft:max_health",base:$(hp)d},{id:"minecraft:follow_range",base:64d},{id:"minecraft:movement_speed",base:$(sp)d},{id:"minecraft:spawn_reinforcements",base:0d}]}
particle minecraft:large_smoke ~ ~1 ~ 0.3 0.5 0.3 0.02 10
