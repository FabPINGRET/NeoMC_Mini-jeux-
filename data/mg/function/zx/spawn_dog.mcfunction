# Chien de l'enfer (petit zoglin) : peu de vie, très rapide
$summon minecraft:zoglin ~ ~ ~ {Tags:["mg.zz","mg.gtg","mg.mob"],PersistenceRequired:1b,CanPickUpLoot:0b,DeathLootTable:"minecraft:empty",Health:$(hpd)f,IsBaby:1b,attributes:[{id:"minecraft:max_health",base:$(hpd)d},{id:"minecraft:follow_range",base:64d},{id:"minecraft:movement_speed",base:$(spd)d},{id:"minecraft:attack_damage",base:4d}]}
particle minecraft:flame ~ ~0.5 ~ 0.3 0.3 0.3 0.05 20
playsound minecraft:entity.wolf.growl hostile @a ~ ~ ~ 1 0.6
