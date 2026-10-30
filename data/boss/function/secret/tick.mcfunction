execute as @n[tag=sc_boss_pos,distance=0..] at @s facing entity @n[tag=sc_boss_dest,distance=0..] eyes run tp @s ~ ~ ~ ~ ~
execute as @n[tag=sc_boss_pos,distance=0..] at @s if entity @n[tag=sc_boss_dest,distance=..1] run tp @s @n[tag=sc_boss_dest,distance=0..]
execute as @n[tag=sc_boss_pos,distance=0..] at @s unless entity @n[tag=sc_boss_dest,distance=..1] run tp @s ^ ^ ^1

execute as @n[tag=sc_boss_pos,distance=0..] at @s run tp @n[tag=sc_boss_body_draw,distance=0..] ~ ~ ~

execute as @n[tag=sc_boss_body_draw,distance=0..] at @s run tp @n[tag=sc_boss_model_body,tag=origin,distance=0..] ~ ~ ~ ~ ~
execute if score sc_targeting_mode Value matches 1 as @n[tag=sc_boss_body_draw,distance=0..] at @s facing entity @p[gamemode=!spectator,tag=targeted,tag=mg.flw] eyes run tp @s ~ ~ ~ ~ 0
execute if score sc_targeting_mode Value matches 2 as @n[tag=sc_boss_body_draw,distance=0..] at @s facing entity @p[gamemode=!spectator,tag=mg.flw] eyes run tp @s ~ ~ ~ ~ 0
execute if score sc_targeting_mode Value matches 3 as @n[tag=sc_boss_body_draw,distance=0..] at @s facing -12471 203 -171 run tp @s ~ ~ ~ ~ 0
execute if score sc_targeting_mode Value matches 4 as @n[tag=sc_boss_body_draw,distance=0..] at @s run tp @s ~ ~ ~ ~25 0
execute if score sc_targeting_mode Value matches 5 as @n[tag=sc_boss_body_draw,distance=0..] at @s run tp @s ~ ~ ~ ~ 0
execute if score sc_targeting_mode Value matches 6 as @n[tag=sc_boss_body_draw,distance=0..] at @s facing -12471 189 -171 run tp @s ~ ~ ~ ~ 0


execute as @n[tag=sc_boss_body_draw,distance=0..] at @s positioned ~ ~5.2 ~ run tp @n[tag=sc_boss_head_draw,distance=0..] ^ ^ ^0.5
execute as @n[tag=sc_boss_head_draw,distance=0..] at @s run tp @n[tag=sc_boss_model_head,tag=origin,distance=0..] ~ ~ ~ ~ ~
execute if score sc_targeting_mode Value matches 1 as @n[tag=sc_boss_head_draw,distance=0..] at @s facing entity @p[gamemode=!spectator,tag=targeted,tag=mg.flw] eyes run tp @s ~ ~ ~ ~ ~
execute if score sc_targeting_mode Value matches 2 as @n[tag=sc_boss_head_draw,distance=0..] at @s facing entity @p[gamemode=!spectator,tag=mg.flw] eyes run tp @s ~ ~ ~ ~ ~
execute if score sc_targeting_mode Value matches 3 as @n[tag=sc_boss_head_draw,distance=0..] at @s facing -12471 203 -171 run tp @s ~ ~ ~ ~ ~
execute if score sc_targeting_mode Value matches 4 as @n[tag=sc_boss_head_draw,distance=0..] at @s run tp @s ~ ~ ~ ~25 0
execute if score sc_targeting_mode Value matches 5 as @n[tag=sc_boss_head_draw,distance=0..] at @s run tp @s ~ ~ ~ ~ 60
execute if score sc_targeting_mode Value matches 6 as @n[tag=sc_boss_head_draw,distance=0..] at @s facing -12471 189 -171 run tp @s ~ ~ ~ ~ ~


execute if score sc_pose Value matches 0..1 as @n[tag=sc_boss_body_draw,distance=0..] at @s run tp @n[tag=sc_boss_larm_draw,distance=0..] ~ ~ ~ ~-15 75
execute if score sc_pose Value matches 2 as @n[tag=sc_boss_head_draw,distance=0..] at @s run tp @n[tag=sc_boss_larm_draw,distance=0..] ~ ~ ~ ~ ~
execute if score sc_pose Value matches 3 as @n[tag=sc_boss_head_draw,distance=0..] at @s rotated ~22 ~ run tp @n[tag=sc_boss_larm_draw,distance=0..] ~ ~ ~ ~ ~
execute if score sc_pose Value matches 4 as @n[tag=sc_boss_head_draw,distance=0..] at @s rotated ~-30 ~ run tp @n[tag=sc_boss_larm_draw,distance=0..] ~ ~ ~ ~ ~
execute if score sc_pose Value matches 5 as @n[tag=sc_boss_body_draw,distance=0..] at @s run tp @n[tag=sc_boss_larm_draw,distance=0..] ~ ~ ~ ~-15 75
execute as @n[tag=sc_boss_body_draw,distance=0..] at @s positioned ~ ~3.7 ~ run tp @n[tag=sc_boss_larm_draw,distance=0..] ^1.7 ^ ^
execute as @n[tag=sc_boss_larm_draw,distance=0..] at @s run tp @n[tag=sc_boss_model_larm,tag=origin,distance=0..] ~ ~ ~ ~ ~

