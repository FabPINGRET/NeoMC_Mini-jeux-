execute as @n[tag=lord_morbex_stand,distance=0..] at @s run particle minecraft:trial_omen ~ ~3 ~ 1 2 1 1 75
tp @n[tag=lord_morbex_stand,distance=0..] -12384 123 355
execute as @n[tag=lord_morbex_stand,distance=0..] at @s run playsound minecraft:block.trial_spawner.spawn_item_begin master @a[tag=mg.flw] ~ ~ ~ 3 1
execute as @n[tag=lord_morbex_stand,distance=0..] at @s run playsound minecraft:block.trial_spawner.spawn_mob master @a[tag=mg.flw] ~ ~ ~ 3 1
