execute if score morbex_hurtable bool matches 1 as @n[tag=l_morbex_2,distance=0..] at @s run particle minecraft:trial_omen ~ ~3 ~ 1 2 1 1 75
execute if score morbex_hurtable bool matches 1 as @e[tag=world_virus_rand,limit=1,sort=random,distance=0..] at @s run tp @n[tag=l_morbex_2,distance=0..] ~ 123 ~
execute if score morbex_hurtable bool matches 1 as @n[tag=l_morbex_2,distance=0..] at @s run playsound minecraft:block.trial_spawner.spawn_item_begin master @a[tag=mg.flw] ~ ~ ~ 3 1
execute if score morbex_hurtable bool matches 1 as @n[tag=l_morbex_2,distance=0..] at @s run playsound minecraft:block.trial_spawner.spawn_mob master @a[tag=mg.flw] ~ ~ ~ 3 1
