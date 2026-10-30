execute as @e[tag=st_hand_draw_1,tag=freefall,distance=0..] at @s run particle dust_pillar{block_state:"stone"} ~ -21 ~ 1.5 0.2 1.5 0.5 20
execute as @e[tag=st_hand_draw_1,tag=freefall,distance=0..] at @s run particle white_smoke ~ -21 ~ 1 0.2 1 0 10
execute as @e[tag=st_hand_draw_2,tag=freefall,distance=0..] at @s run particle dust_pillar{block_state:"stone"} ~ -21 ~ 1.5 0.2 1.5 0.5 20
execute as @e[tag=st_hand_draw_2,tag=freefall,distance=0..] at @s run particle white_smoke ~ -21 ~ 1 0.2 1 0 10
execute as @e[tag=st_hand_draw_3,tag=freefall,distance=0..] at @s run particle dust_pillar{block_state:"stone"} ~ -21 ~ 1.5 0.2 1.5 0.5 20
execute as @e[tag=st_hand_draw_3,tag=freefall,distance=0..] at @s run particle white_smoke ~ -21 ~ 1 0.2 1 0 10
execute as @e[tag=st_hand_draw_4,tag=freefall,distance=0..] at @s run particle dust_pillar{block_state:"stone"} ~ -21 ~ 1.5 0.2 1.5 0.5 20
execute as @e[tag=st_hand_draw_4,tag=freefall,distance=0..] at @s run particle white_smoke ~ -21 ~ 1 0.2 1 0 10

execute as @e[tag=st_hand_shadow_1,distance=0..] at @s positioned ~ ~2 ~ run tag @a[distance=..2.5,tag=mg.flw] add damaged_by_smack
execute as @e[tag=st_hand_shadow_2,distance=0..] at @s positioned ~ ~2 ~ run tag @a[distance=..2.5,tag=mg.flw] add damaged_by_smack
execute as @e[tag=st_hand_shadow_3,distance=0..] at @s positioned ~ ~2 ~ run tag @a[distance=..2.5,tag=mg.flw] add damaged_by_smack
execute as @e[tag=st_hand_shadow_4,distance=0..] at @s positioned ~ ~2 ~ run tag @a[distance=..2.5,tag=mg.flw] add damaged_by_smack

execute as @e[tag=st_hand_shadow_1,distance=0..] at @s positioned ~ ~2 ~ run tag @e[tag=knucklehead,distance=..2.5] add damaged_by_smack
execute as @e[tag=st_hand_shadow_2,distance=0..] at @s positioned ~ ~2 ~ run tag @e[tag=knucklehead,distance=..2.5] add damaged_by_smack
execute as @e[tag=st_hand_shadow_3,distance=0..] at @s positioned ~ ~2 ~ run tag @e[tag=knucklehead,distance=..2.5] add damaged_by_smack
execute as @e[tag=st_hand_shadow_4,distance=0..] at @s positioned ~ ~2 ~ run tag @e[tag=knucklehead,distance=..2.5] add damaged_by_smack

execute as @e[tag=st_hand_shadow_1,distance=0..] at @s positioned ~ ~2 ~ run tag @e[tag=st_boss_walking_statue,distance=..2.5] add damaged_by_smack
execute as @e[tag=st_hand_shadow_2,distance=0..] at @s positioned ~ ~2 ~ run tag @e[tag=st_boss_walking_statue,distance=..2.5] add damaged_by_smack
execute as @e[tag=st_hand_shadow_3,distance=0..] at @s positioned ~ ~2 ~ run tag @e[tag=st_boss_walking_statue,distance=..2.5] add damaged_by_smack
execute as @e[tag=st_hand_shadow_4,distance=0..] at @s positioned ~ ~2 ~ run tag @e[tag=st_boss_walking_statue,distance=..2.5] add damaged_by_smack

execute as @n[tag=shadow,distance=0..] at @s run playsound minecraft:item.mace.smash_ground hostile @a[tag=mg.flw] ~ ~ ~ 3 1

execute as @e[tag=damaged_by_smack,distance=0..] at @s if entity @s[tag=st_boss_walking_statue] run setblock -10446 -48 -385 minecraft:redstone_block

execute as @e[tag=damaged_by_smack,distance=0..] at @s run damage @s 24 minecraft:falling_anvil by @n[tag=st_hand_loc,distance=0..]
tag @a[tag=mg.flw] remove damaged_by_smack
return 1
