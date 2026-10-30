execute if score final_morbex_target_mode Value matches 1 if entity @a[tag=bossroom,tag=targeted,gamemode=!spectator,tag=mg.flw] as @n[tag=lord_morbex_stand,distance=0..] at @s positioned ~ ~4 ~ facing entity @p[tag=bossroom,tag=targeted,gamemode=!spectator,tag=mg.flw] eyes positioned ~ ~-4 ~ run tp @s ~ ~ ~ ~ ~
execute if score final_morbex_target_mode Value matches 1 unless entity @a[tag=bossroom,tag=targeted,gamemode=!spectator,tag=mg.flw] as @n[tag=lord_morbex_stand,distance=0..] at @s positioned ~ ~4 ~ facing entity @p[tag=bossroom,gamemode=!spectator,tag=mg.flw] eyes positioned ~ ~-4 ~ run tp @s ~ ~ ~ ~ ~
execute if score final_morbex_target_mode Value matches 3 as @n[tag=l_morbex_2,distance=0..] at @s run tp @n[tag=lord_morbex_stand,distance=0..] ~ 60 ~


execute as @n[tag=lord_morbex_stand,distance=0..] at @s run particle minecraft:trial_spawner_detection_ominous ~ ~3 ~ 0.8 2 0.8 0 3

execute as @e[tag=mutarid_strong,distance=0..] at @s if block ~ ~-0.1 ~ black_stained_glass run kill @s

scoreboard players remove morbex_repo_timer Value 1
execute if score morbex_hurtable bool matches 1 if score morbex_repo_timer Value matches ..0 run function boss:final/morbex/reposition
execute if score morbex_hurtable bool matches 1 as @n[tag=l_morbex_2,distance=0..] at @s if entity @s[y=115,dy=6] run function boss:final/morbex/reposition
execute if score morbex_repo_timer Value matches ..0 run scoreboard players set morbex_repo_timer Value 200

execute if score final_morbex_health Value matches 0 run tp @n[tag=l_morbex_2,distance=0..] ~ -64 ~
