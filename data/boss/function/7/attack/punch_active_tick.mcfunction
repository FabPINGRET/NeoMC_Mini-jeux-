execute as @n[tag=st_hand_loc,tag=fist,distance=0..] at @s facing entity @n[tag=st_hand_dest,tag=punch_speed,distance=0..] eyes run particle large_smoke ^ ^ ^-1 0.5 0.5 0.5 0 2
execute as @n[tag=st_hand_loc,tag=fist,distance=0..] at @s run playsound minecraft:entity.breeze.slide hostile @a[tag=mg.flw] ~ ~ ~ 1 2
execute as @n[tag=st_hand_loc,tag=fist,distance=0..] at @s positioned ~ -21 ~ as @a[distance=..2,tag=mg.flw] run damage @s 28 minecraft:falling_anvil by @n[tag=st_hand_loc,distance=0..]

execute as @n[tag=st_hand_loc,tag=fist,distance=0..] if entity @s[tag=st_hand_loc_1] as @n[tag=st_hand_dest_1,distance=0..] at @s if entity @n[tag=st_hand_loc_1,distance=..2] run setblock -10446 -48 -380 minecraft:redstone_block
execute as @n[tag=st_hand_loc,tag=fist,distance=0..] if entity @s[tag=st_hand_loc_2] as @n[tag=st_hand_dest_2,distance=0..] at @s if entity @n[tag=st_hand_loc_2,distance=..2] run setblock -10446 -48 -380 minecraft:redstone_block
execute as @n[tag=st_hand_loc,tag=fist,distance=0..] if entity @s[tag=st_hand_loc_3] as @n[tag=st_hand_dest_3,distance=0..] at @s if entity @n[tag=st_hand_loc_3,distance=..2] run setblock -10446 -48 -380 minecraft:redstone_block
execute as @n[tag=st_hand_loc,tag=fist,distance=0..] if entity @s[tag=st_hand_loc_4] as @n[tag=st_hand_dest_4,distance=0..] at @s if entity @n[tag=st_hand_loc_4,distance=..2] run setblock -10446 -48 -380 minecraft:redstone_block

execute as @n[tag=st_hand_loc,tag=fist,distance=0..] if entity @s[tag=st_hand_loc_1] as @n[tag=st_hand_dest_1,distance=0..] at @s if entity @n[tag=st_hand_loc_1,distance=..2] run setblock -10446 -48 -382 air
execute as @n[tag=st_hand_loc,tag=fist,distance=0..] if entity @s[tag=st_hand_loc_2] as @n[tag=st_hand_dest_2,distance=0..] at @s if entity @n[tag=st_hand_loc_2,distance=..2] run setblock -10446 -48 -382 air
execute as @n[tag=st_hand_loc,tag=fist,distance=0..] if entity @s[tag=st_hand_loc_3] as @n[tag=st_hand_dest_3,distance=0..] at @s if entity @n[tag=st_hand_loc_3,distance=..2] run setblock -10446 -48 -382 air
execute as @n[tag=st_hand_loc,tag=fist,distance=0..] if entity @s[tag=st_hand_loc_4] as @n[tag=st_hand_dest_4,distance=0..] at @s if entity @n[tag=st_hand_loc_4,distance=..2] run setblock -10446 -48 -382 air

#execute as @n[tag=st_hand_dest,tag=punch_speed] at @s if entity @e[tag=st_hand_loc,tag=fist,distance=..2] run setblock -10446 -48 -380 minecraft:redstone_block