execute if score sc_pose Value matches 0 as @n[tag=sc_boss_body_draw,distance=0..] at @s run tp @n[tag=sc_boss_rarm_draw,distance=0..] ~ ~ ~ ~15 75
execute if score sc_pose Value matches 1..2 as @n[tag=sc_boss_head_draw,distance=0..] at @s run tp @n[tag=sc_boss_rarm_draw,distance=0..] ~ ~ ~ ~ ~
execute if score sc_pose Value matches 3 as @n[tag=sc_boss_head_draw,distance=0..] at @s rotated ~-22 ~ run tp @n[tag=sc_boss_rarm_draw,distance=0..] ~ ~ ~ ~ ~
execute if score sc_pose Value matches 4 as @n[tag=sc_boss_head_draw,distance=0..] at @s rotated ~30 ~ run tp @n[tag=sc_boss_rarm_draw,distance=0..] ~ ~ ~ ~ ~
execute if score sc_pose Value matches 5 as @n[tag=sc_boss_body_draw,distance=0..] at @s run tp @n[tag=sc_boss_rarm_draw,distance=0..] ~ ~ ~ ~-70 10
execute as @n[tag=sc_boss_body_draw,distance=0..] at @s positioned ~ ~3.7 ~ run tp @n[tag=sc_boss_rarm_draw,distance=0..] ^-1.7 ^ ^
execute as @n[tag=sc_boss_rarm_draw,distance=0..] at @s run tp @n[tag=sc_boss_model_rarm,tag=origin,distance=0..] ~ ~ ~ ~ ~

execute as @n[tag=sc_keyring_pos,distance=0..] at @n[tag=sc_boss_pos,distance=0..] run tp @s ~ ~ ~
execute as @n[tag=sc_keyring_pos,distance=0..] at @s run tp @s ~ ~ ~ ~5 ~
execute as @n[tag=sc_keyring_pos,distance=0..] at @s rotated ~ 0 positioned ^ ^ ^3 run tp @n[tag=sc_boss_model_keyring,tag=1,distance=0..] ~ 185.5 ~ ~ 30
execute as @n[tag=sc_keyring_pos,distance=0..] at @s rotated ~60 0 positioned ^ ^ ^3 run tp @n[tag=sc_boss_model_keyring,tag=2,distance=0..] ~ 185.5 ~ ~ 30
execute as @n[tag=sc_keyring_pos,distance=0..] at @s rotated ~120 0 positioned ^ ^ ^3 run tp @n[tag=sc_boss_model_keyring,tag=3,distance=0..] ~ 185.5 ~ ~ 30
execute as @n[tag=sc_keyring_pos,distance=0..] at @s rotated ~180 0 positioned ^ ^ ^3 run tp @n[tag=sc_boss_model_keyring,tag=4,distance=0..] ~ 185.5 ~ ~ 30
execute as @n[tag=sc_keyring_pos,distance=0..] at @s rotated ~240 0 positioned ^ ^ ^3 run tp @n[tag=sc_boss_model_keyring,tag=5,distance=0..] ~ 185.5 ~ ~ 30
execute as @n[tag=sc_keyring_pos,distance=0..] at @s rotated ~300 0 positioned ^ ^ ^3 run tp @n[tag=sc_boss_model_keyring,tag=6,distance=0..] ~ 185.5 ~ ~ 30

execute unless entity @e[tag=sc_keyring_pos,distance=0..] as @e[tag=sc_boss_model_keyring,tag=origin,distance=0..] at @s run tp @s ~ ~ ~ ~ 0

execute unless entity @e[tag=sc_keyring_pos,distance=0..] as @e[tag=sc_boss_model_keyring,tag=origin,distance=0..] at @s if block ^ ^ ^2 air run tp @s ^ ^ ^2
execute unless entity @e[tag=sc_keyring_pos,distance=0..] as @e[tag=sc_boss_model_keyring,tag=origin,distance=0..] at @s unless block ^ ^ ^2 air run playsound minecraft:block.chain.break hostile @a[tag=mg.flw] ~ ~ ~ 2 1
execute unless entity @e[tag=sc_keyring_pos,distance=0..] as @e[tag=sc_boss_model_keyring,tag=origin,distance=0..] at @s unless block ^ ^ ^2 air run kill @s
execute unless entity @e[tag=sc_keyring_pos,distance=0..] as @e[tag=sc_boss_model_keyring,tag=origin,distance=0..] at @s positioned ^ ^ ^ run particle minecraft:dripping_obsidian_tear ~ ~ ~ 0 0 0 0 1
execute unless entity @e[tag=sc_keyring_pos,distance=0..] as @e[tag=sc_boss_model_keyring,tag=origin,distance=0..] at @s positioned ^ ^ ^-0.5 run particle minecraft:dripping_obsidian_tear ~ ~ ~ 0 0 0 0 1
execute unless entity @e[tag=sc_keyring_pos,distance=0..] as @e[tag=sc_boss_model_keyring,tag=origin,distance=0..] at @s positioned ^ ^ ^-1 run particle minecraft:dripping_obsidian_tear ~ ~ ~ 0 0 0 0 1
execute unless entity @e[tag=sc_keyring_pos,distance=0..] as @e[tag=sc_boss_model_keyring,tag=origin,distance=0..] at @s positioned ^ ^ ^-1.5 run particle minecraft:dripping_obsidian_tear ~ ~ ~ 0 0 0 0 1
execute as @e[tag=sc_boss_model_keyring,tag=origin,distance=0..] at @s positioned ^ ^ ^1 positioned ~ ~ ~ as @a[distance=..1,tag=mg.flw] run damage @s 20 minecraft:mob_attack by @n[tag=sc_boss_name,distance=0..]
execute as @e[tag=sc_boss_model_keyring,tag=origin,distance=0..] at @s positioned ^ ^ ^1 positioned ~ ~-1 ~ as @a[distance=..1,tag=mg.flw] run damage @s 20 minecraft:mob_attack by @n[tag=sc_boss_name,distance=0..]

