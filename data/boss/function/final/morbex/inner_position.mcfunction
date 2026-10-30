execute as @n[tag=lord_morbex_stand,distance=0..] at @s run particle minecraft:trial_omen ~ ~3 ~ 1 2 1 1 75
execute as @e[tag=world_virus_rand,limit=1,sort=random,tag=!outer,distance=0..] at @s run tp @n[tag=lord_morbex_stand,distance=0..] ~ 130 ~
execute as @n[tag=lord_morbex_stand,distance=0..] at @s run playsound minecraft:block.trial_spawner.spawn_item_begin master @a[tag=mg.flw] ~ ~ ~ 3 1
execute as @n[tag=lord_morbex_stand,distance=0..] at @s run playsound minecraft:block.trial_spawner.spawn_mob master @a[tag=mg.flw] ~ ~ ~ 3 1
