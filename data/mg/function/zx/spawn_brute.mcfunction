# Brute (noyé en armure) : 3× plus de vie, frappe fort, plus lent
$summon minecraft:drowned ~ ~ ~ {Tags:["mg.zz","mg.gtg","mg.mob"],PersistenceRequired:1b,CanPickUpLoot:0b,DeathLootTable:"minecraft:empty",Health:$(hpb)f,IsBaby:0b,equipment:{head:{id:"minecraft:iron_helmet",count:1},chest:{id:"minecraft:iron_chestplate",count:1}},drop_chances:{head:0f,chest:0f},attributes:[{id:"minecraft:max_health",base:$(hpb)d},{id:"minecraft:follow_range",base:64d},{id:"minecraft:movement_speed",base:$(spb)d},{id:"minecraft:spawn_reinforcements",base:0d},{id:"minecraft:attack_damage",base:7d}]}
particle minecraft:large_smoke ~ ~1 ~ 0.4 0.6 0.4 0.02 16
execute if score $rp mg.st matches 1 as @e[type=minecraft:drowned,tag=mg.zz,tag=!mg.zmk,distance=..2] run function mg:zx/mask_n {n:5}
