execute as @e[tag=worldgate_to_marker,limit=1,distance=0..] at @s run particle minecraft:witch ~ ~1.5 ~ 0.5 0.5 0.5 2 100 force
execute as @e[tag=worldgate_to_marker,limit=1,distance=0..] at @s run particle minecraft:instant_effect ~ ~1.5 ~ 1 1 1 2 300 force
execute as @e[tag=worldgate_to_marker,limit=1,distance=0..] at @s run fill ~-2 ~-1 ~-2 ~2 ~3 ~2 crying_obsidian replace tuff
execute as @e[tag=worldgate_to_marker,limit=1,distance=0..] at @s run fill ~-2 ~-1 ~-2 ~2 ~3 ~2 amethyst_block replace dead_fire_coral_block
execute as @e[tag=worldgate_to_marker,limit=1,distance=0..] at @s run playsound minecraft:ambient.warped_forest.mood master @a[tag=mg.flw] ~ ~1 ~ 2 1
execute as @e[tag=worldgate_to_marker,limit=1,distance=0..] at @s run playsound minecraft:block.respawn_anchor.set_spawn master @a[tag=mg.flw] ~ ~1 ~ 1 0.1
execute as @e[tag=worldgate_to_marker,limit=1,distance=0..] at @s run playsound minecraft:block.respawn_anchor.ambient master @a[tag=mg.flw] ~ ~1 ~ 1 1
execute as @e[tag=worldgate_to_marker,limit=1,distance=0..] at @s run playsound minecraft:item.trident.riptide_1 master @a[tag=mg.flw] ~ ~1 ~ 2 0.7
execute as @e[tag=worldgate_to_marker,limit=1,distance=0..] at @s run playsound minecraft:entity.evoker.prepare_attack master @a[tag=mg.flw] ~ ~1 ~ 2 1.4
execute as @e[tag=worldgate_to_marker,limit=1,distance=0..] at @s run setblock ~ ~-2 ~ redstone_block
kill @n[tag=worldgate_to_marker,distance=0..]
