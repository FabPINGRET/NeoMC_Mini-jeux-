scoreboard players set final_morbex_target_mode Value 3
tp @n[tag=l_morbex_2,distance=0..] @n[tag=lord_morbex_stand,distance=0..]
execute as @n[tag=l_morbex_2,distance=0..] at @s run particle minecraft:trial_omen ~ ~3 ~ 1 2 1 1 75
execute as @n[tag=l_morbex_2,distance=0..] at @s run playsound minecraft:block.trial_spawner.spawn_item_begin master @a[tag=mg.flw] ~ ~ ~ 3 1
execute as @n[tag=l_morbex_2,distance=0..] at @s run playsound minecraft:block.trial_spawner.spawn_mob master @a[tag=mg.flw] ~ ~ ~ 3 1

scoreboard players set morbex_repo_timer Value 100
scoreboard players set morbex_hurtable bool 1

#activate death check
setblock -12354 42 378 stone
