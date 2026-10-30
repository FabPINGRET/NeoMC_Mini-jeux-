execute as @n[tag=worldgate_from_marker,distance=0..] at @s run particle minecraft:end_rod ~ ~1.5 ~ 0.5 0.5 0.5 0.1 50 force
execute as @n[tag=worldgate_from_marker,distance=0..] at @s run particle minecraft:instant_effect ~ ~1.5 ~ 1 1 1 2 300 force
execute as @n[tag=worldgate_from_marker,distance=0..] at @s run fill ~-2 ~-1 ~-2 ~2 ~3 ~2 glowstone replace tuff
execute as @n[tag=worldgate_from_marker,distance=0..] at @s run fill ~-2 ~-1 ~-2 ~2 ~3 ~2 raw_gold_block replace dead_fire_coral_block
execute as @n[tag=worldgate_from_marker,distance=0..] at @s run playsound minecraft:ambient.warped_forest.mood master @a[tag=mg.flw] ~ ~1 ~ 2 1
execute as @n[tag=worldgate_from_marker,distance=0..] at @s run playsound minecraft:block.respawn_anchor.set_spawn master @a[tag=mg.flw] ~ ~1 ~ 1 0.1
execute as @n[tag=worldgate_from_marker,distance=0..] at @s run playsound minecraft:block.respawn_anchor.ambient master @a[tag=mg.flw] ~ ~1 ~ 1 1
execute as @n[tag=worldgate_from_marker,distance=0..] at @s run playsound minecraft:item.trident.riptide_1 master @a[tag=mg.flw] ~ ~1 ~ 2 0.7
execute as @n[tag=worldgate_from_marker,distance=0..] at @s run playsound minecraft:entity.allay.death master @a[tag=mg.flw] ~ ~1 ~ 2 2
execute as @n[tag=worldgate_from_marker,distance=0..] at @s run setblock ~ ~-2 ~ redstone_block
kill @n[tag=worldgate_from_marker,distance=0..]