execute as @e[tag=sc_boss_model_keystar,tag=origin,distance=0..] at @s if block ^ ^ ^2 air run tp @s ^ ^ ^2
execute as @e[tag=sc_boss_model_keystar,tag=origin,distance=0..] at @s unless block ^ ^ ^2 air run playsound minecraft:block.chain.break hostile @a[tag=mg.flw] ~ ~ ~ 2 1
execute as @e[tag=sc_boss_model_keystar,tag=origin,distance=0..] at @s unless block ^ ^ ^2 air run kill @s
execute as @e[tag=sc_boss_model_keystar,tag=origin,distance=0..] at @s positioned ^ ^ ^ run particle minecraft:dripping_obsidian_tear ~ ~ ~ 0 0 0 0 1
execute as @e[tag=sc_boss_model_keystar,tag=origin,distance=0..] at @s positioned ^ ^ ^-0.5 run particle minecraft:dripping_obsidian_tear ~ ~ ~ 0 0 0 0 1
execute as @e[tag=sc_boss_model_keystar,tag=origin,distance=0..] at @s positioned ^ ^ ^-1 run particle minecraft:dripping_obsidian_tear ~ ~ ~ 0 0 0 0 1
execute as @e[tag=sc_boss_model_keystar,tag=origin,distance=0..] at @s positioned ^ ^ ^-1.5 run particle minecraft:dripping_obsidian_tear ~ ~ ~ 0 0 0 0 1
execute as @e[tag=sc_boss_model_keystar,tag=origin,distance=0..] at @s positioned ^ ^ ^1 positioned ~ ~ ~ as @a[distance=..1,tag=mg.flw] run damage @s 30 minecraft:mob_attack by @n[tag=sc_boss_name,distance=0..]
execute as @e[tag=sc_boss_model_keystar,tag=origin,distance=0..] at @s positioned ^ ^ ^1 positioned ~ ~-1 ~ as @a[distance=..1,tag=mg.flw] run damage @s 30 minecraft:mob_attack by @n[tag=sc_boss_name,distance=0..]

#COLORBALL
execute as @n[tag=sc_boss_colorball,distance=0..] at @s facing entity @n[tag=targeted,distance=0..] feet run tp @s ~ ~ ~ ~ ~
execute as @n[tag=sc_boss_colorball,distance=0..] at @s run tp @s ^ ^ ^0.2

execute as @n[tag=sc_boss_colorball,tag=red,distance=0..] at @s run particle dust{color:[1.000,0.000,0.000],scale:2} ~ ~1.6 ~ 0.2 0.2 0.2 0 1 normal
execute as @n[tag=sc_boss_colorball,tag=blue,distance=0..] at @s run particle dust{color:[0.000,0.000,1.000],scale:2} ~ ~1.6 ~ 0.2 0.2 0.2 0 1 normal

execute as @n[tag=sc_boss_colorball,distance=0..] at @s if entity @a[gamemode=!spectator,distance=..1,tag=mg.flw] run function boss:secret/attack/colorball_explode_player
execute as @n[tag=sc_boss_colorball,distance=0..] at @s positioned ~ ~1 ~ if entity @a[gamemode=!spectator,distance=..1,tag=mg.flw] run function boss:secret/attack/colorball_explode_player

execute as @n[tag=sc_boss_colorball,distance=0..] at @s if entity @e[tag=sc_boss_pos,distance=..2] run function boss:secret/attack/colorball_explode_boss
execute as @n[tag=sc_boss_colorball,distance=0..] at @s positioned ~ ~-1 ~ if entity @e[tag=sc_boss_pos,distance=..2] run function boss:secret/attack/colorball_explode_boss
execute as @n[tag=sc_boss_colorball,distance=0..] at @s positioned ~ ~-2 ~ if entity @e[tag=sc_boss_pos,distance=..2] run function boss:secret/attack/colorball_explode_boss
